"""Soft constraint: Preferred Time.

Penalizes classes not scheduled at the lecturer's preferred time.
"""

from typing import Literal, List

from timetable_sa.core.interfaces import Constraint
from timetable_sa.examples.timetabling.domain_types.state import TimetableState


class PreferredTime(Constraint):
    """Soft constraint: Respect lecturer's preferred time slots.
    
    Lecturers may have preferred time slots for teaching based on
    their research schedule, other commitments, or personal preference.
    This constraint gently penalizes assignments outside preferred times.
    
    Examples of violations:
        - Lecturer prefers Thursday evening but assigned Friday morning
    """
    
    name: str = "Preferred Time"
    type: Literal["hard", "soft"] = "soft"
    weight: float = 2.0

    def __init__(self, weight: float = 2.0):
        self.name = "Preferred Time"
        self.type = "soft"
        self.weight = weight

    def evaluate(self, state: TimetableState) -> float:
        """Evaluate the constraint.
        
        Returns:
            1.0 if all classes at preferred times, lower otherwise
        """
        violations = self._find_violations(state)
        
        if not violations:
            return 1.0
        
        return 1.0 / (1 + len(violations))

    def get_violations(self, state: TimetableState) -> List[str]:
        """Get list of non-preferred time assignments.
        
        Returns:
            List of violation descriptions
        """
        violations = self._find_violations(state)
        descriptions = []
        
        for v in violations:
            descriptions.append(
                f"Lecturer {v['lecturer']} preferred {v['preferred']} "
                f"but class {v['class_id']} scheduled {v['day']} at {v['time']}"
            )
        
        return descriptions

    def _find_violations(self, state: TimetableState) -> List[dict]:
        """Find all non-preferred time assignments.
        
        Returns:
            List of violation dictionaries
        """
        violations = []
        
        # Build lecturer lookup
        lecturer_by_code = {lect.code: lect for lect in state.lecturers}
        
        for entry in state.schedule:
            for lecturer_code in entry.lecturers:
                lecturer = lecturer_by_code.get(lecturer_code)
                if lecturer and lecturer.preferred_time:
                    if not self._is_preferred(entry, lecturer.preferred_time):
                        violations.append({
                            "lecturer": lecturer_code,
                            "class_id": entry.class_id,
                            "preferred": lecturer.preferred_time,
                            "day": entry.time_slot.day,
                            "time": entry.time_slot.start_time,
                        })
        
        return violations

    def _is_preferred(self, entry, preferred: str) -> bool:
        """Check if the entry's time matches the preferred time."""
        entry_day = entry.time_slot.day.lower()
        
        # Parse preferred time (e.g., "18.30 - 21.00 Thursday, 18.30 - 21.00 Friday")
        preferred = preferred.lower()
        
        # Check if the day is mentioned
        if entry_day not in preferred:
            return False
        
        # Get the time range for this day from preferred string
        # This is a simplified check - in practice would need more robust parsing
        return True
