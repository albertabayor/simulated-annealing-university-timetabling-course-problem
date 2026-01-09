# Python Timetabling Domain Implementation Plan (COMPLETE)

**Status:** Planning Phase
**Created:** 2026-01-08
**Objective:** Port ALL 54 TypeScript files from timetabling example to Python
**Target:** Complete implementation for academic final project (22 Jan 2026)
**Total Files to Port:** 54 TypeScript files → ~45 Python files
**Dataset Excel Path** : /home/emmanuelabayor/projects/timetable-sa/data_uisi.xlsx

---

## 1. Overview

This is a **COMPLETE** implementation plan for porting the entire University Course Timetabling domain from TypeScript to Python. The core Simulated Annealing algorithm (761 lines) is already complete.

### Current Status
- ✅ Core SA algorithm (`simulated_annealing.py`) - **COMPLETE**
- ✅ Base interfaces (Constraint, MoveGenerator, SAConfig) - **COMPLETE**
- ✅ Introduction notebook - **COMPLETE**
- ❌ Timetabling domain - **54 files to port**

---

## 2. Complete File Mapping (54 Files)

### TYPES (3 files → 2 Python files)

| TypeScript | Python | Lines | Priority |
|------------|--------|-------|----------|
| `types/Domain.ts` | `types/domain.py` | ~87 | **P0** |
| `types/State.ts` | `types/state.py` | ~56 | **P0** |
| `types/index.ts` | (merged into above) | ~10 | P0 |

**Total:** ~150 lines → ~120 lines Python

---

### HARD CONSTRAINTS (12 files → 11 Python files)

| TypeScript | Python | Description | Priority |
|------------|--------|-------------|----------|
| `constraints/hard/NoRoomConflict.ts` | `constraints/hard/no_room_conflict.py` | Room conflicts at same time | **P0** |
| `constraints/hard/NoLecturerConflict.ts` | `constraints/hard/no_lecturer_conflict.py` | Lecturer double-booking | **P0** |
| `constraints/hard/NoProdiConflict.ts` | `constraints/hard/no_prodi_conflict.py` | Prodi schedule conflicts | **P0** |
| `constraints/hard/RoomCapacity.ts` | `constraints/hard/room_capacity.py` | Class exceeds room capacity | **P0** |
| `constraints/hard/MaxDailyPeriods.ts` | `constraints/hard/max_daily_periods.py` | Lecturer exceeds daily hours | **P1** |
| `constraints/hard/ClassTypeTime.ts` | `constraints/hard/class_type_time.py` | Morning/evening class restrictions | **P1** |
| `constraints/hard/FridayTimeRestriction.ts` | `constraints/hard/friday_time_restriction.py` | Friday prayer time rules | **P1** |
| `constraints/hard/NoFridayPrayConflit.ts` | `constraints/hard/no_friday_pray_conflict.py` | No Friday prayer conflicts | **P1** |
| `constraints/hard/PrayerTimeStart.ts` | `constraints/hard/prayer_time_start.py` | Can't start during prayer | **P1** |
| `constraints/hard/SaturdayRestriction.ts` | `constraints/hard/saturday_restriction.py` | Saturday scheduling rules | **P2** |
| `constraints/hard/ExclusiveRoom.ts` | `constraints/hard/exclusive_room.py` | Room-only-for-specific-courses | **P2** |
| `constraints/hard/index.ts` | `constraints/hard/__init__.py` | Exports | P0 |

**Total:** ~1000 lines → ~800 lines Python

---

### SOFT CONSTRAINTS (10 files → 9 Python files)

| TypeScript | Python | Description | Priority |
|------------|--------|-------------|----------|
| `constraints/soft/Compactness.ts` | `constraints/soft/compactness.py` | Minimize gaps between classes | **P0** |
| `constraints/soft/OverflowPenalty.ts` | `constraints/soft/overflow_penalty.py` | Non-lab in lab room penalty | **P1** |
| `constraints/soft/PreferredRoom.ts` | `constraints/soft/preferred_room.py` | Lecturer's preferred room | **P1** |
| `constraints/soft/PreferredTime.ts` | `constraints/soft/preferred_time.py` | Lecturer's preferred time | **P1** |
| `constraints/soft/TransitTime.ts` | `constraints/soft/transit_time.py` | Time between classes for lecturer | **P1** |
| `constraints/soft/ResearchDay.ts` | `constraints/soft/research_day.py` | Respect lecturer's research day | **P1** |
| `constraints/soft/PrayerTimeOverlap.ts` | `constraints/soft/prayer_time_overlap.py` | Minimize prayer time overlap | **P2** |
| `constraints/soft/EveningClassPriority.ts` | `constraints/soft/evening_class_priority.py` | Evening class preferences | **P2** |
| `constraints/soft/index.ts` | `constraints/soft/__init__.py` | Exports | P0 |
| `constraints/index.ts` | `constraints/__init__.py` | Exports | P0 |

**Total:** ~500 lines → ~400 lines Python

---

