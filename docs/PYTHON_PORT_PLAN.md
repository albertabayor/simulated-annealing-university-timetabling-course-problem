# Python Port Plan: timetable-sa

**Status:** Planning Phase
**Created:** 2026-01-08
**Objective:** Port TypeScript Simulated Annealing library to Python for final project submission

---

## 1. Context & Motivation

### Why This Port Exists
- **Academic Requirement:** Lecturer requires Python/Google Colab for final project
- **Thesis Alignment:** Original TypeScript implementation serves as thesis work
- **Value Proposition:** Demonstrates polyglot engineering capabilities
- **Research Domain:** Python dominates AI/ML optimization research space

### Academic Requirements (from UAS assignment)
- Use Python or Google Colab/Jupyter Notebook
- Minimum 1 year of daily data
- Generate model and simulation with appropriate method
- Present results (22 Jan 2026)
- Submit 10+ page paper (24 Jan 2026)

---

## 2. Architecture Comparison

### TypeScript Structure (Current)
```
timetable-sa/
├── src/
│   ├── core/
│   │   ├── SimulatedAnnealing.ts    # Main solver (960 lines)
│   │   ├── interfaces/
│   │   │   ├── Constraint.ts        # Constraint interface
│   │   │   ├── MoveGenerator.ts     # Move operator interface
│   │   │   └── SAConfig.ts          # Configuration interface
│   │   └── types/
│   │       ├── Solution.ts          # Solution type
│   │       └── Violation.ts         # Violation type
│   └── index.ts
├── examples/
│   └── timetabling/                 # University timetabling example
│       ├── constraints/             # 20+ constraint implementations
│       ├── moves/                   # 10+ move operators
│       └── utils/                   # Helper functions
└── dist/                            # Compiled JavaScript
```

### Proposed Python Structure
```
timetable-sa-python/
├── src/
│   └── timetable_sa/
│       ├── __init__.py
│       ├── core/
│       │   ├── __init__.py
│       │   ├── simulated_annealing.py    # Main solver
│       │   ├── interfaces/
│       │   │   ├── __init__.py
│       │   │   ├── constraint.py         # ABC for constraints
│       │   │   ├── move_generator.py     # ABC for move operators
│       │   │   └── config.py             # Configuration dataclass
│       │   └── types/
│       │       ├── __init__.py
│       │       ├── solution.py           # NamedTuple/TypedDict
│       │       └── violation.py          # TypedDict
│       └── utils/
│           └── __init__.py
├── examples/
│   └── timetabling/
│       ├── constraints/
│       ├── moves/
│       └── utils/
├── notebooks/
│   ├── 01-introduction.ipynb           # For lecturer demo
│   ├── 02-basic-usage.ipynb
│   ├── 03-optimization-visualization.ipynb
│   └── 04-final-project-demo.ipynb
├── tests/
│   └── test_*.py
├── pyproject.toml                      # Modern Python packaging
└── README.md
```

---

## 3. Type System Mapping

### TypeScript → Python

| TypeScript | Python | Notes |
|------------|--------|-------|
| `interface` | `abc.ABC` | Abstract base classes |
| `generic <TState>` | `TypeVar('TState')` | Generic type variable |
| `type Solution<T>` | `TypeAlias` | `Solution = TypeVar('Solution')` |
| `export` | `__all__` | Public API |
| `enum` | `enum.Enum` | Direct mapping |
| `Promise<T>` | `concurrent.futures.Future` | If needed |

### Key Type Translations

**Constraint Interface:**
```typescript
// TypeScript
interface Constraint<TState> {
  name: string;
  type: 'hard' | 'soft';
  weight?: number;
  evaluate(state: TState): number;
  getViolations?(state: TState): string[];
}
```

```python
# Python
from abc import ABC, abstractmethod
from typing import Protocol, runtime_checkable, TypeVar

TState = TypeVar('TState')

@runtime_checkable
class Constraint(ABC):
    name: str
    type: Literal['hard', 'soft']
    weight: float = 10.0

    @abstractmethod
    def evaluate(self, state: TState) -> float:
        """Returns score between 0 and 1"""
        pass

    def get_violations(self, state: TState) -> list[str]:
        return []
```

