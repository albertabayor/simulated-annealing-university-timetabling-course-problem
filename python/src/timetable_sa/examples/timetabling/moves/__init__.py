"""Moves __init__.py"""

"""Moves __init__.py"""

from timetable_sa.examples.timetabling.moves.change_room import (
    ChangeRoom,
)
from timetable_sa.examples.timetabling.moves.change_time_slot import (
    ChangeTimeSlot,
)
from timetable_sa.examples.timetabling.moves.change_time_slot_and_room import (
    ChangeTimeSlotAndRoom,
)
from timetable_sa.examples.timetabling.moves.fix_friday_prayer_conflict import (
    FixFridayPrayerConflict,
)
from timetable_sa.examples.timetabling.moves.fix_lecturer_conflict import (
    FixLecturerConflict,
)
from timetable_sa.examples.timetabling.moves.fix_max_daily_periods import (
    FixMaxDailyPeriods,
)
from timetable_sa.examples.timetabling.moves.fix_room_capacity import (
    FixRoomCapacity,
)
from timetable_sa.examples.timetabling.moves.fix_room_conflict import (
    FixRoomConflict,
)
from timetable_sa.examples.timetabling.moves.swap_classes import (
    SwapClasses,
)
from timetable_sa.examples.timetabling.moves.swap_friday_with_non_friday import (
    SwapFridayWithNonFriday,
)
from timetable_sa.examples.timetabling.moves.fix_class_type_time import (
    FixClassTypeTime,
)

__all__ = [
    "ChangeRoom",
    "ChangeTimeSlot",
    "ChangeTimeSlotAndRoom",
    "FixFridayPrayerConflict",
    "FixLecturerConflict",
    "FixMaxDailyPeriods",
    "FixRoomCapacity",
    "FixRoomConflict",
    "SwapClasses",
    "SwapFridayWithNonFriday",
    "FixClassTypeTime",
]