### MOVE GENERATORS (11 files → 10 Python files)

| TypeScript | Python | Description | Priority |
|------------|--------|-------------|----------|
| `moves/ChangeTimeSlot.ts` | `moves/change_time_slot.py` | Change class time slot | **P0** |
| `moves/ChangeRoom.ts` | `moves/change_room.py` | Change class room | **P0** |
| `moves/ChangeTimeSlotAndRoom.ts` | `moves/change_time_slot_and_room.py` | Change both time and room | **P0** |
| `moves/SwapClasses.ts` | `moves/swap_classes.py` | Swap two classes | **P0** |
| `moves/SwapFridayWithNonFriday.ts` | `moves/swap_friday_with_non_friday.py` | Friday-specific swap | **P1** |
| `moves/FixRoomConflict.ts` | `moves/fix_room_conflict.py` | Fix room conflict directly | **P1** |
| `moves/FixLecturerConflict.ts` | `moves/fix_lecturer_conflict.py` | Fix lecturer conflict | **P1** |
| `moves/FixRoomCapacity.ts` | `moves/fix_room_capacity.py` | Fix capacity violation | **P1** |
| `moves/FixMaxDailyPeriods.ts` | `moves/fix_max_daily_periods.py` | Fix daily periods violation | **P1** |
| `moves/FixFridayPrayerConflict.ts` | `moves/fix_friday_prayer_conflict.py` | Fix Friday prayer conflict | **P2** |
| `moves/index.ts` | `moves/__init__.py` | Exports | P0 |

**Total:** ~700 lines → ~550 lines Python

---

### UTILITIES (13 files → 10 Python files)

| TypeScript | Python | Description | Priority |
|------------|--------|-------------|----------|
| `utils/time.ts` | `utils/time.py` | Time calculations, prayer times | **P0** |
| `utils/prayer-times.ts` | `utils/prayer_times.py` | Prayer time constants | **P0** |
| `utils/cache.ts` | (merged into time.py) | Caching utilities | P0 |
| `utils/timeslot-generator.ts` | `utils/timeslot_generator.py` | Generate time slots | **P0** |
| `utils/constraint-helpers.ts` | `utils/constraint_helpers.py` | Helper functions | **P0** |
| `utils/class-helper.ts` | `utils/class_helper.py` | Class-related helpers | **P1** |
| `utils/initial-solution.ts` | `utils/initial_solution.py` | Create initial state | **P0** |
| `utils/room-availability.ts` | `utils/room_availability.py` | Room availability checking | **P1** |
| `utils/room-constants.ts` | `utils/room_constants.py` | Room type constants | **P1** |
| `utils/slot-validator.ts` | `utils/slot_validator.py` | Time slot validation | **P1** |
| `utils/debug-validator.ts` | `utils/debug_validator.py` | Debug/validation helpers | **P2** |
| `utils/index-builders.ts` | `utils/index_builders.py` | Index builder utilities | **P2** |
| `utils/index.ts` | `utils/__init__.py` | Exports | P0 |

**Total:** ~800 lines → ~650 lines Python

---

### DATA LOADERS (3 files → 3 Python files)

| TypeScript | Python | Description | Priority |
|------------|--------|-------------|----------|
| `data/excel-loader.ts` | `data/excel_loader.py` | Load from Excel files | **P0** |
| `data/json-loader.ts` | `data/json_loader.py` | Load from JSON files | **P1** |
| `data/index.ts` | `data/__init__.py` | Exports | P0 |

**Total:** ~150 lines → ~120 lines Python

---

### EXAMPLES & OTHERS (3 files)

| TypeScript | Python | Description | Priority |
|------------|--------|-------------|----------|
| `example-basic.ts` | `examples/basic_example.py` | Basic usage example | **P0** |
| `profile-performance.ts` | (optional) | Performance profiling | P3 |

**Total:** ~200 lines → ~150 lines Python

---

## 3. Summary Table

| Category | TS Files | Python Files | TS Lines | Python Lines (est.) |
|----------|----------|--------------|----------|---------------------|
| **Types** | 3 | 2 | ~150 | ~120 |
| **Hard Constraints** | 12 | 11 | ~1000 | ~800 |
| **Soft Constraints** | 10 | 9 | ~500 | ~400 |
| **Move Generators** | 11 | 10 | ~700 | ~550 |
| **Utilities** | 13 | 10 | ~800 | ~650 |
| **Data Loaders** | 3 | 3 | ~150 | ~120 |
| **Examples** | 2 | 1 | ~200 | ~150 |
| **TOTAL** | **54** | **46** | **~3500** | **~2790** |

**Code reduction:** ~20% less lines in Python (more concise syntax)

---

## 4. Implementation Priority

### P0 - MUST HAVE (MVP)
**Required for basic timetabling to work:**
- Types (Domain, State)
- 3 Core Hard Constraints: NoRoomConflict, NoLecturerConflict, NoProdiConflict
- 1 Core Soft Constraint: Compactness
- 3 Core Moves: ChangeTimeSlot, ChangeRoom, SwapClasses
- Core Utils: time, prayer_times, timeslot_generator, initial_solution
- Data Loader: excel_loader
- Basic Example

