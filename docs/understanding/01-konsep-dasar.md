# Konsep Dasar Timetable-SA

## 1. Pengenalan

Timetable-SA adalah library optimasi generik yang menggunakan algoritma **Simulated Annealing** untuk menyelesaikan masalah *constraint satisfaction* seperti penjadwalan, alokasi sumber daya, dan masalah optimasi lainnya.

### 1.1 Apa itu Simulated Annealing?

Simulated Annealing adalah algoritma optimasi metaheuristik yang terinspirasi dari proses annealing dalam metalurgi. Dalam metalurgi, annealing adalah proses pemanasan dan pendinginan bertahap material untuk mengurangi defects dan mencapai struktur kristal yang optimal.

Dalam konteks optimasi:
- **Temperature** mewakili tingkat "randomness" dalam pencarian solusi
- **High temperature** → Eksplorasi luas (menerima solusi yang lebih buruk)
- **Low temperature** → Refinemen lokal (hanya menerima solusi yang lebih baik)
- **Cooling schedule** → Penurunan bertahap temperature

### 1.2 Mengapa Simulated Annealing untuk Penjadwalan?

Penjadwalan adalah masalah **NP-hard** yang memiliki karakteristik:
- **Large search space**: Banyak kemungkinan kombinasi
- **Multiple constraints**: Berbagai aturan yang harus dipenuhi
- **Local minima**: Banyak solusi "cukup baik" yang sulit ditinggalkan
- **Complex interactions**: Perubahan satu elemen mempengaruhi banyak yang lain

Simulated Annealing cocok karena:
- ✅ **Escapes local minima** melalui probabilistic acceptance
- ✅ **Handles complex constraints** dengan flexible evaluation
- ✅ **Balances exploration vs exploitation** melalui temperature control
- ✅ **Adaptable** untuk berbagai jenis masalah optimasi

## 2. Arsitektur High-Level

### 2.1 Komponen Utama

```
┌─────────────────────────────────────────────────────────────┐
│                    TIMETABLE-SA CORE                        │
├─────────────────────────────────────────────────────────────┤
│  ┌─────────────────┐  ┌─────────────────┐  ┌──────────────┐ │
│  │ SimulatedAnnealing│  │   Constraint   │  │ MoveGenerator│ │
│  │     Algorithm    │  │   Interface    │  │  Interface   │ │
│  └─────────────────┘  └─────────────────┘  └──────────────┘ │
├─────────────────────────────────────────────────────────────┤
│  ┌─────────────────┐  ┌─────────────────┐  ┌──────────────┐ │
│  │   SAConfig      │  │    Solution     │  │   Violation  │ │
│  │   Interface     │  │     Type        │  │     Type     │ │
│  └─────────────────┘  └─────────────────┘  └──────────────┘ │
└─────────────────────────────────────────────────────────────┘
```

### 2.2 Flow Sistem

1. **Input Definition**
   - State awal (solusi awal)
   - Constraints (aturan yang harus dipenuhi)
   - Move generators (cara memodifikasi solusi)
   - Configuration (parameter algoritma)

2. **Optimization Process**
   - Generate neighbor solutions
   - Evaluate constraint satisfaction
   - Accept/reject based on probability
   - Update best solution found

3. **Output Generation**
   - Optimal solution
   - Performance statistics
   - Violation reports
   - Execution metrics

## 3. Konsep Fundamental

### 3.1 State Representation

State adalah representasi lengkap dari solusi saat ini. Untuk penjadwalan, state mencakup:

```typescript
interface TimetableState {
  schedule: ScheduleEntry[];      // Jadwal saat ini
  availableTimeSlots: TimeSlot[]; // Slot waktu tersedia
  rooms: Room[];                  // Ruangan tersedia
  lecturers: Lecturer[];          // Dosen tersedia
}
```

**Prinsip Penting:**
- State harus **immutable** - tidak dimodifikasi langsung
- Setiap perubahan menghasilkan **new state**
- State cloning harus **efficient** untuk performance

### 3.2 Constraint System

Constraints adalah aturan yang mengevaluasi kualitas solusi.

#### Jenis Constraints:

**Hard Constraints** (WAJIB dipenuhi):
- Tidak ada konflik ruangan
- Kapasitas ruangan mencukupi
- Tidak ada konflik dosen
- Waktu sholat Jumat

**Soft Constraints** (preferensi):
- Waktu preferensi dosen
- Ruangan preferensi
- Kompaknya jadwal
- Waktu transit antar kelas

#### Scoring System:
```typescript
// Hard constraint: Binary scoring
score = hasViolation ? 0 : 1;

// Soft constraint: Gradual scoring
score = Math.max(0, 1 - (violationCount / maxPossibleViolations));
```

### 3.3 Move Generators

Move generators mendefinisikan bagaimana algoritma mengeksplorasi ruang solusi.

