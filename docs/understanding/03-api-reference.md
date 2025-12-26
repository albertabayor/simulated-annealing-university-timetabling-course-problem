# API Reference Lengkap Timetable-SA

## 1. Core Classes

### 1.1 SimulatedAnnealing<TState>

Kelas utama yang mengimplementasikan algoritma optimasi Simulated Annealing.

#### Constructor

```typescript
constructor(
  initialState: TState,
  constraints: Constraint<TState>[],
  moveGenerators: MoveGenerator<TState>[],
  config: SAConfig<TState>
)
```

**Parameters:**
- `initialState`: State awal untuk optimasi
- `constraints`: Array dari constraint objects
- `moveGenerators`: Array dari move generator objects
- `config`: Konfigurasi algoritma

#### Methods

##### solve(): Solution<TState>

Menjalankan algoritma optimasi dan mengembalikan solusi terbaik.

```typescript
const solution = solver.solve();
```

**Returns:** `Solution<TState>` - Solusi optimal dengan statistik lengkap

##### getStats(): OperatorStats

Mengembalikan statistik performa operator yang telah digunakan.

```typescript
const stats = solver.getStats();
```

**Returns:** `OperatorStats` - Statistik detail untuk setiap operator

---

## 2. Interface Definitions

### 2.1 Constraint<TState>

Interface untuk mendefinisikan constraint dalam optimasi.

```typescript
interface Constraint<TState> {
  name: string;
  type: 'hard' | 'soft';
  weight?: number;
  evaluate(state: TState): number;
  describe?(state: TState): string | undefined;
  getViolations?(state: TState): string[];
}
```

#### Properties

- **name** (`string`): Nama unik untuk constraint (digunakan dalam logging)
- **type** (`'hard' | 'soft'`): Tipe constraint
- **weight** (`number`, optional): Weight untuk soft constraints (default: 10)

#### Methods

##### evaluate(state: TState): number

Mengevaluasi constraint untuk state tertentu.

**Parameters:**
- `state`: State yang akan dievaluasi

**Returns:** `number` - Score antara 0 dan 1:
- `1.0` = Fully satisfied (no violation)
- `0.0` = Completely violated
- `0.0-1.0` = Partially satisfied (untuk soft constraints)

**Example:**
```typescript
evaluate(state: TimetableState): number {
  const conflicts = this.findConflicts(state);
  return conflicts.length === 0 ? 1 : 1 / (1 + conflicts.length);
}
```

##### describe?(state: TState): string | undefined

Optional: Memberikan deskripsi human-readable dari violation.

**Parameters:**
- `state`: State yang akan diperiksa

**Returns:** `string | undefined` - Deskripsi violation atau undefined jika tidak ada violation

**Example:**
```typescript
describe(state: TimetableState): string | undefined {
  const conflict = this.findFirstConflict(state);
  return conflict ? 
    `Room ${conflict.room} has overlapping classes: ${conflict.class1} and ${conflict.class2}` : 
    undefined;
}
```

##### getViolations?(state: TState): string[]

Optional: Mengembalikan array semua violations untuk constraint ini.

**Parameters:**
- `state`: State yang akan diperiksa

**Returns:** `string[]` - Array deskripsi violations, kosong jika tidak ada violation

**Example:**
```typescript
getViolations(state: TimetableState): string[] {
  const violations: string[] = [];
  for (const conflict of this.findAllConflicts(state)) {
    violations.push(`Room ${conflict.room} conflict: ${conflict.class1} vs ${conflict.class2}`);
  }
  return violations;
}
```

---

### 2.2 MoveGenerator<TState>

Interface untuk mendefinisikan move operators dalam optimasi.

```typescript
interface MoveGenerator<TState> {
  name: string;
  generate(state: TState, temperature: number): TState;
  canApply(state: TState): boolean;
}
```

#### Properties

- **name** (`string`): Nama unik untuk move operator

#### Methods

##### generate(state: TState, temperature: number): TState

Menghasilkan neighbor state baru dari state saat ini.

**Parameters:**
- `state`: State saat ini (JANGAN dimodifikasi langsung)
- `temperature`: Temperature saat ini untuk menyesuaikan move intensity

**Returns:** `TState` - State baru dengan modifications applied

