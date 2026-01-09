"""Soft constraints __init__.py"""

"""Soft constraints __init__.py"""

from timetable_sa.examples.timetabling.constraints.soft.compactness import (
    Compactness,
)
from timetable_sa.examples.timetabling.constraints.soft.evening_class_priority import (
    EveningClassPriority,
)
from timetable_sa.examples.timetabling.constraints.soft.overflow_penalty import (
    OverflowPenalty,
)
from timetable_sa.examples.timetabling.constraints.soft.preferred_room import (
    PreferredRoom,
)
from timetable_sa.examples.timetabling.constraints.soft.preferred_time import (
    PreferredTime,
)
from timetable_sa.examples.timetabling.constraints.soft.prayer_time_overlap import (
    PrayerTimeOverlap,
)
from timetable_sa.examples.timetabling.constraints.soft.research_day import (
    ResearchDay,
)
from timetable_sa.examples.timetabling.constraints.soft.transit_time import (
    TransitTime,
)

__all__ = [
    "Compactness",
    "EveningClassPriority",
    "OverflowPenalty",
    "PreferredRoom",
    "PreferredTime",
    "PrayerTimeOverlap",
    "ResearchDay",
    "TransitTime",
]
