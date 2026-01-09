"""Tests for utility functions."""

import pytest
from timetable_sa.examples.timetabling.utils.time import (
    time_to_minutes,
    minutes_to_time,
    calculate_end_time,
    parse_time_range,
    get_period_number,
    is_morning_class,
    is_evening_class,
    is_overlap,
    format_duration,
)
from timetable_sa.examples.timetabling.utils.prayer_times import (
    PRAYER_TIMES,
    is_in_prayer_time,
    get_prayer_time_for_day,
    DAYS_OF_WEEK,
)
from timetable_sa.examples.timetabling.utils.constraint_helpers import (
    group_by_room,
    group_by_lecturer,
    group_by_prodi,
    group_by_day,
    check_time_overlap,
    count_conflicts,
)
from timetable_sa.examples.timetabling.utils.class_helper import (
    get_lecturers_for_class,
    needs_lab,
    get_preferred_rooms,
    get_class_identifier,
    filter_classes_by_prodi,
    filter_classes_by_type,
)
from timetable_sa.examples.timetabling.utils.slot_validator import (
    validate_time_slot,
    check_slot_conflict,
    get_period_time_range,
    generate_standard_slot,
    VALID_DAYS,
    VALID_PERIODS,
)


class TestTimeFunctions:
    """Tests for time utility functions."""
    
    def test_time_to_minutes(self):
        """Test converting time string to minutes."""
        assert time_to_minutes("08:00") == 8 * 60
        assert time_to_minutes("00:00") == 0
        assert time_to_minutes("23:59") == 23 * 60 + 59
    
    def test_minutes_to_time(self):
        """Test converting minutes to time string."""
        assert minutes_to_time(480) == "08:00"
        assert minutes_to_time(0) == "00:00"
        assert minutes_to_time(1439) == "23:59"
    
    def test_calculate_end_time(self):
        """Test calculating end time from start and SKS."""
        end_time, duration = calculate_end_time("08:00", 2, "Monday")
        assert end_time == "09:50"  # 2 * 50 + 10 break
        assert duration == 110
    
    def test_parse_time_range(self):
        """Test parsing time range string."""
        start, end = parse_time_range("08:00 - 10:00")
        assert start == "08:00"
        assert end == "10:00"
    
    def test_get_period_number(self):
        """Test getting period number from time."""
        # get_period_number(day, start_time, period_start_hour=7)
        # Period 1: 7:00-7:50 (420-470 min)
        # Period 2: 8:00-8:50 (480-530 min)
        assert get_period_number("Monday", "07:00") == 1
        assert get_period_number("Monday", "08:00") == 2
        assert get_period_number("Monday", "12:30") == 6
        # Different day adds offset
        assert get_period_number("Tuesday", "07:00") == 11
    
    def test_is_overlap(self):
        """Test time overlap detection."""
        # is_overlap(day1, start1, end1, day2, start2, end2)
        assert is_overlap("Monday", "08:00", "09:30", "Monday", "08:30", "10:00") is True
        assert is_overlap("Monday", "08:00", "09:00", "Monday", "10:00", "11:00") is False
        assert is_overlap("Monday", "08:00", "09:00", "Tuesday", "08:00", "09:00") is False  # Different days
        assert is_overlap("Monday", "08:00", "09:00", "Monday", "07:00", "08:00") is False  # Touching is not overlap
    
    def test_format_duration(self):
        """Test duration formatting."""
        assert format_duration(90) == "1h 30m"
        assert format_duration(60) == "1h"
        assert format_duration(30) == "30m"


class TestPrayerTimes:
    """Tests for prayer time utilities."""
    
    def test_prayer_times_structure(self):
        """Test that prayer times have correct structure."""
        assert "DZUHUR" in PRAYER_TIMES
        assert "ASHAR" in PRAYER_TIMES
        assert "MAGHRIB" in PRAYER_TIMES
    
    def test_is_in_prayer_time(self):
        """Test prayer time overlap detection."""
        result = is_in_prayer_time("Monday", 780, 3)  # 13:00, 3 SKS
        assert isinstance(result, dict)
        assert "has_overlap" in result
    
    def test_get_prayer_time_for_day(self):
        """Test getting prayer times for a day."""
        prayers = get_prayer_time_for_day("Monday")
        assert isinstance(prayers, list)
        assert len(prayers) > 0
    
    def test_days_of_week(self):
        """Test that days of week are defined."""
        assert "Monday" in DAYS_OF_WEEK
        assert "Friday" in DAYS_OF_WEEK


