"""Create initial solution for timetable optimization.

This module provides functions to generate an initial (possibly invalid)
timetable state that the Simulated Annealing algorithm can then optimize.
"""

import random
import copy
from typing import Optional

from timetable_sa.examples.timetabling.domain_types.domain import (
    Room,
    Lecturer,
    TimeSlot,
    ClassRequirement,
)
from timetable_sa.examples.timetabling.domain_types.state import (
    ScheduleEntry,
    TimetableState,
)
from timetable_sa.examples.timetabling.utils.time import (
    calculate_end_time,
    time_to_minutes,
)
from timetable_sa.examples.timetabling.utils.timeslot_generator import (
    generate_default_time_slots,
    generate_ts_slots,
)


def create_initial_state(
    classes: list[ClassRequirement],
    rooms: list[Room],
    lecturers: list[Lecturer],
    time_slots: Optional[list[TimeSlot]] = None,
    random_seed: Optional[int] = None,
) -> TimetableState:
    """Create an initial random timetable state.
    
    This creates a random assignment of classes to rooms and time slots.
    The initial state may have constraint violations - that's expected!
    The optimization will fix these violations.
    
    Args:
        classes: List of class requirements to schedule
        rooms: List of available rooms
        lecturers: List of lecturers
        time_slots: List of available time slots (generated if None)
        random_seed: Optional seed for reproducibility
    
    Returns:
        TimetableState with random assignments
    """
    if random_seed is not None:
        random.seed(random_seed)
    
    # Generate time slots if not provided
    if time_slots is None:
        time_slots = generate_default_time_slots()
    
    schedule: list[ScheduleEntry] = []
    
    for class_req in classes:
        # Select a random room (could be any room initially)
        room = random.choice(rooms)
        
        # Select a random time slot
        time_slot = random.choice(time_slots)
        
        # Calculate end time based on SKS
        end_time, _ = calculate_end_time(
            time_slot.start_time,
            class_req.sks,
            time_slot.day
        )
        
        # Get all lecturers for this class
        lecturers_list = class_req.get_lecturers()
        
        # Create schedule entry
        entry = ScheduleEntry(
            class_id=class_req.kode_matakuliah,
            class_name=class_req.mata_kuliah,
            kelas=class_req.kelas,
            prodi=class_req.prodi,
            lecturers=lecturers_list,
            room=room.code,
            time_slot=TimeSlot(
                day=time_slot.day,
                start_time=time_slot.start_time,
                end_time=end_time,
                period=time_slot.period
            ),
            sks=class_req.sks,
            needs_lab=class_req.needs_lab(),
            participants=class_req.peserta,
            class_type=class_req.class_type,
        )
        
        schedule.append(entry)
    
    return TimetableState(
        schedule=schedule,
        available_time_slots=time_slots,
        rooms=rooms,
        lecturers=lecturers,
    )


