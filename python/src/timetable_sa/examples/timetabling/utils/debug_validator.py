"""Debug and validation utilities for timetable optimization."""

from typing import List, Dict, Any, Optional, Tuple
from dataclasses import dataclass


@dataclass
class ValidationIssue:
    """Represents a validation issue found in the timetable."""
    severity: str  # "error", "warning", "info"
    category: str  # e.g., "room_conflict", "capacity", "prayer_time"
    message: str
    entry_id: Optional[str] = None
    details: Optional[Dict[str, Any]] = None


class DebugValidator:
    """Debug validator for timetable state."""
    
    def __init__(self):
        """Initialize validator."""
        self.issues: List[ValidationIssue] = []
    
    def validate_state(self, state) -> List[ValidationIssue]:
        """Validate a complete timetable state.
        
        Args:
            state: Timetable state to validate
            
        Returns:
            List of validation issues found
        """
        self.issues = []
        
        self._check_room_conflicts(state)
        self._check_lecturer_conflicts(state)
        self._check_prodi_conflicts(state)
        self._check_room_capacity(state)
        self._check_prayer_time_violations(state)
        self._check_friday_prayer_conflicts(state)
        self._check_class_type_time(state)
        self._check_max_daily_periods(state)
        self._check_saturday_restriction(state)
        self._check_data_integrity(state)
        
        return self.issues
    
    def _check_room_conflicts(self, state):
        """Check for room conflicts."""
        room_day_period: Dict[Tuple[str, str, int], List] = {}
        
        for entry in state.schedule:
            key = (entry.room, entry.time_slot.day, entry.time_slot.period)
            if key not in room_day_period:
                room_day_period[key] = []
            room_day_period[key].append(entry)
        
        for key, entries in room_day_period.items():
            if len(entries) > 1:
                self.issues.append(ValidationIssue(
                    severity="error",
                    category="room_conflict",
                    message=f"Room {key[0]} has {len(entries)} classes at {key[1]} period {key[2]}",
                    entry_id=entries[0].class_id,
                    details={"room": key[0], "day": key[1], "period": key[2], "entries": [
                        e.class_id for e in entries
                    ]}
                ))
    
    def _check_lecturer_conflicts(self, state):
        """Check for lecturer conflicts."""
        lecturer_day_period: Dict[Tuple[str, str, int], List] = {}
        
        for entry in state.schedule:
            for lecturer in entry.lecturers:
                key = (lecturer, entry.time_slot.day, entry.time_slot.period)
                if key not in lecturer_day_period:
                    lecturer_day_period[key] = []
                lecturer_day_period[key].append(entry)
        
        for key, entries in lecturer_day_period.items():
            if len(entries) > 1:
                self.issues.append(ValidationIssue(
                    severity="error",
                    category="lecturer_conflict",
                    message=f"Lecturer {key[0]} has {len(entries)} classes at {key[1]} period {key[2]}",
                    entry_id=entries[0].class_id,
                    details={"lecturer": key[0], "day": key[1], "period": key[2], "entries": [
                        e.class_id for e in entries
                    ]}
                ))
    
    def _check_prodi_conflicts(self, state):
        """Check for prodi (study program) conflicts."""
        prodi_day_period: Dict[Tuple[str, str, int], List] = {}
        
        for entry in state.schedule:
            key = (entry.prodi, entry.time_slot.day, entry.time_slot.period)
            if key not in prodi_day_period:
                prodi_day_period[key] = []
            prodi_day_period[key].append(entry)
        
        for key, entries in prodi_day_period.items():
            if len(entries) > 1:
                self.issues.append(ValidationIssue(
                    severity="warning",
                    category="prodi_conflict",
                    message=f"Prodi {key[0]} has {len(entries)} classes at {key[1]} period {key[2]}",
                    entry_id=entries[0].class_id,
                    details={"prodi": key[0], "day": key[1], "period": key[2]}
                ))
    
    def _check_room_capacity(self, state):
        """Check for room capacity violations."""
        room_by_code = {r.code: r for r in state.rooms}
        
        for entry in state.schedule:
            room = room_by_code.get(entry.room)
            if room and entry.participants > room.capacity:
                overflow = entry.participants - room.capacity
                self.issues.append(ValidationIssue(
                    severity="error",
                    category="capacity",
                    message=f"Class {entry.class_id} has {entry.participants} students but room {room.code} capacity is {room.capacity} (overflow: {overflow})",
                    entry_id=entry.class_id,
                    details={
                        "class_id": entry.class_id,
                        "participants": entry.participants,
                        "room_code": room.code,
                        "room_capacity": room.capacity,
                        "overflow": overflow
                    }
                ))
    
    def _check_prayer_time_violations(self, state):
        """Check for prayer time violations."""
        from timetable_sa.examples.timetabling.utils.prayer_times import PRAYER_PERIODS
        
        for entry in state.schedule:
            day = entry.time_slot.day
            period = entry.time_slot.period
            
            if day in PRAYER_PERIODS:
                for prayer in PRAYER_PERIODS[day]:
                    if prayer["start_period"] <= period <= prayer["end_period"]:
                        self.issues.append(ValidationIssue(
                            severity="warning",
                            category="prayer_time",
                            message=f"Class {entry.class_id} overlaps with {prayer['name']} on {day}",
                            entry_id=entry.class_id,
                            details={
                                "class_id": entry.class_id,
                                "day": day,
                                "period": period,
                                "prayer_name": prayer["name"],
                                "prayer_periods": f"{prayer['start_period']}-{prayer['end_period']}"
                            }
                        ))
    
    def _check_friday_prayer_conflicts(self, state):
        """Check for Friday prayer time conflicts."""
        from timetable_sa.examples.timetabling.utils.prayer_times import FRIDAY_PRAYER_PERIODS
        
        for entry in state.schedule:
            if entry.time_slot.day != "Friday":
                continue
            
            period = entry.time_slot.period
            for prayer in FRIDAY_PRAYER_PERIODS:
                if prayer["start_period"] <= period <= prayer["end_period"]:
                    self.issues.append(ValidationIssue(
                        severity="error",
                        category="friday_prayer",
                        message=f"Class {entry.class_id} is during Friday Prayer time",
                        entry_id=entry.class_id,
                        details={
                            "class_id": entry.class_id,
                            "period": period,
                            "prayer_name": prayer["name"]
                        }
                    ))
    
    def _check_class_type_time(self, state):
        """Check if class type matches time slot."""
        from timetable_sa.examples.timetabling.utils.time import time_to_minutes
        
        for entry in state.schedule:
            start_minutes = time_to_minutes(entry.time_slot.start_time)
            hour = start_minutes // 60
            
            is_morning = entry.class_type.lower() == "pagi"
            
            if is_morning and hour >= 12:
                self.issues.append(ValidationIssue(
                    severity="warning",
                    category="class_type_time",
                    message=f"Morning class {entry.class_id} scheduled at {entry.time_slot.start_time}",
                    entry_id=entry.class_id,
                    details={
                        "class_id": entry.class_id,
                        "class_type": entry.class_type,
                        "start_time": entry.time_slot.start_time,
                        "expected": "morning (before 12:00)"
                    }
                ))
            elif not is_morning and hour < 16:
                self.issues.append(ValidationIssue(
                    severity="warning",
                    category="class_type_time",
                    message=f"Evening class {entry.class_id} scheduled at {entry.time_slot.start_time}",
                    entry_id=entry.class_id,
                    details={
                        "class_id": entry.class_id,
                        "class_type": entry.class_type,
                        "start_time": entry.time_slot.start_time,
                        "expected": "evening (16:00 or later)"
                    }
                ))
    
    def _check_max_daily_periods(self, state):
        """Check if any lecturer exceeds max daily periods."""
        lecturer_by_code = {l.code: l for l in state.lecturers}
        lecturer_day_counts: Dict[Tuple[str, str], int] = {}
        
        for entry in state.schedule:
            for lecturer in entry.lecturers:
                key = (lecturer, entry.time_slot.day)
                lecturer_day_counts[key] = lecturer_day_counts.get(key, 0) + 1
        
        for (lecturer, day), count in lecturer_day_counts.items():
            lecturer = lecturer_by_code.get(lecturer)
            if lecturer and count > lecturer.max_daily_periods:
                self.issues.append(ValidationIssue(
                    severity="warning",
                    category="max_daily_periods",
                    message=f"Lecturer {lecturer} has {count} classes on {day} (max: {lecturer.max_daily_periods})",
                    details={
                        "lecturer": lecturer,
                        "day": day,
                        "count": count,
                        "max_allowed": lecturer.max_daily_periods
                    }
                ))
    
    def _check_saturday_restriction(self, state):
        """Check for Saturday classes."""
        for entry in state.schedule:
            if entry.time_slot.day == "Saturday":
                self.issues.append(ValidationIssue(
                    severity="warning",
                    category="saturday_restriction",
                    message=f"Class {entry.class_id} is scheduled on Saturday",
                    entry_id=entry.class_id,
                    details={
                        "class_id": entry.class_id,
                        "day": entry.time_slot.day,
                        "period": entry.time_slot.period
                    }
                ))
    
    def _check_data_integrity(self, state):
        """Check for data integrity issues."""
        room_codes = {r.code for r in state.rooms}
        lecturer_codes = {l.code for l in state.lecturers}
        
        for entry in state.schedule:
            # Check room exists
            if entry.room not in room_codes:
                self.issues.append(ValidationIssue(
                    severity="error",
                    category="data_integrity",
                    message=f"Class {entry.class_id} uses unknown room {entry.room}",
                    entry_id=entry.class_id,
                    details={
                        "class_id": entry.class_id,
                        "room": entry.room,
                        "valid_rooms": list(room_codes)
                    }
                ))
            
            # Check lecturers exist
            for lecturer in entry.lecturers:
                if lecturer not in lecturer_codes:
                    self.issues.append(ValidationIssue(
                        severity="error",
                        category="data_integrity",
                        message=f"Class {entry.class_id} uses unknown lecturer {lecturer}",
                        entry_id=entry.class_id,
                        details={
                            "class_id": entry.class_id,
                            "lecturer": lecturer,
                            "valid_lecturers": list(lecturer_codes)
                        }
                    ))
    
    def get_error_count(self) -> int:
        """Get count of error-level issues."""
        return sum(1 for issue in self.issues if issue.severity == "error")
    
    def get_warning_count(self) -> int:
        """Get count of warning-level issues."""
        return sum(1 for issue in self.issues if issue.severity == "warning")
    
    def get_info_count(self) -> int:
        """Get count of info-level issues."""
        return sum(1 for issue in self.issues if issue.severity == "info")
    
    def get_summary(self) -> str:
        """Get a summary of validation results."""
        errors = self.get_error_count()
        warnings = self.get_warning_count()
        infos = self.get_info_count()
        
        lines = ["=" * 60]
        lines.append("VALIDATION SUMMARY")
        lines.append("=" * 60)
        lines.append(f"Total issues: {len(self.issues)}")
        lines.append(f"  Errors: {errors}")
        lines.append(f"  Warnings: {warnings}")
        lines.append(f"  Info: {infos}")
        
        if self.issues:
            lines.append("\nIssues by category:")
            categories: Dict[str, int] = {}
            for issue in self.issues:
                categories[issue.category] = categories.get(issue.category, 0) + 1
            
            for cat, count in sorted(categories.items(), key=lambda x: -x[1]):
                lines.append(f"  {cat}: {count}")
        
        lines.append("=" * 60)
        
        return "\n".join(lines)
    
    def print_report(self):
        """Print a detailed validation report."""
        print("\n" + self.get_summary())
        
        if self.issues:
            print("\nDETAILED ISSUES:")
            print("-" * 60)
            
            for i, issue in enumerate(self.issues, 1):
                print(f"\n{i}. [{issue.severity.upper()}] {issue.category}")
                print(f"   {issue.message}")
                if issue.details:
                    for key, value in issue.details.items():
                        print(f"   {key}: {value}")
        
        print()


def quick_check(state) -> Tuple[bool, List[str]]:
    """Quick validation check for a state.
    
    Args:
        state: Timetable state to check
        
    Returns:
        Tuple of (is_valid, list of issues)
    """
    validator = DebugValidator()
    issues = validator.validate_state(state)
    
    is_valid = all(issue.severity != "error" for issue in issues)
    messages = [issue.message for issue in issues]
    
    return is_valid, messages