class TestConstraintHelpers:
    """Tests for constraint helper functions."""
    
    def test_group_by_room(self, state_with_no_conflicts):
        """Test grouping entries by room."""
        groups = group_by_room(state_with_no_conflicts)
        assert isinstance(groups, dict)
    
    def test_group_by_lecturer(self, state_with_no_conflicts):
        """Test grouping entries by lecturer."""
        groups = group_by_lecturer(state_with_no_conflicts)
        assert isinstance(groups, dict)
    
    def test_group_by_prodi(self, state_with_no_conflicts):
        """Test grouping entries by prodi."""
        groups = group_by_prodi(state_with_no_conflicts)
        assert isinstance(groups, dict)
        assert "Informatika" in groups
        assert "Management" in groups
    
    def test_group_by_day(self, state_with_no_conflicts):
        """Test grouping entries by day."""
        groups = group_by_day(state_with_no_conflicts)
        assert isinstance(groups, dict)
    
    def test_check_time_overlap(self):
        """Test time overlap checking."""
        from timetable_sa.examples.timetabling.domain_types.domain import TimeSlot
        from timetable_sa.examples.timetabling.domain_types.state import ScheduleEntry
        
        # Create schedule entries with time slots
        entry1 = ScheduleEntry(
            class_id="CS101",
            class_name="Test1",
            kelas="IF-1A",
            prodi="Informatika",
            lecturers=["LEC1"],
            room="R101",
            time_slot=TimeSlot(day="Monday", start_time="08:00", end_time="09:00", period=1),
            sks=2,
            needs_lab=False,
            participants=30,
            class_type="pagi",
        )
        entry2 = ScheduleEntry(
            class_id="CS102",
            class_name="Test2",
            kelas="IF-1B",
            prodi="Informatika",
            lecturers=["LEC1"],
            room="R102",
            time_slot=TimeSlot(day="Monday", start_time="08:30", end_time="09:30", period=2),
            sks=2,
            needs_lab=False,
            participants=25,
            class_type="pagi",
        )
        entry3 = ScheduleEntry(
            class_id="CS103",
            class_name="Test3",
            kelas="IF-1C",
            prodi="Informatika",
            lecturers=["LEC1"],
            room="R103",
            time_slot=TimeSlot(day="Monday", start_time="10:00", end_time="11:00", period=3),
            sks=2,
            needs_lab=False,
            participants=20,
            class_type="pagi",
        )
        
        assert check_time_overlap(entry1, entry2) is True
        assert check_time_overlap(entry1, entry3) is False
    
    def test_count_conflicts(self, state_with_room_conflict):
        """Test counting conflicts."""
        # count_conflicts takes entries list and check function
        entries = state_with_room_conflict.schedule
        
        def check_room_conflict(e1, e2):
            return (e1.room == e2.room and 
                    e1.time_slot.day == e2.time_slot.day and
                    e1.time_slot.period == e2.time_slot.period)
        
        count = count_conflicts(entries, check_room_conflict)
        assert count > 0


class TestClassHelpers:
    """Tests for class helper functions."""
    
    def test_get_lecturers_for_class(self, sample_class_requirements):
        """Test getting lecturers for a class."""
        lecturers = get_lecturers_for_class(sample_class_requirements[0])
        assert "LEC1" in lecturers
    
    def test_needs_lab(self, sample_class_requirements):
        """Test lab requirement detection."""
        assert needs_lab(sample_class_requirements[0]) is False
        assert needs_lab(sample_class_requirements[1]) is True
    
    def test_get_preferred_rooms(self, sample_class_requirements):
        """Test getting preferred rooms."""
        rooms = get_preferred_rooms(sample_class_requirements[0])
        assert "R101" in rooms
    
    def test_get_class_identifier(self, sample_class_requirements):
        """Test getting class identifier."""
        identifier = get_class_identifier(sample_class_requirements[0])
        assert identifier == "CS101-IF-1A"
    
    def test_filter_classes_by_prodi(self, sample_class_requirements):
        """Test filtering classes by prodi."""
        filtered = filter_classes_by_prodi(sample_class_requirements, "Informatika")
        assert len(filtered) == 2
    
    def test_filter_classes_by_type(self, sample_class_requirements):
        """Test filtering classes by type."""
        pagi = filter_classes_by_type(sample_class_requirements, "pagi")
        sore = filter_classes_by_type(sample_class_requirements, "sore")
        assert len(pagi) == 2
        assert len(sore) == 1


class TestSlotValidator:
    """Tests for slot validation functions."""
    
    def test_validate_valid_slot(self):
        """Test validating a valid time slot."""
        from timetable_sa.examples.timetabling.domain_types.domain import TimeSlot
        
        slot = TimeSlot(day="Monday", start_time="08:00", end_time="09:00", period=1)
        errors = validate_time_slot(slot)
        assert len(errors) == 0
    
    def test_validate_invalid_day(self):
        """Test validating a slot with invalid day."""
        from timetable_sa.examples.timetabling.domain_types.domain import TimeSlot
        
        slot = TimeSlot(day="Funday", start_time="08:00", end_time="09:00", period=1)
        errors = validate_time_slot(slot)
        assert len(errors) > 0
    
    def test_check_slot_conflict(self):
        """Test slot conflict checking."""
        from timetable_sa.examples.timetabling.domain_types.domain import TimeSlot
        
        slot1 = TimeSlot(day="Monday", start_time="08:00", end_time="09:00", period=1)
        slot2 = TimeSlot(day="Monday", start_time="08:30", end_time="09:30", period=2)
        slot3 = TimeSlot(day="Tuesday", start_time="08:00", end_time="09:00", period=1)
        
        assert check_slot_conflict(slot1, slot2) is True
        assert check_slot_conflict(slot1, slot3) is False
    
    def test_get_period_time_range(self):
        """Test getting time range for a period."""
        start, end = get_period_time_range(1)
        assert start == "07:00"
        assert end == "07:50"
    
    def test_generate_standard_slot(self):
        """Test generating a standard time slot."""
        slot = generate_standard_slot("Monday", 1)
        assert slot.day == "Monday"
        assert slot.period == 1
        assert slot.start_time == "07:00"
    
    def test_valid_days(self):
        """Test that valid days are defined."""
        assert "Monday" in VALID_DAYS
        assert "Friday" in VALID_DAYS
    
    def test_valid_periods(self):
        """Test that valid periods are 1-12."""
        assert 1 in VALID_PERIODS
        assert 12 in VALID_PERIODS
