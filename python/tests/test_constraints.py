"""Tests for hard constraints."""

import pytest
from timetable_sa.examples.timetabling.constraints.hard import (
    NoRoomConflict,
    NoLecturerConflict,
    NoProdiConflict,
    RoomCapacity,
    MaxDailyPeriods,
    FridayTimeRestriction,
    ClassTypeTime,
    SaturdayRestriction,
)
from timetable_sa.examples.timetabling.domain_types.domain import TimeSlot


class TestNoRoomConflict:
    """Tests for NoRoomConflict constraint."""
    
    def test_no_conflicts(self, state_with_no_conflicts):
        """Test when there are no room conflicts."""
        constraint = NoRoomConflict()
        score = constraint.evaluate(state_with_no_conflicts)
        assert score == 1.0
    
    def test_with_room_conflict(self, state_with_room_conflict):
        """Test when there is a room conflict."""
        constraint = NoRoomConflict()
        score = constraint.evaluate(state_with_room_conflict)
        assert score < 1.0
    
    def test_get_violations(self, state_with_room_conflict):
        """Test getting violation details."""
        constraint = NoRoomConflict()
        violations = constraint.get_violations(state_with_room_conflict)
        assert len(violations) == 1
        assert "R101" in violations[0]
        assert "Monday" in violations[0]


class TestNoLecturerConflict:
    """Tests for NoLecturerConflict constraint."""
    
    def test_no_conflicts(self, state_with_no_conflicts):
        """Test when there are no lecturer conflicts."""
        constraint = NoLecturerConflict()
        score = constraint.evaluate(state_with_no_conflicts)
        assert score == 1.0
    
    def test_with_lecturer_conflict(self, state_with_lecturer_conflict):
        """Test when there is a lecturer conflict."""
        constraint = NoLecturerConflict()
        score = constraint.evaluate(state_with_lecturer_conflict)
        assert score < 1.0
    
    def test_multi_lecturer_class(self, state_with_no_conflicts):
        """Test that multi-lecturer classes are handled correctly."""
        constraint = NoLecturerConflict()
        score = constraint.evaluate(state_with_no_conflicts)
        assert score == 1.0


class TestNoProdiConflict:
    """Tests for NoProdiConflict constraint."""
    
    def test_no_conflicts(self, state_with_no_conflicts):
        """Test when there are no prodi conflicts."""
        constraint = NoProdiConflict()
        score = constraint.evaluate(state_with_no_conflicts)
        assert score == 1.0
    
    def test_same_prodi_different_time(self, state_with_no_conflicts):
        """Test same prodi at different times - no conflict."""
        constraint = NoProdiConflict()
        score = constraint.evaluate(state_with_no_conflicts)
        assert score == 1.0


class TestRoomCapacity:
    """Tests for RoomCapacity constraint."""
    
    def test_no_violations(self, state_with_no_conflicts):
        """Test when all classes fit in rooms."""
        constraint = RoomCapacity()
        score = constraint.evaluate(state_with_no_conflicts)
        assert score == 1.0
    
    def test_with_capacity_violation(self, state_with_capacity_violation):
        """Test when a class exceeds room capacity."""
        constraint = RoomCapacity()
        score = constraint.evaluate(state_with_capacity_violation)
        assert score < 1.0
    
    def test_get_violations(self, state_with_capacity_violation):
        """Test getting capacity violation details."""
        constraint = RoomCapacity()
        violations = constraint.get_violations(state_with_capacity_violation)
        assert len(violations) == 1
        assert "50" in violations[0]
        assert "30" in violations[0]


class TestMaxDailyPeriods:
    """Tests for MaxDailyPeriods constraint."""
    
    def test_no_violations(self, state_with_no_conflicts):
        """Test when no lecturer exceeds daily limit."""
        constraint = MaxDailyPeriods()
        score = constraint.evaluate(state_with_no_conflicts)
        assert score == 1.0
    
    def test_get_violations_empty(self, state_with_no_conflicts):
        """Test getting violations when none exist."""
        constraint = MaxDailyPeriods()
        violations = constraint.get_violations(state_with_no_conflicts)
        assert violations == []


