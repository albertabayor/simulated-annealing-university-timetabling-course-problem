"""Hard constraints __init__.py"""

from timetable_sa.examples.timetabling.constraints.hard.no_room_conflict import (
    NoRoomConflict,
)
from timetable_sa.examples.timetabling.constraints.hard.no_lecturer_conflict import (
    NoLecturerConflict,
)
from timetable_sa.examples.timetabling.constraints.hard.no_prodi_conflict import (
    NoProdiConflict,
)
from timetable_sa.examples.timetabling.constraints.hard.room_capacity import (
    RoomCapacity,
)
from timetable_sa.examples.timetabling.constraints.hard.max_daily_periods import (
    MaxDailyPeriods,
)
from timetable_sa.examples.timetabling.constraints.hard.friday_time_restriction import (
    FridayTimeRestriction,
)
from timetable_sa.examples.timetabling.constraints.hard.no_friday_pray_conflict import (
    NoFridayPrayConflict,
)
from timetable_sa.examples.timetabling.constraints.hard.prayer_time_start import (
    PrayerTimeStart,
)
from timetable_sa.examples.timetabling.constraints.hard.class_type_time import (
    ClassTypeTime,
)
from timetable_sa.examples.timetabling.constraints.hard.exclusive_room import (
    ExclusiveRoom,
)
from timetable_sa.examples.timetabling.constraints.hard.saturday_restriction import (
    SaturdayRestriction,
)

__all__ = [
    "ClassTypeTime",
    "ExclusiveRoom",
    "FridayTimeRestriction",
    "MaxDailyPeriods",
    "NoFridayPrayConflict",
    "NoLecturerConflict",
    "NoProdiConflict",
    "NoRoomConflict",
    "PrayerTimeStart",
    "RoomCapacity",
    "SaturdayRestriction",
]
