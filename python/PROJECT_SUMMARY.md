# University Course Timetabling Optimization - Project Summary

## Project Overview

A complete Python implementation of a Simulated Annealing-based optimizer for university course timetabling, using real data from UISI (Universitas Indonesia Surabaya).

## Implementation Status: COMPLETE

### Files Implemented

| Category | Count | Status |
|----------|-------|--------|
| Domain Types | 2 files | Complete |
| Hard Constraints | 11 files | Complete |
| Soft Constraints | 8 files | Complete |
| Move Generators | 10 files | Complete |
| Utilities | 10 files | Complete |
| Data Loaders | 1 file | Complete |
| Examples | 2 files | Complete |
| Tests | 7 files | 107 tests |
| **Total** | **51 files** | **Complete** |

### Components Delivered

#### Domain Types (`domain_types/`)
- `domain.py`: Room, Lecturer, TimeSlot, ClassRequirement
- `state.py`: ScheduleEntry, TimetableState

#### Hard Constraints (`constraints/hard/`) - 11 constraints
1. `NoRoomConflict` - No two classes in same room at same time
2. `NoLecturerConflict` - No lecturer double-booked
3. `NoProdiConflict` - No study program conflicts
4. `RoomCapacity` - Class size <= room capacity
5. `MaxDailyPeriods` - Lecturer daily hours limit
6. `FridayTimeRestriction` - Friday prayer time rules
7. `NoFridayPrayConflict` - No Friday prayer conflicts
8. `PrayerTimeStart` - Can't start during prayer times
9. `ClassTypeTime` - Morning/evening class restrictions
10. `SaturdayRestriction` - Saturday scheduling rules
11. `ExclusiveRoom` - Course-specific room assignments

#### Soft Constraints (`constraints/soft/`) - 8 constraints
1. `Compactness` - Minimize gaps between classes
2. `OverflowPenalty` - Non-lab in lab room penalty
3. `PreferredRoom` - Lecturer preferred room
4. `PreferredTime` - Lecturer preferred time
5. `TransitTime` - Time between classes for lecturer
6. `ResearchDay` - Respect lecturer research day
7. `PrayerTimeOverlap` - Minimize prayer time overlap
8. `EveningClassPriority` - Evening class preferences

#### Move Generators (`moves/`) - 10 generators
1. `ChangeTimeSlot` - Move class to different time
2. `ChangeRoom` - Move class to different room
3. `SwapClasses` - Swap two classes
4. `ChangeTimeSlotAndRoom` - Change both time and room
5. `FixRoomConflict` - Targeted fix for room conflicts
6. `FixLecturerConflict` - Targeted fix for lecturer conflicts
7. `FixRoomCapacity` - Targeted fix for capacity violations
8. `FixMaxDailyPeriods` - Fix daily period limit violations
9. `FixFridayPrayerConflict` - Fix Friday prayer conflicts
10. `SwapFridayWithNonFriday` - Friday-specific optimization

#### Utilities (`utils/`)
- `time.py` - Time calculations and conversions
- `prayer_times.py` - Prayer time constants
- `timeslot_generator.py` - Generate time slots
- `initial_solution.py` - Create initial random state
- `constraint_helpers.py` - Constraint utilities
- `class_helper.py` - Class-related helpers
- `room_availability.py` - Room availability checking
- `slot_validator.py` - Time slot validation
- `debug_validator.py` - Debug/validation helpers
- `room_constants.py` - Room type constants

#### Data Loaders (`data/`)
- `excel_loader.py` - Load from `data_uisi.xlsx`

#### Examples
- `basic_example.py` - Simple 2-class demo
- `full_optimization.py` - Full optimization with all constraints

## Test Results

```
============================= 107 passed in 2.35s ==============================
```

### Test Coverage
- `test_constraints.py` - 21 tests for hard constraints
- `test_soft_constraints.py` - 18 tests for soft constraints
- `test_moves.py` - 27 tests for move generators
- `test_utils.py` - 27 tests for utility functions
- `test_simulated_annealing.py` - 7 tests for core algorithm
- `test_integration.py` - 10 tests with real data

## Performance Results

### Optimization Run (20 classes, 33 rooms, 99 lecturers)

