"""Move generator: Fix Lecturer Conflict.

Directly fixes a lecturer conflict by moving one class to a different time.
"""

import random
from typing import Optional, List, Tuple

from timetable_sa.core.interfaces import MoveGenerator
from timetable_sa.examples.timetabling.domain_types.state import TimetableState, ScheduleEntry
from timetable_sa.examples.timetabling.domain_types.domain import TimeSlot
from timetable_sa.examples.timetabling.utils.time import calculate_end_time, time_to_minutes
from timetable_sa.examples.timetabling.utils.initial_solution import clone_state


class FixLecturerConflict(MoveGenerator):
    """Move generator that directly fixes lecturer conflicts.
    
    This targeted move identifies lecturer double-bookings and
    moves one class to eliminate the conflict.
    """
    
    name: str = "Fix Lecturer Conflict"

    def can_apply(self, state: TimetableState) -> bool:
        """Check if this move can be applied."""
        return len(state.schedule) > 0

    def generate(self, state: TimetableState, temperature: float) -> Optional[TimetableState]:
        """Generate a new state with lecturer conflict fixed."""
        if not self.can_apply(state):
            return None
        
        conflicts = self._find_lecturer_conflicts(state)
        if not conflicts:
            return None
        
        # Pick a random conflict
        conflict = random.choice(conflicts)
        entry_to_move, lecturer = conflict
        
        new_state = clone_state(state)
        
        # Find available time slot
        alternative = self._find_alternative(new_state, entry_to_move, lecturer)
        if alternative is None:
            return None
        
        new_slot = alternative
        
        # Update the entry
        for i, e in enumerate(new_state.schedule):
            if e.class_id == entry_to_move.class_id and e.kelas == entry_to_move.kelas:
                end_time, _ = calculate_end_time(new_slot.start_time, e.sks, new_slot.day)
                
                new_state.schedule[i] = ScheduleEntry(
                    class_id=e.class_id,
                    class_name=e.class_name,
                    kelas=e.kelas,
                    prodi=e.prodi,
                    lecturers=e.lecturers,
                    room=e.room,
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

    def _find_lecturer_conflicts(self, state: TimetableState) -> List[Tuple[ScheduleEntry, str]]:
        """Find lecturer conflicts."""
        conflicts = []
        
        lecturer_entries: dict = {}
        for entry in state.schedule:
            for lecturer in entry.lecturers:
                key = (lecturer, entry.time_slot.day)
                if key not in lecturer_entries:
                    lecturer_entries[key] = []
                lecturer_entries[key].append(entry)
        
        for (lecturer, day), entries in lecturer_entries.items():
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
                        conflicts.append((current, lecturer))
                        break
        
        return conflicts

    def _entries_overlap(self, entry1: ScheduleEntry, entry2: ScheduleEntry) -> bool:
        """Check if two entries overlap."""
        start1 = time_to_minutes(entry1.time_slot.start_time)
        end1 = time_to_minutes(entry1.time_slot.end_time)
        start2 = time_to_minutes(entry2.time_slot.start_time)
        end2 = time_to_minutes(entry2.time_slot.end_time)
        
        return max(start1, start2) < min(end1, end2)

    def _find_alternative(
        self, 
        state: TimetableState, 
        entry: ScheduleEntry,
        lecturer: str
    ) -> Optional[TimeSlot]:
        """Find an available time slot for the entry."""
        for slot in state.available_time_slots:
            # Check if lecturer is free at this time
            is_free = True
            for existing in state.schedule:
                if (lecturer in existing.lecturers and 
                    existing.time_slot.day == slot.day and
                    existing.class_id != entry.class_id):
                    if self._time_overlap(slot, existing.time_slot):
                        is_free = False
                        break
            
            if is_free:
                return slot
        
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
