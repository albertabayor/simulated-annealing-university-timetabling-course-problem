"""Exclusive room constraint."""

from typing import Literal, List
from timetable_sa.core.interfaces import Constraint
from timetable_sa.examples.timetabling.domain_types.state import TimetableState


class ExclusiveRoom(Constraint):
    """Constraint for rooms that can only be used by specific programs.
    
    This is a hard constraint - unauthorized room usage is not allowed.
    """
    
    name: str = "Exclusive Room"
    type: Literal["hard", "soft"] = "hard"
    
    def __init__(self, exclusive_assignments: dict[str, List[str]]):
        """Initialize exclusive room constraint.
        
        Args:
            exclusive_assignments: Dict mapping room codes to list of allowed prodi codes
        """
        self.exclusive_assignments = exclusive_assignments
    
    def evaluate(self, state: TimetableState) -> float:
        """Check if rooms are used by authorized programs only.
        
        Args:
            state: Current timetable state
            
        Returns:
            1.0 if all assignments are authorized, lower score otherwise
        """
        violations = self._find_violations(state)
        
        if not violations:
            return 1.0
        
        return 1.0 / (1 + len(violations))
    
    def _find_violations(self, state: TimetableState) -> List:
        """Find unauthorized room assignments.
        
        Args:
            state: Current timetable state
            
        Returns:
            List of violation details
        """
        violations = []
        
        for entry in state.schedule:
            room_code = entry.room
            prodi_code = entry.prodi
            
            if room_code in self.exclusive_assignments:
                allowed_prodis = self.exclusive_assignments[room_code]
                if prodi_code not in allowed_prodis:
                    violations.append({
                        "class_id": entry.class_id,
                        "room": room_code,
                        "prodi": prodi_code,
                        "allowed_prodis": allowed_prodis
                    })
        
        return violations
    
    def get_violations(self, state: TimetableState) -> List[str]:
        """Get list of exclusive room violations.
        
        Args:
            state: Current timetable state
            
        Returns:
            List of violation descriptions
        """
        violations = self._find_violations(state)
        descriptions = []
        
        for v in violations:
            descriptions.append(
                f"Class {v['class_id']} from prodi {v['prodi']} assigned to "
                f"room {v['room']} which is exclusive to: {', '.join(v['allowed_prodis'])}"
            )
        
        return descriptions
    
    def describe(self, state: TimetableState) -> str | None:
        """Provide human-readable description of violations.
        
        Args:
            state: Current timetable state
            
        Returns:
            Description of violations, or None if satisfied
        """
        violations = self._find_violations(state)
        
        if not violations:
            return None
        
        return f"Found {len(violations)} unauthorized room assignment(s)"
