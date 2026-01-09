"""Prayer time constants for timetabling constraints.

Prayer times in minutes from midnight (matching TypeScript):
- DZUHUR: 11:40 - 12:30 (700-750 minutes)
- ASHAR: 15:00 - 15:30 (900-930 minutes)
- MAGHRIB: 18:00 - 18:30 (1080-1110 minutes)
"""

from typing import List, Dict, Any


# Prayer times as (start_minute, end_minute, name)
# Times are approximate and may vary slightly
PRAYER_TIMES = {
    "DZUHUR": {"start": 700, "end": 750, "duration": 50, "name": "Dzuhur"},
    "ASHAR": {"start": 900, "end": 930, "duration": 30, "name": "Ashar"},
    "MAGHRIB": {"start": 1080, "end": 1110, "duration": 30, "name": "Maghrib"},
}

# Days when Friday prayer applies
FRIDAY_PRAYER_DAY = "Friday"

# Friday prayer time (shorter, 11:40-13:10)
FRIDAY_PRAYER_START = 690  # 11:30
FRIDAY_PRAYER_END = 750   # 12:30

# Standard periods (50 minutes each, with 10 minute breaks)
PERIOD_DURATION = 50
BREAK_DURATION = 10

# Days of week in order
DAYS_OF_WEEK = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
]

# Morning class type
MORNING_CLASS = "pagi"
# Evening class type
EVENING_CLASS = "sore"


def _minute_to_period(minute: int) -> int:
    """Convert minute from midnight to period number (1-indexed).
    
    Assumes periods start at 7:00 AM (420 minutes).
    """
    start_minute = 420  # 7:00 AM
    period_length = PERIOD_DURATION + BREAK_DURATION  # 60 minutes per period
    period = (minute - start_minute) // period_length + 1
    return max(1, period)


# Prayer periods by day - maps day to list of prayer period info with period numbers
def _build_prayer_periods() -> Dict[str, List[Dict[str, Any]]]:
    """Build prayer periods with period numbers for each day."""
    result = {}
    
    for day in DAYS_OF_WEEK:
        day_prayers = []
        for prayer_name, prayer_info in PRAYER_TIMES.items():
            start_period = _minute_to_period(prayer_info["start"])
            end_period = _minute_to_period(prayer_info["end"])
            day_prayers.append({
                "name": prayer_info["name"],
                "start_period": start_period,
                "end_period": end_period,
                "start_minute": prayer_info["start"],
                "end_minute": prayer_info["end"],
            })
        result[day] = day_prayers
    
    return result


PRAYER_PERIODS = _build_prayer_periods()


# Friday prayer periods - special shorter prayer
def _build_friday_prayer_periods() -> List[Dict[str, Any]]:
    """Build Friday prayer period info."""
    return [{
        "name": "Friday Prayer",
        "start_period": _minute_to_period(FRIDAY_PRAYER_START),
        "end_period": _minute_to_period(FRIDAY_PRAYER_END),
        "start_minute": FRIDAY_PRAYER_START,
        "end_minute": FRIDAY_PRAYER_END,
    }]


FRIDAY_PRAYER_PERIODS = _build_friday_prayer_periods()


def is_in_prayer_time(day: str, start_minute: int, sks: int) -> dict:
    """Check if a class overlaps with prayer times.
    
    Args:
        day: Day of the week
        start_minute: Start time in minutes from midnight
        sks: Number of credit hours (each SKS = 50 minutes + break)
    
    Returns:
        Dict with prayer name and overlap in minutes
    """
    end_minute = start_minute + (sks * PERIOD_DURATION) + ((sks - 1) * BREAK_DURATION)
    
    result = {
        "dzuhur_overlap": 0,
        "ashar_overlap": 0,
        "maghrib_overlap": 0,
        "friday_prayer_overlap": 0,
        "has_overlap": False,
    }
    
    # Check regular prayer times
    for prayer_name, prayer_info in PRAYER_TIMES.items():
        prayer_start = prayer_info["start"]
        prayer_end = prayer_info["end"]
        
        # Calculate overlap
        overlap_start = max(start_minute, prayer_start)
        overlap_end = min(end_minute, prayer_end)
        
        if overlap_end > overlap_start:
            overlap_minutes = overlap_end - overlap_start
            if prayer_name == "DZUHUR":
                result["dzuhur_overlap"] = overlap_minutes
            elif prayer_name == "ASHAR":
                result["ashar_overlap"] = overlap_minutes
            elif prayer_name == "MAGHRIB":
                result["maghrib_overlap"] = overlap_minutes
            result["has_overlap"] = True
    
    # Check Friday prayer specifically
    if day == FRIDAY_PRAYER_DAY:
        friday_overlap_start = max(start_minute, FRIDAY_PRAYER_START)
        friday_overlap_end = min(end_minute, FRIDAY_PRAYER_END)
        
        if friday_overlap_end > friday_overlap_start:
            result["friday_prayer_overlap"] = friday_overlap_end - friday_overlap_start
            result["has_overlap"] = True
    
    return result


def get_prayer_time_for_day(day: str) -> list:
    """Get prayer time info for a specific day.
    
    Args:
        day: Day of the week
    
    Returns:
        List of prayer time dictionaries
    """
    prayers = []
    for prayer_name, prayer_info in PRAYER_TIMES.items():
        prayer = {
            "name": prayer_info["name"],
            "start": prayer_info["start"],
            "end": prayer_info["end"],
            "duration": prayer_info["duration"],
        }
        if day == FRIDAY_PRAYER_DAY and prayer_name == "DZUHUR":
            prayer["is_friday_prayer"] = True
            prayer["start"] = FRIDAY_PRAYER_START
            prayer["end"] = FRIDAY_PRAYER_END
        prayers.append(prayer)
    return prayers
