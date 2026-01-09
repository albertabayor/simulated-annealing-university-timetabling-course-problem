# University Course Timetabling Optimization (Python)

A Python implementation of a Simulated Annealing-based optimizer for university course timetabling. Uses real data from UISI (Universitas Indonesia Surabaya) with 11 hard constraints and 8 soft constraints.

## Features

- **Simulated Annealing Optimization**: Multi-phase approach with adaptive operator selection
- **11 Hard Constraints**: Room conflicts, lecturer conflicts, capacity limits, prayer times, etc.
- **8 Soft Constraints**: Compactness, preferences, transit time, etc.
- **10 Move Generators**: Various neighborhood exploration strategies
- **Real Data Support**: Loads from Excel files (`data_uisi.xlsx`)
- **107 Passing Tests**: Comprehensive test suite covering all components

## Quick Start

```bash
cd /home/emmanuelabayor/projects/timetable-sa/python

# Install dependencies
./venv/bin/pip install -e .

# Run basic example
./venv/bin/python src/timetable_sa/examples/timetabling/basic_example.py

# Run tests
./venv/bin/python -m pytest tests/ -v
```

## Project Structure

```
python/
├── src/timetable_sa/
│   ├── core/                          # Core SA algorithm
│   │   ├── simulated_annealing.py    # Main optimizer
│   │   ├── interfaces/               # Constraint, MoveGenerator, Config
│   │   └── types/                    # Solution, Violation types
│   └── examples/timetabling/
│       ├── domain_types/             # Room, Lecturer, TimeSlot, ClassRequirement
│       ├── constraints/
│       │   ├── hard/                 # 11 hard constraints
│       │   └── soft/                 # 8 soft constraints
│       ├── moves/                    # 10 move generators
│       ├── data/                     # Excel loader
│       └── basic_example.py          # Example usage
├── tests/                            # 107 passing tests
└── venv/                             # Python virtual environment
```

## Constraints

### Hard Constraints (Must Satisfy)

| Constraint | Description |
|------------|-------------|
| `NoRoomConflict` | No two classes in same room at same time |
| `NoLecturerConflict` | No lecturer teaching two classes simultaneously |
| `NoProdiConflict` | No students in two classes at same time |
| `RoomCapacity` | Class size <= room capacity |
| `MaxDailyPeriods` | Max 8 periods per day per lecturer |
| `FridayTimeRestriction` | Friday classes only 07:30-11:30 or 13:00-16:00 |
| `SaturdayRestriction` | No classes on Saturday |
| `ExclusiveRoom` | Lab classes only in lab rooms |
| `ClassTypeTime` | Morning/evening classes at correct times |
| `PrayerTimeStart` | Classes don't start during prayer times |
| `NoFridayPrayConflict` | No class during Friday prayer (11:30-12:30) |

### Soft Constraints (Optimize)

| Constraint | Weight | Description |
|------------|--------|-------------|
| `Compactness` | 10 | Minimize gaps in schedule |
| `PreferredRoom` | 5 | Lecturer preferred rooms |
| `PreferredTime` | 5 | Lecturer preferred time slots |
| `TransitTime` | 3 | Minimize travel time between rooms |
| `ResearchDay` | 5 | Respect lecturer research days |
| `PrayerTimeOverlap` | 8 | Minimize overlap with prayer times |
| `OverflowPenalty` | 15 | Penalize class size > room capacity |
| `EveningClassPriority` | 5 | Evening classes in evening slots |

## Move Generators

| Generator | Purpose |
|-----------|---------|
| `ChangeTimeSlot` | Move class to different time slot |
| `ChangeRoom` | Move class to different room |
| `SwapClasses` | Swap two classes' assignments |
| `ChangeTimeSlotAndRoom` | Change both time and room |
| `FixRoomConflict` | Targeted fix for room conflicts |
| `FixLecturerConflict` | Targeted fix for lecturer conflicts |
| `FixRoomCapacity` | Targeted fix for capacity violations |
| `FixFridayPrayerConflict` | Fix Friday prayer time conflicts |
| `SwapFridayWithNonFriday` | Swap Friday and non-Friday classes |
| `FixMaxDailyPeriods` | Fix daily period limit violations |

## Usage with Real Data

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

# Load real UISI data
rooms, lecturers, classes = load_uisi_data()

# Create initial state
time_slots = generate_default_time_slots()
state = create_initial_state(classes[:20], rooms, lecturers, time_slots)

# Define constraints
constraints = [
    NoRoomConflict(),
    NoLecturerConflict(),
    NoProdiConflict(),
    RoomCapacity(),
    Compactness(),
]

# Define move generators
move_generators = [
    ChangeTimeSlot(),
    ChangeRoom(),
    SwapClasses(),
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
print(f"Soft violations: {result['soft_violations']}")
```

## Domain Types

```python
# Room
Room(code, name, type, capacity)

# Lecturer
Lecturer(prodi, code, name, preferred_time, research_day, 
         transit_time, max_daily_periods, preferred_room)

# TimeSlot
TimeSlot(day, period, start_time, end_time, is_break_time)

# ClassRequirement (course to schedule)
ClassRequirement(prodi, kelas, kode_matakuliah, mata_kuliah, sks,
                 jenis, peserta, kode_dosen1, kode_dosen2, ...)
```

## SAConfig Parameters

```python
SAConfig(
    # Core parameters
    initial_temperature: float = 1000.0,
    min_temperature: float = 0.1,
    cooling_rate: float = 0.995,
    max_iterations: int = 5000,
    
    # Required
    clone_state: Callable[[TState], TState],
    
    # Optional
    hard_constraint_weight: float = 10000,
    soft_constraint_weight: float = 10,
    reheating_threshold: int = 500,
    reheating_factor: float = 2.0,
    max_reheats: int = 3,
)
```

## Testing

```bash
# Run all tests
./venv/bin/python -m pytest tests/ -v

# Run specific test file
./venv/bin/python -m pytest tests/test_constraints.py -v

# Run with coverage
./venv/bin/python -m pytest tests/ --cov=src/timetable_sa
```

## Examples

- **basic_example.py**: Simple 2-class optimization demo
- **03-optimization-visualization.ipynb**: Charts for fitness, violations, room utilization
- **04-final-project-demo.ipynb**: Complete academic presentation notebook

## Dependencies

- Python 3.12+
- openpyxl (Excel reading)
- pytest (testing)

Install all dependencies:
```bash
./venv/bin/pip install -e ".[dev]"
```

## Performance

Based on testing with real UISI data (20+ classes):

| Metric | Value |
|--------|-------|
| Test Suite | 107 tests passing |
| Constraint Evaluation | < 10ms per constraint |
| Optimization Iterations | Configurable (default 5000) |
| Hard Violations | Eliminated in Phase 1 |
| Soft Violations | Optimized in Phase 2 |

## License

MIT - Emmanuel Alejandro Albert A Bayor
