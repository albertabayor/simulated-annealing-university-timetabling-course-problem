"""Constraint helper functions for timetabling."""

from collections import defaultdict
from typing import Dict, List, Callable

from timetable_sa.examples.timetabling.domain_types.state import TimetableState, ScheduleEntry
from timetable_sa.examples.timetabling.utils.time import time_to_minutes


def group_by_room(state: TimetableState) -> Dict[str, List[ScheduleEntry]]:
    """Group schedule entries by room.
    
    Args:
        state: Timetable state
    
    Returns:
        Dictionary mapping room code to list of entries
    """
    groups: Dict[str, List[ScheduleEntry]] = defaultdict(list)
    for entry in state.schedule:
        groups[entry.room].append(entry)
    return groups


def group_by_lecturer(state: TimetableState) -> Dict[str, List[ScheduleEntry]]:
    """Group schedule entries by lecturer.
    
    Args:
        state: Timetable state
    
    Returns:
        Dictionary mapping lecturer code to list of entries
    """
    groups: Dict[str, List[ScheduleEntry]] = defaultdict(list)
    for entry in state.schedule:
        for lecturer in entry.lecturers:
            groups[lecturer].append(entry)
    return groups


def group_by_prodi(state: TimetableState) -> Dict[str, List[ScheduleEntry]]:
    """Group schedule entries by study program.
    
    Args:
        state: Timetable state
    
    Returns:
        Dictionary mapping prodi to list of entries
    """
    groups: Dict[str, List[ScheduleEntry]] = defaultdict(list)
    for entry in state.schedule:
        groups[entry.prodi].append(entry)
    return groups


def group_by_day(state: TimetableState) -> Dict[str, List[ScheduleEntry]]:
    """Group schedule entries by day.
    
    Args:
        state: Timetable state
    
    Returns:
        Dictionary mapping day to list of entries
    """
    groups: Dict[str, List[ScheduleEntry]] = defaultdict(list)
    for entry in state.schedule:
        groups[entry.time_slot.day].append(entry)
    return groups


def get_entries_at_time(
    state: TimetableState, 
    day: str, 
    start_time: str
) -> List[ScheduleEntry]:
    """Get all entries at a specific day and start time.
    
    Args:
        state: Timetable state
        day: Day of week
        start_time: Start time string
    
    Returns:
        List of entries at that time
    """
    result = []
    for entry in state.schedule:
        if (entry.time_slot.day == day and 
            entry.time_slot.start_time == start_time):
            result.append(entry)
    return result


def check_time_overlap(entry1: ScheduleEntry, entry2: ScheduleEntry) -> bool:
    """Check if two entries overlap in time.
    
    Args:
        entry1: First schedule entry
        entry2: Second schedule entry
    
    Returns:
        True if entries overlap
    """
    if entry1.time_slot.day != entry2.time_slot.day:
        return False
    
    start1 = time_to_minutes(entry1.time_slot.start_time)
    end1 = time_to_minutes(entry1.time_slot.end_time)
    start2 = time_to_minutes(entry2.time_slot.start_time)
    end2 = time_to_minutes(entry2.time_slot.end_time)
    
    return max(start1, start2) < min(end1, end2)


def count_conflicts(
    entries: List[ScheduleEntry],
    check_fn: Callable[[ScheduleEntry, ScheduleEntry], bool]
) -> int:
    """Count conflicts using a custom check function.
    
    Args:
        entries: List of schedule entries
        check_fn: Function that takes two entries and returns True if they conflict
    
    Returns:
        Number of conflicts found
    """
    count = 0
    for i in range(len(entries)):
        for j in range(i + 1, len(entries)):
            if check_fn(entries[i], entries[j]):
                count += 1
    return count


def calculate_room_utilization(state: TimetableState) -> Dict[str, float]:
    """Calculate room utilization percentage.
    
    Args:
        state: Timetable state
    
    Returns:
        Dictionary mapping room code to utilization percentage
    """
    room_groups = group_by_room(state)
    utilization: Dict[str, float] = {}
    
    # Total possible periods per week (6 days * ~12 periods)
    total_periods = 72
    
    for room, entries in room_groups.items():
        # Count unique time slots used
        used_slots = set()
        for entry in entries:
            used_slots.add((entry.time_slot.day, entry.time_slot.period))
        
        utilization[room] = len(used_slots) / total_periods * 100
    
    return utilization


def calculate_lecturer_workload(state: TimetableState) -> Dict[str, int]:
    """Calculate teaching periods per lecturer.
    
    Args:
        state: Timetable state
    
    Returns:
        Dictionary mapping lecturer code to period count
    """
    lecturer_groups = group_by_lecturer(state)
    workload: Dict[str, int] = {}
    
    for lecturer, entries in lecturer_groups.items():
        # Count unique periods
        periods = set()
        for entry in entries:
            periods.add((entry.time_slot.day, entry.time_slot.period))
        workload[lecturer] = len(periods)
    
    return workload
