"""Move generator: Change Room.

Changes a class's room assignment to a different room.
"""

import random
from typing import Optional

from timetable_sa.core.interfaces import MoveGenerator
from timetable_sa.examples.timetabling.domain_types.state import TimetableState, ScheduleEntry
from timetable_sa.examples.timetabling.utils.time import calculate_end_time, time_to_minutes


class ChangeRoom(MoveGenerator):
    """Move generator that changes a class's room.

    This move helps optimize room utilization and handle capacity constraints.

    Temperature-dependent behavior:
        - High temperature: Any valid room (random)
        - Medium temperature: Prefer rooms of same type
        - Low temperature: Prefer rooms with capacity matching class size

    IMPORTANT: Now validates rooms BEFORE selecting (matching TypeScript behavior).
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

        # Get VALID rooms first (filter by constraints)
        valid_rooms = self._get_valid_rooms(state, entry)

        if not valid_rooms:
            return None

        # Select from valid rooms based on temperature
        new_room = self._select_room_from_valid(state, entry, valid_rooms, temperature)

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

    def _get_valid_rooms(
        self,
        state: TimetableState,
        entry: ScheduleEntry
    ) -> list:
        """Get list of valid rooms for an entry (filtered by constraints).

        This matches TypeScript's validation logic:
        1. Check capacity >= participants
        2. Check lab requirement
        3. Check room availability at entry's time slot
        4. Check lecturer conflicts
        5. Check prodi/class conflicts

        Args:
            state: Current timetable state
            entry: Schedule entry to find valid rooms for

        Returns:
            List of valid Room objects
        """
        valid_rooms = []

        for room in state.rooms:
            # 1. Check capacity
            if room.capacity < entry.participants:
                continue

            # 2. Check lab requirement
            if entry.needs_lab and 'lab' not in room.type.lower():
                continue

            # 3. Check if room is available at this time slot (no conflict)
            if not self._is_room_available_at_time(state, room.code, entry, exclude_class_id=entry.class_id):
                continue

            valid_rooms.append(room)

        return valid_rooms

    def _is_room_available_at_time(
        self,
        state: TimetableState,
        room_code: str,
        entry: ScheduleEntry,
        exclude_class_id: str | None = None
    ) -> bool:
        """Check if a room is available at a given time slot.

        Matches TypeScript's isRoomAvailable() function.

        Args:
            state: Current timetable state
            room_code: Room code to check
            entry: ScheduleEntry with time_slot and sks
            exclude_class_id: Class ID to exclude from conflict check

        Returns:
            True if room is available, False otherwise
        """
        # Get other schedule entries (exclude current entry)
        other_schedule = [
            e for e in state.schedule
            if not (e.class_id == exclude_class_id and e.kelas == entry.kelas)
        ]

        # Calculate end time for the new entry
        new_end_time, _ = calculate_end_time(entry.time_slot.start_time, entry.sks, entry.time_slot.day)
        new_start = time_to_minutes(entry.time_slot.start_time)
        new_end = time_to_minutes(new_end_time)

        for other in other_schedule:
            # Skip if different room
            if other.room != room_code:
                continue

            # Skip if different day
            if other.time_slot.day != entry.time_slot.day:
                continue

            # Calculate other entry's end time
            other_end_time, _ = calculate_end_time(other.time_slot.start_time, other.sks, other.time_slot.day)
            other_start = time_to_minutes(other.time_slot.start_time)
            other_end = time_to_minutes(other_end_time)

            # Check for time overlap (conflict)
            # Two intervals [s1, e1) and [s2, e2) overlap if: s1 < e2 AND s2 < e1
            if new_start < other_end and other_start < new_end:
                return False  # Conflict found

        return True  # No conflicts, room is available

    def _select_room_from_valid(
        self,
        state: TimetableState,
        entry: ScheduleEntry,
        valid_rooms: list,
        temperature: float
    ):
        """Select a room from valid rooms based on temperature.

        Args:
            state: Current timetable state
            entry: Current schedule entry
            valid_rooms: List of pre-filtered valid rooms
            temperature: Current annealing temperature

        Returns:
            Selected Room object or None
        """
        if not valid_rooms:
            return None

        # Get current room for comparison
        current_room = next((r for r in state.rooms if r.code == entry.room), None)

        if temperature > 10000:
            # HIGH TEMPERATURE: Exploration - pick any valid room
            return random.choice(valid_rooms)

        elif temperature > 1000:
            # MEDIUM TEMPERATURE: Balanced - prefer same type
            if current_room:
                same_type_rooms = [r for r in valid_rooms if r.type == current_room.type]
                if same_type_rooms and random.random() < 0.5:
                    return random.choice(same_type_rooms)
            return random.choice(valid_rooms)

        else:
            # LOW TEMPERATURE: Exploitation - prefer closest capacity match
            # Sort by capacity difference (smallest suitable room first)
            sorted_by_capacity = sorted(valid_rooms, key=lambda r: r.capacity - entry.participants)

            # Pick from top 3 best-fit rooms (or less if fewer available)
            top_rooms = sorted_by_capacity[:min(3, len(sorted_by_capacity))]
            if random.random() < 0.8:
                return random.choice(top_rooms)
            else:
                return random.choice(valid_rooms)