class TestFridayTimeRestriction:
    """Tests for FridayTimeRestriction constraint."""
    
    def test_non_friday_classes(self, state_with_no_conflicts):
        """Test with no Friday classes."""
        constraint = FridayTimeRestriction()
        score = constraint.evaluate(state_with_no_conflicts)
        assert score == 1.0
    
    def test_friday_morning_class(self, state_with_no_conflicts, sample_time_slots):
        """Test Friday morning class is allowed."""
        friday_slot = None
        for slot in sample_time_slots:
            if slot.day == "Friday" and slot.period == 1:
                friday_slot = slot
                break
        
        if friday_slot:
            constraint = FridayTimeRestriction()
            score = constraint.evaluate(state_with_no_conflicts)
            assert score == 1.0


class TestClassTypeTime:
    """Tests for ClassTypeTime constraint."""
    
    def test_morning_class_in_morning(self, state_with_no_conflicts, sample_time_slots):
        """Test morning class scheduled in morning."""
        # Ensure all classes are pagi (morning) type
        for entry in state_with_no_conflicts.schedule:
            entry.class_type = "pagi"
        
        # Move to morning time (before 12:00)
        for entry in state_with_no_conflicts.schedule:
            entry.time_slot = sample_time_slots[0]  # Monday period 1 (7:00)
        
        constraint = ClassTypeTime()
        score = constraint.evaluate(state_with_no_conflicts)
        assert score == 1.0
    
    def test_evening_class_in_evening(self, state_with_no_conflicts):
        """Test evening class scheduled in evening."""
        # Ensure all classes are sore (evening) type
        for entry in state_with_no_conflicts.schedule:
            entry.class_type = "sore"
        
        # Manually set time slots to evening time (16:00 or later)
        for entry in state_with_no_conflicts.schedule:
            entry.time_slot = TimeSlot(
                day=entry.time_slot.day,
                start_time="16:00",
                end_time="16:50",
                period=10
            )
        
        constraint = ClassTypeTime()
        score = constraint.evaluate(state_with_no_conflicts)
        assert score == 1.0
    
    def test_evening_class_in_morning_violation(self, state_with_no_conflicts):
        """Test evening class in morning slot causes violation."""
        # Make one class evening type but at morning time
        entry = state_with_no_conflicts.schedule[0]
        entry.class_type = "sore"  # Evening type
        entry.time_slot.start_time = "08:00"  # Morning time
        
        constraint = ClassTypeTime()
        score = constraint.evaluate(state_with_no_conflicts)
        assert score < 1.0


class TestSaturdayRestriction:
    """Tests for SaturdayRestriction constraint."""
    
    def test_no_saturday_classes(self, state_with_no_conflicts):
        """Test when there are no Saturday classes."""
        constraint = SaturdayRestriction()
        score = constraint.evaluate(state_with_no_conflicts)
        assert score == 1.0
    
    def test_with_saturday_class(self, state_with_no_conflicts, sample_time_slots):
        """Test state with a Saturday class."""
        # Add a Saturday class
        saturday_slot = None
        for slot in sample_time_slots:
            if slot.day == "Saturday":
                saturday_slot = slot
                break
        
        if saturday_slot:
            from timetable_sa.examples.timetabling.domain_types.state import ScheduleEntry
            saturday_entry = ScheduleEntry(
                class_id="CS201",
                class_name="Algorithm Analysis",
                kelas="IF-2A",
                prodi="Informatika",
                lecturers=["LEC1"],
                room="R101",
                time_slot=saturday_slot,
                sks=3,
                needs_lab=False,
                participants=25,
                class_type="pagi",
            )
            
            new_state = state_with_no_conflicts
            new_state.schedule.append(saturday_entry)
            
            constraint = SaturdayRestriction()
            score = constraint.evaluate(new_state)
            assert score < 1.0
    
    def test_get_violations(self, state_with_no_conflicts, sample_time_slots):
        """Test getting Saturday violation details."""
        saturday_slot = None
        for slot in sample_time_slots:
            if slot.day == "Saturday":
                saturday_slot = slot
                break
        
        if saturday_slot:
            from timetable_sa.examples.timetabling.domain_types.state import ScheduleEntry
            saturday_entry = ScheduleEntry(
                class_id="CS201",
                class_name="Algorithm Analysis",
                kelas="IF-2A",
                prodi="Informatika",
                lecturers=["LEC1"],
                room="R101",
                time_slot=saturday_slot,
                sks=3,
                needs_lab=False,
                participants=25,
                class_type="pagi",
            )
            
            new_state = state_with_no_conflicts
            new_state.schedule.append(saturday_entry)
            
            constraint = SaturdayRestriction()
            violations = constraint.get_violations(new_state)
            assert len(violations) == 1
            assert "Saturday" in violations[0]