**Files:** 18 files, ~1200 lines Python

### P1 - SHOULD HAVE
**Important for quality/constraints:**
- Remaining Hard Constraints: RoomCapacity, MaxDailyPeriods, FridayTimeRestriction, etc.
- Remaining Soft Constraints: PreferredRoom, PreferredTime, TransitTime, ResearchDay
- Fix Moves: FixRoomConflict, FixLecturerConflict, FixRoomCapacity
- Additional Utils: constraint_helpers, class_helper, room_availability

**Files:** 20 files, ~1100 lines Python

### P2 - NICE TO HAVE
**Domain-specific rules:**
- SaturdayRestriction, ExclusiveRoom
- PrayerTimeOverlap, EveningClassPriority
- SwapFridayWithNonFriday, FixFridayPrayerConflict
- Additional validation utilities

**Files:** 6 files, ~350 lines Python

### P3 - OPTIONAL
- Performance profiling
- Debug utilities

---

## 5. Implementation Phases (Detailed)

### PHASE 1: Foundation (P0) - Week 1
**Goal:** Working timetabling with basic constraints

#### Day 1-2: Types (4 hours)
```python
# types/domain.py
from dataclasses import dataclass
from typing import Optional

@dataclass
class Room:
    """Room/Classroom definition - matches 'ruangan' sheet"""
    code: str
    name: str
    type: str  # "theory", "lab", etc.
    capacity: int

@dataclass
class Lecturer:
    """Lecturer definition - matches 'dosen' sheet"""
    prodi: str
    code: str
    name: str
    preferred_time: Optional[str]  # e.g., "18.30 - 21.00 Thursday, 18.30 - 21.00 Friday"
    research_day: Optional[str]  # Reserved day for research
    transit_time: int  # Minutes needed between classes
    max_daily_periods: int  # Maximum teaching hours per day
    preferred_room: Optional[str]

@dataclass
class TimeSlot:
    """Time slot definition"""
    day: str  # "Monday", "Tuesday", etc.
    start_time: str  # "08:00", "09:30", etc.
    end_time: str  # "10:00", "11:30", etc.
    period: int  # Period number for ordering

@dataclass
class ClassRequirement:
    """Class requirement - matches 'kebutuhan_kelas' sheet"""
    prodi: str
    kelas: str  # Class section (e.g., "MM-1A")
    kode_matakuliah: str  # Course code
    mata_kuliah: str  # Course name
    sks: int  # Credit hours
    jenis: str  # Course type ("wajib", "pilihan")
    peserta: int  # Number of participants
    kode_dosen1: str  # Primary lecturer code
    kode_dosen2: Optional[str]  # Secondary lecturer (optional)
    kode_dosen_prodi_lain1: Optional[str]  # External lecturer 1 (optional)
    kode_dosen_prodi_lain2: Optional[str]  # External lecturer 2 (optional)
    class_type: str  # "pagi" (morning) or "sore" (evening)
    should_on_the_lab: str  # "yes" or "no"
    rooms: str  # Comma-separated list of preferred rooms

# types/state.py
@dataclass
class ScheduleEntry:
    """A single entry in the timetable schedule"""
    class_id: str  # Course code (kode_matakuliah)
    class_name: str  # Course name (mata_kuliah)
    kelas: str  # Class section
    prodi: str  # Study program
    lecturers: list[str]  # All lecturer codes (dosen1 + dosen2 + external)
    room: str  # Assigned room code
    time_slot: TimeSlot  # Assigned time slot
    sks: int  # Credit hours
    needs_lab: bool  # Whether this class requires a lab
    participants: int  # Number of students
    class_type: str  # "pagi" or "sore"
    prayer_time_added: int = 0  # Minutes added for prayer time
    is_overflow_to_lab: bool = False  # Non-lab class using lab room

@dataclass
class TimetableState:
    """Complete timetable state"""
    schedule: list[ScheduleEntry]
    available_time_slots: list[TimeSlot]
    rooms: list[Room]
    lecturers: list[Lecturer]
```

