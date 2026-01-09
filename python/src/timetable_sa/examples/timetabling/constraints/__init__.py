"""Constraints __init__.py"""

from timetable_sa.examples.timetabling.constraints.hard import (
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
)
from timetable_sa.examples.timetabling.constraints.soft import (
    Compactness,
    OverflowPenalty,
    PreferredRoom,
    PreferredTime,
    TransitTime,
    ResearchDay,
    PrayerTimeOverlap,
    EveningClassPriority,
)

__all__ = [
    # Hard constraints
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
    # Soft constraints
    "Compactness",
    "OverflowPenalty",
    "PreferredRoom",
    "PreferredTime",
    "TransitTime",
    "ResearchDay",
    "PrayerTimeOverlap",
    "EveningClassPriority",
]
