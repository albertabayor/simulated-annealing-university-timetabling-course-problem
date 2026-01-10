"""Move generator: Fix Class Type Time violation.

Moves a class to a valid time slot that matches its class type (pagi/sore).
"""

import random
from typing import Optional

from timetable_sa.core.interfaces import MoveGenerator
from timetable_sa.examples.timetabling.domain_types.state import TimetableState, ScheduleEntry
from timetable_sa.examples.timetabling.domain_types.domain import TimeSlot
from timetable_sa.examples.timetabling.constraints.hard.class_type_time import ClassTypeTime
from timetable_sa.examples.timetabling.utils.time import calculate_end_time, time_to_minutes
from timetable_sa.examples.timetabling.utils.class_helper import has_class_overlap


class FixClassTypeTime(MoveGenerator):
    """Move generator that fixes class type time violations.

    This operator specifically targets the ClassTypeTime hard constraint,
    moving classes to time slots that match their class type:
    - pagi (morning) classes: before 15:30
    - sore (evening) classes: 15:30 or later

    This is a "fix" operator that should only be used when there are
    ClassTypeTime violations present.
    """

    name: str = "Fix Class Type Time"

    def __init__(self):
        super().__init__()
        self._constraint = ClassTypeTime()

    def can_apply(self, state: TimetableState) -> bool:
        """Check if this move can be applied.

        This operator can only apply if there are class type time violations.
        """
        violations = self._constraint._find_violations(state)
        return len(violations) > 0

    def generate(self, state: TimetableState, temperature: float) -> Optional[TimetableState]:
        """Generate a new state with a class type time violation fixed.

        Args:
            state: Current timetable state
            temperature: Current annealing temperature (ignored for fix operators)

        Returns:
            New state with one class moved to a valid time slot, or None
        """
        if not self.can_apply(state):
            return None

        # Get all class type time violations
        violations = self._constraint._find_violations(state)

        if not violations:
            return None

        # Pick a random violation to fix
        violation = random.choice(violations)
        class_id = violation["class_id"]

        # Find the entry in the schedule
        target_entry = None
        for entry in state.schedule:
            if entry.class_id == class_id:
                target_entry = entry
                break

        if target_entry is None:
            return None

        # Find valid time slots for this class
        valid_slots = self._find_valid_time_slots(state, target_entry)

        if not valid_slots:
            # Debug: Log why no valid slots found
            import logging
            logging.getLogger(__name__).warning(
                f"FixClassTypeTime: No valid slots for {target_entry.class_id} "
                f"(class_type={target_entry.class_type}, current_time={target_entry.time_slot.start_time})"
            )
            return None

        # Select a valid time slot (prefer nearby slots)
        new_slot = self._select_time_slot(target_entry, valid_slots)

        # Create new state
        from timetable_sa.examples.timetabling.utils.initial_solution import clone_state
        new_state = clone_state(state)

        # Update the entry
        for i, e in enumerate(new_state.schedule):
            if e.class_id == target_entry.class_id and e.kelas == target_entry.kelas:
                end_time, prayer_time_added = calculate_end_time(
                    new_slot.start_time,
                    e.sks,
                    new_slot.day
                )

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

    def _find_valid_time_slots(
        self,
        state: TimetableState,
        entry: ScheduleEntry
    ) -> list[TimeSlot]:
        """Find valid time slots for a class that match its class type.

        Args:
            state: Current timetable state
            entry: Schedule entry to find valid slots for

        Returns:
            List of valid TimeSlot objects
        """
        valid_slots = []
        current_minutes = time_to_minutes(entry.time_slot.start_time)

        for slot in state.available_time_slots:
            slot_minutes = time_to_minutes(slot.start_time)

            # Skip if it's the same slot
            if slot.day == entry.time_slot.day and slot.period == entry.time_slot.period:
                continue

            # Check class type compatibility
            if entry.class_type.lower() == "pagi":
                # Morning class must start before 15:30
                if slot_minutes >= 15 * 60 + 30:
                    continue
            else:  # sore
                # Evening class must start at 15:30 or later
                if slot_minutes < 15 * 60 + 30:
                    continue

            # Check if slot would cause conflicts
            if not self._is_slot_available(state, entry, slot):
                continue

            valid_slots.append(slot)

        return valid_slots

    def _is_slot_available(
        self,
        state: TimetableState,
        entry: ScheduleEntry,
        slot: TimeSlot
    ) -> bool:
        """Check if a time slot is available for a class.

        Checks for:
        - Room availability
        - Lecturer availability
        - Prodi/class conflicts

        Args:
            state: Current timetable state
            entry: Schedule entry
            slot: Time slot to check

        Returns:
            True if slot is available, False otherwise
        """
        slot_start = time_to_minutes(slot.start_time)
        slot_end, _ = calculate_end_time(slot.start_time, entry.sks, slot.day)
        slot_end = time_to_minutes(slot_end)

        for other in state.schedule:
            # Skip same entry
            if other.class_id == entry.class_id and other.kelas == entry.kelas:
                continue

            # Check room conflict
            if other.room == entry.room and other.time_slot.day == slot.day:
                other_start = time_to_minutes(other.time_slot.start_time)
                other_end, _ = calculate_end_time(other.time_slot.start_time, other.sks, other.time_slot.day)
                other_end = time_to_minutes(other_end)

                if slot_start < other_end and other_start < slot_end:
                    return False  # Room conflict

            # Check lecturer conflict
            if any(lect in other.lecturers for lect in entry.lecturers):
                if other.time_slot.day == slot.day:
                    other_start = time_to_minutes(other.time_slot.start_time)
                    other_end, _ = calculate_end_time(other.time_slot.start_time, other.sks, other.time_slot.day)
                    other_end = time_to_minutes(other_end)

                    if slot_start < other_end and other_start < slot_end:
                        return False  # Lecturer conflict

            # Check prodi/class conflict
            if other.prodi == entry.prodi and has_class_overlap(entry.kelas, other.kelas):
                if other.time_slot.day == slot.day:
                    other_start = time_to_minutes(other.time_slot.start_time)
                    other_end, _ = calculate_end_time(other.time_slot.start_time, other.sks, other.time_slot.day)
                    other_end = time_to_minutes(other_end)

                    if slot_start < other_end and other_start < slot_end:
                        return False  # Prodi/class conflict

        return True

    def _select_time_slot(
        self,
        entry: ScheduleEntry,
        valid_slots: list[TimeSlot]
    ) -> Optional[TimeSlot]:
        """Select a time slot from valid options.

        Prefers:
        1. Same day, nearby period
        2. Same day
        3. Any valid slot

        Args:
            entry: Current schedule entry
            valid_slots: List of valid time slots

        Returns:
            Selected TimeSlot or None
        """
        if not valid_slots:
            return None

        # Prefer same day
        same_day_slots = [
            s for s in valid_slots
            if s.day == entry.time_slot.day
        ]

        if same_day_slots:
            # Prefer nearby period
            current_period = entry.time_slot.period
            nearby_slots = [
                s for s in same_day_slots
                if abs(s.period - current_period) <= 2
            ]

            if nearby_slots:
                return random.choice(nearby_slots)

            return random.choice(same_day_slots)

        return random.choice(valid_slots)