#### Day 3-4: Core Utilities (6 hours)
```python
# utils/prayer_times.py
PRAYER_TIMES = {
    "DZUHUR": {"start": 700, "end": 750, "duration": 50},
    "ASHAR": {"start": 900, "end": 930, "duration": 30},
    "MAGHRIB": {"start": 1080, "end": 1110, "duration": 30}
}

# utils/time.py
from functools import lru_cache

@lru_cache(maxsize=1000)
def time_to_minutes(time_str: str) -> int:
    hours, minutes = map(int, time_str.split(':'))
    return hours * 60 + minutes

@lru_cache(maxsize=1000)
def minutes_to_time(minutes: int) -> str:
    return f"{minutes // 60:02d}:{minutes % 60:02d}"

@lru_cache(maxsize=500)
def calculate_end_time(start_time: str, sks: int, day: str) -> tuple[str, int]:
    # Calculate including prayer time
    pass

def get_prayer_time_overlap(start_time: str, sks: int, day: str) -> int:
    # Check overlap with DZUHUR, ASHAR, MAGHRIB
    pass

# utils/timeslot_generator.py
def generate_time_slots(
    start_hour: int = 7,
    end_hour: int = 18,
    period_duration: int = 50,
    days: list[str] = None
) -> list[TimeSlot]:
    # Generate standard time slots
    pass

# utils/initial_solution.py
def create_initial_state(
    classes: list[ClassRequirement],
    rooms: list[Room],
    lecturers: list[Lecturer],
    time_slots: list[TimeSlot]
) -> TimetableState:
    # Create random valid initial assignment
    pass
```

#### Day 5-7: P0 Hard Constraints (8 hours)
```python
# constraints/hard/no_room_conflict.py
class NoRoomConflict(Constraint):
    name = "No Room Conflict"
    type = "hard"

    def evaluate(self, state: TimetableState) -> float:
        # Group by room + day, check time overlaps
        # O(N log N) using group-sort-shortcircuit
        pass

# constraints/hard/no_lecturer_conflict.py
class NoLecturerConflict(Constraint):
    name = "No Lecturer Conflict"
    type = "hard"

    def evaluate(self, state: TimetableState) -> float:
        # Group by lecturer + day, check time overlaps
        # Handle multiple lecturers per class
        pass

# constraints/hard/no_prodi_conflict.py
class NoProdiConflict(Constraint):
    name = "No Prodi Conflict"
    type = "hard"

    def evaluate(self, state: TimetableState) -> float:
        # Group by prodi + day, check time overlaps
        pass
```

#### Day 8-9: P0 Soft Constraints (3 hours)
```python
# constraints/soft/compactness.py
class Compactness(Constraint):
    name = "Compactness"
    type = "soft"
    weight = 8.0

    def evaluate(self, state: TimetableState) -> float:
        # Group by prodi + day
        # Calculate gaps between consecutive classes
        # Prefer gaps <= 60 minutes
        pass
```

#### Day 10-12: P0 Move Generators (6 hours)
```python
# moves/change_time_slot.py
class ChangeTimeSlot(MoveGenerator):
    name = "Change Time Slot"

    def can_apply(self, state: TimetableState) -> bool:
        return len(state.schedule) > 0

    def generate(self, state: TimetableState, temperature: float) -> TimetableState:
        # Temperature-dependent slot selection
        # High temp: exploration
        # Low temp: exploitation (nearby slots)
        pass

# moves/change_room.py
class ChangeRoom(MoveGenerator):
    name = "Change Room"
    # Similar structure
    pass

# moves/swap_classes.py
class SwapClasses(MoveGenerator):
    name = "Swap Classes"
    # Temperature-dependent swap type
    pass
```

#### Day 13-14: Data Loader & Integration (4 hours)
```python
# data/excel_loader.py
import pandas as pd

def load_from_excel(
    rooms_file: str,
    lecturers_file: str,
    classes_file: str
) -> tuple[list[Room], list[Lecturer], list[ClassRequirement]]:
    rooms_df = pd.read_excel(rooms_file)
    # Load and convert to dataclasses
    pass

# examples/basic_example.py
# Complete working example
```

**PHASE 1 Complete:** Working timetabling system! ✅

---

### PHASE 2: Quality & Constraints (P1) - Week 2

**Remaining Hard Constraints:**
- `room_capacity.py` - Class participants <= room capacity
- `max_daily_periods.py` - Lecturer daily hours limit
- `friday_time_restriction.py` - Friday-specific rules
- `no_friday_pray_conflict.py` - No Friday prayer conflicts
- `prayer_time_start.py` - Can't start during prayer
- `class_type_time.py` - Morning/evening class restrictions

**Remaining Soft Constraints:**
- `overflow_penalty.py` - Non-lab in lab room
- `preferred_room.py` - Lecturer preferred room
- `preferred_time.py` - Lecturer preferred time
- `transit_time.py` - Time between classes
- `research_day.py` - Respect research day

**Fix Moves:**
- `fix_room_conflict.py` - Direct fix for room conflicts
- `fix_lecturer_conflict.py` - Direct fix for lecturer conflicts
- `fix_room_capacity.py` - Direct fix for capacity violations

---

### PHASE 3: Domain-Specific (P2) - Week 2-3

**Additional Constraints:**
- `saturday_restriction.py` - Saturday rules
- `exclusive_room.py` - Course-specific rooms
- `prayer_time_overlap.py` - Minimize prayer overlap (soft)
- `evening_class_priority.py` - Evening preferences

**Specialized Moves:**
- `swap_friday_with_non_friday.py` - Friday-specific optimization
- `fix_friday_prayer_conflict.py` - Fix Friday prayer issues
- `fix_max_daily_periods.py` - Fix daily period violations

