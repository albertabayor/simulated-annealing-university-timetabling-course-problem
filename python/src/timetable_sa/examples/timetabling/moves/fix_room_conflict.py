"""Move generator: Fix Room Conflict.

Directly fixes a room conflict by moving one class to an available room/time.
"""

import random
from typing import Optional, List, Tuple

from timetable_sa.core.interfaces import MoveGenerator
from timetable_sa.examples.timetabling.domain_types.state import TimetableState, ScheduleEntry
from timetable_sa.examples.timetabling.domain_types.domain import TimeSlot
from timetable_sa.examples.timetabling.utils.time import calculate_end_time, time_to_minutes
from timetable_sa.examples.timetabling.utils.initial_solution import clone_state


class FixRoomConflict(MoveGenerator):
    """Move generator that directly fixes room conflicts.
    
    This is a targeted move that identifies room conflicts and
    moves one of the conflicting classes to a valid alternative.
    """
    
    name: str = "Fix Room Conflict"

    def can_apply(self, state: TimetableState) -> bool:
        """Check if this move can be applied."""
        return len(state.schedule) > 0

    def generate(self, state: TimetableState, temperature: float) -> Optional[TimetableState]:
        """Generate a new state with room conflict fixed."""
        if not self.can_apply(state):
            return None
        
        # Find room conflicts
        conflicts = self._find_room_conflicts(state)
        if not conflicts:
            return None
        
        # Pick a random conflict and move one class
        conflict = random.choice(conflicts)
        entry_to_move, conflicting_entries = conflict
        
        new_state = clone_state(state)
        
        # Find available alternative
        alternative = self._find_alternative(new_state, entry_to_move, conflicting_entries)
        if alternative is None:
            return None
        
        # Update the entry
        new_room, new_slot = alternative
        for i, e in enumerate(new_state.schedule):
            if e.class_id == entry_to_move.class_id and e.kelas == entry_to_move.kelas:
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

    def _find_room_conflicts(self, state: TimetableState) -> List[Tuple[ScheduleEntry, List[ScheduleEntry]]]:
        """Find room conflicts in the schedule."""
        conflicts = []
        
        # Group by (day, room)
        by_day_room: dict = {}
        for entry in state.schedule:
            key = (entry.time_slot.day, entry.room)
            if key not in by_day_room:
                by_day_room[key] = []
            by_day_room[key].append(entry)
        
        # Check for overlaps
        for (day, room), entries in by_day_room.items():
            if len(entries) < 2:
                continue
            
            sorted_entries = sorted(
                entries,
                key=lambda e: time_to_minutes(e.time_slot.start_time)
            )
            
            for i in range(len(sorted_entries) - 1):
                current = sorted_entries[i]
                for j in range(i + 1, len(sorted_entries)):
                    next_entry = sorted_entries[j]
                    if self._entries_overlap(current, next_entry):
                        conflicts.append((current, [next_entry]))
                        break
        
        return conflicts

    def _entries_overlap(self, entry1: ScheduleEntry, entry2: ScheduleEntry) -> bool:
        """Check if two entries overlap in time."""
        start1 = time_to_minutes(entry1.time_slot.start_time)
        end1 = time_to_minutes(entry1.time_slot.end_time)
        start2 = time_to_minutes(entry2.time_slot.start_time)
        end2 = time_to_minutes(entry2.time_slot.end_time)
        
        return max(start1, start2) < min(end1, end2)

    def _find_alternative(
        self, 
        state: TimetableState, 
        entry: ScheduleEntry,
        conflicting: List[ScheduleEntry]
    ) -> Optional[tuple]:
        """Find an available (room, slot) combination."""
        
        for slot in state.available_time_slots:
            for room in state.rooms:
                # Check if this combination is valid
                if room.capacity < entry.participants:
                    continue
                
                # Check if room is free at this time
                is_free = True
                for existing in state.schedule:
                    if (existing.room == room.code and 
                        existing.time_slot.day == slot.day and
                        existing.class_id != entry.class_id):
                        # Check time overlap
                        if self._time_overlap(slot, existing.time_slot):
                            is_free = False
                            break
                
                if is_free:
                    return (room, slot)
        
        return None

    def _time_overlap(self, slot1: TimeSlot, slot2: TimeSlot) -> bool:
        """Check if two time slots overlap."""
        if slot1.day != slot2.day:
            return False
        
        start1 = time_to_minutes(slot1.start_time)
        end1 = time_to_minutes(slot1.end_time)
        start2 = time_to_minutes(slot2.start_time)
        end2 = time_to_minutes(slot2.end_time)
        
        return max(start1, start2) < min(end1, end2)
