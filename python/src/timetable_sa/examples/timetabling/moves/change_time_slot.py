"""Move generator: Change Time Slot.

Changes a class's time slot to a different available slot.
"""

import random
from typing import Optional

from timetable_sa.core.interfaces import MoveGenerator
from timetable_sa.examples.timetabling.domain_types.state import TimetableState, ScheduleEntry
from timetable_sa.examples.timetabling.domain_types.domain import TimeSlot


class ChangeTimeSlot(MoveGenerator):
    """Move generator that changes a class's time slot.
    
    This is a fundamental move that allows the algorithm to explore
    different time assignments for classes.
    
    Temperature-dependent behavior:
        - High temperature: Random slot from all available
        - Medium temperature: Prefer nearby periods
        - Low temperature: Prefer same period or adjacent periods
    """
    
    name: str = "Change Time Slot"

    def can_apply(self, state: TimetableState) -> bool:
        """Check if this move can be applied."""
        return len(state.schedule) > 0 and len(state.available_time_slots) > 1

    def generate(self, state: TimetableState, temperature: float) -> Optional[TimetableState]:
        """Generate a new state with one class's time slot changed.

        Args:
            state: Current timetable state
            temperature: Current annealing temperature

        Returns:
            New state with one time slot change, or None if cannot apply
        """
        if not self.can_apply(state):
            return None

        # Select a random class to modify
        entry = random.choice(state.schedule)

        # Select new time slot based on temperature
        new_slot = self._select_time_slot(state, entry, temperature)

        if new_slot is None:
            return None

        # Create new state
        from timetable_sa.examples.timetabling.utils.initial_solution import clone_state
        new_state = clone_state(state)

        # Find and modify the entry
        for i, e in enumerate(new_state.schedule):
            if e.class_id == entry.class_id and e.kelas == entry.kelas:
                # Calculate new end time
                from timetable_sa.examples.timetabling.utils.time import calculate_end_time
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

    def _select_time_slot(
        self,
        state: TimetableState,
        current_entry: ScheduleEntry,
        temperature: float
    ) -> Optional[TimeSlot]:
        """Select a new time slot based on temperature."""
        available_slots = state.available_time_slots

        if not available_slots:
            return None

        if temperature > 10000:
            # High temperature: Pure random exploration
            return random.choice(available_slots)
        
        elif temperature > 1000:
            # Medium temperature: Mostly random with slight preference for same period
            current_period = current_entry.time_slot.period
            
            # 70% chance of same period range
            if random.random() < 0.7:
                same_period_slots = [
                    s for s in available_slots 
                    if abs(s.period - current_period) <= 3
                ]
                if same_period_slots:
                    return random.choice(same_period_slots)
            
            return random.choice(available_slots)
        
        else:
            # Low temperature: Exploitation - prefer same day/adjacent periods
            current_day = current_entry.time_slot.day
            current_period = current_entry.time_slot.period
            
            # Prefer same day
            same_day_slots = [
                s for s in available_slots 
                if s.day == current_day
            ]
            
            if same_day_slots:
                # Prefer nearby periods
                nearby_slots = [
                    s for s in same_day_slots 
                    if abs(s.period - current_period) <= 2
                ]
                if nearby_slots:
                    return random.choice(nearby_slots)
                return random.choice(same_day_slots)
            
            return random.choice(available_slots)
