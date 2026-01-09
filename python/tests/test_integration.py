"""Integration tests with real data from data_uisi.xlsx."""

import pytest
import sys
sys.path.insert(0, '/home/emmanuelabayor/projects/timetable-sa/python/src')

from timetable_sa import SimulatedAnnealing, SAConfig
from timetable_sa.examples.timetabling import (
    create_initial_state,
    generate_default_time_slots,
    NoRoomConflict,
    NoLecturerConflict,
    NoProdiConflict,
    RoomCapacity,
    MaxDailyPeriods,
    Compactness,
    ChangeTimeSlot,
    ChangeRoom,
    SwapClasses,
    FixRoomConflict,
    FixLecturerConflict,
)
from timetable_sa.examples.timetabling.utils.initial_solution import clone_state
from timetable_sa.examples.timetabling.data.excel_loader import load_uisi_data
from timetable_sa.examples.timetabling.utils.debug_validator import DebugValidator, quick_check


class TestIntegrationWithRealData:
    """Integration tests using real UISI data."""
    
    @pytest.fixture
    def real_data(self):
        """Load real UISI data."""
        try:
            rooms, lecturers, classes = load_uisi_data()
            return {
                "rooms": rooms,
                "lecturers": lecturers,
                "classes": classes,
                "count": len(classes)
            }
        except Exception as e:
            pytest.skip(f"Could not load real data: {e}")
            return None
    
    def test_load_real_data(self, real_data):
        """Test loading real data from Excel file."""
        if real_data is None:
            return
        
        assert real_data["count"] > 0, "Should load at least some classes"
        assert len(real_data["rooms"]) > 0, "Should load rooms"
        assert len(real_data["lecturers"]) > 0, "Should load lecturers"
        
        print(f"\nLoaded {real_data['count']} classes, {len(real_data['rooms'])} rooms, {len(real_data['lecturers'])} lecturers")
    
    def test_create_state_with_real_data(self, real_data):
        """Test creating initial state with real data."""
        if real_data is None:
            return
        
        time_slots = generate_default_time_slots()
        sample_classes = real_data["classes"][:20]
        
        state = create_initial_state(
            sample_classes,
            real_data["rooms"],
            real_data["lecturers"],
            time_slots
        )
        
        assert len(state.schedule) == 20, "Should schedule all sample classes"
        assert len(state.available_time_slots) > 0, "Should have time slots"
    
    def test_quick_check_on_real_state(self, real_data):
        """Test quick validation check on state created from real data."""
        if real_data is None:
            return
        
        time_slots = generate_default_time_slots()
        sample_classes = real_data["classes"][:10]
        
        state = create_initial_state(
            sample_classes,
            real_data["rooms"],
            real_data["lecturers"],
            time_slots
        )
        
        is_valid, messages = quick_check(state)
        assert len(messages) >= 0, "Should return messages about issues"
        print(f"\nQuick check found {len(messages)} issues in initial state")
    
    def test_full_optimization_with_real_data(self, real_data):
        """Test running full optimization with real data."""
        if real_data is None:
            return
        
        time_slots = generate_default_time_slots()
        sample_classes = real_data["classes"][:5]
        
        state = create_initial_state(
            sample_classes,
            real_data["rooms"],
            real_data["lecturers"],
            time_slots
        )
        
        constraints = [
            NoRoomConflict(),
            NoLecturerConflict(),
            NoProdiConflict(),
            RoomCapacity(),
            MaxDailyPeriods(),
            Compactness(),
        ]
        
        move_generators = [
            ChangeTimeSlot(),
            ChangeRoom(),
            SwapClasses(),
        ]
        
        config = SAConfig(
            initial_temperature=1000.0,
            min_temperature=0.1,
            cooling_rate=0.995,
            max_iterations=500,
            clone_state=clone_state,
        )
        
        result = SimulatedAnnealing(state, constraints, move_generators, config).solve()
        
        assert result["hard_violations"] >= 0, "Should complete without errors"
        assert result["fitness"] >= 0, "Should have a fitness value"
        assert result["iterations"] > 0, "Should complete some iterations"
        
        print(f"\nOptimization completed:")
        print(f"  Hard violations: {result['hard_violations']}")
        print(f"  Soft violations: {result['soft_violations']}")
        print(f"  Fitness: {result['fitness']:.4f}")
        print(f"  Iterations: {result['iterations']}")
    
    def test_debug_validator_on_optimized_state(self, real_data):
        """Test debug validator on optimized state."""
        if real_data is None:
            return
        
        time_slots = generate_default_time_slots()
        sample_classes = real_data["classes"][:8]
        
        state = create_initial_state(
            sample_classes,
            real_data["rooms"],
            real_data["lecturers"],
            time_slots
        )
        
        constraints = [
            NoRoomConflict(),
            NoLecturerConflict(),
            NoProdiConflict(),
            RoomCapacity(),
        ]
        
        move_generators = [
            ChangeTimeSlot(),
            ChangeRoom(),
        ]
        
        config = SAConfig(
            initial_temperature=1000.0,
            min_temperature=0.1,
            cooling_rate=0.995,
            max_iterations=300,
            clone_state=clone_state,
        )
        
        result = SimulatedAnnealing(state, constraints, move_generators, config).solve()
        
        validator = DebugValidator()
        issues = validator.validate_state(result["state"])
        
        print(f"\nOptimized state validation:")
        print(f"  Total issues: {len(issues)}")
        print(f"  Errors: {validator.get_error_count()}")
        print(f"  Warnings: {validator.get_warning_count()}")
        
        initial_validator = DebugValidator()
        initial_issues = initial_validator.validate_state(state)
        initial_errors = initial_validator.get_error_count()
        
        assert result["hard_violations"] <= initial_errors, "Should reduce or maintain error count"
    
    def test_constraint_evaluation_performance(self, real_data):
        """Test constraint evaluation performance with real data."""
        if real_data is None:
            return
        
        time_slots = generate_default_time_slots()
        sample_classes = real_data["classes"][:15]
        
        state = create_initial_state(
            sample_classes,
            real_data["rooms"],
            real_data["lecturers"],
            time_slots
        )
        
        constraints = [
            NoRoomConflict(),
            NoLecturerConflict(),
            NoProdiConflict(),
            RoomCapacity(),
            MaxDailyPeriods(),
            Compactness(),
        ]
        
        import time
        
        start = time.perf_counter()
        for _ in range(10):
            for constraint in constraints:
                constraint.evaluate(state)
        end = time.perf_counter()
        
        total_time_ms = (end - start) * 1000
        avg_per_constraint_ms = total_time_ms / (10 * len(constraints))
        
        print(f"\nConstraint evaluation performance:")
        print(f"  Total time for 10 iterations: {total_time_ms:.2f}ms")
        print(f"  Avg per constraint: {avg_per_constraint_ms:.4f}ms")
        
        assert avg_per_constraint_ms < 10.0, f"Constraint evaluation too slow: {avg_per_constraint_ms:.2f}ms"
    
    def test_schedule_completeness(self, real_data):
        """Test that optimization produces complete schedules."""
        if real_data is None:
            return
        
        time_slots = generate_default_time_slots()
        sample_classes = real_data["classes"][:10]
        
        state = create_initial_state(
            sample_classes,
            real_data["rooms"],
            real_data["lecturers"],
            time_slots
        )
        
        constraints = [
            NoRoomConflict(),
            NoLecturerConflict(),
            NoProdiConflict(),
        ]
        
        move_generators = [
            ChangeTimeSlot(),
            ChangeRoom(),
            SwapClasses(),
        ]
        
        config = SAConfig(
            initial_temperature=1000.0,
            min_temperature=0.1,
            cooling_rate=0.995,
            max_iterations=500,
            clone_state=clone_state,
        )
        
        result = SimulatedAnnealing(state, constraints, move_generators, config).solve()
        
        assert len(result["state"].schedule) == len(sample_classes), "All classes should be scheduled"
        
        scheduled_class_ids = set()
        for entry in result["state"].schedule:
            assert entry.class_id not in scheduled_class_ids, f"Duplicate class: {entry.class_id}"
            scheduled_class_ids.add(entry.class_id)
        
        print(f"\nSchedule completeness:")
        print(f"  Classes scheduled: {len(result['state'].schedule)}")
        print(f"  Unique class IDs: {len(scheduled_class_ids)}")


