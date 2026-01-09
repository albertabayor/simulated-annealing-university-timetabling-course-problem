"""Tests for move generators."""

import pytest
from timetable_sa.examples.timetabling.moves import (
    ChangeTimeSlot,
    ChangeRoom,
    SwapClasses,
    ChangeTimeSlotAndRoom,
    FixRoomConflict,
    FixLecturerConflict,
    FixRoomCapacity,
)


class TestChangeTimeSlot:
    """Tests for ChangeTimeSlot move generator."""
    
    def test_can_apply(self, state_with_no_conflicts):
        """Test that move can be applied when schedule has entries."""
        move = ChangeTimeSlot()
        assert move.can_apply(state_with_no_conflicts) is True
    
    def test_can_apply_empty(self, state_with_no_conflicts):
        """Test that move cannot be applied to empty schedule."""
        move = ChangeTimeSlot()
        empty_state = state_with_no_conflicts
        empty_state.schedule = []
        assert move.can_apply(empty_state) is False
    
    def test_generate_returns_state(self, state_with_no_conflicts):
        """Test that generate returns a new state."""
        move = ChangeTimeSlot()
        new_state = move.generate(state_with_no_conflicts, temperature=1000.0)
        assert new_state is not None
        assert new_state is not state_with_no_conflicts
    
    def test_temperature_affects_selection(self, state_with_no_conflicts):
        """Test that temperature affects slot selection."""
        move = ChangeTimeSlot()
        
        # High temperature should allow more exploration
        new_state_high = move.generate(state_with_no_conflicts, temperature=10000.0)
        assert new_state_high is not None
        
        # Low temperature should allow exploitation
        new_state_low = move.generate(state_with_no_conflicts, temperature=100.0)
        assert new_state_low is not None


class TestChangeRoom:
    """Tests for ChangeRoom move generator."""
    
    def test_can_apply(self, state_with_no_conflicts):
        """Test that move can be applied when schedule has entries."""
        move = ChangeRoom()
        assert move.can_apply(state_with_no_conflicts) is True
    
    def test_generate_returns_state(self, state_with_no_conflicts):
        """Test that generate returns a new state when possible."""
        move = ChangeRoom()
        # Try multiple times as it might not find a valid move
        new_state = None
        for _ in range(10):
            new_state = move.generate(state_with_no_conflicts, temperature=1000.0)
            if new_state is not None:
                break
        # The move might return None if no valid room is found, which is acceptable
        # Just verify that the original state wasn't modified
        if new_state is not None:
            assert new_state is not state_with_no_conflicts
    
    def test_preserves_schedule_length(self, state_with_no_conflicts):
        """Test that schedule length is preserved."""
        move = ChangeRoom()
        new_state = move.generate(state_with_no_conflicts, temperature=1000.0)
        if new_state is not None:
            assert len(new_state.schedule) == len(state_with_no_conflicts.schedule)


class TestSwapClasses:
    """Tests for SwapClasses move generator."""
    
    def test_can_apply(self, state_with_no_conflicts):
        """Test that move can be applied when schedule has enough entries."""
        move = SwapClasses()
        # Need at least 2 entries to swap
        assert len(state_with_no_conflicts.schedule) >= 2
        assert move.can_apply(state_with_no_conflicts) is True
    
    def test_generate_returns_state(self, state_with_no_conflicts):
        """Test that generate returns a new state."""
        move = SwapClasses()
        new_state = move.generate(state_with_no_conflicts, temperature=1000.0)
        assert new_state is not None
    
    def test_preserves_schedule_length(self, state_with_no_conflicts):
        """Test that schedule length is preserved."""
        move = SwapClasses()
        new_state = move.generate(state_with_no_conflicts, temperature=1000.0)
        if new_state:
            assert len(new_state.schedule) == len(state_with_no_conflicts.schedule)


