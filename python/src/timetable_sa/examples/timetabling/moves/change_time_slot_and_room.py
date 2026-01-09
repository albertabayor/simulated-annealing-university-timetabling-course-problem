"""Move generator: Change Time Slot and Room.

Changes both time slot and room for a class in one move.
"""

import random
from typing import Optional

from timetable_sa.core.interfaces import MoveGenerator
from timetable_sa.examples.timetabling.domain_types.state import TimetableState, ScheduleEntry
from timetable_sa.examples.timetabling.domain_types.domain import TimeSlot
from timetable_sa.examples.timetabling.utils.time import calculate_end_time
from timetable_sa.examples.timetabling.utils.initial_solution import clone_state


class ChangeTimeSlotAndRoom(MoveGenerator):
    """Move generator that changes both time slot and room.
    
    This combined move can be more effective than separate moves
    when both time and room need to change simultaneously.
    
    Temperature-dependent behavior:
        - High temperature: Any slot and room combination
        - Low temperature: Prefer valid combinations
    """
    
    name: str = "Change Time Slot and Room"

    def can_apply(self, state: TimetableState) -> bool:
        """Check if this move can be applied."""
        return len(state.schedule) > 0 and len(state.available_time_slots) > 1 and len(state.rooms) > 1

    def generate(self, state: TimetableState, temperature: float) -> Optional[TimetableState]:
        """Generate a new state with time slot AND room changed."""
        if not self.can_apply(state):
            return None
        
        entry = random.choice(state.schedule)
        
        # Select new time slot
        new_slot = self._select_time_slot(state, entry, temperature)
        if new_slot is None:
            return None
        
        # Select new room
        new_room = self._select_room(state, entry, temperature)
        if new_room is None:
            return None
        
        new_state = clone_state(state)
        
        # Find and modify the entry
        for i, e in enumerate(new_state.schedule):
            if e.class_id == entry.class_id and e.kelas == entry.kelas:
                end_time, _ = calculate_end_time(new_slot.start_time, e.sks, new_slot.day)
                
                new_state.schedule[i] = ScheduleEntry(
                    class_id=e.class_id,
                    class_name=e.class_name,
                    kelas=e.kelas,
                    prodi=e.prodi,
                    lecturers=e.lecturers,
                    room=new_room.code,
                    time_slot=TimeSlot(
                        day=new_slot.day,
                        start_time=new_slot.start_time,
                        end_time=end_time,
                        period=new_slot.period
                    ),
                    sks=e.sks,
                    needs_lab=e.needs_lab,
                    participants=e.participants,
                    class_type=e.class_type,
                    prayer_time_added=e.prayer_time_added,
                    is_overflow_to_lab=e.is_overflow_to_lab,
                )
                break
        
        return new_state

    def _select_time_slot(self, state: TimetableState, current_entry: ScheduleEntry, temperature: float) -> Optional[TimeSlot]:
        """Select a new time slot."""
        available_slots = state.available_time_slots
        if not available_slots:
            return None
        
        return random.choice(available_slots)

    def _select_room(self, state: TimetableState, current_entry: ScheduleEntry, temperature: float):
        """Select a new room."""
        rooms = state.rooms
        if not rooms:
            return None
        
        return random.choice(rooms)
