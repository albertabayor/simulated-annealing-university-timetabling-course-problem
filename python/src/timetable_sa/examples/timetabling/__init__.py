"""
Timetabling domain implementation for university course scheduling.

This module provides a complete timetabling solution using Simulated Annealing:
- Types: Room, Lecturer, TimeSlot, ClassRequirement, TimetableState
- Constraints: NoRoomConflict, NoLecturerConflict, RoomCapacity, etc.
- Moves: ChangeTimeSlot, ChangeRoom, SwapClasses, FixRoomConflict, etc.
- Utilities: Time functions, prayer times, time slot generation, etc.
- Data loading: Excel loader for data_uisi.xlsx
"""

from timetable_sa.examples.timetabling.domain_types.domain import (
    Room,
    Lecturer,
    TimeSlot,
    ClassRequirement,
)
from timetable_sa.examples.timetabling.domain_types.state import (
    TimetableState,
    ScheduleEntry,
    OptimizationResult,
)
from timetable_sa.examples.timetabling.constraints import (
    NoRoomConflict,
    NoLecturerConflict,
    NoProdiConflict,
    RoomCapacity,
    MaxDailyPeriods,
    FridayTimeRestriction,
    NoFridayPrayConflict,
    PrayerTimeStart,
    ClassTypeTime,
    SaturdayRestriction,
    ExclusiveRoom,
    Compactness,
    OverflowPenalty,
    PreferredRoom,
    PreferredTime,
    TransitTime,
    ResearchDay,
    PrayerTimeOverlap,
    EveningClassPriority,
)
from timetable_sa.examples.timetabling.moves import (
    ChangeTimeSlot,
    ChangeRoom,
    SwapClasses,
    ChangeTimeSlotAndRoom,
    FixRoomConflict,
    FixLecturerConflict,
    FixRoomCapacity,
    SwapFridayWithNonFriday,
    FixFridayPrayerConflict,
    FixMaxDailyPeriods,
    FixClassTypeTime,
)
from timetable_sa.examples.timetabling.utils.time import (
    time_to_minutes,
    minutes_to_time,
    calculate_end_time,
)
from timetable_sa.examples.timetabling.utils.timeslot_generator import (
    generate_ts_slots,
    generate_default_time_slots,
)
from timetable_sa.examples.timetabling.utils.initial_solution import (
    create_initial_state,
    create_greedy_initial_state_v2,
    clone_state,
)
from timetable_sa.examples.timetabling.utils.constraint_helpers import (
    group_by_room,
    group_by_lecturer,
    group_by_prodi,
    group_by_day,
    calculate_room_utilization,
    calculate_lecturer_workload,
)
from timetable_sa.examples.timetabling.utils.class_helper import (
    get_lecturers_for_class,
    needs_lab,
    get_preferred_rooms,
    filter_classes_by_prodi,
    filter_classes_by_type,
)
from timetable_sa.examples.timetabling.utils.room_availability import (
    RoomAvailabilityChecker,
    find_available_slot,
)
from timetable_sa.examples.timetabling.data import (
    load_uisi_data,
    load_sample_data,
)

__version__ = "0.1.0"

__all__ = [
    # Types
    "Room",
    "Lecturer", 
    "TimeSlot",
    "ClassRequirement",
    "TimetableState",
    "ScheduleEntry",
    "OptimizationResult",
    # Hard Constraints
    "NoRoomConflict",
    "NoLecturerConflict",
    "NoProdiConflict",
    "RoomCapacity",
    "MaxDailyPeriods",
    "FridayTimeRestriction",
    "NoFridayPrayConflict",
    "PrayerTimeStart",
    "ClassTypeTime",
    "SaturdayRestriction",
    "ExclusiveRoom",
    # Soft Constraints
    "Compactness",
    "OverflowPenalty",
    "PreferredRoom",
    "PreferredTime",
    "TransitTime",
    "ResearchDay",
    "PrayerTimeOverlap",
    "EveningClassPriority",
    # Moves
    "ChangeTimeSlot",
    "ChangeRoom",
    "SwapClasses",
    "ChangeTimeSlotAndRoom",
    "FixRoomConflict",
    "FixLecturerConflict",
    "FixRoomCapacity",
    "SwapFridayWithNonFriday",
    "FixFridayPrayerConflict",
    "FixMaxDailyPeriods",
    "FixClassTypeTime",
    # Utilities
    "time_to_minutes",
    "minutes_to_time",
    "calculate_end_time",
    "generate_ts_slots",
    "generate_default_time_slots",
    "create_initial_state",
    "create_greedy_initial_state_v2",
    "clone_state",
    "group_by_room",
    "group_by_lecturer",
    "group_by_prodi",
    "group_by_day",
    "calculate_room_utilization",
    "calculate_lecturer_workload",
    "get_lecturers_for_class",
    "needs_lab",
    "get_preferred_rooms",
    "filter_classes_by_prodi",
    "filter_classes_by_type",
    "RoomAvailabilityChecker",
    "find_available_slot",
    # Data
    "load_uisi_data",
    "load_sample_data",
]
