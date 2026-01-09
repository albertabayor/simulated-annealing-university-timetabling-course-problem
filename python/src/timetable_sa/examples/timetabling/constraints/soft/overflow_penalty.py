"""Soft constraint: Overflow Penalty.

Penalizes non-lab classes that are assigned to lab rooms.
"""

from typing import Literal, List

from timetable_sa.core.interfaces import Constraint
from timetable_sa.examples.timetabling.domain_types.state import TimetableState, ScheduleEntry


class OverflowPenalty(Constraint):
    """Soft constraint: Penalize non-lab classes in lab rooms.
    
    Lab rooms are specialized and expensive resources. This constraint
    penalizes scheduling non-lab ("theory") classes in lab rooms,
    freeing up labs for classes that actually need them.
    
    Examples of violations:
        - Theory class in Computer Lab
        - Lecture in chemistry lab
    """
    
    name: str = "Overflow Penalty"
    type: Literal["hard", "soft"] = "soft"
    weight: float = 3.0

    def __init__(self, weight: float = 3.0):
        self.name = "Overflow Penalty"
        self.type = "soft"
        self.weight = weight

    def evaluate(self, state: TimetableState) -> float:
        """Evaluate the constraint.
        
        Returns:
            1.0 if no overflow, lower score for overflow assignments
        """
        overflow_count = self._count_overflow(state)
        
        if overflow_count == 0:
            return 1.0
        
        return 1.0 / (1 + overflow_count)

    def get_violations(self, state: TimetableState) -> List[str]:
        """Get list of overflow assignments.
        
        Returns:
            List of violation descriptions
        """
        violations = self._find_violations(state)
        descriptions = []
        
        for entry, room_info in violations:
            descriptions.append(
                f"Class {entry.class_id} ({entry.kelas}) is a {'' if entry.needs_lab else 'non-'}lab "
                f"class assigned to lab room {room_info['code']}"
            )
        
        return descriptions

    def _find_violations(self, state: TimetableState) -> List[tuple[ScheduleEntry, dict]]:
        """Find all overflow assignments (non-lab in lab rooms).
        
        Matches TypeScript's isOverflowToLab check:
        - Lab classes: !entry.needsLab
        - Lab rooms: entry.isOverflowToLab or room type contains 'lab'
        - Lab classes in lab rooms: needsLab AND (isOverflowToLab OR isLabRoom)
        
        Returns:
            List of (entry, room info) tuples
        """
        violations = []
        
        # Build room lookup
        room_by_code = {r.code: r for r in state.rooms}
        
        for entry in state.schedule:
            room = room_by_code.get(entry.room)
            
            if not room:
                continue
            
            # Check if room is lab (Type includes 'lab' or LAB_ROOMS includes code)
            room_is_lab = room.type.lower() in ["lab", "laboratory", "labs"] 
            
            class_needs_lab = entry.needs_lab
            
            # Overflow: lab class in lab room OR non-lab class using lab room
            is_overflow = (room_is_lab or entry.is_overflow_to_lab) and not class_needs_lab
            
            if is_overflow:
                violations.append((entry, {"code": room.code, "type": room.type}))
        
        return violations

    def _count_overflow(self, state: TimetableState) -> int:
        """Count the number of overflow assignments."""
        return len(self._find_violations(state))