**Important Notes:**
- **JANGAN** memodifikasi input `state`. Selalu clone state terlebih dahulu
- Gunakan `temperature` untuk menyesuaikan move size:
  - High temp: Large, random moves
  - Low temp: Small, focused moves

**Example:**
```typescript
generate(state: TimetableState, temperature: number): TimetableState {
  // Clone state untuk menghindari modifikasi input
  const newState = JSON.parse(JSON.stringify(state));
  
  // Temperature-dependent move selection
  const moveSize = temperature > 100 ? 'large' : 'small';
  
  // Apply modification
  this.applyMove(newState, moveSize);
  
  return newState;
}
```

##### canApply(state: TState): boolean

Memeriksa apakah move operator dapat diterapkan pada state saat ini.

**Parameters:**
- `state`: State yang akan diperiksa

**Returns:** `boolean` - `true` jika move dapat diterapkan, `false` jika tidak

**Example:**
```typescript
canApply(state: TimetableState): boolean {
  // Tidak bisa swap jika kurang dari 2 kelas
  return state.schedule.length >= 2;
}
```

---

### 2.3 SAConfig<TState>

Interface untuk konfigurasi algoritma Simulated Annealing.

```typescript
interface SAConfig<TState> {
  initialTemperature: number;
  minTemperature: number;
  coolingRate: number;
  maxIterations: number;
  hardConstraintWeight: number;
  cloneState: (state: TState) => TState;
  reheatingThreshold?: number;
  reheatingFactor?: number;
  maxReheats?: number;
  logging?: LoggingConfig;
}
```

#### Required Properties

##### initialTemperature: number

Temperature awal untuk proses annealing.

- **Range**: 100 - 10000
- **Default**: 1000
- **Guidelines**:
  - Terlalu tinggi → Wasted iterations pada random exploration
  - Terlalu rendah → Stuck di local minima

##### minTemperature: number

Temperature minimum (stopping criterion).

- **Range**: 0.001 - 1
- **Default**: 0.01

##### coolingRate: number

Cooling rate (temperature decay factor).

- **Range**: 0.95 - 0.999
- **Default**: 0.995
- **Formula**: `T = T * coolingRate` setiap iterasi
- **Guidelines**:
  - Higher (0.999): Slower cooling, better results
  - Lower (0.95): Faster cooling, may miss optimum

##### maxIterations: number

Maximum jumlah iterasi (stopping criterion).

- **Range**: 10000 - 100000
- **Default**: 50000

##### hardConstraintWeight: number

Penalty weight untuk hard constraint violations.

- **Range**: 1000 - 100000
- **Default**: 10000
- **Purpose**: Memastikan hard constraints diprioritaskan

##### cloneState: (state: TState) => TState

Function untuk cloning state (deep copy).

**Example Implementations:**
```typescript
// Simple JSON-based cloning
cloneState: (state) => JSON.parse(JSON.stringify(state))

// Custom cloning untuk performance
cloneState: (state) => ({
  ...state,
  schedule: state.schedule.map(entry => ({ ...entry }))
})
```

#### Optional Properties

##### reheatingThreshold?: number

Jumlah iterasi tanpa improvement sebelum reheating.

- **Range**: 1000 - 5000
- **Default**: undefined (no reheating)
- **Purpose**: Escape dari local minima

##### reheatingFactor?: number

Factor untuk meningkatkan temperature saat reheating.

- **Range**: 1.5 - 3.0
- **Default**: 2.0
- **Formula**: `T = T * reheatingFactor`

##### maxReheats?: number

Maximum jumlah reheating events.

- **Default**: 3
- **Purpose**: Mencegah infinite reheating loops

##### logging?: LoggingConfig

Konfigurasi logging (lihat LoggingConfig interface).

---

### 2.4 LoggingConfig

Interface untuk konfigurasi logging.

```typescript
interface LoggingConfig {
  enabled?: boolean;
  level?: 'debug' | 'info' | 'warn' | 'error' | 'none';
  logInterval?: number;
  output?: 'console' | 'file' | 'both';
  filePath?: string;
}
```

#### Properties

- **enabled** (`boolean`, default: `true`): Enable/disable logging
- **level** (`string`, default: `'info'`): Logging level
- **logInterval** (`number`, default: `1000`): Log progress setiap N iterasi
- **output** (`string`, default: `'console'`): Output destination
- **filePath** (`string`, default: `'./sa-optimization.log'`): File path untuk file logging

