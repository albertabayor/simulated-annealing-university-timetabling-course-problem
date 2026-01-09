"""Time utility functions for timetabling."""

from functools import lru_cache


@lru_cache(maxsize=1000)
def time_to_minutes(time_str: str) -> int:
    """Convert time string (HH:MM) to minutes from midnight.
    
    Args:
        time_str: Time in format "HH:MM" (e.g., "08:30", "14:00")
    
    Returns:
        Minutes from midnight
    
    Examples:
        >>> time_to_minutes("00:00")
        0
        >>> time_to_minutes("08:30")
        510
        >>> time_to_minutes("14:00")
        840
    """
    hours, minutes = map(int, time_str.split(':'))
    return hours * 60 + minutes


@lru_cache(maxsize=1000)
def minutes_to_time(minutes: int) -> str:
    """Convert minutes from midnight to time string (HH:MM).
    
    Args:
        minutes: Minutes from midnight
    
    Returns:
        Time in format "HH:MM"
    
    Examples:
        >>> minutes_to_time(0)
        '00:00'
        >>> minutes_to_time(510)
        '08:30'
        >>> minutes_to_time(840)
        '14:00'
    """
    hours = minutes // 60
    mins = minutes % 60
    return f"{hours:02d}:{mins:02d}"


def calculate_end_time(start_time: str, sks: int, day: str) -> tuple[str, int]:
    """Calculate end time for a class based on start time and SKS.
    
    Matches TypeScript's calculateEndTime exactly:
    - Each SKS is 50 minutes
    - Prayer time overlap is added to the duration
    
    Args:
        start_time: Start time in format "HH:MM"
        sks: Number of credit hours
        day: Day of the week (for prayer time calculation)
    
    Returns:
        Tuple of (end_time_str, total_duration_minutes)
    
    Examples:
        >>> calculate_end_time("08:00", 2, "Monday")
        ('10:00', 110)
        >>> calculate_end_time("18:30", 3, "Thursday")
        ('21:50', 200)  # 3*50 + 50 prayer time = 200
    """
    start_minutes = time_to_minutes(start_time)
    
    # Each SKS is 50 minutes (matching TypeScript)
    class_minutes = sks * 50
    
    # Add prayer time overlap (simplified - matches TypeScript behavior)
    prayer_time = _get_prayer_time_overlap(start_time, sks, day)
    
    total_duration = class_minutes + prayer_time
    end_minutes = start_minutes + total_duration
    
    return minutes_to_time(end_minutes), total_duration


def _get_prayer_time_overlap(start_time: str, sks: int, day: str) -> int:
    """Calculate prayer time overlap in minutes.
    
    Matches TypeScript's getPrayerTimeOverlap exactly.
    """
    PRAYER_TIMES = {
        'DZUHUR': {'start': 11*60+40, 'end': 12*60+30, 'duration': 50},
        'ASHAR': {'start': 15*60, 'end': 15*60+30, 'duration': 30},
        'MAGHRIB': {'start': 18*60, 'end': 18*60+30, 'duration': 30},
    }
    
    start_minutes = time_to_minutes(start_time)
    class_minutes = sks * 50
    end_minutes = start_minutes + class_minutes
    
    total_prayer_time = 0
    
    # DZUHUR (11:40-12:30)
    if start_minutes < PRAYER_TIMES['DZUHUR']['end'] and end_minutes > PRAYER_TIMES['DZUHUR']['start']:
        if end_minutes > PRAYER_TIMES['DZUHUR']['end']:
            total_prayer_time += PRAYER_TIMES['DZUHUR']['duration']
    
    # ASHAR (15:00-15:30)
    if start_minutes < PRAYER_TIMES['ASHAR']['end'] and end_minutes > PRAYER_TIMES['ASHAR']['start']:
        if end_minutes > PRAYER_TIMES['ASHAR']['end']:
            total_prayer_time += PRAYER_TIMES['ASHAR']['duration']
    
    # MAGHRIB (18:00-18:30)
    if start_minutes < PRAYER_TIMES['MAGHRIB']['end'] and end_minutes > PRAYER_TIMES['MAGHRIB']['start']:
        if end_minutes > PRAYER_TIMES['MAGHRIB']['end']:
            total_prayer_time += PRAYER_TIMES['MAGHRIB']['duration']
    
    return total_prayer_time


def parse_time_range(time_range: str) -> tuple[str, str]:
    """Parse a time range string like "08:00 - 10:00".
    
    Args:
        time_range: Time range in format "HH:MM - HH:MM"
    
    Returns:
        Tuple of (start_time, end_time)
    
    Examples:
        >>> parse_time_range("08:00 - 10:00")
        ('08:00', '10:00')
        >>> parse_time_range("18.30 - 21.00")
        ('18.30', '21.00')
    """
    # Handle both " - " and " -" separators
    parts = time_range.replace('.', ':').split('-')
    start = parts[0].strip()
    end = parts[1].strip() if len(parts) > 1 else start
    
    # Normalize to HH:MM format
    def normalize(t: str) -> str:
        t = t.strip()
        if ':' not in t:
            return t + ":00"
        return t
    
    return normalize(start), normalize(end)


