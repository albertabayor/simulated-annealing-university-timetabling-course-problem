"""Hard constraint: Prayer Time Start.

Ensures classes do not start during prayer times (Dzuhur, Ashar, Maghrib).
"""

from typing import Literal, List

from timetable_sa.core.interfaces import Constraint
from timetable_sa.examples.timetabling.domain_types.state import TimetableState
from timetable_sa.examples.timetabling.utils.prayer_times import PRAYER_TIMES
from timetable_sa.examples.timetabling.utils.time import time_to_minutes


class PrayerTimeStart(Constraint):
    """Hard constraint: Classes should not start during prayer times.
    
    Classes should not begin during the main prayer times to show
    respect for the prayer schedule and allow students/lecturers
    to attend prayers.
    
    Prayer times (approximate):
    - Dzuhur: 11:50-12:40
    - Ashar: 15:00-15:30
    - Maghrib: 17:45-18:15
    
    Examples of violations:
        - Class starting at 12:00 (during Dzuhur)
        - Class starting at 15:10 (during Ashar)
    """
    
    name: str = "Prayer Time Start"
    type: Literal["hard", "soft"] = "hard"

    def evaluate(self, state: TimetableState) -> float:
        """Evaluate the constraint.
        
        Returns:
            1.0 if no classes start during prayer times
        """
        violations = self._find_violations(state)
        
        if not violations:
            return 1.0
        
        return 1.0 / (1 + len(violations))

    def get_violations(self, state: TimetableState) -> List[str]:
        """Get detailed list of prayer time start violations.
        
        Returns:
            List of violation descriptions
        """
        violations = self._find_violations(state)
        descriptions = []
        
        for v in violations:
            descriptions.append(
                f"Class {v['class_id']} on {v['day']} at {v['start_time']} "
                f"starts during {v['prayer']} prayer time"
            )
        
        return descriptions

    def _find_violations(self, state: TimetableState) -> List[dict]:
        """Find all prayer time start violations.
        
        Matches TypeScript's isStartingDuringPrayerTime():
        - Returns TRUE if start time is BETWEEN prayer times (exclusive)
        - Classes CAN start AT prayer start time or AFTER prayer end time
        
        Examples:
        - Starting at 11:00 (before Dzuhur) -> OK
        - Starting at 11:40 (at Dzuhur start) -> VIOLATION
        - Starting at 12:00 (during Dzuhur) -> VIOLATION
        - Starting at 12:31 (after Dzuhur end) -> OK
        """
        violations = []
        
        for entry in state.schedule:
            start_minutes = time_to_minutes(entry.time_slot.start_time)
            day = entry.time_slot.day
            
            for prayer_name, prayer_info in PRAYER_TIMES.items():
                prayer_start = prayer_info["start"]
                prayer_end = prayer_info["end"]
                
                # Don't apply on Friday (handled by NoFridayPrayConflit)
                if day == "Friday" or prayer_name == "DZUHUR":
                    continue
                
                # Check if start time is DURING prayer time (exclusive boundaries)
                # Violation if: prayer_start < start_minutes < prayer_end
                if prayer_start < start_minutes < prayer_end:
                    violations.append({
                        "class_id": entry.class_id,
                        "kelas": entry.kelas,
                        "day": day,
                        "start_time": entry.time_slot.start_time,
                        "prayer": prayer_name,
                    })
        
        return violations