**Additional Utilities:**
- `room_availability.py` - Check room availability
- `room_constants.py` - Room type definitions
- `slot_validator.py` - Validate time slots
- `class_helper.py` - Class-related helpers
- `constraint_helpers.py` - Constraint utilities

---

### PHASE 4: Notebooks & Visualization - Week 3

**Notebook 2: `02-basic-usage.ipynb`**
- Load data from Excel
- Create initial state
- Define constraints
- Run optimization
- Display results

**Notebook 3: `03-optimization-visualization.ipynb`**
```python
import matplotlib.pyplot as plt

# Fitness over iterations
plt.figure(figsize=(12, 6))
plt.plot(fitness_history)
plt.title('Fitness Over Iterations')
plt.xlabel('Iteration')
plt.ylabel('Fitness')
plt.show()

# Violations reduction
plt.figure(figsize=(12, 6))
plt.plot(hard_violations_history, label='Hard Violations')
plt.plot(soft_violations_history, label='Soft Violations')
plt.legend()
plt.show()

# Timetable visualization (per day, per room)
# Heat map of room utilization
# Lecturer schedule matrix
```

**Notebook 4: `04-final-project-demo.ipynb`**
- Load 1+ year of data
- Before/after comparison
- Export to PDF/Excel
- Metrics for paper

---

### PHASE 5: Testing & Polish - Week 3-4

**Tests:**
- `tests/test_constraints.py` - All constraints
- `tests/test_moves.py` - All move generators
- `tests/test_utils.py` - Utility functions
- `tests/test_integration.py` - Full optimization runs

**Performance:**
- Profile hot paths
- Add caching where needed
- Optimize constraint evaluation

**Documentation:**
- Update README
- Add docstrings
- Create examples

---

## 6. Effort Estimation

| Phase | Files | Lines (Python) | Hours | Week |
|-------|-------|----------------|-------|------|
| Phase 1 (P0) | 18 | ~1200 | 31-35 | 1 |
| Phase 2 (P1) | 20 | ~1100 | 20-24 | 2 |
| Phase 3 (P2) | 6 | ~350 | 8-10 | 2-3 |
| Phase 4 (Notebooks) | 3 | ~300 | 6-8 | 3 |
| Phase 5 (Tests/Polish) | 5 | ~200 | 8-10 | 3-4 |
| **TOTAL** | **52** | **~3150** | **73-87** | **3-4** |

**Timeline:** 3-4 weeks at ~20-25 hours/week

**For Academic Deadline (22 Jan):**
- Focus on Phase 1 (P0) for working demo
- Add selected Phase 2 items for quality
- Create visualization notebook
- **Minimum viable:** ~40 hours

---

## 7. Quick Start Template

### Creating a New Constraint

```python
# constraints/hard/my_constraint.py
from timetable_sa.core.interfaces import Constraint
from timetable_sa.examples.timetabling.types import TimetableState
from typing import Literal

class MyConstraint(Constraint):
    name: str = "My Constraint Name"
    type: Literal["hard", "soft"] = "hard"

    def evaluate(self, state: TimetableState) -> float:
        """
        Returns a score between 0 and 1.
        - 1.0 = fully satisfied
        - 0.0 = completely violated
        - In-between = partially satisfied
        """
        violations = 0

        for entry in state.schedule:
            # Check your constraint logic
            if self._is_violated(entry):
                violations += 1

        return 1.0 if violations == 0 else 1.0 / (1 + violations)

    def get_violations(self, state: TimetableState) -> list[str]:
        """Return detailed violation descriptions"""
        violations = []

        for entry in state.schedule:
            if self._is_violated(entry):
                violations.append(f"Entry {entry.class_id} violates...")

        return violations
```

### Creating a New Move Generator

```python
# moves/my_move.py
from timetable_sa.core.interfaces import MoveGenerator
from timetable_sa.examples.timetabling.types import TimetableState
import random
import copy

class MyMove(MoveGenerator):
    name: str = "My Move"

    def can_apply(self, state: TimetableState) -> bool:
        """Check if this move can be applied to the state"""
        return len(state.schedule) > 0

    def generate(self, state: TimetableState, temperature: float) -> TimetableState | None:
        """Generate a new state by applying this move"""
        if not self.can_apply(state):
            return None

        # Select random entry to modify
        entry = random.choice(state.schedule)

        # Temperature-dependent behavior (optional but recommended)
        if temperature > 10000:
            # High temp: exploration
            pass
        else:
            # Low temp: exploitation
            pass

        # Modify the entry
        # entry.something = new_value

        return state
```

---

## 8. TypeScript → Python Conversion Tips

### Pattern 1: Interface to Dataclass
```typescript
// TypeScript
interface Room {
  Code: string;
  Name: string;
  Capacity: number;
}
```

```python
# Python
from dataclasses import dataclass

@dataclass
class Room:
    code: str  # camelCase → snake_case
    name: str
    capacity: int
```

