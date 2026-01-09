"""Move generator: Fix Room Capacity.

Moves a class that exceeds room capacity to a larger room.
"""

import random
from typing import Optional

from timetable_sa.core.interfaces import MoveGenerator
from timetable_sa.examples.timetabling.domain_types.state import TimetableState, ScheduleEntry
from timetable_sa.examples.timetabling.utils.initial_solution import clone_state


class FixRoomCapacity(MoveGenerator):
    """Move generator that fixes capacity violations.
    
    This move identifies classes in rooms that are too small
    and moves them to rooms with adequate capacity.
    """
    
    name: str = "Fix Room Capacity"

    def can_apply(self, state: TimetableState) -> bool:
        """Check if this move can be applied."""
        return len(state.schedule) > 0 and len(state.rooms) > 1

    def generate(self, state: TimetableState, temperature: float) -> Optional[TimetableState]:
        """Generate a new state with capacity violation fixed."""
        if not self.can_apply(state):
            return None
        
        # Find capacity violations
        violations = self._find_violations(state)
        if not violations:
            return None
        
        # Pick a random violation
        entry = random.choice(violations)
        
        new_state = clone_state(state)
        
        # Find a larger room
        larger_room = self._find_larger_room(state, entry)
        if larger_room is None:
            return None
        
        # Update the entry
        for i, e in enumerate(new_state.schedule):
            if e.class_id == entry.class_id and e.kelas == entry.kelas:
                new_state.schedule[i] = ScheduleEntry(
                    class_id=e.class_id,
                    class_name=e.class_name,
                    kelas=e.kelas,
                    prodi=e.prodi,
                    lecturers=e.lecturers,
                    room=larger_room.code,
                    time_slot=e.time_slot,
                    sks=e.sks,
                    needs_lab=e.needs_lab,
                    participants=e.participants,
                    class_type=e.class_type,
                    prayer_time_added=e.prayer_time_added,
                    is_overflow_to_lab=e.is_overflow_to_lab,
                )
                break
        
        return new_state

    def _find_violations(self, state: TimetableState) -> list[ScheduleEntry]:
        """Find classes that exceed their room capacity."""
        violations = []
        
        room_by_code = {r.code: r for r in state.rooms}
        
        for entry in state.schedule:
            room = room_by_code.get(entry.room)
            if room and entry.participants > room.capacity:
                violations.append(entry)
        
        return violations

    def _find_larger_room(self, state: TimetableState, entry: ScheduleEntry):
        """Find a room with adequate capacity."""
        
        # Filter rooms that can accommodate the class
        suitable = [r for r in state.rooms if r.capacity >= entry.participants]
        
        if not suitable:
            return None
        
        # Sort by capacity (prefer closest fit)
        suitable.sort(key=lambda r: r.capacity)
        
        return suitable[0] if suitable else None