def get_period_number(day: str, start_time: str, period_start_hour: int = 7) -> int:
    """Get the period number for a time slot.
    
    Args:
        day: Day of the week
        start_time: Start time in format "HH:MM"
        period_start_hour: Hour when first period starts (default 7 = 07:00)
    
    Returns:
        Period number (1-based)
    
    Examples:
        >>> get_period_number("Monday", "07:00")
        1
        >>> get_period_number("Monday", "08:00")
        2
    """
    day_index = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"].index(day)
    start_minutes = time_to_minutes(start_time)
    period_start_minutes = period_start_hour * 60
    
    # Each period is 50 + 10 = 60 minutes
    period_length = 60
    
    offset_minutes = start_minutes - period_start_minutes
    period = (offset_minutes // period_length) + 1
    
    return max(1, period + day_index * 10)


def is_morning_class(class_type: str) -> bool:
    """Check if a class type is morning ('pagi').
    
    Args:
        class_type: "pagi" for morning, "sore" for evening
    
    Returns:
        True if morning class
    """
    return class_type.lower() == "pagi"


def is_evening_class(class_type: str) -> bool:
    """Check if a class type is evening ('sore').
    
    Args:
        class_type: "pagi" for morning, "sore" for evening
    
    Returns:
        True if evening class
    """
    return class_type.lower() == "sore"


def is_overlap(
    day1: str, start1: str, end1: str,
    day2: str, start2: str, end2: str
) -> bool:
    """Check if two time slots overlap.
    
    Args:
        day1: First day
        start1: First start time
        end1: First end time
        day2: Second day
        start2: Second start time
        end2: Second end time
    
    Returns:
        True if slots overlap
    """
    if day1 != day2:
        return False
    
    s1 = time_to_minutes(start1)
    e1 = time_to_minutes(end1)
    s2 = time_to_minutes(start2)
    e2 = time_to_minutes(end2)
    
    return max(s1, s2) < min(e1, e2)


def is_valid_friday_start_time(start_time: str) -> bool:
    """Check if start time is valid for Friday (TypeScript behavior).
    
    Cannot start at exactly 11:00, 11:40, 12:00, 12:30, 13:00.
    But 13:20, 13:30, etc are OK!
    
    Args:
        start_time: Time in format "HH:MM"
    
    Returns:
        True if valid Friday start time
    """
    prohibited = ['11:00', '11:40', '12:00', '12:30', '13:00']
    return start_time not in prohibited


def is_starting_during_prayer_time(start_time: str) -> bool:
    """Check if a class would start during prayer time.
    
    Classes CAN start AT prayer start time (e.g., 18:00) or after prayer end time (e.g., 18:30).
    But they cannot start DURING prayer time (e.g., 18:15).
    
    Args:
        start_time: Time in format "HH:MM"
    
    Returns:
        True if starting during prayer time
    """
    start_minutes = time_to_minutes(start_time)
    
    # DZUHUR (11:40-12:30): cannot start between 11:40 and 12:30 (exclusive)
    if start_minutes > 700 and start_minutes < 750:
        return True
    
    # ASHAR (15:00-15:30): cannot start between 15:00 and 15:30 (exclusive)
    if start_minutes > 900 and start_minutes < 930:
        return True
    
    # MAGHRIB (18:00-18:30): cannot start between 18:00 and 18:30 (exclusive)
    if start_minutes > 1080 and start_minutes < 1110:
        return True
    
    return False


def is_overlap(
    day1: str, start1: str, end1: str,
    day2: str, start2: str, end2: str
) -> bool:
    """Check if two time slots overlap.
    
    Args:
        day1: First day
        start1: First start time
        end1: First end time
        day2: Second day
        start2: Second start time
        end2: Second end time
    
    Returns:
        True if slots overlap
    """
    if day1 != day2:
        return False
    
    s1 = time_to_minutes(start1)
    e1 = time_to_minutes(end1)
    s2 = time_to_minutes(start2)
    e2 = time_to_minutes(end2)
    
    return max(s1, s2) < min(e1, e2)


def format_duration(minutes: int) -> str:
    """Format duration in minutes to human-readable string.
    
    Args:
        minutes: Duration in minutes
    
    Returns:
        Formatted string like "1h 30m" or "45m"
    """
    hours = minutes // 60
    mins = minutes % 60
    
    if hours > 0:
        if mins > 0:
            return f"{hours}h {mins}m"
        return f"{hours}h"
    return f"{mins}m"
