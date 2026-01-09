"""Time slot validation utilities."""

from typing import List, Dict, Optional
from timetable_sa.examples.timetabling.domain_types.domain import TimeSlot
from timetable_sa.examples.timetabling.utils.time import time_to_minutes


VALID_DAYS = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
]

VALID_PERIODS = list(range(1, 13))

MIN_START_HOUR = 7
MAX_END_HOUR = 21


class SlotValidationError:
    """Error class for slot validation failures."""
    
    def __init__(self, message: str, slot: Optional[TimeSlot] = None):
        self.message = message
        self.slot = slot
    
    def __str__(self) -> str:
        return self.message
    
    def __repr__(self) -> str:
        return f"SlotValidationError(message={self.message!r}, slot={self.slot})"


def validate_time_slot(slot: TimeSlot) -> List[SlotValidationError]:
    """Validate a single time slot.
    
    Args:
        slot: Time slot to validate
        
    Returns:
        List of validation errors (empty if valid)
    """
    errors = []
    
    if slot.day not in VALID_DAYS:
        errors.append(SlotValidationError(
            f"Invalid day: {slot.day}. Must be one of {VALID_DAYS}",
            slot
        ))
    
    if slot.period not in VALID_PERIODS:
        errors.append(SlotValidationError(
            f"Invalid period: {slot.period}. Must be 1-12",
            slot
        ))
    
    try:
        start_minutes = time_to_minutes(slot.start_time)
        end_minutes = time_to_minutes(slot.end_time)
        
        if start_minutes >= end_minutes:
            errors.append(SlotValidationError(
                f"Start time ({slot.start_time}) must be before end time ({slot.end_time})",
                slot
            ))
        
        start_hour = start_minutes // 60
        if start_hour < MIN_START_HOUR or start_hour > MAX_END_HOUR:
            errors.append(SlotValidationError(
                f"Start hour {start_hour} outside valid range ({MIN_START_HOUR}-{MAX_END_HOUR})",
                slot
            ))
    
    except ValueError:
        errors.append(SlotValidationError(
            f"Invalid time format: {slot.start_time} or {slot.end_time}. Expected HH:MM",
            slot
        ))
    
    return errors


def validate_time_slots(slots: List[TimeSlot]) -> Dict[str, List[SlotValidationError]]:
    """Validate multiple time slots.
    
    Args:
        slots: List of time slots to validate
        
    Returns:
        Dictionary mapping slot index to list of validation errors
    """
    errors: Dict[str, List[SlotValidationError]] = {}
    
    for i, slot in enumerate(slots):
        slot_errors = validate_time_slot(slot)
        if slot_errors:
            errors[str(i)] = slot_errors
    
    return errors


def check_slot_conflict(slot1: TimeSlot, slot2: TimeSlot) -> bool:
    """Check if two time slots conflict.
    
    Args:
        slot1: First time slot
        slot2: Second time slot
        
    Returns:
        True if slots conflict
    """
    if slot1.day != slot2.day:
        return False
    
    start1 = time_to_minutes(slot1.start_time)
    end1 = time_to_minutes(slot1.end_time)
    start2 = time_to_minutes(slot2.start_time)
    end2 = time_to_minutes(slot2.end_time)
    
    return max(start1, start2) < min(end1, end2)


def find_conflicting_slots(slots: List[TimeSlot]) -> List[tuple[int, int]]:
    """Find all conflicting slot pairs.
    
    Args:
        slots: List of time slots to check
        
    Returns:
        List of (index1, index2) tuples for conflicting slots
    """
    conflicts = []
    
    for i in range(len(slots)):
        for j in range(i + 1, len(slots)):
            if check_slot_conflict(slots[i], slots[j]):
                conflicts.append((i, j))
    
    return conflicts


def get_period_time_range(period: int) -> tuple[str, str]:
    """Get the time range for a standard period.
    
    Args:
        period: Period number (1-12)
        
    Returns:
        Tuple of (start_time, end_time) strings
    """
    period_duration = 50
    break_duration = 10
    
    start_minutes = (MIN_START_HOUR * 60) + ((period - 1) * (period_duration + break_duration))
    end_minutes = start_minutes + period_duration
    
    start_time = f"{start_minutes // 60:02d}:{start_minutes % 60:02d}"
    end_time = f"{end_minutes // 60:02d}:{end_minutes % 60:02d}"
    
    return start_time, end_time


def generate_standard_slot(day: str, period: int) -> TimeSlot:
    """Generate a standard time slot for a day and period.
    
    Args:
        day: Day of the week
        period: Period number (1-12)
        
    Returns:
        TimeSlot with standard times
    """
    start_time, end_time = get_period_time_range(period)
    
    return TimeSlot(
        day=day,
        start_time=start_time,
        end_time=end_time,
        period=period
    )


def are_slots_equivalent(slot1: TimeSlot, slot2: TimeSlot) -> bool:
    """Check if two slots are equivalent (same day and period).
    
    Args:
        slot1: First time slot
        slot2: Second time slot
        
    Returns:
        True if slots are equivalent
    """
    return slot1.day == slot2.day and slot1.period == slot2.period


def sort_slots_by_time(slots: List[TimeSlot]) -> List[TimeSlot]:
    """Sort slots by day and then by period.
    
    Args:
        slots: List of time slots to sort
        
    Returns:
        Sorted list of time slots
    """
    day_order = {day: i for i, day in enumerate(VALID_DAYS)}
    
    return sorted(slots, key=lambda s: (day_order.get(s.day, 999), s.period))