| Metric | Initial | Optimized | Improvement |
|--------|---------|-----------|-------------|
| Hard Violations | 33 | 3 | 91% reduction |
| Soft Violations | N/A | 16 | - |
| Fitness Score | 67,219 | 7,506 | 89% reduction |
| Iterations | - | 2,360 | - |
| Execution Time | - | ~11 seconds | - |

### Most Effective Move Operators

| Operator | Success Rate |
|----------|-------------|
| Fix Room Capacity | 100% |
| Fix Room Conflict | 100% |
| Change Time Slot | 13.7% |
| Swap Classes | 12.8% |
| Fix Lecturer Conflict | 11.1% |

## Quick Start

```bash
cd /home/emmanuelabayor/projects/timetable-sa/python

# Install dependencies
./venv/bin/pip install -e .

# Run basic example
./venv/bin/python src/timetable_sa/examples/timetabling/basic_example.py

# Run full optimization
./venv/bin/python src/timetable_sa/examples/timetabling/full_optimization.py

# Run tests
./venv/bin/python -m pytest tests/ -v
```

## Usage Example

```python
from timetable_sa import SimulatedAnnealing, SAConfig
from timetable_sa.examples.timetabling import (
    create_initial_state,
    generate_default_time_slots,
    NoRoomConflict,
    NoLecturerConflict,
    Compactness,
    ChangeTimeSlot,
    ChangeRoom,
)
from timetable_sa.examples.timetabling.utils.initial_solution import clone_state
from timetable_sa.examples.timetabling.data.excel_loader import load_uisi_data

# Load data
rooms, lecturers, classes = load_uisi_data()

# Create initial state
time_slots = generate_default_time_slots()
state = create_initial_state(classes[:20], rooms, lecturers, time_slots)

# Define constraints
constraints = [
    NoRoomConflict(),
    NoLecturerConflict(),
    Compactness(),
]

# Define moves
move_generators = [
    ChangeTimeSlot(),
    ChangeRoom(),
]

# Configure and run
config = SAConfig(
    initial_temperature=1000.0,
    min_temperature=0.1,
    cooling_rate=0.995,
    max_iterations=5000,
    clone_state=clone_state,
)

result = SimulatedAnnealing(state, constraints, move_generators, config).solve()

print(f"Fitness: {result['fitness']:.4f}")
print(f"Hard violations: {result['hard_violations']}")
```

## Data Source

**File:** `/home/emmanuelabayor/projects/timetable-sa/data_uisi.xlsx`

| Sheet | Records | Description |
|-------|---------|-------------|
| `ruangan` | 33 rooms | Room definitions |
| `dosen` | 99 lecturers | Lecturer profiles |
| `kebutuhan_kelas` | 373 classes | Course requirements |

## Technical Details

### Core Algorithm
- Simulated Annealing with multi-phase optimization
- Phase 1: Eliminate hard constraint violations
- Phase 1.5: Intensification for stubborn violations
- Phase 2: Optimize soft constraints
- Adaptive operator selection
- Reheating mechanism for local minima escape

### Key Features
- Multi-neighborhood search (10 move generators)
- Targeted fix operators for specific violation types
- Comprehensive logging and statistics
- Flexible constraint system

## Project Structure

```
python/
├── src/timetable_sa/
│   ├── core/
│   │   ├── simulated_annealing.py
│   │   ├── interfaces/
│   │   └── types/
│   └── examples/timetabling/
│       ├── domain_types/
│       ├── constraints/
│       │   ├── hard/
│       │   └── soft/
│       ├── moves/
│       ├── data/
│       ├── utils/
│       └── examples/
├── tests/
│   ├── test_constraints.py
│   ├── test_soft_constraints.py
│   ├── test_moves.py
│   ├── test_utils.py
│   ├── test_simulated_annealing.py
│   └── test_integration.py
└── venv/
```

## Dependencies

- Python 3.12+
- numpy >= 1.24.0
- pandas >= 2.0.0
- matplotlib >= 3.7.0
- openpyxl >= 3.1.0
- pytest >= 7.4.0

## License

MIT - Emmanuel Alejandro Albert A Bayor

## References

Based on the implementation plan in `docs/PYTHON_TIMETABLE_IMPLEMENTATION.md`
