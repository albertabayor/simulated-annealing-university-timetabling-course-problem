"""Soft constraint: Transit Time.

Penalizes insufficient transit time between classes for lecturers.
"""

from typing import Literal, List
from collections import defaultdict

from timetable_sa.core.interfaces import Constraint
from timetable_sa.examples.timetabling.domain_types.state import TimetableState
from timetable_sa.examples.timetabling.utils.time import time_to_minutes


class TransitTime(Constraint):
    """Soft constraint: Ensure adequate transit time between classes.
    
    Lecturers need time to travel between classrooms. This constraint
    penalizes schedules where lecturers have back-to-back classes
    in different buildings/rooms without adequate transit time.
    """
    
    name: str = "Transit Time"
    type: Literal["hard", "soft"] = "soft"
    weight: float = 2.0

    def __init__(self, weight: float = 2.0):
        self.name = "Transit Time"
        self.type = "soft"
        self.weight = weight

    def evaluate(self, state: TimetableState) -> float:
        """Evaluate the constraint.
        
        Returns:
            1.0 if all transit times are adequate
        """
        violations = self._find_violations(state)
        
        if not violations:
            return 1.0
        
        total_deficit = sum(v["deficit"] for v in violations)
        return 1.0 / (1 + total_deficit / 30.0)

    def get_violations(self, state: TimetableState) -> List[str]:
        """Get list of transit time violations."""
        violations = self._find_violations(state)
        descriptions = []
        
        for v in violations:
            descriptions.append(
                f"Lecturer {v['lecturer']} on {v['day']}: "
                f"Only {v['gap']} min between {v['class1']} and {v['class2']} "
                f"(needs {v['required']} min, deficit: {v['deficit']})"
            )
        
        return descriptions

    def _find_violations(self, state: TimetableState) -> List[dict]:
        """Find all transit time violations."""
        violations = []
        
        lecturer_by_code = {lect.code: lect for lect in state.lecturers}
        lecturer_day_entries: dict = defaultdict(list)
        
        for entry in state.schedule:
            for lecturer in entry.lecturers:
                key = (lecturer, entry.time_slot.day)
                lecturer_day_entries[key].append(entry)
        
        for (lecturer_code, day), entries in lecturer_day_entries.items():
            lecturer = lecturer_by_code.get(lecturer_code)
            required_transit = lecturer.transit_time if lecturer else 10
            
            sorted_entries = sorted(
                entries,
                key=lambda e: time_to_minutes(e.time_slot.start_time)
            )
            
            for i in range(len(sorted_entries) - 1):
                current = sorted_entries[i]
                next_entry = sorted_entries[i + 1]
                
                current_end = time_to_minutes(current.time_slot.end_time)
                next_start = time_to_minutes(next_entry.time_slot.start_time)
                
                gap = next_start - current_end
                
                if current.room != next_entry.room and gap < required_transit:
                    violations.append({
                        "lecturer": lecturer_code,
                        "day": day,
                        "class1": current.class_id,
                        "class2": next_entry.class_id,
                        "gap": gap,
                        "required": required_transit,
                        "deficit": max(0, required_transit - gap),
                    })
        
        return violations