def create_greedy_initial_state(
    classes: list[ClassRequirement],
    rooms: list[Room],
    lecturers: list[Lecturer],
    time_slots: Optional[list[TimeSlot]] = None,
) -> TimetableState:
    """Create an initial state using greedy assignment.
    
    Tries to assign classes to avoid obvious conflicts, but still
    may have some violations that need to be fixed.
    
    Args:
        classes: List of class requirements to schedule
        rooms: List of available rooms
        lecturers: List of lecturers
        time_slots: List of available time slots
    
    Returns:
        TimetableState with greedy assignments
    """
    # Generate time slots if not provided
    if time_slots is None:
        time_slots = generate_default_time_slots()
    
    # Group time slots by day
    slots_by_day: dict[str, list[TimeSlot]] = {}
    for slot in time_slots:
        if slot.day not in slots_by_day:
            slots_by_day[slot.day] = []
        slots_by_day[slot.day].append(slot)
    
    # Sort slots by start time
    for day in slots_by_day:
        slots_by_day[day].sort(key=lambda s: time_to_minutes(s.start_time))
    
    # Track used room + slot combinations
    used_slots: dict[str, TimeSlot] = {}  # "room_code|day|start" -> time_slot
    
    schedule: list[ScheduleEntry] = []
    
    for class_req in classes:
        # Get available slots for this class type (morning/evening)
        preferred_day_slots: list[TimeSlot] = []
        
        for day, slots in slots_by_day.items():
            for slot in slots:
                # Check if room is available
                key = f"{slot.day}|{slot.start_time}"
                
                # Try to find a valid assignment
                if key not in used_slots:
                    preferred_day_slots.append(slot)
        
        if preferred_day_slots:
            time_slot = random.choice(preferred_day_slots)
        else:
            # Fall back to any slot
            time_slot = random.choice(time_slots)
        
        # Calculate end time
        end_time, _ = calculate_end_time(
            time_slot.start_time,
            class_req.sks,
            time_slot.day
        )
        
        # Select room (prefer appropriate type)
        available_rooms = [r for r in rooms]
        if class_req.needs_lab():
            # For lab classes, prefer lab rooms
            lab_rooms = [r for r in rooms if r.type.lower() == "lab"]
            if lab_rooms:
                available_rooms = lab_rooms
        
        room = random.choice(available_rooms)
        
        # Mark slot as used
        key = f"{time_slot.day}|{time_slot.start_time}"
        used_slots[key] = time_slot
        
        # Get lecturers
        lecturers_list = class_req.get_lecturers()
        
        # Create entry
        entry = ScheduleEntry(
            class_id=class_req.kode_matakuliah,
            class_name=class_req.mata_kuliah,
            kelas=class_req.kelas,
            prodi=class_req.prodi,
            lecturers=lecturers_list,
            room=room.code,
            time_slot=TimeSlot(
                day=time_slot.day,
                start_time=time_slot.start_time,
                end_time=end_time,
                period=time_slot.period
            ),
            sks=class_req.sks,
            needs_lab=class_req.needs_lab(),
            participants=class_req.peserta,
            class_type=class_req.class_type,
        )
        
        schedule.append(entry)
    
    return TimetableState(
        schedule=schedule,
        available_time_slots=time_slots,
        rooms=rooms,
        lecturers=lecturers,
    )


def clone_state(state: TimetableState) -> TimetableState:
    """Create a deep copy of the timetable state.

    Args:
        state: The state to clone

    Returns:
        A deep copy of the state
    """
    return TimetableState(
        schedule=copy.deepcopy(state.schedule),
        available_time_slots=copy.deepcopy(state.available_time_slots),
        rooms=state.rooms,
        lecturers=state.lecturers,
    )