---

## 3. Type Definitions

### 3.1 Solution<TState>

Interface untuk solusi yang dikembalikan oleh algoritma.

```typescript
interface Solution<TState> {
  state: TState;
  fitness: number;
  hardViolations: number;
  softViolations: number;
  iterations: number;
  reheats: number;
  finalTemperature: number;
  violations: Violation[];
  operatorStats: OperatorStats;
}
```

#### Properties

- **state** (`TState`): State terbaik yang ditemukan
- **fitness** (`number`): Final fitness score (lower is better)
- **hardViolations** (`number`): Jumlah hard constraint violations
- **softViolations** (`number`): Jumlah soft constraint violations
- **iterations** (`number`): Total iterasi yang dilakukan
- **reheats** (`number`): Jumlah reheating events
- **finalTemperature** (`number`): Temperature akhir
- **violations** (`Violation[]`): Detail semua violations
- **operatorStats** (`OperatorStats`): Statistik operator performance

---

### 3.2 Violation

Interface untuk representasi constraint violation.

```typescript
interface Violation {
  constraintName: string;
  constraintType: 'hard' | 'soft';
  score: number;
  description?: string;
}
```

#### Properties

- **constraintName** (`string`): Nama constraint yang dilanggar
- **constraintType** (`'hard' | 'soft'`): Tipe constraint
- **score** (`number`): Severity score (0 = completely violated, 1 = satisfied)
- **description** (`string`, optional): Deskripsi human-readable violation

---

### 3.3 OperatorStats

Interface untuk statistik performa operator.

```typescript
interface OperatorStats {
  [operatorName: string]: {
    attempts: number;
    improvements: number;
    accepted: number;
    successRate: number;
  };
}
```

#### Properties

- **attempts** (`number`): Jumlah kali operator dicoba
- **improvements** (`number`): Jumlah kali operator menghasilkan improvement
- **accepted** (`number`): Jumlah kali operator diterima (termasuk worse moves)
- **successRate** (`number`): Success rate (improvements / attempts)

---

## 4. Usage Examples

### 4.1 Basic Usage

```typescript
import { SimulatedAnnealing } from 'timetable-sa';

// Define constraints
const constraints = [
  new NoRoomConflict(),
  new PreferredTime(10),
  // ... other constraints
];

// Define move generators
const moveGenerators = [
  new ChangeTimeSlot(),
  new SwapClasses(),
  // ... other moves
];

// Configure algorithm
const config = {
  initialTemperature: 1000,
  minTemperature: 0.01,
  coolingRate: 0.995,
  maxIterations: 50000,
  hardConstraintWeight: 10000,
  cloneState: (state) => JSON.parse(JSON.stringify(state)),
};

// Create solver and run optimization
const solver = new SimulatedAnnealing(
  initialState,
  constraints,
  moveGenerators,
  config
);

const solution = solver.solve();
console.log('Fitness:', solution.fitness);
console.log('Hard violations:', solution.hardViolations);
```

### 4.2 Advanced Configuration

```typescript
const advancedConfig = {
  initialTemperature: 100000,
  minTemperature: 0.0000001,
  coolingRate: 0.9998,
  maxIterations: 100000,
  hardConstraintWeight: 100000,
  
  // Custom cloning for performance
  cloneState: (state) => ({
    ...state,
    schedule: state.schedule.map(entry => ({ ...entry })),
    availableTimeSlots: [...state.availableTimeSlots],
  }),
  
  // Reheating configuration
  reheatingThreshold: 500,
  reheatingFactor: 1.5,
  maxReheats: 10,
  
  // Logging configuration
  logging: {
    enabled: true,
    level: 'debug',
    logInterval: 500,
    output: 'both',
    filePath: './optimization.log',
  },
};
```

### 4.3 Custom Constraint Implementation