#### Jenis Moves:

**Local Moves**:
- Change time slot satu kelas
- Change room satu kelas
- Modify property tunggal

**Swap Moves**:
- Tukar waktu dua kelas
- Tukar ruangan dua kelas
- Tukar dosen dua kelas

**Targeted Moves**:
- Fix specific violation
- Resolve conflict
- Improve particular aspect

#### Temperature-Dependent Moves:
```typescript
generate(state: TState, temperature: number): TState {
  if (temperature > 1000) {
    // High temp: Large, random moves
    return this.makeLargeMove(state);
  } else {
    // Low temp: Small, focused moves
    return this.makeSmallMove(state);
  }
}
```

## 4. Algoritma Dua Fase

Timetable-SA mengimplementasikan algoritma **dua fase** yang unik:

### 4.1 Fase 1: Eliminasi Hard Constraints (60% iterasi)

**Tujuan**: Menghilangkan semua pelanggaran hard constraints

**Strategi**:
- Fokus pada penyelesaian konflik fundamental
- Prioritaskan pengurangan hard violations
- Gunakan targeted operators untuk specific violations

**Acceptance Criteria**:
```typescript
if (newHardViolations < currentHardViolations) {
  return 1.0; // Always accept
} else if (newHardViolations === currentHardViolations) {
  return standardAcceptanceProbability();
} else {
  return 0.0; // Never accept worse hard violations
}
```

### 4.2 Fase 2: Optimasi Soft Constraints (40% iterasi)

**Tujuan**: Mengoptimalkan preferensi sambil mempertahankan hard constraints

**Strategi**:
- Maintain hard constraint satisfaction
- Optimize soft constraint violations
- Balance competing preferences

**Acceptance Criteria**:
```typescript
if (newHardViolations > bestHardViolations) {
  return 0.0; // NEVER accept hard violations
} else if (newHardViolations < bestHardViolations) {
  return 1.0; // Always accept improvement
} else {
  return standardAcceptanceProbability();
}
```

## 5. Adaptive Operator Selection

Algoritma menggunakan **adaptive operator selection** untuk meningkatkan efektivitas:

### 5.1 Selection Strategy

```typescript
// 30% random selection (exploration)
if (Math.random() < 0.3) {
  return randomOperator();
}

// 70% weighted selection (exploitation)
return selectBySuccessRate();
```

### 5.2 Success Rate Tracking

Setiap operator melacak:
- **Attempts**: Jumlah kali dicoba
- **Improvements**: Jumlah kali menghasilkan improvement
- **Success Rate**: improvements / attempts

### 5.3 Weighted Selection

```typescript
const weights = operators.map(op => op.successRate || 0.5);
const totalWeight = weights.reduce((sum, w) => sum + w, 0);

// Weighted random selection
let random = Math.random() * totalWeight;
for (let i = 0; i < operators.length; i++) {
  random -= weights[i];
  if (random <= 0) return operators[i];
}
```

## 6. Reheating Mechanism

Untuk menghindari terjebak di local minima:

### 6.1 Detection

Monitor iterasi tanpa improvement:
```typescript
if (iterationsWithoutImprovement >= reheatingThreshold) {
  triggerReheating();
}
```

### 6.2 Reheating Process

```typescript
// Increase temperature
temperature *= reheatingFactor;

// Reset counters
iterationsWithoutImprovement = 0;
reheats++;
```

### 6.3 Limits

- Maximum reheating events
- Minimum temperature threshold
- Maximum total iterations

## 7. Fitness Calculation

### 7.1 Formula

```typescript
Fitness = (HardViolations × HardConstraintWeight) + SoftPenalty

Dimana:
HardViolations = Σ(1 - score) untuk setiap hard constraint
SoftPenalty = Σ((1 - score) × weight) untuk setiap soft constraint
```

### 7.2 Weight Strategy

- **Hard Constraint Weight**: 1000-100000 (sangat tinggi)
- **Soft Constraint Weights**: 1-100 (sesuai importance)
- **Weight Ratio**: Hard weight >> Soft weight total

### 7.3 Optimization Goals

1. **Primary**: Minimize hard violations (target: 0)
2. **Secondary**: Minimize soft violations
3. **Tertiary**: Balance competing preferences

## 8. Performance Considerations

### 8.1 Computational Complexity

- **Time**: O(iterations × constraints × moves)
- **Space**: O(state size + constraint data)
- **Bottlenecks**: State cloning, constraint evaluation

### 8.2 Optimization Strategies

**State Cloning**:
```typescript
// Slow but simple
cloneState: (state) => JSON.parse(JSON.stringify(state))

// Fast but complex
cloneState: (state) => ({
  ...state,
  schedule: state.schedule.map(entry => ({ ...entry })),
})
```

