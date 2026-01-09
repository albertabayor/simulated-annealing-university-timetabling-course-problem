"""Soft constraint: Preferred Room.

Penalizes classes not assigned to the lecturer's preferred room.
"""

from typing import Literal, List

from timetable_sa.core.interfaces import Constraint
from timetable_sa.examples.timetabling.domain_types.state import TimetableState


class PreferredRoom(Constraint):
    """Soft constraint: Respect lecturer's preferred room.
    
    Lecturers may have preferred rooms based on room familiarity,
    equipment needs, or personal preference. This constraint
    gently penalizes assignments to non-preferred rooms.
    
    Examples of violations:
        - Lecturer prefers Room A but assigned to Room B
    """
    
    name: str = "Preferred Room"
    type: Literal["hard", "soft"] = "soft"
    weight: float = 2.0

    def __init__(self, weight: float = 2.0):
        self.name = "Preferred Room"
        self.type = "soft"
        self.weight = weight

    def evaluate(self, state: TimetableState) -> float:
        """Evaluate the constraint.
        
        Returns:
            1.0 if all classes in preferred rooms, lower otherwise
        """
        violations = self._find_violations(state)
        
        if not violations:
            return 1.0
        
        return 1.0 / (1 + len(violations))

    def get_violations(self, state: TimetableState) -> List[str]:
        """Get list of non-preferred room assignments.
        
        Returns:
            List of violation descriptions
        """
        violations = self._find_violations(state)
        descriptions = []
        
        for v in violations:
            descriptions.append(
                f"Lecturer {v['lecturer']} preferred room {v['preferred']} "
                f"but class {v['class_id']} assigned to {v['assigned']}"
            )
        
        return descriptions

    def _find_violations(self, state: TimetableState) -> List[dict]:
        """Find all non-preferred room assignments.
        
        Returns:
            List of violation dictionaries
        """
        violations = []
        
        # Build lecturer lookup
        lecturer_by_code = {lect.code: lect for lect in state.lecturers}
        
        for entry in state.schedule:
            for lecturer_code in entry.lecturers:
                lecturer = lecturer_by_code.get(lecturer_code)
                if lecturer and lecturer.preferred_room:
                    if entry.room != lecturer.preferred_room:
                        violations.append({
                            "lecturer": lecturer_code,
                            "class_id": entry.class_id,
                            "preferred": lecturer.preferred_room,
                            "assigned": entry.room,
                        })
        
        return violations
