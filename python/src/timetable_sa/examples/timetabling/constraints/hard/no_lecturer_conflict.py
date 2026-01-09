"""Hard constraint: No Lecturer Conflict.

Ensures no lecturer is scheduled for two classes at the same time.
"""

from typing import Literal, List
from collections import defaultdict

from timetable_sa.core.interfaces import Constraint
from timetable_sa.examples.timetabling.domain_types.state import TimetableState


class NoLecturerConflict(Constraint):
    """Hard constraint: No lecturer can have two classes at the same time.
    
    This is a fundamental constraint - lecturer conflicts make a schedule invalid.
    
    Examples of violations:
        - Lecturer A is teaching Class X on Monday 08:00 and Class Y on Monday 08:00
        - Lecturer B has three classes overlapping on Friday evening
    """
    
    name: str = "No Lecturer Conflict"
    type: Literal["hard", "soft"] = "hard"

    def evaluate(self, state: TimetableState) -> float:
        """Evaluate the constraint.
        
        Returns:
            1.0 if no lecturer conflicts, lower score otherwise
        """
        conflicts = self._find_conflicts(state)
        
        if not conflicts:
            return 1.0
        
        return 1.0 / (1 + len(conflicts))

    def get_violations(self, state: TimetableState) -> List[str]:
        """Get detailed list of lecturer conflicts.
        
        Returns:
            List of violation descriptions
        """
        conflicts = self._find_conflicts(state)
        violations = []
        
        for conflict in conflicts:
            lecturer = conflict["lecturer"]
            day = conflict["day"]
            time = conflict["time"]
            classes = conflict["classes"]
            
            class_info = [f"{c.class_id} ({c.kelas})" for c in classes]
            violation = f"Lecturer {lecturer} has conflict on {day} at {time}: {', '.join(class_info)}"
            violations.append(violation)
        
        return violations

    def _find_conflicts(self, state: TimetableState) -> List[dict]:
        """Find all lecturer conflicts in the schedule.
        
        Each class can have multiple lecturers, so we need to:
        1. Collect all (lecturer, day, time_slot) assignments
        2. Find overlaps for each lecturer
        """
        # Build lecturer -> entries mapping
        # Each entry in schedule may have multiple lecturers
        lecturer_entries: dict = defaultdict(list)
        
        for entry in state.schedule:
            for lecturer in entry.lecturers:
                lecturer_entries[lecturer].append(entry)
        
        conflicts = []
        
        # Check each lecturer for conflicts
        for lecturer, entries in lecturer_entries.items():
            if len(entries) < 2:
                continue
            
            # Sort by day and start time
            sorted_entries = sorted(
                entries,
                key=lambda e: (e.time_slot.day, e.time_slot.start_time)
            )
            
            # Check for overlaps
            for i in range(len(sorted_entries) - 1):
                current = sorted_entries[i]
                
                # Check subsequent entries for same-day conflicts
                j = i + 1
                same_day_conflicts = []
                
                while j < len(sorted_entries) and sorted_entries[j].time_slot.day == current.time_slot.day:
                    next_entry = sorted_entries[j]
                    
                    if self._entries_overlap(current, next_entry):
                        same_day_conflicts.append(next_entry)
                    
                    j += 1
                
                # If there are conflicts, record them
                if same_day_conflicts:
                    all_conflicting = [current] + same_day_conflicts
                    time_slot = f"{current.time_slot.start_time}-{current.time_slot.end_time}"
                    
                    if not any(
                        c["lecturer"] == lecturer 
                        and c["day"] == current.time_slot.day 
                        and c["time"] == time_slot
                        for c in conflicts
                    ):
                        conflicts.append({
                            "lecturer": lecturer,
                            "day": current.time_slot.day,
                            "time": time_slot,
                            "classes": all_conflicting
                        })
        
        return conflicts

    def _entries_overlap(self, entry1, entry2) -> bool:
        """Check if two schedule entries overlap in time."""
        from timetable_sa.examples.timetabling.utils.time import time_to_minutes
        
        start1 = time_to_minutes(entry1.time_slot.start_time)
        end1 = time_to_minutes(entry1.time_slot.end_time)
        start2 = time_to_minutes(entry2.time_slot.start_time)
        end2 = time_to_minutes(entry2.time_slot.end_time)
        
        return max(start1, start2) < min(end1, end2)
