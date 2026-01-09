"""Move generator to swap Friday classes with non-Friday days."""

import random
from typing import Optional
from timetable_sa.core.interfaces import MoveGenerator
from timetable_sa.examples.timetabling.domain_types.state import TimetableState, ScheduleEntry
from timetable_sa.examples.timetabling.domain_types.domain import TimeSlot
from timetable_sa.examples.timetabling.utils.initial_solution import clone_state


class SwapFridayWithNonFriday(MoveGenerator):
    """Move generator that moves Friday classes to non-Friday days.
    
    This is a targeted move generator for fixing Friday-related violations.
    """
    
    name: str = "Swap Friday With Non Friday"
    
    def __init__(self, target_days: Optional[list[str]] = None):
        """Initialize swap Friday with non-Friday move generator.
        
        Args:
            target_days: List of non-Friday days to consider (default: all except Friday)
        """
        self.target_days = target_days or [
            "Monday", "Tuesday", "Wednesday", "Thursday"
        ]
    
    def can_apply(self, state: TimetableState) -> bool:
        """Check if this move can be applied."""
        return any(
            entry.time_slot.day == "Friday"
            for entry in state.schedule
        )
    
    def generate(self, state: TimetableState, temperature: float) -> Optional[TimetableState]:
        """Generate a new state with a Friday class moved to a non-Friday day.
        
        Args:
            state: Current timetable state
            temperature: Current annealing temperature
            
        Returns:
            New state with Friday class moved, or None if cannot apply
        """
        if not self.can_apply(state):
            return None
        
        friday_entries = [
            entry for entry in state.schedule
            if entry.time_slot.day == "Friday"
        ]
        
        entry = random.choice(friday_entries)
        
        available_slots = []
        for day in self.target_days:
            for period in range(1, 13):
                new_time_slot = next(
                    (slot for slot in state.available_time_slots 
                     if slot.day == day and slot.period == period),
                    None
                )
                if new_time_slot:
                    is_available = not any(
                        e.room == entry.room and
                        e.time_slot.day == day and
                        e.time_slot.period == period
                        for e in state.schedule
                    )
                    
                    lecturer_available = not any(
                        e.lecturers[0] if e.lecturers else None == entry.lecturers[0] if entry.lecturers else None and
                        e.time_slot.day == day and
                        e.time_slot.period == period
                        for e in state.schedule
                    )
                    
                    prodi_available = not any(
                        e.prodi == entry.prodi and
                        e.time_slot.day == day and
                        e.time_slot.period == period
                        for e in state.schedule
                    )
                    
                    if is_available and lecturer_available and prodi_available:
                        available_slots.append(new_time_slot)
        
        if not available_slots:
            return None
        
        new_time_slot = random.choice(available_slots)
        new_state = clone_state(state)
        
        for i, e in enumerate(new_state.schedule):
            if e.class_id == entry.class_id and e.kelas == entry.kelas:
                from timetable_sa.examples.timetabling.utils.time import calculate_end_time
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
