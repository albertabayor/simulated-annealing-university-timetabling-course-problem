"""Hard constraint: No Friday Prayer Conflict.

Ensures no classes are scheduled during Friday prayer time (11:40-13:10).
Matches TypeScript: 11:40-13:10 (exclusive boundaries).
"""

from typing import Literal, List

from timetable_sa.core.interfaces import Constraint
from timetable_sa.examples.timetabling.domain_types.state import TimetableState
from timetable_sa.examples.timetabling.utils.prayer_times import (
    FRIDAY_PRAYER_START,
    FRIDAY_PRAYER_END,
)


class NoFridayPrayConflict(Constraint):
    """Hard constraint: No classes during Friday prayer time.
    
    The Friday prayer (Jumu'ah) is a special congregational prayer
    that Muslims are required to attend. Classes should not conflict
    with this important religious observance.
    
    Examples of violations:
        - Any class scheduled during 11:30-12:30 on Friday
    """
    
    name: str = "No Friday Prayer Conflict"
    type: Literal["hard", "soft"] = "hard"

    def evaluate(self, state: TimetableState) -> float:
        """Evaluate the constraint.
        
        Returns:
            1.0 if no classes during Friday prayer, 0.0 otherwise
        """
        violations = self._find_violations(state)
        
        if not violations:
            return 1.0
        
        # Severe penalty - should be close to 0 for prayer conflicts
        return 0.1 / len(violations)

    def get_violations(self, state: TimetableState) -> List[str]:
        """Get detailed list of Friday prayer conflicts.
        
        Returns:
            List of violation descriptions
        """
        violations = self._find_violations(state)
        descriptions = []
        
        for v in violations:
            descriptions.append(
                f"Class {v['class_id']} ({v['kelas']}) on Friday at "
                f"{v['time']} conflicts with Friday prayer "
                f"(11:30-12:30)"
            )
        
        return descriptions

    def _find_violations(self, state: TimetableState) -> List[dict]:
        """Find all Friday prayer conflicts.
        
        Returns:
            List of violation dictionaries
        """
        violations = []
        
        from timetable_sa.examples.timetabling.utils.time import time_to_minutes
        
        for entry in state.schedule:
            if entry.time_slot.day != "Friday":
                continue
            
            start_minutes = time_to_minutes(entry.time_slot.start_time)
            end_minutes = time_to_minutes(entry.time_slot.end_time)
            
            # Check overlap with Friday prayer time (11:40-13:10)
            # Violation if: (start < 11:40 AND end > 11:40) OR (start < 13:10 AND end > 13:10)
            if (start_minutes < FRIDAY_PRAYER_START and end_minutes > FRIDAY_PRAYER_START) or \
               (start_minutes < FRIDAY_PRAYER_END and end_minutes > FRIDAY_PRAYER_END):
                violations.append({
                    "class_id": entry.class_id,
                    "kelas": entry.kelas,
                    "time": f"{entry.time_slot.start_time}-{entry.time_slot.end_time}",
                    "overlap_minutes": max(0, min(
                        min(FRIDAY_PRAYER_END, end_minutes) - FRIDAY_PRAYER_START,
                        min(FRIDAY_PRAYER_END, end_minutes) - FRIDAY_PRAYER_END
                    )),
                })
        
        return violations