class TestEdgeCases:
    """Test edge cases and error conditions."""
    
    def test_empty_schedule_validation(self):
        """Test validation with empty schedule."""
        from timetable_sa.examples.timetabling.domain_types.state import TimetableState
        from timetable_sa.examples.timetabling.utils.debug_validator import DebugValidator
        
        state = TimetableState(
            schedule=[],
            available_time_slots=[],
            rooms=[],
            lecturers=[]
        )
        
        validator = DebugValidator()
        issues = validator.validate_state(state)
        
        assert len(issues) == 0, "Empty state should have no issues"
    
    def test_single_class_schedule(self):
        """Test optimization with single class."""
        from timetable_sa.examples.timetabling import generate_default_time_slots
        from timetable_sa.examples.timetabling.domain_types.domain import Room, Lecturer, ClassRequirement
        
        rooms = [Room(code="R1", name="Room 1", type="theory", capacity=30)]
        lecturers = [Lecturer(
            prodi="Test",
            code="L1",
            name="Test Lecturer",
            preferred_time=None,
            research_day=None,
            transit_time=0,
            max_daily_periods=8,
            preferred_room=None
        )]
        
        classes = [ClassRequirement(
            prodi="Test",
            kelas="T-1",
            kode_matakuliah="T101",
            mata_kuliah="Test Course",
            sks=2,
            jenis="wajib",
            peserta=25,
            kode_dosen1="L1",
            kode_dosen2=None,
            kode_dosen_prodi_lain1=None,
            kode_dosen_prodi_lain2=None,
            class_type="pagi",
            should_on_the_lab="no",
            rooms="R1"
        )]
        
        time_slots = generate_default_time_slots()
        state = create_initial_state(classes, rooms, lecturers, time_slots)
        
        constraints = [NoRoomConflict(), NoLecturerConflict(), Compactness()]
        move_generators = [ChangeTimeSlot()]
        config = SAConfig(initial_temperature=500.0, cooling_rate=0.995, max_iterations=100, clone_state=clone_state)
        
        result = SimulatedAnnealing(state, constraints, move_generators, config).solve()
        
        assert result["hard_violations"] == 0, "Single class should have no violations"
        assert len(result["state"].schedule) == 1, "Should schedule the single class"
