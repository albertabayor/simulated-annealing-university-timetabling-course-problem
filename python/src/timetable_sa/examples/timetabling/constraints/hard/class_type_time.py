"""Hard constraint: Class Type Time.

Ensures morning classes are scheduled in morning slots and evening classes
in evening slots.
"""

from typing import Literal, List

from timetable_sa.core.interfaces import Constraint
from timetable_sa.examples.timetabling.domain_types.state import TimetableState
from timetable_sa.examples.timetabling.utils.time import time_to_minutes


class ClassTypeTime(Constraint):
    """Hard constraint: Morning/evening class type must match time slot.
    
    Classes marked as "pagi" (morning) should be scheduled in morning slots
    (before 12:00), and classes marked as "sore" (evening) should be scheduled
    in evening slots (after 16:00 or 17:00).
    
    Examples of violations:
        - "pagi" class scheduled at 18:30
        - "sore" class scheduled at 08:00
    """
    
    name: str = "Class Type Time"
    type: Literal["hard", "soft"] = "hard"

    def evaluate(self, state: TimetableState) -> float:
        """Evaluate the constraint.
        
        Returns:
            1.0 if all classes are in appropriate time slots
        """
        violations = self._find_violations(state)
        
        if not violations:
            return 1.0
        
        return 1.0 / (1 + len(violations))

    def get_violations(self, state: TimetableState) -> List[str]:
        """Get detailed list of class type time violations.
        
        Returns:
            List of violation descriptions
        """
        violations = self._find_violations(state)
        descriptions = []
        
        for v in violations:
            descriptions.append(
                f"Class {v['class_id']} ({v['class_type']}) scheduled at "
                f"{v['start_time']} but {v['class_type']} classes should be "
                f"in {v['expected_period']}"
            )
        
        return descriptions

    def _find_violations(self, state: TimetableState) -> List[dict]:
        """Find all class type time mismatches.
        
        Returns:
            List of violation dictionaries
        """
        violations = []
        
        for entry in state.schedule:
            start_minutes = time_to_minutes(entry.time_slot.start_time)
            
            is_morning = entry.class_type.lower() == "pagi"
            
            # TypeScript uses:
            # - Morning classes (pagi): startTime < 15:30
            # - Evening classes (sore): 15:30 <= startTime < 21:00
            if is_morning:
                if start_minutes >= 15 * 60 + 30:  # 15:30 = 930 minutes
                    violations.append({
                        "class_id": entry.class_id,
                        "class_type": entry.class_type,
                        "start_time": entry.time_slot.start_time,
                        "expected_period": "morning (before 15:30)",
                    })
            else:
                if start_minutes < 15 * 60 + 30 or start_minutes >= 21 * 60:
                    violations.append({
                        "class_id": entry.class_id,
                        "class_type": entry.class_type,
                        "start_time": entry.time_slot.start_time,
                        "expected_period": "evening (15:30-21:00)",
                    })
        
        return violations