def create_greedy_initial_state_v2(
    classes: list[ClassRequirement],
    rooms: list[Room],
    lecturers: list[Lecturer],
    time_slots: list[TimeSlot],
    random_seed: Optional[int] = None,
) -> TimetableState:
    """Create initial state using greedy assignment (matches TypeScript approach exactly).

    This version exactly matches the TypeScript initial-solution.ts with advanced features:
    - SKS-based end time calculation
    - Class type filtering (pagi/sore)
    - Saturday restrictions for non-MM programs
    - Lab requirement handling
    - Sophisticated conflict detection

    Args:
        classes: List of class requirements to schedule
        rooms: List of available rooms
        lecturers: List of lecturers
        time_slots: List of available time slots
        random_seed: Optional seed for reproducibility

    Returns:
        TimetableState with greedy assignments
    """
    if random_seed is not None:
        random.seed(random_seed)

    # Generate pagi and sore slots exactly like TypeScript
    TIME_SLOTS_PAGI = generate_ts_slots("07:30", "15:30", 50)
    TIME_SLOTS_SORE = generate_ts_slots("15:30", "21:00", 50)

    # Filter evening slots (start >= 18:00) like TypeScript
    EVENING_START_MINUTES = time_to_minutes("18:00")
    TIME_SLOTS_EVENING = [s for s in TIME_SLOTS_SORE if time_to_minutes(s.start_time) >= EVENING_START_MINUTES]

    schedule: list[ScheduleEntry] = []
    skipped = []
    success_count = 0

    # Shuffle classes for random placement order (matching TypeScript)
    shuffled_classes = list(classes)
    random.shuffle(shuffled_classes)

    def has_class_overlap(kelas1: str, kelas2: str) -> bool:
        """Check if two classes have overlapping class codes (matches TypeScript)."""
        classes1 = [c.strip().upper() for c in kelas1.split(',')]
        classes2 = [c.strip().upper() for c in kelas2.split(',')]
        for c1 in classes1:
            for c2 in classes2:
                if c1 == c2:
                    return True
        return False

    def has_time_overlap(start1: str, end1: str, start2: str, end2: str) -> bool:
        """Check if two time ranges overlap."""
        s1 = time_to_minutes(start1)
        e1 = time_to_minutes(end1)
        s2 = time_to_minutes(start2)
        e2 = time_to_minutes(end2)
        return s1 < e2 and s2 < e1

    def has_conflict(new_entry: ScheduleEntry, existing_schedule: list[ScheduleEntry]) -> bool:
        """Check if new entry conflicts with any existing entry (matches TypeScript)."""
        for existing in existing_schedule:
            if new_entry.time_slot.day != existing.time_slot.day:
                continue

            # Calculate actual end times based on SKS (matching TypeScript)
            end1, _ = calculate_end_time(new_entry.time_slot.start_time, new_entry.sks, new_entry.time_slot.day)
            end2, _ = calculate_end_time(existing.time_slot.start_time, existing.sks, existing.time_slot.day)

            if not has_time_overlap(new_entry.time_slot.start_time, end1,
                                    existing.time_slot.start_time, end2):
                continue

            # 1. Room conflict
            if new_entry.room == existing.room:
                return True

            # 2. Lecturer conflict
            for lect in new_entry.lecturers:
                if lect in existing.lecturers:
                    return True

            # 3. Prodi/Class conflict
            if new_entry.prodi == existing.prodi and has_class_overlap(new_entry.kelas, existing.kelas):
                return True

        return False

    for class_req in shuffled_classes:
        lecturers_list = class_req.get_lecturers()

        if not lecturers_list:
            skipped.append(f"{class_req.kode_matakuliah}: No lecturers")
            continue

        # Get class properties (matching TypeScript)
        participants = class_req.peserta
        needs_lab = class_req.needs_lab()
        class_type = class_req.class_type.lower()
        prodi = class_req.prodi
        sks = class_req.sks

        # Filter time slots exactly like TypeScript
        # Use TIME_SLOTS_PAGI for pagi, TIME_SLOTS_SORE for sore
        slots = TIME_SLOTS_SORE if class_type == 'sore' else TIME_SLOTS_PAGI

        # Filter Saturday for non-Magister Manajemen (matching TypeScript)
        is_mm = 'magister manajemen' in prodi.lower()
        if not is_mm:
            slots = [s for s in slots if s.day != 'Saturday']

        if not slots:
            skipped.append(f"{class_req.kode_matakuliah}: No valid slots")
            continue

        placed = False

        for slot in slots:
            # Find suitable rooms (matching TypeScript logic)
            suitable_rooms = []
            for r in rooms:
                # Check capacity
                if r.capacity < participants:
                    continue
                # Check lab requirement
                if needs_lab and 'lab' not in r.type.lower():
                    continue
                suitable_rooms.append(r)

            if not suitable_rooms:
                continue

            random.shuffle(suitable_rooms)

            # Try each suitable room until find one without conflict
            for room in suitable_rooms:
                end_time, prayer_time = calculate_end_time(slot.start_time, sks, slot.day)

                entry = ScheduleEntry(
                    class_id=class_req.kode_matakuliah,
                    class_name=class_req.mata_kuliah,
                    kelas=class_req.kelas,
                    prodi=prodi,
                    lecturers=lecturers_list,
                    room=room.code,
                    time_slot=TimeSlot(
                        day=slot.day,
                        start_time=slot.start_time,
                        end_time=end_time,
                        period=slot.period
                    ),
                    sks=sks,
                    needs_lab=needs_lab,
                    participants=participants,
                    class_type=class_type,
                )

                if not has_conflict(entry, schedule):
                    schedule.append(entry)
                    placed = True
                    success_count += 1
                    break

            if placed:
                break

        if not placed:
            skipped.append(f"{class_req.kode_matakuliah}: No available slot")

    print(f"   Placed: {success_count}/{len(classes)}")
    if skipped:
        for s in skipped[:10]:
            print(f"   Skipped: {s}")
        if len(skipped) > 10:
            print(f"   ... and {len(skipped) - 10} more")

    # Verify no conflicts
    conflict_count = 0
    for entry in schedule:
        if has_conflict(entry, [e for e in schedule if e.class_id != entry.class_id]):
            conflict_count += 1

    if conflict_count > 0:
        print(f"   WARNING: {conflict_count} entries have conflicts!")
    else:
        print(f"   No conflicts in initial state")

    return TimetableState(
        schedule=schedule,
        available_time_slots=time_slots,
        rooms=rooms,
        lecturers=lecturers,
    )
