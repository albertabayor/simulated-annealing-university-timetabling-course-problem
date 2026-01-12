"""Move generator: Swap Classes.

Swaps the time slots and rooms of two classes.
"""

import random
from typing import Optional, Tuple

from timetable_sa.core.interfaces import MoveGenerator
from timetable_sa.examples.timetabling.domain_types.state import TimetableState, ScheduleEntry
from timetable_sa.examples.timetabling.domain_types.domain import TimeSlot
from timetable_sa.examples.timetabling.utils.time import calculate_end_time, time_to_minutes


class SwapClasses(MoveGenerator):
    """Move generator that swaps two classes' assignments.

    This is a powerful move that can quickly resolve multiple conflicts
    by exchanging the schedules of two classes.

    Temperature-dependent behavior:
        - High temperature: Any two classes
        - Medium temperature: Same prodi classes
        - Low temperature: Classes with similar characteristics

    IMPORTANT: Now validates swaps to avoid creating class type time violations.
    """

    name: str = "Swap Classes"

    def can_apply(self, state: TimetableState) -> bool:
        """Check if this move can be applied."""
        return len(state.schedule) >= 2

    def _select_classes_to_swap(
        self, state: TimetableState, temperature: float
    ) -> Tuple[Optional[ScheduleEntry], Optional[ScheduleEntry]]:
        """Select two classes to swap based on temperature.

        Temperature-dependent selection:
        - High temp (>10000): Random any two classes
        - Medium temp (>1000): Prefer same prodi
        - Low temp (<=1000): Prefer similar classes
        """
        if len(state.schedule) < 2:
            return None, None

        # High temperature: pure random selection
        if temperature > 10000:
            entry1, entry2 = random.sample(state.schedule, 2)
            return entry1, entry2

        # Medium temperature: prefer same prodi
        if temperature > 1000:
            # Try to find same prodi classes (50% chance)
            if random.random() < 0.5:
                entry1 = random.choice(state.schedule)
                same_prodi = [
                    e for e in state.schedule
                    if e.class_id != entry1.class_id and e.prodi == entry1.prodi
                ]
                if same_prodi:
                    entry2 = random.choice(same_prodi)
                    return entry1, entry2
            # Fallback to random
            entry1, entry2 = random.sample(state.schedule, 2)
            return entry1, entry2

        # Low temperature: prefer similar classes (same prodi, similar SKS)
        entry1 = random.choice(state.schedule)
        candidates = [
            e for e in state.schedule
            if e.class_id != entry1.class_id and e.prodi == entry1.prodi
        ]
        if candidates:
            # Prefer similar SKS
            candidates.sort(key=lambda x: abs(x.sks - entry1.sks))
            # Pick from top 3 most similar
            entry2 = random.choice(candidates[:min(3, len(candidates))])
            return entry1, entry2

        # Fallback to random if no candidates
        entry1, entry2 = random.sample(state.schedule, 2)
        return entry1, entry2

    def _is_class_type_compatible_swap(
        self,
        entry1: ScheduleEntry,
        entry2: ScheduleEntry,
        swap_time: bool
    ) -> bool:
        """Check if swapping time slots would violate class type time constraint.

        Args:
            entry1: First class entry
            entry2: Second class entry
            swap_time: Whether time slots are being swapped

        Returns:
            True if swap is compatible with class types, False otherwise
        """
        if not swap_time:
            return True  # No time swap, no class type issue

        # If both classes have same type, swap is always OK
        if entry1.class_type.lower() == entry2.class_type.lower():
            return True

        # Different class types - need to check if time slots are compatible
        # Constraint: pagi < 15:30, sore >= 15:30

        # Get entry1's time slot that entry2 would get
        entry1_slot_minutes = time_to_minutes(entry1.time_slot.start_time)
        # Get entry2's time slot that entry1 would get
        entry2_slot_minutes = time_to_minutes(entry2.time_slot.start_time)

        # Check if entry1 (pagi) can use entry2's time slot
        if entry1.class_type.lower() == "pagi":
            if entry2_slot_minutes >= 15 * 60 + 30:  # 15:30
                return False  # pagi class would get sore time slot

        # Check if entry2 (sore) can use entry1's time slot
        if entry2.class_type.lower() == "sore":
            if entry1_slot_minutes < 15 * 60 + 30:  # 15:30
                return False  # sore class would get pagi time slot

        return True

    def generate(self, state: TimetableState, temperature: float) -> Optional[TimetableState]:
        """Generate a new state with two classes swapped.

        Temperature-dependent behavior matching TypeScript:
        - High temp (>10000): Prefer full swaps for exploration
        - Medium temp (>1000): Same prodi preference
        - Low temp (<=1000): Prefer similar classes for exploitation
        """
        if not self.can_apply(state):
            return None

        # Select two different classes to swap
        entry1, entry2 = self._select_classes_to_swap(state, temperature)

        if entry1 is None or entry2 is None:
            return None

        # Temperature-dependent swap type selection
        swap_time = random.random() < 0.5 if temperature > 1000 else random.random() < 0.4
        swap_room = random.random() < 0.3 if temperature > 10000 else random.random() < 0.4

        # Validate class type compatibility before swapping time
        if swap_time:
            if not self._is_class_type_compatible_swap(entry1, entry2, swap_time):
                # Swap would violate class type time constraint, skip this swap
                return None

        from timetable_sa.examples.timetabling.utils.time import calculate_end_time

        # Create new state
        from timetable_sa.examples.timetabling.utils.initial_solution import clone_state
        new_state = clone_state(state)

        # Swap entries
        # Process time swap for both entries (no break - need to process BOTH entry1 AND entry2)
        for i, e in enumerate(new_state.schedule):
            if swap_time:
                if e.class_id == entry1.class_id and e.kelas == entry1.kelas:
                    temp_slot = entry2.time_slot
                    new_state.schedule[i] = self._create_swapped_entry(e, entry2, temp_slot, None)
                elif e.class_id == entry2.class_id and e.kelas == entry2.kelas:
                    temp_slot = entry1.time_slot
                    new_state.schedule[i] = self._create_swapped_entry(e, entry1, temp_slot, None)

        # Process room swap for both entries (no break - need to process BOTH entry1 AND entry2)
        for i, e in enumerate(new_state.schedule):
            if swap_room:
                if e.class_id == entry1.class_id and e.kelas == entry1.kelas:
                    temp_room = entry2.room
                    new_state.schedule[i] = self._create_swapped_entry(e, entry2, None, temp_room)
                elif e.class_id == entry2.class_id and e.kelas == entry2.kelas:
                    temp_room = entry1.room
                    new_state.schedule[i] = self._create_swapped_entry(e, entry1, None, temp_room)

        # Recalculate end times for swapped entries
        # IMPORTANT: Match on BOTH class_id AND kelas to uniquely identify entries
        # This prevents modifying all entries with the same class_id (e.g., IF-1A and IF-1B both having IF13P114)
        for i, e in enumerate(new_state.schedule):
            if (e.class_id == entry1.class_id and e.kelas == entry1.kelas) or \
               (e.class_id == entry2.class_id and e.kelas == entry2.kelas):
                end_time, _ = calculate_end_time(
                    e.time_slot.start_time,
                    e.sks,
                    e.time_slot.day
                )
                new_state.schedule[i] = ScheduleEntry(
                    class_id=e.class_id,
                    class_name=e.class_name,
                    kelas=e.kelas,
                    prodi=e.prodi,
                    lecturers=e.lecturers,
                    room=e.room,
                    time_slot=TimeSlot(
                        day=e.time_slot.day,
                        start_time=e.time_slot.start_time,
                        end_time=end_time,
                        period=e.time_slot.period
                    ),
                    sks=e.sks,
                    needs_lab=e.needs_lab,
                    participants=e.participants,
                    class_type=e.class_type,
                    prayer_time_added=e.prayer_time_added,
                    is_overflow_to_lab=e.is_overflow_to_lab,
                )

        return new_state

    def _create_swapped_entry(
        self,
        source_entry: ScheduleEntry,
        target_entry: ScheduleEntry,
        new_slot: TimeSlot | None = None,
        new_room: str | None = None
    ) -> ScheduleEntry:
        """Create a new entry with swapped time slot and/or room."""
        time_slot = new_slot if new_slot else source_entry.time_slot
        room = new_room if new_room else source_entry.room

        end_time, _ = calculate_end_time(
            time_slot.start_time,
            target_entry.sks,
            time_slot.day
        )

        return ScheduleEntry(
            class_id=target_entry.class_id,
            class_name=target_entry.class_name,
            kelas=target_entry.kelas,
            prodi=target_entry.prodi,
            lecturers=target_entry.lecturers,
            room=room,
            time_slot=TimeSlot(
                day=time_slot.day,
                start_time=time_slot.start_time,
                end_time=end_time,
                period=time_slot.period
            ),
            sks=target_entry.sks,
            needs_lab=target_entry.needs_lab,
            participants=target_entry.participants,
            class_type=target_entry.class_type,
            prayer_time_added=target_entry.prayer_time_added,
            is_overflow_to_lab=target_entry.is_overflow_to_lab,
        )
