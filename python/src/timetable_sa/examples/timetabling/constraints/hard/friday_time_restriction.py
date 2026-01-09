"""Hard constraint: Friday Time Restriction.

Ensures classes on Friday don't start at prohibited times (during prayer).

Matches TypeScript's FridayTimeRestriction using is_valid_friday_start_time().
"""

from typing import Literal, List

from timetable_sa.core.interfaces import Constraint
from timetable_sa.examples.timetabling.domain_types.state import TimetableState
from timetable_sa.examples.timetabling.utils.time import is_valid_friday_start_time


class FridayTimeRestriction(Constraint):
    """Hard constraint: Friday time restrictions.
    
    On Fridays, classes cannot start at:
    - 11:00
    - 11:40
    - 12:00
    - 12:30
    - 13:00
    
    Examples of violations:
        - Class on Friday 11:00
        - Class on Friday 12:30
    """
    
    name: str = "Friday Time Restriction"
    type: Literal["hard", "soft"] = "hard"
    
    def evaluate(self, state: TimetableState) -> float:
        """Evaluate Friday time restriction.
        
        Uses is_valid_friday_start_time() to check prohibited start times.
        
        Args:
            state: Current timetable state
        
        Returns:
            1.0 if all Friday classes have valid start times, lower score otherwise
        """
        violations = self._find_violations(state)
        
        if not violations:
            return 1.0
        
        return 1.0 / (1 + len(violations))
    
    def get_violations(self, state: TimetableState) -> List[str]:
        """Get detailed list of Friday time violations.
        
        Args:
            state: Current timetable state
            
        Returns:
            List of violation descriptions
        """
        violations = self._find_violations(state)
        descriptions = []
        
        for v in violations:
            descriptions.append(
                f"Class {v['class_id']} ({v['kelas']}) on Friday starts at "
                f"{v['start']} (prohibited: {v['prohibited_times']})"
            )
        
        return descriptions
    
    def _find_violations(self, state: TimetableState) -> List[dict]:
        """Find all Friday time violations.
        
        Matches TypeScript: checks is_valid_friday_start_time().
        
        Args:
            state: Current timetable state
            
        Returns:
            List of violation dictionaries
        """
        violations = []
        
        for entry in state.schedule:
            if entry.time_slot.day != "Friday":
                continue
            
            if is_valid_friday_start_time(entry.time_slot.start_time):
                continue
            
            violations.append({
                "class_id": entry.class_id,
                "kelas": entry.kelas,
                "start": entry.time_slot.start_time,
                "prohibited_times": "11:00, 11:40, 12:00, 12:30, 13:00"
            })
        
        return violations
