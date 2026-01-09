"""Room availability checking utilities."""

from typing import List, Set, Dict, Any, Optional

from timetable_sa.examples.timetabling.domain_types.state import TimetableState, ScheduleEntry
from timetable_sa.examples.timetabling.domain_types.domain import Room


class RoomAvailabilityChecker:
    """Check room availability at specific times.
    
    Matches TypeScript's room-availability.ts functionality.
    """
    
    def __init__(self, state: TimetableState):
        """Initialize with timetable state.
        
        Args:
            state: Timetable state
        """
        self.state = state
        self._occupied: Set[str] = set()
        self._build_index()
    
    def _build_index(self) -> None:
        """Build index of room occupancy."""
        for entry in self.state.schedule:
            key = f"{entry.room}|{entry.time_slot.day}|{entry.time_slot.period}"
            self._occupied.add(key)
    
    def is_room_available(self, room_code: str, day: str, period: int) -> bool:
        """Check if room is available at a specific time.
        
        Args:
            room_code: Room code
            day: Day of week
            period: Period number
        
        Returns:
            True if room is available, False otherwise
        """
        key = f"{room_code}|{day}|{period}"
        return key not in self._occupied
    
    def find_best_matching_room(
        self,
        day: str,
        period: int,
        participants: int,
        needs_lab: bool = False,
        room_type: Optional[str] = None
    ) -> Optional[Room]:
        """Find best matching room for a class.
        
        Args:
            day: Day of week
            period: Period number
            participants: Number of students
            needs_lab: Whether lab is required
            room_type: Optional room type preference
        
        Returns:
            Best matching room or None
        """
        available = self.get_available_rooms(day, period, participants, needs_lab, room_type)
        
        if not available:
            return None
        
        # Prefer smallest room that fits (efficient resource usage)
        available.sort(key=lambda r: r.capacity)
        return available[0]
    
    def get_available_rooms(
        self, 
        day: str, 
        period: int,
        min_capacity: int = 0,
        room_type: Optional[str] = None,
    ) -> List[Room]:
        """Get list of available rooms at a specific time.
        
        Args:
            day: Day of week
            period: Period number
            min_capacity: Minimum room capacity
            room_type: Room type filter ("theory", "lab", etc.)
        
        Returns:
            List of available rooms
        """
        available = []
        for room in self.state.rooms:
            if room.capacity < min_capacity:
                continue
            if room_type and room.type.lower() != room_type.lower():
                continue
            if self.is_room_available(room.code, day, period):
                available.append(room)
        return available
    
    def find_best_room(
        self,
        day: str,
        period: int,
        participants: int,
        needs_lab: bool = False,
    ) -> Optional[Room]:
        """Find the best room for a class at a specific time.
        
        Args:
            day: Day of week
            period: Period number
            participants: Number of students
            needs_lab: Whether lab is required
        
        Returns:
            Best matching room or None
        """
        room_type = "lab" if needs_lab else None
        available = self.get_available_rooms(
            day, period, 
            min_capacity=participants,
            room_type=room_type,
        )
        
        if not available:
            return None
        
        # Prefer smallest room that fits (efficient resource usage)
        available.sort(key=lambda r: r.capacity)
        return available[0]
    
    def get_conflicting_entries(self, room_code: str, day: str, period: int) -> List[ScheduleEntry]:
        """Get entries conflicting with a specific room/time.
        
        Args:
            room_code: Room code
            day: Day of week
            period: Period number
        
        Returns:
            List of conflicting entries
        """
        conflicts = []
        for entry in self.state.schedule:
            if (entry.room == room_code and 
                entry.time_slot.day == day and
                entry.time_slot.period == period):
                conflicts.append(entry)
        return conflicts
    
    def get_schedule_for_room(self, room_code: str) -> Dict[str, List[ScheduleEntry]]:
        """Get schedule for a specific room, grouped by day.

        Args:
            room_code: Room code

        Returns:
            Dictionary mapping day to list of entries
        """
        schedule: Dict[str, List[ScheduleEntry]] = {}
        for entry in self.state.schedule:
            if entry.room == room_code:
                day = entry.time_slot.day
                if day not in schedule:
                    schedule[day] = []
                schedule[day].append(entry)
        return schedule


def find_available_slot(
    state: TimetableState,
    room_code: str,
    duration_periods: int = 2,
    preferred_days: Optional[List[str]] = None,
    start_period: int = 1,
    end_period: int = 12
) -> Dict[str, Any]:
    """Find an available time slot for a room.

    Matches TypeScript's findAvailableSlot functionality.

    Args:
        state: Timetable state
        room_code: Room code
        duration_periods: Duration in periods
        preferred_days: Preferred days (default: all weekdays)
        start_period: Start period (default: 1)
        end_period: End period (default: 12)

    Returns:
        Dictionary with day, start_period, end_period, and available keys
    """
    checker = RoomAvailabilityChecker(state)

    for day in preferred_days if preferred_days else ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]:
        for period in range(start_period, end_period + 1):
            if checker.is_room_available(room_code, day, period):
                return {
                    "day": day,
                    "start_period": period,
                    "end_period": period,
                    "available": True
                }

    return {"available": False}