**Configuration:**
```typescript
// TypeScript
interface SAConfig<TState> {
  initialTemperature: number;
  minTemperature: number;
  coolingRate: number;
  maxIterations: number;
  hardConstraintWeight: number;
  cloneState: (state: TState) => TState;
}
```

```python
# Python
from dataclasses import dataclass, field
from typing import Callable, TypeVar

TState = TypeVar('TState')

@dataclass
class SAConfig:
    initial_temperature: float = 1000.0
    min_temperature: float = 0.01
    cooling_rate: float = 0.995
    max_iterations: int = 50000
    hard_constraint_weight: float = 10000.0
    clone_state: Callable[[TState], TState] = field(default=None)

    # Advanced features
    enable_intensification: bool = True
    tabu_search_enabled: bool = False
    logging_enabled: bool = True
```

---

## 4. Core Algorithm Port: Key Changes

### 4.1 SimulatedAnnealing Class (960 lines → ~800 lines Python)

**Porting Strategy:**
1. Convert class structure with `@dataclass` for config
2. Use TypeVar for generic state handling
3. Maintain all advanced features (Tabu Search, Intensification, Reheating)
4. Replace `Map` with `dict` and `Set` with `set`
5. Use `random` module instead of `Math.random()`

**Critical Methods to Port:**
| Method | Lines | Complexity |
|--------|-------|------------|
| `solve()` | ~400 | High - Multi-phase orchestration |
| `calculateFitnessAndViolations()` | ~40 | Medium - Optimization critical |
| `generateNeighbor()` | ~20 | Low - Simple selection |
| `selectMoveGenerator()` | ~30 | Medium - Roulette wheel |
| `getStateSignature()` | ~20 | Low - String hashing |
| `acceptanceProbabilityPhase1/2()` | ~60 | Low - Mathematical formulas |
| Tabu Search methods | ~100 | Medium - List management |
| Intensification logic | ~140 | High - Complex restart logic |

### 4.2 Performance Considerations

| Aspect | TypeScript | Python | Mitigation |
|--------|-----------|--------|------------|
| Type safety | Compile-time | Runtime + mypy | Use strict type hints |
| Iteration speed | V8 optimized | CPython slower | Use NumPy for data ops |
| Memory efficiency | Good | Good | Avoid excessive object creation |
| Hot loops | JIT-optimized | Interpreter | Use `@lru_cache`, profile |

---

## 5. Advanced Features Mapping

### 5.1 Multi-Phase Optimization
- **Phase 1:** Hard constraint elimination (60% iterations)
- **Phase 1.5:** Intensification (optional, 2000 iterations)
- **Phase 2:** Soft constraint optimization (remaining)

```python
def solve(self) -> Solution[TState]:
    # Phase 1: Eliminate hard constraints
    phase1_iterations = math.floor(self.max_iterations * 0.6)
    while (temp > self.initial_temperature / 10 and
           iteration < phase1_iterations and
           best_hard_violations > 0):
        # ... implementation

    # Phase 1.5: Intensification
    if best_hard_violations > 0 and self.config.enable_intensification:
        for attempt in range(self.max_intensification_attempts):
            # ... implementation

    # Phase 2: Optimize soft constraints
    while temp > self.min_temperature and iteration < self.max_iterations:
        # ... strict enforcement of hard constraints
```

### 5.2 Tabu Search
- State signature generation
- Tabu list with iteration tracking
- Automatic cleanup

```python
def get_state_signature(self, state: TState) -> str:
    schedule = getattr(state, 'schedule', None)
    if not schedule:
        return str(random.random())

    assignments = []
    for entry in schedule:
        if hasattr(entry, 'classId') and hasattr(entry, 'timeSlot'):
            assignments.append(
                f"{entry.classId}:{entry.timeSlot.day}:"
                f"{entry.timeSlot.startTime}:{entry.room}"
            )
    return '|'.join(sorted(assignments))
```

### 5.3 Adaptive Operator Selection
- Roulette wheel selection
- 70% weighted by success rate, 30% random exploration

```python
def select_move_generator(self, generators: list[MoveGenerator]) -> MoveGenerator:
    # 30% random exploration
    if random.random() < 0.3:
        return random.choice(generators)

    # 70% weighted by success rate
    weights = [self.operator_stats[g.name].success_rate or 0.5
               for g in generators]
    total = sum(weights)

    if total == 0:
        return random.choice(generators)

    r = random.random() * total
    for i, w in enumerate(weights):
        r -= w
        if r <= 0:
            return generators[i]
    return generators[-1]
```