```typescript
class CustomConstraint implements Constraint<TimetableState> {
  name = 'Custom Constraint';
  type = 'hard' as const;
  
  evaluate(state: TimetableState): number {
    // Custom evaluation logic
    const violations = this.findViolations(state);
    return violations.length === 0 ? 1 : 1 / (1 + violations.length);
  }
  
  getViolations(state: TimetableState): string[] {
    const violations: string[] = [];
    for (const violation of this.findViolations(state)) {
      violations.push(`Custom violation: ${violation.description}`);
    }
    return violations;
  }
  
  private findViolations(state: TimetableState): any[] {
    // Implementation to find violations
    return [];
  }
}
```

### 4.4 Custom Move Generator Implementation

```typescript
class CustomMove implements MoveGenerator<TimetableState> {
  name = 'Custom Move';
  
  canApply(state: TimetableState): boolean {
    return state.schedule.length > 0;
  }
  
  generate(state: TimetableState, temperature: number): TimetableState {
    // Clone state
    const newState = JSON.parse(JSON.stringify(state));
    
    // Temperature-dependent move size
    const moveIntensity = temperature > 100 ? 'large' : 'small';
    
    // Apply custom move logic
    this.applyCustomMove(newState, moveIntensity);
    
    return newState;
  }
  
  private applyCustomMove(state: TimetableState, intensity: string): void {
    // Implementation of custom move logic
  }
}
```

## 5. Error Handling

### 5.1 Common Errors

1. **Invalid Temperature Values**
   ```typescript
   // Wrong
   initialTemperature: -100;  // Negative
   coolingRate: 1.5;          // > 1
   
   // Correct
   initialTemperature: 1000;
   coolingRate: 0.995;
   ```

2. **Missing Required Properties**
   ```typescript
   // Wrong - missing cloneState
   const config = {
     initialTemperature: 1000,
     // cloneState missing
   };
   
   // Correct
   const config = {
     initialTemperature: 1000,
     cloneState: (state) => JSON.parse(JSON.stringify(state)),
   };
   ```

3. **State Mutation**
   ```typescript
   // Wrong - modifying input state
   generate(state: TState, temperature: number): TState {
     state.schedule[0].room = 'new-room';  // Don't do this!
     return state;
   }
   
   // Correct - clone first
   generate(state: TState, temperature: number): TState {
     const newState = JSON.parse(JSON.stringify(state));
     newState.schedule[0].room = 'new-room';
     return newState;
   }
   ```

### 5.2 Debugging Tips

1. **Enable Debug Logging**
   ```typescript
   const config = {
     logging: {
       enabled: true,
       level: 'debug',
       logInterval: 100,
     },
   };
   ```

2. **Check Violations**
   ```typescript
   const solution = solver.solve();
   console.log('Violations:', solution.violations);
   
   // Check specific constraint violations
   const roomViolations = solution.violations.filter(
     v => v.constraintName === 'No Room Conflict'
   );
   ```

3. **Monitor Operator Performance**
   ```typescript
   const stats = solution.operatorStats;
   for (const [name, stat] of Object.entries(stats)) {
     console.log(`${name}: ${stat.successRate}% success rate`);
   }
   ```

## 6. Performance Optimization

### 6.1 Efficient State Cloning

```typescript
// Slow but simple
cloneState: (state) => JSON.parse(JSON.stringify(state))

// Fast but requires manual implementation
cloneState: (state) => ({
  ...state,
  schedule: state.schedule.map(entry => ({ ...entry })),
  // Only clone what's necessary
})
```

### 6.2 Smart Move Selection

```typescript
class SmartMove implements MoveGenerator<TState> {
  generate(state: TState, temperature: number): TState {
    // Use temperature to adjust move intensity
    const moveSize = this.calculateMoveSize(temperature);
    
    // Apply targeted moves for high temperature
    // Apply refined moves for low temperature
    return this.applyMove(state, moveSize);
  }
  
  private calculateMoveSize(temperature: number): string {
    if (temperature > 1000) return 'large';
    if (temperature > 100) return 'medium';
    return 'small';
  }
}
```

### 6.3 Constraint Optimization

```typescript
class OptimizedConstraint implements Constraint<TState> {
  private cache = new Map<string, number>();
  
  evaluate(state: TState): number {
    // Use caching for expensive computations
    const stateHash = this.hashState(state);
    
    if (this.cache.has(stateHash)) {
      return this.cache.get(stateHash)!;
    }
    
    const result = this.expensiveEvaluation(state);
    this.cache.set(stateHash, result);
    return result;
  }
}