**Constraint Caching**:
```typescript
class CachedConstraint {
  private cache = new Map<string, number>();
  
  evaluate(state: TState): number {
    const hash = this.hashState(state);
    if (this.cache.has(hash)) {
      return this.cache.get(hash)!;
    }
    const result = this.calculateScore(state);
    this.cache.set(hash, result);
    return result;
  }
}
```

### 8.3 Parameter Tuning

**Initial Temperature**:
- Too high → Wasted iterations
- Too low → Stuck in local minima
- Guideline: Start with 1000-10000

**Cooling Rate**:
- Too high (0.999) → Slow convergence
- Too low (0.95) → Miss optimal solution
- Guideline: 0.995-0.999

**Max Iterations**:
- Small problems: 10000-50000
- Medium problems: 50000-100000
- Large problems: 100000+

## 9. Best Practices

### 9.1 Constraint Design

1. **Hard Constraints**: Binary scoring (0 atau 1)
2. **Soft Constraints**: Gradual scoring (0-1) dengan weight
3. **Efficient Evaluation**: Gunakan caching untuk expensive computations
4. **Clear Messages**: Provide actionable violation descriptions

### 9.2 Move Generator Design

1. **Temperature Awareness**: Adjust move intensity berdasarkan temperature
2. **Constraint Awareness**: Generate valid moves ketika memungkinkan
3. **Targeted Operators**: Create specific operators untuk common violations
4. **Success Tracking**: Monitor operator effectiveness

### 9.3 Configuration Tuning

1. **Start Conservative**: Begin dengan moderate parameters
2. **Monitor Progress**: Gunakan logging untuk track optimization
3. **Adjust Based on Results**: Tune parameters berdasarkan solution quality
4. **Consider Problem Size**: Scale parameters dengan problem complexity

## 10. Common Pitfalls

### 10.1 State Mutation

```typescript
// WRONG - Modifying input state
generate(state: TState, temperature: number): TState {
  state.schedule[0].room = 'new-room';  // Don't do this!
  return state;
}

// CORRECT - Clone first
generate(state: TState, temperature: number): TState {
  const newState = JSON.parse(JSON.stringify(state));
  newState.schedule[0].room = 'new-room';
  return newState;
}
```

### 10.2 Inefficient Constraints

```typescript
// WRONG - O(n³) complexity
evaluate(state: TState): number {
  for (let i = 0; i < state.schedule.length; i++) {
    for (let j = 0; j < state.schedule.length; j++) {
      for (let k = 0; k < state.schedule.length; k++) {
        // Expensive nested computation
      }
    }
  }
}

// BETTER - O(n²) with caching
evaluate(state: TState): number {
  const conflicts = this.findConflicts(state);
  return conflicts.length === 0 ? 1 : 1 / (1 + conflicts.length);
}
```

### 10.3 Poor Parameter Selection

```typescript
// WRONG - Too aggressive cooling
const config = {
  initialTemperature: 100,
  coolingRate: 0.9,      // Too fast
  maxIterations: 1000,   // Too few
};

// BETTER - Conservative approach
const config = {
  initialTemperature: 1000,
  coolingRate: 0.995,
  maxIterations: 50000,
};
```

## 11. Extensibility

### 11.1 Domain-Specific Implementation

Library ini dirancang untuk:
- **Generic**: Bisa untuk berbagai domain problems
- **Unopinionated**: Tidak memaksakan struktur spesifik
- **Extensible**: Mudah ditambahkan constraints dan moves

### 11.2 Custom Domain Types

Users dapat mendefinisikan:
- Custom state types
- Domain-specific constraints
- Specialized move operators
- Custom evaluation functions

### 11.3 Integration Patterns

- REST API integration
- Database persistence
- Real-time updates
- Web interface
- Mobile applications

## 12. Summary

Timetable-SA adalah library optimasi yang powerful dan flexible dengan karakteristik:

### 12.1 Strengths
- ✅ **Generic**: Dapat digunakan untuk berbagai masalah optimasi
- ✅ **Effective**: Proven algorithm dengan dua fase optimasi
- ✅ **Adaptive**: Smart operator selection dan reheating mechanism
- ✅ **Extensible**: Mudah dikustomisasi untuk domain spesifik
- ✅ **Robust**: Error handling dan comprehensive logging

### 12.2 Use Cases
- University course timetabling
- School scheduling
- Exam timetabling
- Resource allocation
- Meeting scheduling
- Shift planning
- Facility scheduling

### 12.3 Next Steps
1. Pahami domain problem Anda
2. Definisikan state representation
3. Implement constraints
4. Create move generators
5. Tune parameters
6. Test dan validate
7. Deploy dan monitor

Dengan pemahaman konsep dasar ini, Anda siap untuk menjelajahi implementasi detail dan mulai menggunakan Timetable-SA untuk masalah optimasi Anda!