"""Hard constraint: Room Capacity.

Ensures class participants do not exceed room capacity.
"""

from typing import Literal, List

from timetable_sa.core.interfaces import Constraint
from timetable_sa.examples.timetabling.domain_types.state import TimetableState, ScheduleEntry
from timetable_sa.examples.timetabling.domain_types.domain import Room


class RoomCapacity(Constraint):
    """Hard constraint: Class participants must not exceed room capacity.
    
    This ensures that classes are assigned to rooms that can accommodate
    all registered students.
    
    Examples of violations:
        - Class with 35 students in Room with capacity 30
        - Large lecture in small seminar room
    """
    
    name: str = "Room Capacity"
    type: Literal["hard", "soft"] = "hard"

    def evaluate(self, state: TimetableState) -> float:
        """Evaluate the constraint.
        
        Returns:
            1.0 if all classes fit in their rooms, lower score otherwise
        """
        violations = self._find_violations(state)
        
        if not violations:
            return 1.0
        
        return 1.0 / (1 + len(violations))

    def get_violations(self, state: TimetableState) -> List[str]:
        """Get detailed list of capacity violations.
        
        Returns:
            List of violation descriptions
        """
        violations = self._find_violations(state)
        descriptions = []
        
        for entry, room in violations:
            overflow = entry.participants - room.capacity
            descriptions.append(
                f"Class {entry.class_id} ({entry.kelas}) has {entry.participants} students "
                f"but room {room.code} capacity is {room.capacity} (overflow: {overflow})"
            )
        
        return descriptions

    def _find_violations(self, state: TimetableState) -> List[tuple[ScheduleEntry, Room]]:
        """Find all capacity violations.
        
        Returns:
            List of (entry, room) tuples where capacity is exceeded
        """
        violations = []
        
        # Build room lookup
        room_by_code = {r.code: r for r in state.rooms}
        
        for entry in state.schedule:
            room = room_by_code.get(entry.room)
            if room and entry.participants > room.capacity:
                violations.append((entry, room))
        
        return violations
