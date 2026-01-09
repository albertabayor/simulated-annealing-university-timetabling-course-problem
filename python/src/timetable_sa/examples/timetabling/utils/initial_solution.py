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