---

## 6. Jupyter Notebook Strategy

### For Lecturer Demo & Final Project

**Notebook 1: Introduction & Setup**
```python
# Installation
!pip install timetable-sa

# Imports
from timetable_sa import SimulatedAnnealing, Constraint, MoveGenerator
from timetable_sa.examples.timetabling import *
```

**Notebook 2: Basic Usage**
```python
# Load data
data = load_from_excel('courses.xlsx')

# Define constraints
constraints = [
    NoRoomConflict(),
    NoLecturerConflict(),
    RoomCapacity(),
    # ...
]

# Run optimization
sa = SimulatedAnnealing(
    initial_state=data.initial_state,
    constraints=constraints,
    move_generators=moves,
    config=SAConfig(max_iterations=50000)
)

solution = sa.solve()

# Visualize results
plot_optimization_progress(solution)
plot_timetable(solution.state)
```

**Notebook 3: Final Project Demo**
- Load real university data (1+ year)
- Show constraint violations in current schedule
- Run optimization
- Compare before/after
- Export to PDF/Excel

---

## 7. Implementation Plan

### Phase 1: Core Library (Week 1)
- [ ] Set up project structure (`pyproject.toml`, directories)
- [ ] Implement base interfaces (ABC classes)
- [ ] Port `SimulatedAnnealing` core class
- [ ] Implement `SAConfig` dataclass
- [ ] Add basic logging

### Phase 2: Advanced Features (Week 1-2)
- [ ] Implement Tabu Search
- [ ] Implement Intensification (Phase 1.5)
- [ ] Implement Reheating mechanism
- [ ] Add operator statistics tracking

### Phase 3: Example Domain (Week 2)
- [ ] Port timetabling types
- [ ] Port 5-10 key constraints (hard + soft)
- [ ] Port 5 key move generators
- [ ] Add data loading (Excel/CSV)

### Phase 4: Notebooks & Visualization (Week 2-3)
- [ ] Create introduction notebook
- [ ] Create basic usage notebook
- [ ] Add visualization functions (matplotlib/seaborn)
- [ ] Create final project demo notebook
- [ ] Add progress plots, timetable visualizations

### Phase 5: Testing & Documentation (Week 3)
- [ ] Unit tests for core algorithms
- [ ] Integration tests
- [ ] README with examples
- [ ] API documentation (docstrings)

