"""Time slot generation utilities."""

from typing import Optional, List

from timetable_sa.examples.timetabling.domain_types.domain import TimeSlot
from timetable_sa.examples.timetabling.utils.time import time_to_minutes


class TimeSlotGenerator:
    """Generator for time slots based on configuration."""
    
    DEFAULT_DAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    
    def __init__(
        self,
        start_hour: int = 7,
        end_hour: int = 21,
        period_duration: int = 50,
        break_duration: int = 10,
        days: Optional[List[str]] = None,
    ):
        self.start_hour = start_hour
        self.end_hour = end_hour
        self.period_duration = period_duration
        self.break_duration = break_duration
        self.days = days if days is not None else self.DEFAULT_DAYS.copy()

    def generate(self) -> List[TimeSlot]:
        """Generate all time slots based on configuration.
        
        Returns:
            List of TimeSlot objects
        """
        time_slots = []
        period = 1

        for day in self.days:
            current_hour = self.start_hour
            current_minute = 0

            while current_hour < self.end_hour or (
                current_hour == self.end_hour and current_minute == 0
            ):
                start_time = f"{current_hour:02d}:{current_minute:02d}"
                
                # Calculate end time
                end_minutes = current_minute + self.period_duration
                end_hour = current_hour + end_minutes // 60
                end_minute = end_minutes % 60
                end_time = f"{end_hour:02d}:{end_minute:02d}"

                time_slots.append(TimeSlot(
                    day=day,
                    start_time=start_time,
                    end_time=end_time,
                    period=period
                ))

                period += 1

                # Move to next period
                current_minute += self.period_duration + self.break_duration
                if current_minute >= 60:
                    current_hour += current_minute // 60
                    current_minute = current_minute % 60

        return time_slots

    def generate_standard_slots(self) -> List[TimeSlot]:
        """Generate standard 50-minute periods with 10-minute breaks.
        
        Standard schedule:
        - Period 1: 07:00 - 07:50
        - Period 2: 08:00 - 08:50
        - ...
        - Period N: N:00 - N:50
        """
        time_slots = []
        period = 1

        for day in self.days:
            for hour in range(self.start_hour, self.end_hour):
                # First period of the hour
                start_time = f"{hour:02d}:00"
                end_time = f"{hour:02d}:{self.period_duration:02d}"

                time_slots.append(TimeSlot(
                    day=day,
                    start_time=start_time,
                    end_time=end_time,
                    period=period
                ))
                period += 1

                # Second period of the hour (with break after first)
                start_minute = self.period_duration + self.break_duration
                if start_minute < 60:
                    end_hour = hour
                    end_minute = start_minute + self.period_duration
                    if end_minute >= 60:
                        end_hour = hour + 1
                        end_minute -= 60
                    end_time = f"{end_hour:02d}:{end_minute:02d}"

                    time_slots.append(TimeSlot(
                        day=day,
                        start_time=f"{hour:02d}:{start_minute:02d}",
                        end_time=end_time,
                        period=period
                    ))
                    period += 1

        return time_slots

    def generate_morning_slots(self) -> List[TimeSlot]:
        """Generate morning time slots only (before 12:00)."""
        return self._generate_filtered_slots(max_hour=12)

    def generate_evening_slots(self) -> List[TimeSlot]:
        """Generate evening time slots only (from 17:00 onwards)."""
        return self._generate_filtered_slots(min_hour=17)

    def _generate_filtered_slots(self, min_hour: Optional[int] = None, max_hour: Optional[int] = None) -> List[TimeSlot]:
        """Generate filtered time slots based on hour constraints."""
        all_slots = self.generate()
        
        filtered = []
        for slot in all_slots:
            start_minutes = time_to_minutes(slot.start_time)
            slot_hour = start_minutes // 60
            
            if min_hour is not None and slot_hour < min_hour:
                continue
            if max_hour is not None and slot_hour >= max_hour:
                continue
            
            filtered.append(slot)
        
        return filtered

    def get_slots_for_day(self, day: str) -> List[TimeSlot]:
        """Get all time slots for a specific day."""
        return [slot for slot in self.generate() if slot.day == day]

    def get_slots_by_period(self, period: int) -> List[TimeSlot]:
        """Get all time slots at a specific period number."""
        return [slot for slot in self.generate() if slot.period == period]


def generate_default_time_slots() -> List[TimeSlot]:
    """Generate default time slots (07:00 - 21:00, Monday-Saturday).
    
    Returns:
        List of standard time slots
    """
    generator = TimeSlotGenerator(
        start_hour=7,
        end_hour=22,
        period_duration=50,
        break_duration=10,
        days=["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    )
    return generator.generate()


def generate_morning_slots() -> List[TimeSlot]:
    """Generate morning time slots (07:00 - 12:00).
    
    Returns:
        List of morning time slots
    """
    generator = TimeSlotGenerator(
        start_hour=7,
        end_hour=12,
        period_duration=50,
        break_duration=10,
        days=["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    )
    return generator.generate()


def generate_evening_slots() -> List[TimeSlot]:
    """Generate evening time slots (17:00 - 21:00).
    
    Returns:
        List of evening time slots
    """
    generator = TimeSlotGenerator(
        start_hour=17,
        end_hour=22,
        period_duration=50,
        break_duration=10,
        days=["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    )
    return generator.generate()