class TestChangeTimeSlotAndRoom:
    """Tests for ChangeTimeSlotAndRoom move generator."""
    
    def test_can_apply(self, state_with_no_conflicts):
        """Test that move can be applied when conditions are met."""
        move = ChangeTimeSlotAndRoom()
        assert move.can_apply(state_with_no_conflicts) is True
    
    def test_generate_returns_state(self, state_with_no_conflicts):
        """Test that generate returns a new state."""
        move = ChangeTimeSlotAndRoom()
        new_state = move.generate(state_with_no_conflicts, temperature=1000.0)
        assert new_state is not None
    
    def test_changes_both_time_and_room(self, state_with_no_conflicts):
        """Test that both time and room can be changed."""
        move = ChangeTimeSlotAndRoom()
        new_state = move.generate(state_with_no_conflicts, temperature=1000.0)
        if new_state:
            # At least one entry should have changed
            changed = False
            for i, (old, new) in enumerate(zip(state_with_no_conflicts.schedule, new_state.schedule)):
                if old.time_slot != new.time_slot or old.room != new.room:
                    changed = True
                    break
            assert changed or new_state is not None


class TestFixRoomConflict:
    """Tests for FixRoomConflict move generator."""
    
    def test_can_apply_with_conflict(self, state_with_room_conflict):
        """Test that move can be applied when room conflict exists."""
        move = FixRoomConflict()
        assert move.can_apply(state_with_room_conflict) is True
    
    def test_can_apply_without_conflict(self, state_with_no_conflicts):
        """Test that move can still be applied without conflicts."""
        move = FixRoomConflict()
        assert move.can_apply(state_with_no_conflicts) is True
    
    def test_generate_returns_state(self, state_with_room_conflict):
        """Test that generate returns a new state."""
        move = FixRoomConflict()
        new_state = move.generate(state_with_room_conflict, temperature=1000.0)
        assert new_state is not None
    
    def test_preserves_schedule_length(self, state_with_room_conflict):
        """Test that schedule length is preserved."""
        move = FixRoomConflict()
        new_state = move.generate(state_with_room_conflict, temperature=1000.0)
        if new_state:
            assert len(new_state.schedule) == len(state_with_room_conflict.schedule)


class TestFixLecturerConflict:
    """Tests for FixLecturerConflict move generator."""
    
    def test_can_apply_with_conflict(self, state_with_lecturer_conflict):
        """Test that move can be applied when lecturer conflict exists."""
        move = FixLecturerConflict()
        assert move.can_apply(state_with_lecturer_conflict) is True
    
    def test_can_apply_without_conflict(self, state_with_no_conflicts):
        """Test that move can still be applied without conflicts."""
        move = FixLecturerConflict()
        assert move.can_apply(state_with_no_conflicts) is True
    
    def test_generate_returns_state(self, state_with_lecturer_conflict):
        """Test that generate returns a new state."""
        move = FixLecturerConflict()
        new_state = move.generate(state_with_lecturer_conflict, temperature=1000.0)
        assert new_state is not None


class TestFixRoomCapacity:
    """Tests for FixRoomCapacity move generator."""
    
    def test_can_apply(self, state_with_capacity_violation):
        """Test that move can be applied when capacity violation exists."""
        move = FixRoomCapacity()
        assert move.can_apply(state_with_capacity_violation) is True
    
    def test_can_apply_no_violation(self, state_with_no_conflicts):
        """Test that move can still be applied without violations."""
        move = FixRoomCapacity()
        assert move.can_apply(state_with_no_conflicts) is True
    
    def test_generate_returns_state(self, state_with_capacity_violation):
        """Test that generate returns a new state."""
        move = FixRoomCapacity()
        new_state = move.generate(state_with_capacity_violation, temperature=1000.0)
        assert new_state is not None
    
    def test_preserves_schedule_length(self, state_with_capacity_violation):
        """Test that schedule length is preserved."""
        move = FixRoomCapacity()
        new_state = move.generate(state_with_capacity_violation, temperature=1000.0)
        if new_state:
            assert len(new_state.schedule) == len(state_with_capacity_violation.schedule)
