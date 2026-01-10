"""Move generator: Change Time Slot.

Changes a class's time slot to a different available slot.
"""

import random
from typing import Optional

from timetable_sa.core.interfaces import MoveGenerator
from timetable_sa.examples.timetabling.domain_types.state import TimetableState, ScheduleEntry
from timetable_sa.examples.timetabling.domain_types.domain import TimeSlot
from timetable_sa.examples.timetabling.utils.time import calculate_end_time, time_to_minutes
from timetable_sa.examples.timetabling.utils.class_helper import has_class_overlap


class ChangeTimeSlot(MoveGenerator):
    """Move generator that changes a class's time slot.

    This is a fundamental move that allows the algorithm to explore
    different time assignments for classes.

    Temperature-dependent behavior:
        - High temperature: Random slot from all available valid slots
        - Medium temperature: Prefer nearby periods
        - Low temperature: Prefer same period or adjacent periods

    IMPORTANT: Now validates time slots BEFORE selecting (matching TypeScript behavior).
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

        # Get VALID time slots first (filter by constraints)
        valid_slots = self._get_valid_time_slots(state, entry)

        if not valid_slots:
            return None

        # Select from valid time slots based on temperature
        new_slot = self._select_time_slot_from_valid(state, entry, valid_slots, temperature)

        if new_slot is None:
            return None

        # Create new state
        from timetable_sa.examples.timetabling.utils.initial_solution import clone_state
        new_state = clone_state(state)

        # Find and modify the entry
        for i, e in enumerate(new_state.schedule):
            if e.class_id == entry.class_id and e.kelas == entry.kelas:
                end_time, prayer_time_added = calculate_end_time(new_slot.start_time, e.sks, new_slot.day)

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
                    prayer_time_added=prayer_time_added,
                    is_overflow_to_lab=e.is_overflow_to_lab,
                )
                break

        return new_state

    def _get_valid_time_slots(
        self,
        state: TimetableState,
        entry: ScheduleEntry
    ) -> list[TimeSlot]:
        """Get list of valid time slots for an entry (filtered by constraints).

        This matches TypeScript's validation logic:
        1. Check class type (pagi vs sore)
        2. Check room availability at time slot
        3. Check lecturer availability at time slot
        4. Check prodi/class conflicts at time slot

        Args:
            state: Current timetable state
            entry: Schedule entry to find valid time slots for

        Returns:
            List of valid TimeSlot objects
        """
        valid_slots = []

        for time_slot in state.available_time_slots:
            # 1. Check class type (pagi vs sore)
            # Constraint: pagi < 15:30, sore >= 15:30
            if entry.class_type.lower() == 'sore':
                # Evening class should start at 15:30 or later
                if time_to_minutes(time_slot.start_time) < time_to_minutes("15:30"):
                    continue
            else:
                # Morning class should start before 15:30
                if time_to_minutes(time_slot.start_time) >= time_to_minutes("15:30"):
                    continue

            # 2. Check room availability at this time slot
            if not self._is_room_available_at_time(state, entry.room, time_slot, entry.sks, exclude_class_id=entry.class_id):
                continue

            # 3. Check lecturer availability at this time slot
            if not self._are_lecturers_available_at_time(state, entry.lecturers, time_slot, entry.sks, exclude_class_id=entry.class_id):
                continue

            # 4. Check prodi/class conflicts at this time slot
            if not self._is_prodi_slot_available(state, entry.prodi, entry.kelas, time_slot, entry.sks, exclude_class_id=entry.class_id):
                continue

            valid_slots.append(time_slot)

        return valid_slots

    def _is_room_available_at_time(
        self,
        state: TimetableState,
        room_code: str,
        time_slot: TimeSlot,
        sks: int,
        exclude_class_id: str | None = None
    ) -> bool:
        """Check if a room is available at a given time slot."""
        other_schedule = [
            e for e in state.schedule
            if not (e.class_id == exclude_class_id and e.kelas == getattr(e, 'kelas', ''))
        ]

        end_time, _ = calculate_end_time(time_slot.start_time, sks, time_slot.day)
        new_start = time_to_minutes(time_slot.start_time)
        new_end = time_to_minutes(end_time)

        for other in other_schedule:
            if other.room != room_code:
                continue
            if other.time_slot.day != time_slot.day:
                continue

            other_end_time, _ = calculate_end_time(other.time_slot.start_time, other.sks, other.time_slot.day)
            other_start = time_to_minutes(other.time_slot.start_time)
            other_end = time_to_minutes(other_end_time)

            if new_start < other_end and other_start < new_end:
                return False

        return True

    def _are_lecturers_available_at_time(
        self,
        state: TimetableState,
        lecturers: list,
        time_slot: TimeSlot,
        sks: int,
        exclude_class_id: str | None = None
    ) -> bool:
        """Check if all lecturers are available at a given time slot."""
        other_schedule = [
            e for e in state.schedule
            if not (e.class_id == exclude_class_id and e.kelas == getattr(e, 'kelas', ''))
        ]

        end_time, _ = calculate_end_time(time_slot.start_time, sks, time_slot.day)
        new_start = time_to_minutes(time_slot.start_time)
        new_end = time_to_minutes(end_time)

        for other in other_schedule:
            # Check if any lecturer is shared
            if not any(lect in other.lecturers for lect in lecturers):
                continue
            if other.time_slot.day != time_slot.day:
                continue

            other_end_time, _ = calculate_end_time(other.time_slot.start_time, other.sks, other.time_slot.day)
            other_start = time_to_minutes(other.time_slot.start_time)
            other_end = time_to_minutes(other_end_time)

            if new_start < other_end and other_start < new_end:
                return False  # Lecturer conflict

        return True

    def _is_prodi_slot_available(
        self,
        state: TimetableState,
        prodi: str,
        kelas: str,
        time_slot: TimeSlot,
        sks: int,
        exclude_class_id: str | None = None
    ) -> bool:
        """Check if prodi/class has no conflicts at a given time slot."""
        other_schedule = [
            e for e in state.schedule
            if not (e.class_id == exclude_class_id and e.kelas == getattr(e, 'kelas', ''))
        ]

        end_time, _ = calculate_end_time(time_slot.start_time, sks, time_slot.day)
        new_start = time_to_minutes(time_slot.start_time)
        new_end = time_to_minutes(end_time)

        for other in other_schedule:
            # Check if same prodi and overlapping class
            if other.prodi != prodi:
                continue
            if not has_class_overlap(kelas, other.kelas):
                continue
            if other.time_slot.day != time_slot.day:
                continue

            other_end_time, _ = calculate_end_time(other.time_slot.start_time, other.sks, other.time_slot.day)
            other_start = time_to_minutes(other.time_slot.start_time)
            other_end = time_to_minutes(other_end_time)

            if new_start < other_end and other_start < new_end:
                return False  # Prodi/class conflict

        return True

    def _select_time_slot_from_valid(
        self,
        state: TimetableState,
        entry: ScheduleEntry,
        valid_slots: list[TimeSlot],
        temperature: float
    ) -> Optional[TimeSlot]:
        """Select a time slot from valid slots based on temperature.

        Args:
            state: Current timetable state
            entry: Current schedule entry
            valid_slots: List of pre-filtered valid time slots
            temperature: Current annealing temperature

        Returns:
            Selected TimeSlot object or None
        """
        if not valid_slots:
            return None

        current_period = entry.time_slot.period
        current_day = entry.time_slot.day

        if temperature > 10000:
            # HIGH TEMPERATURE: Pure random exploration
            return random.choice(valid_slots)

        elif temperature > 1000:
            # MEDIUM TEMPERATURE: Mostly random with slight preference for nearby periods
            # 70% chance of same period range
            if random.random() < 0.7:
                nearby_slots = [
                    s for s in valid_slots
                    if abs(s.period - current_period) <= 3
                ]
                if nearby_slots:
                    return random.choice(nearby_slots)
            return random.choice(valid_slots)

        else:
            # LOW TEMPERATURE: Exploitation - prefer same day/adjacent periods
            # Prefer same day
            same_day_slots = [
                s for s in valid_slots
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

            return random.choice(valid_slots)