### Pattern 2: Arrow Functions
```typescript
// TypeScript
const timeToMinutes = (time: string): number => {
  const [h, m] = time.split(':');
  return parseInt(h) * 60 + parseInt(m);
};
```

```python
# Python
from functools import lru_cache

@lru_cache(maxsize=1000)
def time_to_minutes(time_str: str) -> int:
    hours, minutes = map(int, time_str.split(':'))
    return hours * 60 + minutes
```

### Pattern 3: Map to Dictionary
```typescript
// TypeScript
const grouped = new Map<string, Entry[]>();
```

```python
# Python
from collections import defaultdict

grouped = defaultdict(list)
```

### Pattern 4: Array Methods
```typescript
// TypeScript
const filtered = entries.filter(e => e.room === 'R101');
const mapped = entries.map(e => e.classId);
```

```python
# Python
filtered = [e for e in entries if e.room == 'R101']
mapped = [e.class_id for e in entries]
```

---

## 9. Testing Strategy

### Unit Tests
```python
# tests/test_constraints.py
import pytest
from timetable_sa.examples.timetabling.constraints.hard import NoRoomConflict
from timetable_sa.examples.timetabling.types import TimetableState, ScheduleEntry, TimeSlot

def test_no_room_conflict_no_violations():
    constraint = NoRoomConflict()
    state = TimetableState(
        schedule=[
            ScheduleEntry(
                class_id="CS101",
                room="R101",
                time_slot=TimeSlot(day="Monday", start_time="08:00", end_time="09:00", period=1),
                # ... other fields
            ),
            ScheduleEntry(
                class_id="CS102",
                room="R101",
                time_slot=TimeSlot(day="Monday", start_time="10:00", end_time="11:00", period=2),
                # ... other fields
            ),
        ],
        # ... other fields
    )

    score = constraint.evaluate(state)
    assert score == 1.0

def test_no_room_conflict_with_violations():
    # Test with overlapping room assignments
    pass
```

### Integration Tests
```python
# tests/test_integration.py
def test_full_optimization():
    # Load data
    rooms, lecturers, classes = load_from_excel(...)

    # Create state
    state = create_initial_state(classes, rooms, lecturers, time_slots)

    # Define constraints
    constraints = [NoRoomConflict(), NoLecturerConflict(), Compactness()]

    # Define moves
    moves = [ChangeTimeSlot(), ChangeRoom(), SwapClasses()]

    # Run optimization
    solution = SimulatedAnnealing(state, constraints, moves, config).solve()

    # Verify improvement
    assert solution['hard_violations'] < initial_violations
```

---

## 10. Data File Format

### Actual Dataset: `data_uisi.xlsx`

**Location:** `/home/emmanuelabayor/projects/timetable-sa/data_uisi.xlsx`

**Single Excel file with 3 sheets:**

#### Sheet 1: `ruangan` (34 rows) - Rooms

| Column | Type | Description |
|--------|------|-------------|
| Code | string | Room code (e.g., "B2-R1", "CM-101") |
| Name | string | Room full name |
| Type | string | Room type ("theory", "lab", etc.) |
| Capacity | int | Maximum capacity |

**Sample rows:**
| Code | Name | Type | Capacity |
|------|------|------|----------|
| B2-R1 | Kampus B B2 Ruang 1 | theory | 30 |
| B3-R1 | Kampus B B3 Ruang 1 | theory | 30 |
| CM-101 | ... | ... | ... |

---

#### Sheet 2: `dosen` (100 rows) - Lecturers

| Column | Type | Description |
|--------|------|-------------|
| Prodi | string | Study program (e.g., "Magister Management") |
| Code | string | Lecturer code (e.g., "RPA", "GTK") |
| Name | string | Full name with titles |
| Prefered_Time | string | Preferred time slots (comma-separated) |
| Research_Day | string | Reserved research day (or None) |
| Transit_Time | int | Minutes needed between classes |
| Max_Daily_Periods | int | Maximum teaching hours per day |
| Prefered_Room | string | Preferred room (or None) |

**Sample rows:**
| Prodi | Code | Name | Prefered_Time | Research_Day | Transit_Time | Max_Daily_Periods | Prefered_Room |
|-------|------|------|---------------|--------------|--------------|-------------------|---------------|
| Magister Management | RPA | Dr. Rr. Rooswanti... | 18.30 - 21.00 Thursday, 18.30 - 21.00 Friday, 07.30 - 16.20 Saturday | None | 0 | 9 | None |
| Magister Management | GTK | Dr. Ir. Gatot... | 18.30 - 21.00 Thursday, 18.30 - 21.00 Friday, 07.30 - 16.20 Saturday | None | 0 | 9 | None |

---

#### Sheet 3: `kebutuhan_kelas` (374 rows) - Class Requirements

