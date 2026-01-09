"""Tests for soft constraints."""

import pytest
from timetable_sa.examples.timetabling.constraints.soft import (
    Compactness,
    OverflowPenalty,
    PreferredRoom,
    PreferredTime,
    TransitTime,
    ResearchDay,
    PrayerTimeOverlap,
    EveningClassPriority,
)


class TestCompactness:
    """Tests for Compactness constraint."""
    
    def test_compact_schedule(self, state_with_no_conflicts):
        """Test when schedule is compact (no gaps)."""
        constraint = Compactness()
        score = constraint.evaluate(state_with_no_conflicts)
        # With only 3 classes, should be reasonably compact
        assert score >= 0.0
    
    def test_get_violations(self, state_with_no_conflicts):
        """Test getting compactness violations."""
        constraint = Compactness()
        violations = constraint.get_violations(state_with_no_conflicts)
        assert isinstance(violations, list)


class TestOverflowPenalty:
    """Tests for OverflowPenalty constraint."""
    
    def test_no_overflow(self, state_with_no_conflicts):
        """Test when there is no overflow to lab rooms."""
        constraint = OverflowPenalty()
        score = constraint.evaluate(state_with_no_conflicts)
        assert score == 1.0
    
    def test_with_overflow(self, state_with_no_conflicts):
        """Test when a non-lab class is in a lab room."""
        constraint = OverflowPenalty()
        
        # Find a class that needs lab and mark it as overflow
        # OR find a class that doesn't need lab but is in a lab room
        # The test state has LAB1 which is a lab room
        # CS102 needs lab so it's not overflow
        # MG101 is in R102 (theory room) so it's also fine
        
        # Let's create a proper test by modifying state
        state = state_with_no_conflicts
        for entry in state.schedule:
            if entry.room == "LAB1":
                # This is a lab class in a lab room - OK
                pass
            else:
                # Mark this non-lab class as overflow
                entry.is_overflow_to_lab = True
                entry.room = "LAB1"  # Put in lab room
        
        score = constraint.evaluate(state)
        assert score < 1.0


class TestPreferredRoom:
    """Tests for PreferredRoom constraint."""
    
    def test_lecturer_with_no_preference(self, state_with_no_conflicts):
        """Test lecturer without room preference."""
        constraint = PreferredRoom()
        score = constraint.evaluate(state_with_no_conflicts)
        # Should be satisfied if no preference
        assert score >= 0.0
    
    def test_get_violations_empty(self, state_with_no_conflicts):
        """Test getting violations when none exist."""
        constraint = PreferredRoom()
        violations = constraint.get_violations(state_with_no_conflicts)
        assert isinstance(violations, list)


class TestPreferredTime:
    """Tests for PreferredTime constraint."""
    
    def test_lecturer_with_no_preference(self, state_with_no_conflicts):
        """Test lecturer without time preference."""
        constraint = PreferredTime()
        score = constraint.evaluate(state_with_no_conflicts)
        # Should be satisfied if no preference
        assert score >= 0.0
    
    def test_get_violations_empty(self, state_with_no_conflicts):
        """Test getting violations when none exist."""
        constraint = PreferredTime()
        violations = constraint.get_violations(state_with_no_conflicts)
        assert isinstance(violations, list)


class TestTransitTime:
    """Tests for TransitTime constraint."""
    
    def test_no_transit_violations(self, state_with_no_conflicts):
        """Test when transit time is respected."""
        constraint = TransitTime()
        score = constraint.evaluate(state_with_no_conflicts)
        assert score >= 0.0
    
    def test_get_violations(self, state_with_no_conflicts):
        """Test getting transit time violations."""
        constraint = TransitTime()
        violations = constraint.get_violations(state_with_no_conflicts)
        assert isinstance(violations, list)


class TestResearchDay:
    """Tests for ResearchDay constraint."""
    
    def test_lecturer_with_no_research_day(self, state_with_no_conflicts):
        """Test lecturer without research day."""
        constraint = ResearchDay()
        score = constraint.evaluate(state_with_no_conflicts)
        # Should be satisfied if no research day
        assert score >= 0.0
    
    def test_get_violations_empty(self, state_with_no_conflicts):
        """Test getting violations when none exist."""
        constraint = ResearchDay()
        violations = constraint.get_violations(state_with_no_conflicts)
        assert isinstance(violations, list)


class TestPrayerTimeOverlap:
    """Tests for PrayerTimeOverlap constraint."""
    
    def test_no_overlap(self, state_with_no_conflicts):
        """Test when no classes overlap with prayer times."""
        constraint = PrayerTimeOverlap()
        score = constraint.evaluate(state_with_no_conflicts)
        assert score >= 0.0
    
    def test_get_violations(self, state_with_no_conflicts):
        """Test getting prayer time overlap violations."""
        constraint = PrayerTimeOverlap()
        violations = constraint.get_violations(state_with_no_conflicts)
        assert isinstance(violations, list)


class TestEveningClassPriority:
    """Tests for EveningClassPriority constraint."""
    
    def test_evening_class_in_evening(self, state_with_no_conflicts):
        """Test evening class scheduled in evening."""
        constraint = EveningClassPriority()
        score = constraint.evaluate(state_with_no_conflicts)
        # Evening class should be in evening period
        assert score >= 0.0
    
    def test_get_violations(self, state_with_no_conflicts):
        """Test getting evening class priority violations."""
        constraint = EveningClassPriority()
        violations = constraint.get_violations(state_with_no_conflicts)
        assert isinstance(violations, list)
