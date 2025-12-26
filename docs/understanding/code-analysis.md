# timetable-sa Code Analysis and Understanding

## Table of Contents
1. [Package Overview](#package-overview)
2. [How It Works](#how-it-works)
3. [Core Components](#core-components)
4. [Algorithm Flow](#algorithm-flow)
5. [Code Suggestions and Improvements](#code-suggestions-and-improvements)
6. [Example Output](#example-output)
7. [Best Practices](#best-practices)

---

## Package Overview

**timetable-sa** is a generic, unopinionated **Simulated Annealing** library for solving **constraint satisfaction problems** (CSP). While the name suggests timetabling, it's actually a versatile optimization framework that can solve any CSP, including:
- Course timetabling
- Resource allocation
- Job scheduling
- Nurse rostering
- Vehicle routing
- Any problem with constraints

### Key Characteristics
- **Type-safe**: Written in TypeScript with full type inference
- **Framework-agnostic**: No dependencies on specific scheduling data structures
- **Two-phase optimization**: Eliminates hard violations first, then optimizes soft constraints
- **Adaptive operators**: Learns which move operators work best and uses them more frequently
- **Reheating support**: Can escape local minima by increasing temperature

---

## How It Works

### Simulated Annealing (SA) Explained

Simulated Annealing is a probabilistic optimization algorithm inspired by the annealing process in metallurgy. Here's the core idea:

1. **Start with a high temperature** → Accept many random changes (exploration)
2. **Gradually cool down** → Accept fewer bad changes, focus on improvements (exploitation)
3. **Accept worse moves with probability** `P = exp((currentFitness - newFitness) / temperature)`

This allows the algorithm to escape local minima early on, while converging to a good solution as it cools.

### The Two-Phase Approach

Your implementation uses a clever **two-phase strategy**:

#### Phase 1: Hard Constraint Elimination (0-60% of iterations)
- Focuses exclusively on eliminating hard constraint violations
- Temperature starts high and ends at `initialTemperature / 10`
- **Always accepts** moves that reduce hard violations
- **Never accepts** moves that increase hard violations
- Stops when hard violations = 0 or phase 1 iterations exhausted

#### Phase 2: Soft Constraint Optimization (60-100% of iterations)
- Maintains hard constraint satisfaction (strict enforcement)
- Optimizes soft constraints (preferences)
- Temperature continues cooling from Phase 1 end temperature
- **Never accepts** moves that increase hard violations
- Standard SA acceptance for soft constraint optimization

This two-phase approach ensures a valid solution before optimizing preferences.

---

## Core Components

### 1. **State (`TState`)**

The state represents a complete solution to your problem.

```typescript
// Example: Timetabling state
interface TimetableState {
  schedule: ScheduleEntry[];      // Current schedule
  availableTimeSlots: TimeSlot[]; // Available slots
  rooms: Room[];                  // Available rooms
  lecturers: Lecturer[];          // Available lecturers
}
```

### 2. **Constraints**

Constraints evaluate how good a state is, returning a score from **0 to 1**.

#### Hard Constraints
- Must be satisfied (binary: 0 or 1)
- Example: "No two classes in same room at same time"
- Heavily penalized if violated (`hardConstraintWeight`)

```typescript
class NoRoomConflict implements Constraint<TimetableState> {
  name = 'No Room Conflict';
  type = 'hard' as const;

  evaluate(state: TimetableState): number {
    // Return 1 if satisfied, 0 if violated
    return this.hasConflicts(state) ? 0 : 1;
  }

  getViolations(state: TimetableState): string[] {
    // Return list of all violations
    return this.findConflicts(state);
  }
}
```

#### Soft Constraints
- Preferences (0 to 1, can be partial)
- Example: "Professor prefers morning classes"
- Lightly penalized with custom `weight`

```typescript
class PreferredTime implements Constraint<TimetableState> {
  name = 'Preferred Time';
  type = 'soft' as const;
  weight = 10; // Customize importance

  evaluate(state: TimetableState): number {
    // Return 1.0 = perfect, 0.5 = okay, 0.0 = terrible
    return this.calculatePreferenceScore(state);
  }
}
```

### 3. **Move Generators**

Move generators create "neighbor" states by modifying the current state.

```typescript
class ChangeTimeSlot implements MoveGenerator<TimetableState> {
  name = 'Change Time Slot';

  canApply(state: TimetableState): boolean {
    return state.schedule.length > 0; // Can we apply this move?
  }

  generate(state: TimetableState, temperature: number): TimetableState {
    // 1. Clone state (DON'T modify input)
    const newState = this.cloneState(state);

    // 2. Apply modification
    const randomClass = newState.schedule[Math.floor(Math.random() * newState.schedule.length)];
    randomClass.timeSlot = this.pickRandomSlot(newState.availableTimeSlots);

    // 3. Return new state
    return newState;
  }
}
```

### 4. **SA Configuration**

Controls the algorithm's behavior.

```typescript
const config: SAConfig<TimetableState> = {
  initialTemperature: 100000,   // High for exploration
  minTemperature: 0.0000001,    // Low for convergence
  coolingRate: 0.9998,          // Slow cooling
  maxIterations: 60000,         // Total iterations
  hardConstraintWeight: 100000, // Prioritize hard constraints

  cloneState: (state) => ({    // Efficient cloning
    ...state,
    schedule: state.schedule.map(e => ({ ...e }))
  }),

  reheatingThreshold: 500,      // Reheat if stuck
  reheatingFactor: 150,         // Temperature multiplier
  maxReheats: 10,

  logging: {
    enabled: true,
    level: 'info',
    logInterval: 500,
  },
};
```

---

## Algorithm Flow

```
┌─────────────────────────────────────────────────────────────────┐
│                    INITIALIZATION                                │
├─────────────────────────────────────────────────────────────────┤
│  1. Load initial state                                           │
│  2. Separate hard/soft constraints                              │
│  3. Initialize move operators                                   │
│  4. Set initial temperature                                     │
└─────────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────────┐
│                  PHASE 1: HARD CONSTRAINT ELIMINATION          │
├─────────────────────────────────────────────────────────────────┤
│  For each iteration (0-60% of maxIterations):                   │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │  1. Select move operator (adaptive or random)          │   │
│  │  2. Apply move to generate neighbor state              │   │
│  │  3. Evaluate new state's hard violations               │   │
│  │                                                         │   │
│  │  IF new hard violations < current:                     │   │
│  │      → Accept (always)                                │   │
│  │  ELSE IF new hard violations == current:               │   │
│  │      → Accept if fitness improves OR                   │   │
│  │        with probability exp((current - new) / temp)   │   │
│  │  ELSE (worse hard violations):                         │   │
│  │      → Reject (never)                                 │   │
│  │                                                         │   │
│  │  4. Update best solution                               │   │
│  │  5. Cool down (temp *= coolingRate)                    │   │
│  │  6. Log progress                                       │   │
│  └─────────────────────────────────────────────────────────┘   │
│                                                                 │
│  Stopping conditions:                                           │
│  - Temperature < initialTemp / 10                              │
│  - Hard violations = 0                                         │
│  - Phase 1 iterations exhausted                                │
└─────────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────────┐
│                 PHASE 2: SOFT CONSTRAINT OPTIMIZATION           │
├─────────────────────────────────────────────────────────────────┤
│  For each iteration (60-100% of maxIterations):                 │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │  1. Select move operator (adaptive or random)          │   │
│  │  2. Apply move to generate neighbor state              │   │
│  │  3. Evaluate new state                                │   │
│  │                                                         │   │
│  │  IF new hard violations > bestHardViolations:         │   │
│  │      → Reject (strictly enforce hard constraints)     │   │
│  │  ELSE IF new hard violations < bestHardViolations:    │   │
│  │      → Accept (always)                                │   │
│  │  ELSE (same hard violations):                          │   │
│  │      → Accept if fitness improves OR                   │   │
│  │        with probability exp((current - new) / temp)   │   │
│  │                                                         │   │
│  │  4. Update best solution                               │   │
│  │  5. Cool down (temp *= coolingRate)                    │   │
│  │  6. Log progress                                       │   │
│  └─────────────────────────────────────────────────────────┘   │
│                                                                 │
│  Stopping conditions:                                           │
│  - Temperature < minTemperature                                │
│  - Total iterations > maxIterations                            │
└─────────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────────┐
│                      RETURN SOLUTION                             │
├─────────────────────────────────────────────────────────────────┤
│  - Best state found                                              │
│  - Fitness score                                                 │
│  - Hard/soft violation counts                                   │
│  - Detailed violation list                                     │
│  - Operator statistics                                          │
└─────────────────────────────────────────────────────────────────┘
```

### Adaptive Operator Selection

The algorithm learns which move operators work best:

```typescript
// Line 377-407 in SimulatedAnnealing.ts
private selectMoveGenerator(generators: MoveGenerator<TState>[]): MoveGenerator<TState> {
  // 30% random (exploration)
  if (Math.random() < 0.3) {
    return random(generators);
  }

  // 70% weighted by success rate (exploitation)
  const weights = generators.map(gen =>
    this.operatorStats[gen.name].successRate || 0.5
  );

  return weightedRandom(generators, weights);
}
```

This means operators that frequently lead to improvements get selected more often.

---

## Code Suggestions and Improvements

### 1. **Performance: Deep Cloning is Expensive**

**Issue**: `JSON.parse(JSON.stringify(state))` is very slow for large states.

**Current approach** (optimized in example):
```typescript
cloneState: (state) => ({
  ...state,
  schedule: state.schedule.map(e => ({ ...e }))
})
```

**Suggestion**: Consider using a more efficient cloning library:

```typescript
import { cloneDeep } from 'lodash-es';

cloneState: (state) => cloneDeep(state)
```

Or implement a custom clone method for your state type:
```typescript
cloneState: (state) => ({
  ...state,
  schedule: state.schedule.map(entry => ({
    ...entry,
    timeSlot: { ...entry.timeSlot }
  }))
})
```

### 2. **Memory: Reuse State Objects**

**Issue**: Creates many intermediate state objects during neighbor generation.

**Suggestion**: Implement object pooling for states:
```typescript
class StatePool<TState> {
  private pool: TState[] = [];

  get(): TState {
    return this.pool.pop() ?? this.createFresh();
  }

  release(state: TState): void {
    this.pool.push(state);
  }
}
```

### 3. **Caching: Cache Constraint Evaluations**

**Issue**: Constraints are re-evaluated multiple times for the same state.

**Suggestion**: Implement memoization:
```typescript
class MemoizedConstraint<TState> implements Constraint<TState> {
  private cache = new Map<string, { score: number; violations: string[] }>();

  evaluate(state: TState): number {
    const key = this.getStateKey(state);
    if (this.cache.has(key)) {
      return this.cache.get(key)!.score;
    }

    const score = this.wrappedConstraint.evaluate(state);
    this.cache.set(key, { score, violations: [] });
    return score;
  }

  private getStateKey(state: TState): string {
    // Create a hash of the state
    return JSON.stringify(state.schedule);
  }
}
```

### 4. **Algorithm: Implement Tabu Search**

**Suggestion**: Add Tabu list to avoid cycling:
```typescript
private tabuList: string[] = [];
private tabuTenure: number = 100; // Move stays in tabu for 100 iterations

private isTabu(state: TState): boolean {
  const key = this.getStateKey(state);
  return this.tabuList.includes(key);
}

private updateTabuList(state: TState, iteration: number): void {
  const key = this.getStateKey(state);
  this.tabuList.push(key);

  // Remove old tabus
  this.tabuList = this.tabuList.filter((_, i) =>
    iteration - i < this.tabuTenure
  );
}
```

### 5. **Type Safety: Improve Type Guards**

**Issue**: `constraint.getViolations` is optional and checked at runtime.

**Suggestion**: Use type predicates:
```typescript
interface Constraint<TState> {
  // ... other properties
  getViolations?(state: TState): string[];
}

// Type guard
function hasGetViolations<TState>(
  constraint: Constraint<TState>
): constraint is Constraint<TState> & { getViolations(state: TState): string[] } {
  return 'getViolations' in constraint && typeof constraint.getViolations === 'function';
}

// Usage
if (hasGetViolations(constraint)) {
  const violations = constraint.getViolations(state); // TypeScript knows this exists
}
```

### 6. **Config: Add Early Termination**

**Suggestion**: Stop early if optimal solution found:
```typescript
interface SAConfig<TState> {
  // ... existing config
  targetFitness?: number; // Stop if fitness <= this value
  targetHardViolations?: number; // Stop if hard violations <= this value
}

// In solve() method:
if (this.config.targetFitness && currentFitness <= this.config.targetFitness) {
  this.log('info', 'Target fitness reached, terminating early');
  break;
}

if (this.config.targetHardViolations && currentHardViolations <= this.config.targetHardViolations) {
  this.log('info', 'Target hard violations reached, terminating early');
  break;
}
```

### 7. **Move Generators: Implement Temperature-Dependent Moves**

**Issue**: Current move generators don't use temperature parameter effectively.

**Suggestion**: Make moves more radical at high temperatures:
```typescript
generate(state: TimetableState, temperature: number): TimetableState {
  const newState = this.cloneState(state);

  // High temperature: random big changes
  // Low temperature: local refinements
  const moveIntensity = this.calculateMoveIntensity(temperature);

  if (temperature > 1000) {
    // Exploration mode: completely random time slot
    entry.timeSlot = this.pickRandomSlot(newState.availableTimeSlots);
  } else if (temperature > 100) {
    // Moderate: prefer same day, different time
    entry.timeSlot = this.pickSameDayDifferentTime(entry);
  } else {
    // Exploitation: nearby time slot
    entry.timeSlot = this.pickNearbyTimeSlot(entry, 1);
  }

  return newState;
}
```

### 8. **Logging: Add Progress Callbacks**

**Suggestion**: Allow users to track progress:
```typescript
interface SAConfig<TState> {
  // ... existing config
  onProgress?: (progress: {
    iteration: number;
    phase: number;
    temperature: number;
    fitness: number;
    hardViolations: number;
    bestFitness: number;
  }) => void;
}

// In solve() method:
if (this.config.onProgress && iteration % logInterval === 0) {
  this.config.onProgress({
    iteration,
    phase: phase1Iteration < phase1MaxIterations ? 1 : 2,
    temperature,
    fitness: currentFitness,
    hardViolations: currentHardViolations,
    bestFitness,
  });
}
```

### 9. **Parallelization: Multi-Start SA**

**Suggestion**: Run multiple SA instances in parallel and pick the best:
```typescript
async function parallelSimulatedAnnealing<TState>(
  initialState: TState,
  constraints: Constraint<TState>[],
  moveGenerators: MoveGenerator<TState>[],
  config: SAConfig<TState>,
  numInstances: number = 4
): Promise<Solution<TState>> {
  const instances = Array(numInstances).fill(null).map(() =>
    new SimulatedAnnealing(initialState, constraints, moveGenerators, config)
  );

  const solutions = await Promise.all(
    instances.map(solver => solver.solve())
  );

  return solutions.reduce((best, current) =>
    current.fitness < best.fitness ? current : best
  );
}
```

### 10. **Testing: Add Deterministic Mode**

**Suggestion**: Set seed for reproducible results:
```typescript
interface SAConfig<TState> {
  // ... existing config
  randomSeed?: number;
}

// In constructor:
if (this.config.randomSeed !== undefined) {
  // Use a seeded random number generator
  this.rng = new SeededRandom(this.config.randomSeed);
} else {
  this.rng = Math.random;
}

// Replace all Math.random() calls with this.rng()
```

---

## Example Output

### Console Output Example

```bash
======================================================================
  UNIVERSITY COURSE TIMETABLING - Simulated Annealing v2.0
======================================================================

📂 Loading data from Excel file...
✅ Data loaded successfully!
   Rooms: 25
   Lecturers: 45
   Classes: 180

🏗️  Generating initial timetable (greedy algorithm)...

⚖️  Setting up constraints...
   Hard constraints: 10
   Soft constraints: 8

🔄 Setting up move operators...
   Targeted operators: 6 (including Friday swap operator)
   General operators: 4 (including smart time+room operator)
   Total operators: 10

⚙️  Configuring Simulated Annealing...
   Initial temperature: 100000
   Cooling rate: 0.9998
   Max iterations: 60000

🚀 Starting optimization...

======================================================================
[2024-12-26T19:00:00.000Z] [INFO] Simulated Annealing initialized {"hardConstraints":10,"softConstraints":8,"moveGenerators":10,"config":{"initialTemperature":100000,"minTemperature":1e-7,"coolingRate":0.9998,"maxIterations":60000}}
[2024-12-26T19:00:00.050Z] [INFO] Starting optimization...
[2024-12-26T19:00:00.050Z] [INFO] Phase 1: Eliminating hard constraint violations
[2024-12-26T19:00:00.060Z] [INFO] Initial state {"fitness":"345.67","hardViolations":12}
[2024-12-26T19:00:05.000Z] [INFO] [Phase 1] Iteration 500: Temp = 90479.47, Hard violations = 8, Best = 8
[2024-12-26T19:00:10.000Z] [INFO] [Phase 1] Iteration 1000: Temp = 81915.83, Hard violations = 5, Best = 5
[2024-12-26T19:00:15.000Z] [INFO] [Phase 1] Iteration 1500: Temp = 74247.06, Hard violations = 3, Best = 3
[2024-12-26T19:00:20.000Z] [INFO] [Phase 1] Iteration 2000: Temp = 67322.42, Hard violations = 1, Best = 1
[2024-12-26T19:00:25.000Z] [INFO] [Phase 1] Iteration 2500: Temp = 61095.34, Hard violations = 0, Best = 0
[2024-12-26T19:00:25.100Z] [INFO] Phase 1 complete: Hard violations = 0

[2024-12-26T19:00:25.100Z] [INFO] Phase 2: Optimizing soft constraints
[2024-12-26T19:00:30.000Z] [INFO] [Phase 2] Iteration 35000: Temp = 0.05, Current = 45.32, Best = 42.15
[2024-12-26T19:00:35.000Z] [INFO] [Phase 2] Iteration 40000: Temp = 0.01, Current = 38.67, Best = 35.21
[2024-12-26T19:00:40.000Z] [INFO] [Phase 2] Iteration 45000: Temp = 0.002, Current = 32.45, Best = 28.90
[2024-12-26T19:00:45.000Z] [INFO] [Phase 2] Iteration 50000: Temp = 0.0005, Current = 28.90, Best = 25.67
[2024-12-26T19:00:50.000Z] [INFO] [Phase 2] Iteration 55000: Temp = 0.0001, Current = 25.67, Best = 23.45
[2024-12-26T19:00:55.000Z] [INFO] [Phase 2] Iteration 60000: Temp = 0.00002, Current = 23.45, Best = 21.30

[2024-12-26T19:00:55.050Z] [INFO] Optimization complete {"iterations":60000,"reheats":3,"finalTemperature":"0.000016","fitness":"21.30","hardViolations":0,"softViolations":5}
[2024-12-26T19:00:55.060Z] [INFO] Operator Statistics:
[2024-12-26T19:00:55.060Z] [INFO]   Fix Friday Prayer Conflict: Attempts = 12543, Improvements = 8432, Accepted = 9876, Success Rate = 67.20%
[2024-12-26T19:00:55.060Z] [INFO]   Swap Friday With NonFriday: Attempts = 8765, Improvements = 5432, Accepted = 7654, Success Rate = 61.95%
[2024-12-26T19:00:55.060Z] [INFO]   Fix Lecturer Conflict: Attempts = 15234, Improvements = 9123, Accepted = 11234, Success Rate = 59.89%
[2024-12-26T19:00:55.060Z] [INFO]   Fix Room Conflict: Attempts = 10987, Improvements = 6543, Accepted = 8765, Success Rate = 59.54%
[2024-12-26T19:00:55.060Z] [INFO]   ChangeTimeSlotAndRoom: Attempts = 5432, Improvements = 3210, Accepted = 4321, Success Rate = 59.09%
[2024-12-26T19:00:55.060Z] [INFO]   Change Time Slot: Attempts = 3456, Improvements = 1987, Accepted = 2567, Success Rate = 57.50%
[2024-12-26T19:00:55.060Z] [INFO]   Change Room: Attempts = 2876, Improvements = 1598, Accepted = 2098, Success Rate = 55.56%
[2024-12-26T19:00:55.060Z] [INFO]   Swap Classes: Attempts = 1987, Improvements = 1098, Accepted = 1456, Success Rate = 55.26%
[2024-12-26T19:00:55.060Z] [INFO]   FixMaxDailyPeriods: Attempts = 2134, Improvements = 1176, Accepted = 1565, Success Rate = 55.11%
[2024-12-26T19:00:55.060Z] [INFO]   FixRoomCapacity: Attempts = 1234, Improvements = 654, Accepted = 876, Success Rate = 53.00%

======================================================================

✨ OPTIMIZATION COMPLETE!

Cache stats: {"hits":152345,"misses":23456,"hitRate":86.67%}

📊 RESULTS:
   Final fitness: 21.30
   Hard constraint violations: 0
   Soft constraint violations: 5
   Total iterations: 60000
   Reheating events: 3
   Final temperature: 0.000016
   Classes scheduled: 180/180

📈 OPERATOR STATISTICS:
   Fix Friday Prayer Conflict:
      Attempts: 12543
      Improvements: 8432
      Success rate: 67.20%
   Swap Friday With NonFriday:
      Attempts: 8765
      Improvements: 5432
      Success rate: 61.95%
   Fix Lecturer Conflict:
      Attempts: 15234
      Improvements: 9123
      Success rate: 59.89%
   Fix Room Conflict:
      Attempts: 10987
      Improvements: 6543
      Success rate: 59.54%
   ChangeTimeSlotAndRoom:
      Attempts: 5432
      Improvements: 3210
      Success rate: 59.09%
   Change Time Slot:
      Attempts: 3456
      Improvements: 1987
      Success rate: 57.50%
   Change Room:
      Attempts: 2876
      Improvements: 1598
      Success rate: 55.56%
   Swap Classes:
      Attempts: 1987
      Improvements: 1098
      Success rate: 55.26%
   FixMaxDailyPeriods:
      Attempts: 2134
      Improvements: 1176
      Success rate: 55.11%
   FixRoomCapacity:
      Attempts: 1234
      Improvements: 654
      Success rate: 53.00%

⚠️  VIOLATIONS (5):
   - [soft] Preferred Time: Prof. Smith prefers morning classes, but scheduled at 14:00
   - [soft] Preferred Room: CS101 preferred room LAB-1, but assigned to LAB-2
   - [soft] Transit Time: Only 15 minutes between classes, needs 30 minutes
   - [soft] Compactness: 3 gaps in Monday schedule
   - [soft] Research Day: Prof. Johnson has classes on research day (Wednesday)

======================================================================
✅ Example completed successfully!
======================================================================

💾 Results saved to: timetable-result.json
```

### Solution Object Structure (JSON)

```json
{
  "fitness": 21.30,
  "hardViolations": 0,
  "softViolations": 5,
  "iterations": 60000,
  "reheats": 3,
  "finalTemperature": 0.000016,
  "schedule": [
    {
      "classId": "CS101",
      "className": "Introduction to Computer Science",
      "class": "A",
      "prodi": "Computer Science",
      "lecturers": ["PROF001"],
      "room": "LAB-1",
      "timeSlot": {
        "day": "Monday",
        "startTime": "08:00",
        "endTime": "10:00",
        "period": 1
      },
      "sks": 3,
      "needsLab": true,
      "participants": 45,
      "classType": "pagi",
      "prayerTimeAdded": 0
    },
    {
      "classId": "CS102",
      "className": "Data Structures",
      "class": "A",
      "prodi": "Computer Science",
      "lecturers": ["PROF002"],
      "room": "LAB-2",
      "timeSlot": {
        "day": "Monday",
        "startTime": "10:00",
        "endTime": "12:00",
        "period": 2
      },
      "sks": 3,
      "needsLab": true,
      "participants": 40,
      "classType": "pagi",
      "prayerTimeAdded": 15
    }
    // ... more classes
  ],
  "violation": [
    {
      "constraintName": "Preferred Time",
      "constraintType": "soft",
      "score": 0.7,
      "description": "Prof. Smith prefers morning classes, but scheduled at 14:00"
    },
    {
      "constraintName": "Preferred Room",
      "constraintType": "soft",
      "score": 0.8,
      "description": "CS101 preferred room LAB-1, but assigned to LAB-2"
    }
    // ... more violations
  ]
}
```

---

## Best Practices

### 1. **Configuring Temperature**

```typescript
// Too low: Gets stuck in local minima
const badConfig = {
  initialTemperature: 10,
  coolingRate: 0.95
};

// Too high: Wastes iterations
const alsoBad = {
  initialTemperature: 10000000,
  coolingRate: 0.99999
};

// Good: Balanced exploration and exploitation
const goodConfig = {
  initialTemperature: 100000,
  coolingRate: 0.9998,
  maxIterations: 60000
};
```

### 2. **Designing Constraints**

```typescript
// ❌ Bad: Binary hard constraint
evaluate(state: TimetableState): number {
  return this.hasAnyConflict(state) ? 0 : 1;
}

// ✅ Good: Granular scoring with getViolations()
evaluate(state: TimetableState): number {
  const violations = this.countConflicts(state);
  return 1 / (1 + violations);
}

getViolations(state: TimetableState): string[] {
  return this.findAllConflicts(state).map(c =>
    `Room ${c.room}: ${c.class1} vs ${c.class2}`
  );
}
```

### 3. **Creating Move Operators**

```typescript
// ❌ Bad: Doesn't clone state
generate(state: TimetableState): TimetableState {
  const entry = state.schedule[0];
  entry.timeSlot = newSlot; // MUTATES INPUT!
  return state;
}

// ✅ Good: Clones properly
generate(state: TimetableState): TimetableState {
  const newState = {
    ...state,
    schedule: state.schedule.map(e => ({ ...e, timeSlot: { ...e.timeSlot } }))
  };
  newState.schedule[0].timeSlot = newSlot; // Safe
  return newState;
}
```

### 4. **Balancing Move Operators**

```typescript
// Mix of targeted and general operators
const moves: MoveGenerator<TState>[] = [
  // Targeted: Fix specific problems
  new FixLecturerConflict(),
  new FixRoomConflict(),

  // General: Explore solution space
  new ChangeTimeSlot(),
  new ChangeRoom(),
  new SwapClasses(),

  // Advanced: Multiple changes
  new ChangeTimeSlotAndRoom(),
];
```

### 5. **Setting Weights**

```typescript
const constraints: Constraint<TState>[] = [
  // Hard constraints: Always must be satisfied
  new NoLecturerConflict(),     // type = 'hard'
  new NoRoomConflict(),          // type = 'hard'

  // Soft constraints: Prioritize by importance
  new Compactness(15),           // Very important
  new PrayerTimeOverlap(20),     // Very important
  new PreferredTime(10),         // Important
  new PreferredRoom(10),         // Important
  new TransitTime(5),            // Less important
  new ResearchDay(10),           // Moderate importance
];
```

### 6. **Performance Tuning**

```typescript
// Use efficient cloning
cloneState: (state) => ({
  ...state,
  schedule: state.schedule.map(e => ({ ...e }))
})

// Use caching in constraints
class CachedConstraint implements Constraint<TState> {
  private cache = new Map<string, number>();

  evaluate(state: TState): number {
    const key = this.hash(state);
    if (this.cache.has(key)) {
      return this.cache.get(key)!;
    }
    const score = this.evaluateImpl(state);
    this.cache.set(key, score);
    return score;
  }
}

// Tune logging for production
const config = {
  logging: {
    enabled: true,
    level: 'info',      // Not 'debug' in production
    logInterval: 1000,   // Log less frequently
  }
};
```

---

## Summary

**timetable-sa** is a well-designed, flexible optimization library that:

✅ Separates concerns (state, constraints, moves, algorithm)
✅ Uses a proven optimization algorithm (Simulated Annealing)
✅ Implements two-phase optimization (hard → soft)
✅ Provides adaptive operator selection
✅ Supports reheating to escape local minima
✅ Is fully type-safe with TypeScript
✅ Includes comprehensive logging and statistics

**Key strengths:**
- Generic and reusable across domains
- Well-structured code with clear interfaces
- Smart operator statistics for learning
- Flexible configuration options

**Areas for improvement:**
- Performance (cloning, caching)
- Advanced features (Tabu search, parallelization)
- Testing utilities (deterministic mode, progress callbacks)
- Type safety improvements (type guards)

This is an excellent foundation for building constraint satisfaction optimizers!
