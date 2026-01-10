"""Move generator: Change Time Slot and Room.

Changes both time slot and room for a class in one move.
"""

import random
from typing import Optional, NamedTuple

from timetable_sa.core.interfaces import MoveGenerator
from timetable_sa.examples.timetabling.domain_types.state import TimetableState, ScheduleEntry
from timetable_sa.examples.timetabling.domain_types.domain import TimeSlot
from timetable_sa.examples.timetabling.utils.time import calculate_end_time, time_to_minutes
from timetable_sa.examples.timetabling.utils.class_helper import has_class_overlap


class TimeSlotRoomCombo(NamedTuple):
    """A validated time slot and room combination."""
    time_slot: TimeSlot
    room_code: str
    room_type: str
    capacity: int


class ChangeTimeSlotAndRoom(MoveGenerator):
    """Move generator that changes both time slot and room.

    This combined move can be more effective than separate moves
    when both time and room need to change simultaneously.

    Temperature-dependent behavior:
        - High temperature: Any valid combination (exploration)
        - Medium temperature: Prefer different days
        - Low temperature: Prefer nearby slots and similar rooms (exploitation)

    IMPORTANT: Now validates combinations BEFORE selecting (matching TypeScript behavior).
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

        # Get ALL valid (time slot, room) combinations
        combinations = self._get_valid_combinations(state, entry)

        if not combinations:
            return None

        # Select from valid combinations based on temperature
        selected_combo = self._select_combination(state, entry, combinations, temperature)

        if selected_combo is None:
            return None

        # Create new state
        from timetable_sa.examples.timetabling.utils.initial_solution import clone_state
        new_state = clone_state(state)

        # Find and modify the entry
        for i, e in enumerate(new_state.schedule):
            if e.class_id == entry.class_id and e.kelas == entry.kelas:
                end_time, prayer_time_added = calculate_end_time(
                    selected_combo.time_slot.start_time,
                    e.sks,
                    selected_combo.time_slot.day
                )

                # Update overflow status
                is_lab_room = 'lab' in selected_combo.room_type.lower()
                is_overflow = not e.needs_lab and is_lab_room

                new_state.schedule[i] = ScheduleEntry(
                    class_id=e.class_id,
                    class_name=e.class_name,
                    kelas=e.kelas,
                    prodi=e.prodi,
                    lecturers=e.lecturers,
                    room=selected_combo.room_code,
                    time_slot=TimeSlot(
                        day=selected_combo.time_slot.day,
                        start_time=selected_combo.time_slot.start_time,
                        end_time=end_time,
                        period=selected_combo.time_slot.period
                    ),
                    sks=e.sks,
                    needs_lab=e.needs_lab,
                    participants=e.participants,
                    class_type=e.class_type,
                    prayer_time_added=prayer_time_added,
                    is_overflow_to_lab=is_overflow,
                )
                break

        return new_state

    def _get_valid_combinations(
        self,
        state: TimetableState,
        entry: ScheduleEntry
    ) -> list[TimeSlotRoomCombo]:
        """Get all valid time slot and room combinations for an entry.

        This matches TypeScript's getValidTimeSlotAndRoomCombinations() function.

        Validates:
        1. Room capacity >= participants
        2. Lab requirement matches
        3. Room availability at time slot
        4. Lecturer availability at time slot
        5. Prodi/class conflicts at time slot

        Args:
            state: Current timetable state
            entry: Schedule entry to find combinations for

        Returns:
            List of valid TimeSlotRoomCombo objects
        """
        combinations = []

        for time_slot in state.available_time_slots:
            # Skip if time slot doesn't match class type (pagi vs sore)
            # Constraint: pagi < 15:30, sore >= 15:30
            if entry.class_type.lower() == 'sore':
                # Evening class should start at 15:30 or later
                if time_to_minutes(time_slot.start_time) < time_to_minutes("15:30"):
                    continue
            else:
                # Morning class should start before 15:30
                if time_to_minutes(time_slot.start_time) >= time_to_minutes("15:30"):
                    continue

            # For each time slot, find suitable rooms
            for room in state.rooms:
                # 1. Check capacity
                if room.capacity < entry.participants:
                    continue

                # 2. Check lab requirement
                if entry.needs_lab and 'lab' not in room.type.lower():
                    continue

                # 3. Check room availability at this time slot
                if not self._is_room_available_at_time(state, room.code, time_slot, entry.sks, exclude_class_id=entry.class_id):
                    continue

                # 4. Check lecturer availability at this time slot
                if not self._are_lecturers_available_at_time(state, entry.lecturers, time_slot, entry.sks, exclude_class_id=entry.class_id):
                    continue

                # 5. Check prodi/class conflicts at this time slot
                if not self._is_prodi_slot_available(state, entry.prodi, entry.kelas, time_slot, entry.sks, exclude_class_id=entry.class_id):
                    continue

                # All checks passed - this is a valid combination
                combinations.append(TimeSlotRoomCombo(
                    time_slot=time_slot,
                    room_code=room.code,
                    room_type=room.type,
                    capacity=room.capacity
                ))

        return combinations

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

    def _select_combination(
        self,
        state: TimetableState,
        entry: ScheduleEntry,
        combinations: list[TimeSlotRoomCombo],
        temperature: float
    ) -> Optional[TimeSlotRoomCombo]:
        """Select a combination based on temperature.

        Matches TypeScript's temperature-dependent selection logic.
        """
        if not combinations:
            return None

        if temperature > 10000:
            # HIGH TEMPERATURE: Exploration - any valid combination
            return random.choice(combinations)

        elif temperature > 1000:
            # MEDIUM TEMPERATURE: Prefer different days for diversity
            different_day_combos = [
                c for c in combinations
                if c.time_slot.day != entry.time_slot.day
            ]
            if different_day_combos and random.random() < 0.7:
                return random.choice(different_day_combos)
            return random.choice(combinations)

        else:
            # LOW TEMPERATURE: Prefer nearby time slots on same day
            same_day_combos = [
                c for c in combinations
                if c.time_slot.day == entry.time_slot.day
            ]
            nearby_combos = [
                c for c in same_day_combos
                if abs(c.time_slot.period - entry.time_slot.period) <= 2
            ]

            if nearby_combos and random.random() < 0.7:
                return random.choice(nearby_combos)
            elif same_day_combos and random.random() < 0.5:
                return random.choice(same_day_combos)
            else:
                return random.choice(combinations)