### Phase 6: Final Project Paper (Week 3-4)
- [ ] Gather results from runs
- [ ] Generate charts/tables for paper
- [ ] Write 10+ page paper (following lecturer's format)

---

## 8. Dependencies

### Core Dependencies
```toml
[tool.poetry.dependencies]
python = "^3.11"
numpy = "^1.26.0"      # For numerical operations
pandas = "^2.1.0"      # For data handling
matplotlib = "^3.8.0"  # For visualization
openpyxl = "^3.1.0"    # For Excel loading
dataclasses-json = "^0.6.0"  # For JSON serialization

[tool.poetry.dev-dependencies]
pytest = "^7.4.0"
pytest-cov = "^4.1.0"
mypy = "^1.7.0"
black = "^23.12.0"
ruff = "^0.1.0"
jupyter = "^1.0.0"
```

---

## 9. Branch Strategy

```
main                          # TypeScript version (current)
└── feature/python-port        # Python development
    ├── core-implementation    # Phase 1
    ├── advanced-features      # Phase 2
    ├── examples-domain        # Phase 3
    ├── notebooks-viz          # Phase 4
    └── testing-docs           # Phase 5
```

---

## 10. Success Criteria

### Minimum Viable Port (MVP)
- [ ] Core `SimulatedAnnealing` class working
- [ ] 3 hard constraints implemented
- [ ] 3 move operators implemented
- [ ] 1 working example (timetabling)
- [ ] 1 Jupyter notebook demo

### Full Feature Parity
- [ ] All advanced features (Tabu Search, Intensification, Reheating)
- [ ] All constraints from TypeScript version
- [ ] All move operators from TypeScript version
- [ ] Comprehensive test coverage (>80%)
- [ ] Complete documentation

### Academic Requirements
- [ ] Python code working in Google Colab
- [ ] Demo notebook for lecturer presentation
- [ ] Results suitable for 10+ page paper
- [ ] Visualizations (plots, charts)
- [ ] Data: 1+ year of real/simulated data

---

## 11. Risks & Mitigations

| Risk | Impact | Mitigation |
|------|--------|------------|
| Python performance slower than TS | Medium | Profile hot paths, use NumPy |
| Type hints not enforced at runtime | Low | Use mypy in CI, runtime checks |
| Lecturer unfamiliar with packages | Low | Provide notebook with !pip install |
| Time constraint for submission | High | Prioritize MVP, cut non-essential features |
| Google Colab limitations | Low | Test early, provide fallbacks |

---

## 12. Estimated Effort

| Task | Time (hours) |
|------|--------------|
| Project setup & structure | 2 |
| Core SimulatedAnnealing port | 6-8 |
| Advanced features | 4-6 |
| Timetabling domain (constraints + moves) | 6-8 |
| Jupyter notebooks & visualization | 4-6 |
| Testing | 2-4 |
| Documentation | 2-3 |
| Final project paper preparation | 4-6 |
| **Total** | **30-43 hours** |

**Timeline:** 3-4 weeks at ~10 hours/week

---

## 13. Quick Reference: Key File Mappings

| TypeScript File | Python File | Lines (est.) |
|----------------|-------------|--------------|
| `SimulatedAnnealing.ts` | `simulated_annealing.py` | 960 → 800 |
| `SAConfig.ts` | `config.py` | 360 → 200 |
| `Constraint.ts` | `constraint.py` | 128 → 80 |
| `MoveGenerator.ts` | `move_generator.py` | 100 → 70 |
| `Solution.ts` | `solution.py` | 93 → 60 |
| `Violation.ts` | `violation.py` | 30 → 20 |

**Total core:** ~1671 lines → ~1230 lines Python (~26% reduction)

---

## 14. Next Steps

1. **Review this plan** - Confirm approach and priorities
2. **Create branch** - `git checkout -b feature/python-port`
3. **Set up project** - Initialize Python structure
4. **Start with MVP** - Core SA class + 1 simple example
5. **Test in Colab** - Verify lecturer requirements met
6. **Iterate** - Add features based on time remaining

---

## Appendix A: Code Comparison Example

### TypeScript: NoRoomConstraint
```typescript
export class NoRoomConflict implements Constraint<TimetableState> {
  name = 'No Room Conflict';
  type = 'hard' as const;

  evaluate(state: TimetableState): number {
    const violations: Array<{day: string, startTime: string, room: string}> = [];

    for (let i = 0; i < state.schedule.length; i++) {
      for (let j = i + 1; j < state.schedule.length; j++) {
        const a = state.schedule[i];
        const b = state.schedule[j];

        if (a.timeSlot.day === b.timeSlot.day &&
            a.timeSlot.startTime === b.timeSlot.startTime &&
            a.room === b.room) {
          violations.push({day: a.timeSlot.day, startTime: a.timeSlot.startTime, room: a.room});
        }
      }
    }

    return violations.length === 0 ? 1 : 1 / (1 + violations.length);
  }

  getViolations(state: TimetableState): string[] {
    // ... implementation
  }
}
```

### Python: NoRoomConstraint
```python
from typing import Literal
from timetable_sa.core.interfaces import Constraint
from timetable_sa.examples.timetabling.types import TimetableState

class NoRoomConflict(Constraint):
    name: str = 'No Room Conflict'
    type: Literal['hard', 'soft'] = 'hard'

    def evaluate(self, state: TimetableState) -> float:
        violations = []

        for i, entry_a in enumerate(state.schedule):
            for entry_b in state.schedule[i+1:]:
                if (entry_a.time_slot.day == entry_b.time_slot.day and
                    entry_a.time_slot.start_time == entry_b.time_slot.start_time and
                    entry_a.room == entry_b.room):
                    violations.append({
                        'day': entry_a.time_slot.day,
                        'start_time': entry_a.time_slot.start_time,
                        'room': entry_a.room
                    })

        return 1.0 if len(violations) == 0 else 1.0 / (1 + len(violations))

    def get_violations(self, state: TimetableState) -> list[str]:
        # ... implementation
        return violations
```

---

**Document Version:** 1.0
**Last Updated:** 2026-01-08
