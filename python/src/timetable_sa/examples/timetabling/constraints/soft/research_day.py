"""Soft constraint: Research Day.

Penalizes scheduling classes on lecturer's designated research day.
"""

from typing import Literal, List

from timetable_sa.core.interfaces import Constraint
from timetable_sa.examples.timetabling.domain_types.state import TimetableState


class ResearchDay(Constraint):
    """Soft constraint: Respect lecturer's research day.
    
    Lecturers may have designated research days when they should not
    be scheduled for teaching. This constraint gently penalizes
    scheduling on research days.
    
    Examples of violations:
        - Lecturer has Wednesday as research day but scheduled Wednesday
    """
    
    name: str = "Research Day"
    type: Literal["hard", "soft"] = "soft"
    weight: float = 3.0

    def __init__(self, weight: float = 3.0):
        self.name = "Research Day"
        self.type = "soft"
        self.weight = weight

    def evaluate(self, state: TimetableState) -> float:
        """Evaluate the constraint.
        
        Returns:
            1.0 if no classes on research days
        """
        violations = self._find_violations(state)
        
        if not violations:
            return 1.0
        
        return 1.0 / (1 + len(violations))

    def get_violations(self, state: TimetableState) -> List[str]:
        """Get list of research day violations.
        
        Returns:
            List of violation descriptions
        """
        violations = self._find_violations(state)
        descriptions = []
        
        for v in violations:
            descriptions.append(
                f"Lecturer {v['lecturer']} has {v['research_day']} as research day "
                f"but class {v['class_id']} scheduled on {v['scheduled_day']}"
            )
        
        return descriptions

    def _find_violations(self, state: TimetableState) -> List[dict]:
        """Find all research day violations.
        
        Returns:
            List of violation dictionaries
        """
        violations = []
        
        # Build lecturer lookup
        lecturer_by_code = {lect.code: lect for lect in state.lecturers}
        
        for entry in state.schedule:
            for lecturer_code in entry.lecturers:
                lecturer = lecturer_by_code.get(lecturer_code)
                if lecturer and lecturer.research_day:
                    scheduled_day = entry.time_slot.day.lower()
                    research_day = lecturer.research_day.lower()
                    
                    if scheduled_day == research_day:
                        violations.append({
                            "lecturer": lecturer_code,
                            "class_id": entry.class_id,
                            "research_day": lecturer.research_day,
                            "scheduled_day": entry.time_slot.day,
                        })
        
        return violations
