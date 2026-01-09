"""Evening class priority constraint."""

from typing import Literal, List
from timetable_sa.core.interfaces import Constraint
from timetable_sa.examples.timetabling.domain_types.state import TimetableState


class EveningClassPriority(Constraint):
    """Soft constraint that prefers scheduling certain classes in the evening.
    
    This is a soft constraint - it rewards evening scheduling for classes
    that should be in the evening but doesn't penalize other times heavily.
    """
    
    EVENING_START_PERIOD = 8
    
    name: str = "Evening Class Priority"
    type: Literal["hard", "soft"] = "soft"
    weight: float = 10.0
    
    def evaluate(self, state: TimetableState) -> float:
        """Check for classes that should be in evening but aren't.
        
        Args:
            state: Current timetable state
            
        Returns:
            1.0 if all evening classes are in evening, lower score otherwise
        """
        non_evening = self._find_non_evening(state)
        
        if not non_evening:
            return 1.0
        
        return 1.0 / (1 + len(non_evening) * 0.3)
    
    def _find_non_evening(self, state: TimetableState) -> List:
        """Find evening classes not scheduled in evening slots.
        
        Args:
            state: Current timetable state
            
        Returns:
            List of classes that should be in evening but aren't
        """
        non_evening = []
        
        for entry in state.schedule:
            if entry.class_type == "sore" and entry.time_slot.period < self.EVENING_START_PERIOD:
                non_evening.append({
                    "class_id": entry.class_id,
                    "current_period": entry.time_slot.period,
                    "suggested_period": self.EVENING_START_PERIOD
                })
        
        return non_evening
    
    def get_violations(self, state: TimetableState) -> List[str]:
        """Get list of evening class priority violations.
        
        Args:
            state: Current timetable state
            
        Returns:
            List of violation descriptions
        """
        non_evening = self._find_non_evening(state)
        descriptions = []
        
        for ne in non_evening:
            descriptions.append(
                f"Evening class {ne['class_id']} scheduled at period {ne['current_period']}, "
                f"should be in evening (period >= {ne['suggested_period']})"
            )
        
        return descriptions
    
    def describe(self, state: TimetableState) -> str | None:
        """Provide human-readable description of violations.
        
        Args:
            state: Current timetable state
            
        Returns:
            Description of violations, or None if satisfied
        """
        non_evening = self._find_non_evening(state)
        
        if not non_evening:
            return None
        
        return f"Found {len(non_evening)} evening class(es) not in evening slots"