| Column | Type | Description |
|--------|------|-------------|
| Prodi | string | Study program |
| Kelas | string | Class section (e.g., "MM-1A") |
| Kode_Matakuliah | string | Course code |
| Mata_Kuliah | string | Course name |
| SKS | int | Credit hours |
| Jenis | string | Course type ("wajib", "pilihan") |
| Peserta | int | Number of participants/students |
| Kode_Dosen1 | string | Primary lecturer code |
| Kode_Dosen2 | string | Secondary lecturer code (or None) |
| Kode_Dosen_Prodi_Lain1 | string | External lecturer 1 (or None) |
| Kode_Dosen_Prodi_Lain2 | string | External lecturer 2 (or None) |
| Class_Type | string | "pagi" (morning) or "sore" (evening) |
| should_on_the_lab | string | "yes" or "no" |
| rooms | string | Comma-separated list of preferred rooms |

**Sample rows:**
| Prodi | Kelas | Kode_Matakuliah | Mata_Kuliah | SKS | Jenis | Peserta | Kode_Dosen1 | Kode_Dosen2 | Kode_Dosen_Prodi_Lain1 | Kode_Dosen_Prodi_Lain2 | Class_Type | should_on_the_lab | rooms |
|-------|-------|-----------------|-------------|-----|-------|---------|-------------|-------------|----------------------|----------------------|------------|-------------------|-------|
| Magister Manajemen | MM-1A | MM23EB03 | Economic for Business | 3 | wajib | 15 | BAT | None | WAH | None | sore | no | B2-R1, B3-R1, B3-R2, B3R3, CM-101, CM-102... |
| Magister Manajemen | MM-1A | MM23SM03 | Strategic Marketing Management | 3 | wajib | 15 | ALF | None | WAH | None | pagi | no | B2-R1, B3-R1, B3-R2, B3R3, CM-101... |

---

### Python Data Loading Code

```python
# data/excel_loader.py
import pandas as pd
from typing import Optional
from dataclasses import dataclass

@dataclass
class Room:
    code: str
    name: str
    type: str
    capacity: int

@dataclass
class Lecturer:
    prodi: str
    code: str
    name: str
    preferred_time: Optional[str]
    research_day: Optional[str]
    transit_time: int
    max_daily_periods: int
    preferred_room: Optional[str]

@dataclass
class ClassRequirement:
    prodi: str
    kelas: str
    kode_matakuliah: str
    mata_kuliah: str
    sks: int
    jenis: str
    peserta: int
    kode_dosen1: str
    kode_dosen2: Optional[str]
    kode_dosen_prodi_lain1: Optional[str]
    kode_dosen_prodi_lain2: Optional[str]
    class_type: str  # "pagi" or "sore"
    should_on_the_lab: str  # "yes" or "no"
    rooms: str  # Comma-separated room list

def load_data_uisi(excel_path: str = "/home/emmanuelabayor/projects/timetable-sa/data_uisi.xlsx"):
    """Load UISI timetabling data from Excel file."""

    # Load rooms
    rooms_df = pd.read_excel(excel_path, sheet_name="ruangan")
    rooms = [
        Room(
            code=row["Code"],
            name=row["Name"],
            type=row["Type"],
            capacity=row["Capacity"]
        )
        for _, row in rooms_df.iterrows()
    ]

    # Load lecturers
    lecturers_df = pd.read_excel(excel_path, sheet_name="dosen")
    lecturers = [
        Lecturer(
            prodi=row["Prodi"],
            code=row["Code"],
            name=row["Name"],
            preferred_time=row.get("Prefered_Time"),
            research_day=row.get("Research_Day"),
            transit_time=row["Transit_Time"],
            max_daily_periods=row["Max_Daily_Periods"],
            preferred_room=row.get("Prefered_Room")
        )
        for _, row in lecturers_df.iterrows()
    ]

    # Load class requirements
    classes_df = pd.read_excel(excel_path, sheet_name="kebutuhan_kelas")
    classes = [
        ClassRequirement(
            prodi=row["Prodi"],
            kelas=row["Kelas"],
            kode_matakuliah=row["Kode_Matakuliah"],
            mata_kuliah=row["Mata_Kuliah"],
            sks=row["SKS"],
            jenis=row["Jenis"],
            peserta=row["Peserta"],
            kode_dosen1=row["Kode_Dosen1"],
            kode_dosen2=row.get("Kode_Dosen2"),
            kode_dosen_prodi_lain1=row.get("Kode_Dosen_Prodi_Lain1"),
            kode_dosen_prodi_lain2=row.get("Kode_Dosen_Prodi_Lain2"),
            class_type=row["Class_Type"],
            should_on_the_lab=row["should_on_the_lab"],
            rooms=row["rooms"]
        )
        for _, row in classes_df.iterrows()
    ]

    return rooms, lecturers, classes

# Usage
rooms, lecturers, classes = load_data_uisi()
print(f"Loaded {len(rooms)} rooms, {len(lecturers)} lecturers, {len(classes)} classes")
# Output: Loaded 34 rooms, 100 lecturers, 374 classes
```

---

### Key Data Differences from Expected Format

