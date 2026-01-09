"""Move generator: Change Room.

Changes a class's room assignment to a different room.
"""

import random
from typing import Optional

from timetable_sa.core.interfaces import MoveGenerator
from timetable_sa.examples.timetabling.domain_types.state import TimetableState, ScheduleEntry


class ChangeRoom(MoveGenerator):
    """Move generator that changes a class's room.
    
    This move helps optimize room utilization and handle capacity constraints.
    
    Temperature-dependent behavior:
        - High temperature: Any room (random)
        - Medium temperature: Prefer rooms of same type
        - Low temperature: Prefer rooms with capacity matching class size
    """
    
    name: str = "Change Room"

    def can_apply(self, state: TimetableState) -> bool:
        """Check if this move can be applied."""
        return len(state.schedule) > 0 and len(state.rooms) > 1

    def generate(self, state: TimetableState, temperature: float) -> Optional[TimetableState]:
        """Generate a new state with one class's room changed.
        
        Args:
            state: Current timetable state
            temperature: Current annealing temperature
        
        Returns:
            New state with one room change, or None if cannot apply
        """
        if not self.can_apply(state):
            return None
        
        # Select a random class to modify
        entry = random.choice(state.schedule)
        
        # Select new room based on temperature
        new_room = self._select_room(state, entry, temperature)
        
        if new_room is None or new_room.code == entry.room:
            return None
        
        # Create new state
        from timetable_sa.examples.timetabling.utils.initial_solution import clone_state
        new_state = clone_state(state)
        
        # Find and modify the entry
        for i, e in enumerate(new_state.schedule):
            if e.class_id == entry.class_id and e.kelas == entry.kelas:
                new_state.schedule[i] = ScheduleEntry(
                    class_id=e.class_id,
                    class_name=e.class_name,
                    kelas=e.kelas,
                    prodi=e.prodi,
                    lecturers=e.lecturers,
                    room=new_room.code,
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

    def _select_room(
        self, 
        state: TimetableState, 
        current_entry: ScheduleEntry,
        temperature: float
    ):
        """Select a new room based on temperature and constraints."""
        rooms = state.rooms
        
        if not rooms:
            return None
        
        if temperature > 10000:
            # High temperature: Pure random
            return random.choice(rooms)
        
        elif temperature > 1000:
            # Medium temperature: Prefer same type room
            current_room = next((r for r in rooms if r.code == current_entry.room), None)
            if current_room:
                same_type = [r for r in rooms if r.type == current_room.type]
                if same_type and random.random() < 0.7:
                    return random.choice(same_type)
            
            return random.choice(rooms)
        
        else:
            # Low temperature: Prefer capacity-matching room
            participants = current_entry.participants
            
            # Find rooms with capacity >= participants
            suitable = [r for r in rooms if r.capacity >= participants]
            
            if suitable:
                # Prefer closest capacity match
                suitable.sort(key=lambda r: r.capacity - participants)
                # Add some randomness
                if random.random() < 0.7:
                    return suitable[0]
            
            return random.choice(rooms)
