"""Move generator to fix Friday prayer time conflicts."""

import random
from typing import Optional
from timetable_sa.core.interfaces import MoveGenerator
from timetable_sa.examples.timetabling.domain_types.state import TimetableState, ScheduleEntry
from timetable_sa.examples.timetabling.domain_types.domain import TimeSlot
from timetable_sa.examples.timetabling.utils.prayer_times import FRIDAY_PRAYER_PERIODS
from timetable_sa.examples.timetabling.utils.time import calculate_end_time
from timetable_sa.examples.timetabling.utils.initial_solution import clone_state


class FixFridayPrayerConflict(MoveGenerator):
    """Move generator that relocates classes from Friday prayer times.
    
    This targets classes scheduled during Friday prayer periods and
    moves them to non-prayer times on the same day or other days.
    """
    
    name: str = "Fix Friday Prayer Conflict"
    
    def __init__(self, prefer_same_day: bool = True):
        """Initialize fix Friday prayer conflict move generator.
        
        Args:
            prefer_same_day: Whether to prefer same-day relocation
        """
        self.prefer_same_day = prefer_same_day
    
    def can_apply(self, state: TimetableState) -> bool:
        """Check if this move can be applied."""
        return any(
            self._is_in_friday_prayer(entry)
            for entry in state.schedule
        )
    
    def generate(self, state: TimetableState, temperature: float) -> Optional[TimetableState]:
        """Generate a new state with Friday prayer conflict fixed."""
        if not self.can_apply(state):
            return None
        
        conflicting_entries = [
            entry for entry in state.schedule
            if self._is_in_friday_prayer(entry)
        ]
        
        entry = random.choice(conflicting_entries)
        new_time_slots = self._find_alternative_slots(entry, state)
        
        if not new_time_slots:
            return None
        
        new_time_slot = random.choice(new_time_slots)
        new_state = clone_state(state)
        
        for i, e in enumerate(new_state.schedule):
            if e.class_id == entry.class_id and e.kelas == entry.kelas:
                end_time, _ = calculate_end_time(new_time_slot.start_time, e.sks, new_time_slot.day)
                
                new_state.schedule[i] = ScheduleEntry(
                    class_id=e.class_id,
                    class_name=e.class_name,
                    kelas=e.kelas,
                    prodi=e.prodi,
                    lecturers=e.lecturers,
                    room=e.room,
                    time_slot=TimeSlot(
                        day=new_time_slot.day,
                        start_time=new_time_slot.start_time,
                        end_time=end_time,
                        period=new_time_slot.period
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
    
    def _is_in_friday_prayer(self, entry: ScheduleEntry) -> bool:
        """Check if entry is during Friday prayer time."""
        if entry.time_slot.day != "Friday":
            return False
        
        for prayer_info in FRIDAY_PRAYER_PERIODS:
            if prayer_info["start_period"] <= entry.time_slot.period <= prayer_info["end_period"]:
                return True
        
        return False
    
    def _find_alternative_slots(self, entry: ScheduleEntry, state: TimetableState) -> list:
        """Find alternative time slots for the entry."""
        alternatives = []
        
        if self.prefer_same_day:
            friday_non_prayer = self._get_available_slots(
                entry, state, "Friday", exclude_prayer=True
            )
            alternatives.extend(friday_non_prayer)
        
        other_days = ["Monday", "Tuesday", "Wednesday", "Thursday"]
        for day in other_days:
            day_slots = self._get_available_slots(entry, state, day)
            alternatives.extend(day_slots)
        
        return alternatives
    
    def _get_available_slots(
        self,
        entry: ScheduleEntry,
        state: TimetableState,
        day: str,
        exclude_prayer: bool = False
    ) -> list:
        """Get available time slots for a given day."""
        available = []
        
        for period in range(1, 13):
            if exclude_prayer and day == "Friday":
                in_prayer = any(
                    p["start_period"] <= period <= p["end_period"]
                    for p in FRIDAY_PRAYER_PERIODS
                )
                if in_prayer:
                    continue
            
            for slot in state.available_time_slots:
                if slot.day != day or slot.period != period:
                    continue
                
                room_conflict = any(
                    e.room == entry.room and
                    e.time_slot.day == day and
                    e.time_slot.period == period
                    for e in state.schedule
                )
                
                lecturer_conflict = any(
                    e.lecturers and entry.lecturers and
                    e.lecturers[0] == entry.lecturers[0] and
                    e.time_slot.day == day and
                    e.time_slot.period == period
                    for e in state.schedule
                )
                
                prodi_conflict = any(
                    e.prodi == entry.prodi and
                    e.time_slot.day == day and
                    e.time_slot.period == period
                    for e in state.schedule
                )
                
                if not room_conflict and not lecturer_conflict and not prodi_conflict:
                    available.append(slot)
        
        return available