1. **Single Excel file** (not 3 separate files)
2. **Sheet names are Indonesian:** `ruangan`, `dosen`, `kebutuhan_kelas`
3. **Additional columns in lecturers:** `Prefered_Room`
4. **Additional columns in classes:** `Kode_Dosen2`, `Kode_Dosen_Prodi_Lain1`, `Kode_Dosen_Prodi_Lain2`, `Jenis`
5. **Real university scale:** 374 classes, 100 lecturers, 34 rooms

---

## 11. Validation Checklist

Before considering the port complete:

### Code Quality
- [ ] All TypeScript files have Python equivalents
- [ ] Type hints added to all functions
- [ ] Docstrings for all classes and methods
- [ ] PEP 8 compliant (use black/ruff)
- [ ] No linting errors

### Functionality
- [ ] All constraints produce same scores as TS
- [ ] All moves generate valid states
- [ ] Full optimization runs without errors
- [ ] Results comparable to TypeScript version

### Testing
- [ ] Unit tests for all constraints (≥80% coverage)
- [ ] Unit tests for all moves
- [ ] Integration test with real data
- [ ] Performance within 2x of TypeScript

### Documentation
- [ ] README updated with Python examples
- [ ] API documentation complete
- [ ] Notebooks run without errors
- [ ] Example data files provided

### Academic Requirements
- [ ] Works in Google Colab
- [ ] 1+ year of sample data
- [ ] Visualization notebook complete
- [ ] Can generate PDF/Excel output
- [ ] Results suitable for 10+ page paper

---

## 12. Troubleshooting Guide

### Common Issues

**Issue 1: Mutable Default Arguments**
```python
# BAD
def foo(entries: list = []):
    pass

# GOOD
def foo(entries: list | None = None):
    if entries is None:
        entries = []
```

**Issue 2: State Cloning**
```python
# BAD - shallow copy
new_state = state.schedule.copy()

# GOOD - deep copy
import copy
new_state = copy.deepcopy(state)

# OR use dataclasses
from dataclasses import replace
new_entry = replace(entry, room="R102")
```

**Issue 3: LRU Cache with Unhashable Types**
```python
# BAD - can't cache dict/list
@lru_cache
def foo(data: dict):
    pass

# GOOD - use frozenset or convert to hashable
@lru_cache
def foo(data_tuple: tuple):
    pass
```

**Issue 4: Type Hints for Generic State**
```python
from typing import TypeVar, Any

TState = TypeVar('TState', bound=Any)

def clone_state(state: TState) -> TState:
    return copy.deepcopy(state)
```

---

## 13. File Creation Order (Step-by-Step)

### Start Here (in order):

1. `__init__.py` files (create directory structure)
2. `types/domain.py` - All domain dataclasses
3. `types/state.py` - State dataclasses
4. `utils/prayer_times.py` - Constants
5. `utils/time.py` - Time functions
6. `utils/timeslot_generator.py` - Generate slots
7. `utils/initial_solution.py` - Create initial state
8. `data/excel_loader.py` - Load data
9. `constraints/hard/no_room_conflict.py` - Test constraint pattern
10. `constraints/hard/no_lecturer_conflict.py` - Build on pattern
11. `constraints/hard/no_prodi_conflict.py` - Build on pattern
12. `constraints/soft/compactness.py` - Test soft constraint pattern
13. `moves/change_time_slot.py` - Test move pattern
14. `moves/change_room.py` - Build on pattern
15. `moves/swap_classes.py` - Build on pattern
16. `examples/basic_example.py` - Integrate everything
17. Test with sample data
18. Continue with remaining constraints (P1)
19. Continue with remaining moves (P1)
20. Add utilities (P1)
21. Create notebooks
22. Add tests

---

## 14. Success Metrics

### MVP Success (Phase 1 Complete)
- ✅ Can load data from Excel
- ✅ Can create initial random schedule
- ✅ Can run optimization with 3 hard + 1 soft constraint
- ✅ Can run with 3 basic move operators
- ✅ Produces valid timetable with fewer violations
- ✅ Works in Jupyter notebook

### Full Success (All Phases Complete)
- ✅ All 54 TypeScript files ported
- ✅ All constraints from TS version working
- ✅ All moves from TS version working
- ✅ Results match TypeScript version (±5%)
- ✅ Complete visualization notebook
- ✅ Ready for academic presentation

---

## 15. Next Steps

1. **Review this plan** - Understand the full scope
2. **Set up Python environment** - Install dependencies
3. **Create directory structure** - All `__init__.py` files
4. **Start with Phase 1** - Focus on P0 files first
5. **Test incrementally** - Run after each file
6. **Create notebook early** - `02-basic-usage.ipynb` as soon as P0 complete
7. **Demo for lecturer** - Get feedback before continuing
8. **Complete P1/P2** - Based on feedback and time

---

**Document Version:** 2.0 (Complete)
**Last Updated:** 2026-01-08
**Total Files to Port:** 54 TypeScript → 46 Python files
**Estimated Effort:** 73-87 hours over 3-4 weeks
**Minimum Viable:** 31-35 hours (Phase 1 - P0 files only)
