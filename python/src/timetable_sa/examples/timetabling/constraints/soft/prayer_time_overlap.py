"""Prayer time overlap constraint."""

from typing import Literal, List
from timetable_sa.core.interfaces import Constraint
from timetable_sa.examples.timetabling.domain_types.state import TimetableState
from timetable_sa.examples.timetabling.utils.prayer_times import PRAYER_PERIODS


class PrayerTimeOverlap(Constraint):
    """Soft constraint to minimize class overlap with prayer times.
    
    This is a soft constraint - it penalizes classes during prayer times
    but doesn't completely forbid them.
    """
    
    name: str = "Prayer Time Overlap"
    type: Literal["hard", "soft"] = "soft"
    weight: float = 50.0
    
    def evaluate(self, state: TimetableState) -> float:
        """Check for classes that overlap with prayer times.
        
        Args:
            state: Current timetable state
            
        Returns:
            1.0 if no overlap, lower score based on overlap count
        """
        overlapping = self._find_overlapping(state)
        
        if not overlapping:
            return 1.0
        
        return 1.0 / (1 + len(overlapping) * 0.5)
    
    def _find_overlapping(self, state: TimetableState) -> List:
        """Find classes overlapping with prayer times.
        
        Args:
            state: Current timetable state
            
        Returns:
            List of overlapping class details
        """
        overlapping = []
        
        for entry in state.schedule:
            day = entry.time_slot.day
            period = entry.time_slot.period
            
            if day in PRAYER_PERIODS:
                prayer_periods = PRAYER_PERIODS[day]
                for prayer_info in prayer_periods:
                    if prayer_info["start_period"] <= period <= prayer_info["end_period"]:
                        overlapping.append({
                            "class_id": entry.class_id,
                            "day": day,
                            "period": period,
                            "prayer_name": prayer_info["name"]
                        })
                        break
        
        return overlapping
    
    def get_violations(self, state: TimetableState) -> List[str]:
        """Get list of prayer time overlap violations.
        
        Args:
            state: Current timetable state
            
        Returns:
            List of violation descriptions
        """
        overlapping = self._find_overlapping(state)
        descriptions = []
        
        for o in overlapping:
            descriptions.append(
                f"Class {o['class_id']} overlaps with {o['prayer_name']} "
                f"on {o['day']} at period {o['period']}"
            )
        
        return descriptions
    
    def describe(self, state: TimetableState) -> str | None:
        """Provide human-readable description of violations.
        
        Args:
            state: Current timetable state
            
        Returns:
            Description of violations, or None if satisfied
        """
        overlapping = self._find_overlapping(state)
        
        if not overlapping:
            return None
        
        return f"Found {len(overlapping)} class(es) overlapping with prayer times"
