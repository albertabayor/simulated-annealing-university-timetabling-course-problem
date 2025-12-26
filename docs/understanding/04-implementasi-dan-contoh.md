# Implementasi dan Contoh Lengkap

## 1. Overview Implementasi University Course Timetabling

Dokumen ini menjelaskan implementasi lengkap sistem penjadwalan mata kuliah universitas menggunakan Timetable-SA package, dengan contoh konkret dari folder `examples/timetabling`.

### 1.1 Struktur Proyek

```
examples/timetabling/
├── example-basic.ts           # Main implementation file
├── types/
│   ├── Domain.ts              # Domain-specific types
│   ├── State.ts               # State definition
│   └── index.ts               # Type exports
├── constraints/
│   ├── hard/                  # Hard constraints
│   │   ├── NoRoomConflict.ts
│   │   ├── NoLecturerConflict.ts
│   │   ├── RoomCapacity.ts
│   │   └── ...
│   ├── soft/                  # Soft constraints
│   │   ├── PreferredTime.ts
│   │   ├── PreferredRoom.ts
│   │   └── ...
│   └── index.ts               # Constraint exports
├── moves/
│   ├── ChangeTimeSlot.ts
│   ├── ChangeRoom.ts
│   ├── SwapClasses.ts
│   └── index.ts               # Move exports
├── data/
│   ├── excel-loader.ts        # Excel data loading
│   ├── json-loader.ts         # JSON data loading
│   └── index.ts               # Data loader exports
├── utils/
│   ├── initial-solution.ts    # Greedy initial solution
│   ├── time.ts                # Time utilities
│   └── index.ts               # Utility exports
└── data_uisi.xlsx             # Sample data file
```

## 2. Domain Types Definition

### 2.1 Core Domain Types

File [`types/Domain.ts`](examples/timetabling/types/Domain.ts:1) mendefinisikan tipe data fundamental:

#### Room Definition
```typescript
export interface Room {
  Code: string;        // Room identifier (e.g., "LAB-101")
  Name: string;        // Room name (e.g., "Computer Lab 101")
  Type: string;        // Room type (e.g., "Lab", "Lecture Hall")
  Capacity: number;    // Maximum capacity
}
```

#### Lecturer Definition
```typescript
export interface Lecturer {
  "Prodi Code": string;        // Study program code
  Code: string;                // Lecturer identifier
  Name: string;                // Lecturer name
  Prefered_Time: string;       // Preferred teaching time
  Research_Day: string;         // Research day
  Transit_Time: number;         // Minutes between classes
  Max_Daily_Periods: number;    // Max teaching hours per day
  Prefered_Room: string;       // Preferred room
}
```

#### Class Requirement Definition
```typescript
export interface ClassRequirement {
  Prodi: string;                        // Study program
  Kelas: string;                        // Class section (A, B, C)
  Kode_Matakuliah: string;             // Course code
  Mata_Kuliah: string;                 // Course name
  SKS: number;                         // Credit hours
  Jenis: string;                       // Course type
  Peserta: number;                     // Number of participants
  Kode_Dosen1: string;                 // Primary lecturer
  Kode_Dosen2: string;                 // Secondary lecturer
  Class_Type: string;                  // "pagi" or "sore"
  should_on_the_lab: string;           // Lab requirement
  rooms: string;                       // Preferred room
}
```

### 2.2 State Definition

File [`types/State.ts`](examples/timetabling/types/State.ts:1) mendefinisikan state untuk optimasi:

#### Schedule Entry
```typescript
export interface ScheduleEntry {
  classId: string;              // Course code
  className: string;            // Course name
  class: string | string[];     // Class section(s)
  prodi: string;                // Study program
  lecturers: string[];          // Lecturer codes
  room: string;                 // Room code
  timeSlot: TimeSlot;          // Scheduled time
  sks: number;                  // Credit hours
  needsLab: boolean;           // Lab requirement
  participants: number;         // Student count
  classType: string;           // Morning/evening
  prayerTimeAdded: number;     // Prayer time adjustment
  isOverflowToLab?: boolean;   // Non-lab in lab room
}
```

#### Complete Timetable State
```typescript
export interface TimetableState {
  schedule: ScheduleEntry[];           // Current schedule
  availableTimeSlots: TimeSlot[];      // Available slots
  rooms: Room[];                       // Available rooms
  lecturers: Lecturer[];              // Available lecturers
}
```

## 3. Data Loading Implementation

### 3.1 Excel Data Loader

File [`data/excel-loader.ts`](examples/timetabling/data/excel-loader.ts:1) mengimplementasikan loading data dari Excel:

```typescript
import * as XLSX from 'xlsx';
import type { TimetableInput } from '../types/index.js';

export function loadDataFromExcel(filePath: string): TimetableInput {
  const workbook = XLSX.readFile(filePath);
  
  // Load rooms
  const roomsSheet = workbook.Sheets['Rooms'];
  const rooms = XLSX.utils.sheet_to_json<Room>(roomsSheet);
  
  // Load lecturers
  const lecturersSheet = workbook.Sheets['Lecturers'];
  const lecturers = XLSX.utils.sheet_to_json<Lecturer>(lecturersSheet);
  
  // Load classes
  const classesSheet = workbook.Sheets['Classes'];
  const classes = XLSX.utils.sheet_to_json<ClassRequirement>(classesSheet);
  
  return { rooms, lecturers, classes };
}
```

### 3.2 Data Structure

Excel file structure:
- **Sheet "Rooms"**: Daftar ruangan dengan kapasitas dan tipe
- **Sheet "Lecturers"**: Data dosen dengan preferensi
- **Sheet "Classes"**: Persyaratan mata kuliah

## 4. Initial Solution Generation

### 4.1 Greedy Algorithm Implementation

File [`utils/initial-solution.ts`](examples/timetabling/utils/initial-solution.ts:1) mengimplementasikan algoritma greedy:

```typescript
export function generateInitialSolution(data: TimetableInput): TimetableState {
  const { rooms, lecturers, classes } = data;
  const schedule: ScheduleEntry[] = [];
  
  for (const classReq of classes) {
    // Extract lecturer codes
    const lecturerCodes = extractLecturerCodes(classReq);
    
    // Get class properties
    const participants = classReq.Peserta || 30;
    const needsLab = classReq.should_on_the_lab?.toLowerCase() === 'yes';
    const classType = classReq.Class_Type?.toLowerCase() || 'pagi';
    
    // Filter appropriate time slots
    const slots = filterTimeSlots(classType, classReq.Prodi);
    
    // Try to place class
    for (const slot of slots) {
      const suitableRooms = findSuitableRooms(rooms, participants, needsLab);
      
      for (const room of suitableRooms) {
        const entry = createScheduleEntry(classReq, lecturerCodes, room, slot);
        
        if (!hasConflict(entry, schedule)) {
          schedule.push(entry);
          break; // Found valid placement
        }
      }
    }
  }
  
  return {
    schedule,
    availableTimeSlots: getAllTimeSlots(),
    rooms,
    lecturers,
  };
}
```

### 4.2 Conflict Detection

```typescript
function hasConflict(entry: ScheduleEntry, schedule: ScheduleEntry[]): boolean {
  for (const existing of schedule) {
    // Same day check
    if (entry.timeSlot.day !== existing.timeSlot.day) continue;
    
    // Time overlap check
    if (!hasTimeOverlap(entry, existing)) continue;
    
    // Check conflicts
    if (entry.room === existing.room) return true;           // Room conflict
    if (hasLecturerConflict(entry, existing)) return true;   // Lecturer conflict
    if (hasClassConflict(entry, existing)) return true;       // Class conflict
  }
  
  return false;
}
```

## 5. Constraints Implementation

### 5.1 Hard Constraints

#### No Room Conflict

File [`constraints/hard/NoRoomConflict.ts`](examples/timetabling/constraints/hard/NoRoomConflict.ts:1):

```typescript
export class NoRoomConflict implements Constraint<TimetableState> {
  name = 'No Room Conflict';
  type = 'hard' as const;

  evaluate(state: TimetableState): number {
    const { schedule } = state;
    let violationCount = 0;

    for (let i = 0; i < schedule.length; i++) {
      for (let j = i + 1; j < schedule.length; j++) {
        const entry1 = schedule[i];
        const entry2 = schedule[j];

        if (this.hasRoomConflict(entry1, entry2)) {
          violationCount++;
        }
      }
    }

    // Return score between 0 and 1
    return violationCount === 0 ? 1 : 1 / (1 + violationCount);
  }

  getViolations(state: TimetableState): string[] {
    const violations: string[] = [];
    
    for (let i = 0; i < schedule.length; i++) {
      for (let j = i + 1; j < schedule.length; j++) {
        const entry1 = schedule[i];
        const entry2 = schedule[j];

        if (this.hasRoomConflict(entry1, entry2)) {
          violations.push(
            `Room ${entry1.room} occupied by ${entry1.classId} and ${entry2.classId} on ${entry1.timeSlot.day}`
          );
        }
      }
    }

    return violations;
  }

  private hasRoomConflict(entry1: ScheduleEntry, entry2: ScheduleEntry): boolean {
    // Same room and day with time overlap
    return entry1.room === entry2.room &&
           entry1.timeSlot.day === entry2.timeSlot.day &&
           this.isTimeOverlap(entry1, entry2);
  }
}
```

#### Room Capacity

```typescript
export class RoomCapacity implements Constraint<TimetableState> {
  name = 'Room Capacity';
  type = 'hard' as const;

  evaluate(state: TimetableState): number {
    const { schedule, rooms } = state;
    const roomMap = new Map(rooms.map(r => [r.Code, r]));
    let violationCount = 0;

    for (const entry of schedule) {
      const room = roomMap.get(entry.room);
      if (room && entry.participants > room.Capacity) {
        violationCount++;
      }
    }

    return violationCount === 0 ? 1 : 1 / (1 + violationCount);
  }
}
```

### 5.2 Soft Constraints

#### Preferred Time

File [`constraints/soft/PreferredTime.ts`](examples/timetabling/constraints/soft/PreferredTime.ts:1):

```typescript
export class PreferredTime implements Constraint<TimetableState> {
  name = 'Preferred Time';
  type = 'soft' as const;
  weight: number;

  constructor(weight: number = 10) {
    this.weight = weight;
  }

  evaluate(state: TimetableState): number {
    const { schedule, lecturers } = state;
    const lecturerMap = new Map(lecturers.map(l => [l.Code, l]));

    let totalScore = 0;
    let count = 0;

    for (const entry of schedule) {
      for (const lecturerCode of entry.lecturers) {
        const lecturer = lecturerMap.get(lecturerCode);
        if (!lecturer || !lecturer.Prefered_Time) continue;

        count++;

        if (this.matchesPreferredTime(entry, lecturer.Prefered_Time)) {
          totalScore += 1;
        }
      }
    }

    return count > 0 ? totalScore / count : 1;
  }

  private matchesPreferredTime(entry: ScheduleEntry, preferredTime: string): boolean {
    // Parse preferred time format: "08.00 - 10.00 monday, 13.00 - 15.00 tuesday"
    const dailySchedules = preferredTime.toLowerCase().split(', ');
    
    for (const schedule of dailySchedules) {
      const [timeRange, day] = schedule.trim().split(' ');
      if (day !== entry.timeSlot.day.toLowerCase()) continue;
      
      const [startTime, endTime] = timeRange.split(' - ');
      if (this.isTimeInRange(entry.timeSlot.startTime, startTime, endTime)) {
        return true;
      }
    }
    
    return false;
  }
}
```

## 6. Move Generators Implementation

### 6.1 Basic Move: Change Time Slot

File [`moves/ChangeTimeSlot.ts`](examples/timetabling/moves/ChangeTimeSlot.ts:1):

```typescript
export class ChangeTimeSlot implements MoveGenerator<TimetableState> {
  name = "Change Time Slot";

  canApply(state: TimetableState): boolean {
    return state.schedule.length > 0;
  }

  generate(state: TimetableState, temperature: number): TimetableState {
    // Clone state
    const newState = JSON.parse(JSON.stringify(state)) as TimetableState;

    // Pick random class
    const randomIndex = Math.floor(Math.random() * newState.schedule.length);
    const entry = newState.schedule[randomIndex];

    // Get constraint-aware valid slots
    const { preferred, acceptable } = getValidTimeSlotsWithPriority(newState, entry);

    // Prefer non-Friday slots (80% of time)
    let slotsToUse = preferred.length > 0 ? preferred : acceptable;
    
    if (slotsToUse.length === 0) {
      return newState; // No valid slots available
    }

    // Pick random valid time slot
    const newSlot = slotsToUse[Math.floor(Math.random() * slotsToUse.length)];

    // Update time slot
    entry.timeSlot = {
      period: newSlot.period,
      day: newSlot.day,
      startTime: newSlot.startTime,
      endTime: newSlot.endTime,
    };

    return newState;
  }
}
```

### 6.2 Advanced Move: Fix Specific Violation

```typescript
export class FixFridayPrayerConflict implements MoveGenerator<TimetableState> {
  name = "Fix Friday Prayer Conflict";

  canApply(state: TimetableState): boolean {
    return this.hasFridayPrayerConflict(state);
  }

  generate(state: TimetableState, temperature: number): TimetableState {
    const newState = JSON.parse(JSON.stringify(state));
    
    // Find Friday classes with prayer time conflicts
    const conflictingClasses = newState.schedule.filter(entry => 
      entry.timeSlot.day === 'Friday' && 
      this.isInPrayerTime(entry.timeSlot.startTime)
    );

    if (conflictingClasses.length === 0) return newState;

    // Fix first conflicting class
    const entry = conflictingClasses[0];
    const newSlot = this.findAlternativeSlot(newState, entry);
    
    if (newSlot) {
      entry.timeSlot = newSlot;
    }

    return newState;
  }

  private hasFridayPrayerConflict(state: TimetableState): boolean {
    return state.schedule.some(entry => 
      entry.timeSlot.day === 'Friday' && 
      this.isInPrayerTime(entry.timeSlot.startTime)
    );
  }
}
```

## 7. Main Implementation

### 7.1 Complete Implementation Flow

File [`example-basic.ts`](examples/timetabling/example-basic.ts:1) menunjukkan implementasi lengkap:

```typescript
import { SimulatedAnnealing } from "timetable-sa";
import type { SAConfig, Constraint, MoveGenerator } from "timetable-sa";
import type { TimetableState } from "./types/index.js";

// 1. Load data from Excel
console.log("📂 Loading data from Excel file...");
const data = loadDataFromExcel("./data_uisi.xlsx");

// 2. Generate initial solution
console.log("🏗️  Generating initial timetable...");
const initialState = generateInitialSolution(data);

// 3. Define constraints
const constraints: Constraint<TimetableState>[] = [
  // Hard constraints
  new NoLecturerConflict(),
  new NoRoomConflict(),
  new RoomCapacity(),
  new NoProdiConflict(),
  new NoFridayPrayConflict(),
  new MaxDailyPeriods(),
  new ClassTypeTime(),
  new SaturdayRestriction(),
  new FridayTimeRestriction(),
  new PrayerTimeStart(),
  new ExclusiveRoom(),

  // Soft constraints with weights
  new PreferredTime(10),
  new PreferredRoom(10),
  new TransitTime(5),
  new Compactness(15),
  new PrayerTimeOverlap(20),
  new EveningClassPriority(20),
  new ResearchDay(10),
  new OverflowPenalty(10),
];

// 4. Define move operators
const moveGenerators: MoveGenerator<TimetableState>[] = [
  // Targeted operators (higher priority)
  new FixFridayPrayerConflict(),
  new SwapFridayWithNonFriday(),
  new FixLecturerConflict(),
  new FixRoomConflict(),
  new FixMaxDailyPeriods(),
  new FixRoomCapacity(),

  // General operators
  new ChangeTimeSlotAndRoom(),
  new ChangeTimeSlot(),
  new ChangeRoom(),
  new SwapClasses(),
];

// 5. Configure Simulated Annealing
const config: SAConfig<TimetableState> = {
  initialTemperature: 100000,
  minTemperature: 0.0000001,
  coolingRate: 0.9998,
  maxIterations: 100000,
  hardConstraintWeight: 100000,
  
  cloneState: (state) => JSON.parse(JSON.stringify(state)),
  
  reheatingThreshold: 500,
  reheatingFactor: 1.5,
  maxReheats: 10,
  
  logging: {
    enabled: true,
    level: "info",
    logInterval: 500,
  },
};

// 6. Create solver and run optimization
const solver = new SimulatedAnnealing(initialState, constraints, moveGenerators, config);
const solution = solver.solve();

// 7. Display results
console.log("✨ OPTIMIZATION COMPLETE!");
console.log(`Final fitness: ${solution.fitness.toFixed(2)}`);
console.log(`Hard violations: ${solution.hardViolations}`);
console.log(`Soft violations: ${solution.softViolations}`);
console.log(`Iterations: ${solution.iterations}`);
```

### 7.2 Result Analysis

```typescript
// Display operator statistics
console.log("📈 OPERATOR STATISTICS:");
for (const [operatorName, stats] of Object.entries(solution.operatorStats)) {
  console.log(`  ${operatorName}:`);
  console.log(`    Attempts: ${stats.attempts}`);
  console.log(`    Improvements: ${stats.improvements}`);
  console.log(`    Success rate: ${(stats.successRate * 100).toFixed(2)}%`);
}

// Display violations
if (solution.violations.length > 0) {
  console.log(`⚠️  VIOLATIONS (${solution.violations.length}):`);
  solution.violations.slice(0, 10).forEach((v) => {
    console.log(`  - [${v.constraintType}] ${v.constraintName}: ${v.description}`);
  });
} else {
  console.log("🎉 NO VIOLATIONS - Perfect timetable!");
}

// Save results
fs.writeFileSync("timetable-result.json", JSON.stringify({
  fitness: solution.fitness,
  hardViolations: solution.hardViolations,
  softViolations: solution.softViolations,
  iterations: solution.iterations,
  schedule: solution.state.schedule,
  violations: solution.violations,
}, null, 2));
```

## 8. Advanced Features

### 8.1 Time Slot Validation

```typescript
export function getValidTimeSlotsWithPriority(
  state: TimetableState, 
  entry: ScheduleEntry
): { preferred: TimeSlot[], acceptable: TimeSlot[] } {
  const preferred: TimeSlot[] = [];
  const acceptable: TimeSlot[] = [];

  for (const slot of state.availableTimeSlots) {
    // Check basic constraints
    if (!isValidTimeSlot(slot, entry)) continue;

    // Check prayer time restrictions
    if (isPrayerTimeConflict(slot, entry)) {
      acceptable.push(slot); // Still acceptable but not preferred
    } else {
      preferred.push(slot); // Preferred slot
    }
  }

  return { preferred, acceptable };
}
```

### 8.2 Room Assignment Logic

```typescript
function findSuitableRooms(
  rooms: Room[], 
  participants: number, 
  needsLab: boolean
): Room[] {
  return rooms.filter(room => {
    // Check capacity
    if (room.Capacity < participants) return false;
    
    // Check lab requirement
    if (needsLab && !room.Type.toLowerCase().includes('lab')) return false;
    
    return true;
  });
}
```

### 8.3 Prayer Time Handling

```typescript
export const PRAYER_TIMES = {
  Friday: {
    Dhuhr: { start: 660, end: 720 },    // 11:00 - 12:00
    Ashar: { start: 900, end: 960 },    // 15:00 - 16:00
  }
};

export function isPrayerTimeConflict(slot: TimeSlot, entry: ScheduleEntry): boolean {
  if (slot.day !== 'Friday') return false;
  
  const startTime = timeToMinutes(slot.startTime);
  const endTime = timeToMinutes(slot.endTime) + entry.prayerTimeAdded;
  
  // Check if class overlaps with prayer times
  for (const prayer of Object.values(PRAYER_TIMES.Friday)) {
    if (startTime < prayer.end && endTime > prayer.start) {
      return true;
    }
  }
  
  return false;
}
```

## 9. Performance Optimization

### 9.1 Efficient State Cloning

```typescript
// Custom cloning for better performance
cloneState: (state) => ({
  ...state,
  schedule: state.schedule.map(entry => ({ ...entry })),
  availableTimeSlots: [...state.availableTimeSlots],
  // Don't clone rooms and lecturers as they don't change
  rooms: state.rooms,
  lecturers: state.lecturers,
})
```

### 9.2 Smart Move Selection

```typescript
class SmartChangeTimeSlot implements MoveGenerator<TimetableState> {
  generate(state: TimetableState, temperature: number): TimetableState {
    const newState = JSON.parse(JSON.stringify(state));
    
    // Temperature-dependent strategy
    if (temperature > 10000) {
      // High temp: random exploration
      return this.randomMove(newState);
    } else {
      // Low temp: targeted improvement
      return this.targetedMove(newState);
    }
  }
}
```

### 9.3 Constraint Caching

```typescript
class CachedConstraint implements Constraint<TimetableState> {
  private cache = new Map<string, number>();
  
  evaluate(state: TimetableState): number {
    const stateHash = this.hashState(state);
    
    if (this.cache.has(stateHash)) {
      return this.cache.get(stateHash)!;
    }
    
    const result = this.calculateScore(state);
    this.cache.set(stateHash, result);
    return result;
  }
  
  private hashState(state: TimetableState): string {
    // Create hash from schedule
    return state.schedule.map(e => 
      `${e.classId}-${e.room}-${e.timeSlot.day}-${e.timeSlot.startTime}`
    ).join('|');
  }
}
```

## 10. Testing and Validation

### 10.1 Constraint Testing

```typescript
function testConstraints(state: TimetableState): void {
  const constraints = [
    new NoRoomConflict(),
    new RoomCapacity(),
    new NoLecturerConflict(),
  ];
  
  for (const constraint of constraints) {
    const score = constraint.evaluate(state);
    console.log(`${constraint.name}: ${score}`);
    
    if (score < 1) {
      const violations = constraint.getViolations?.(state) || [];
      violations.forEach(v => console.log(`  - ${v}`));
    }
  }
}
```

### 10.2 Solution Validation

```typescript
function validateSolution(solution: Solution<TimetableState>): boolean {
  // Check all hard constraints are satisfied
  if (solution.hardViolations > 0) {
    console.error("Solution has hard constraint violations!");
    return false;
  }
  
  // Check all classes are scheduled
  const expectedClasses = /* get from input */;
  if (solution.state.schedule.length !== expectedClasses.length) {
    console.error("Not all classes are scheduled!");
    return false;
  }
  
  return true;
}
```

## 11. Best Practices

### 11.1 Constraint Design

1. **Hard Constraints**: Binary scoring (0 or 1)
2. **Soft Constraints**: Gradual scoring (0-1) with appropriate weights
3. **Efficient Evaluation**: Use caching for expensive computations
4. **Clear Violation Messages**: Provide actionable violation descriptions

### 11.2 Move Generator Design

1. **Temperature Awareness**: Adjust move intensity based on temperature
2. **Constraint Awareness**: Generate valid moves when possible
3. **Targeted Operators**: Create specific operators for common violations
4. **Success Rate Tracking**: Monitor operator effectiveness

### 11.3 Configuration Tuning

1. **Start Conservative**: Begin with moderate parameters
2. **Monitor Progress**: Use logging to track optimization
3. **Adjust Based on Results**: Tune parameters based on solution quality
4. **Consider Problem Size**: Scale parameters with problem complexity

## 12. Common Issues and Solutions

### 12.1 No Convergence

**Problem**: Algorithm doesn't converge to good solution
**Solutions**:
- Increase initial temperature
- Decrease cooling rate (slower cooling)
- Increase max iterations
- Add more targeted move operators

### 12.2 Too Many Violations

**Problem**: Final solution has many violations
**Solutions**:
- Increase hard constraint weight
- Add more specific move operators
- Improve initial solution quality
- Check constraint implementation for bugs

### 12.3 Slow Performance

**Problem**: Optimization takes too long
**Solutions**:
- Optimize state cloning
- Use constraint caching
- Reduce problem complexity
- Parallelize constraint evaluation

### 12.4 Local Optima

**Problem**: Gets stuck in local optimum
**Solutions**:
- Enable reheating mechanism
- Increase exploration moves
- Add diversity to move operators
- Use higher initial temperature

## 13. Extension Ideas

### 13.1 Multi-Objective Optimization

```typescript
interface MultiObjectiveSolution<TState> extends Solution<TState> {
  objectives: {
    hardConstraints: number;
    softConstraints: number;
    lecturerPreference: number;
    roomUtilization: number;
  };
}
```

### 13.2 Dynamic Constraints

```typescript
class DynamicConstraint implements Constraint<TimetableState> {
  private weight: number;
  
  constructor(initialWeight: number) {
    this.weight = initialWeight;
  }
  
  adjustWeight(newWeight: number): void {
    this.weight = newWeight;
  }
  
  evaluate(state: TimetableState): number {
    // Use current weight in evaluation
    return this.calculateScore(state) * this.weight;
  }
}
```

### 13.3 Hybrid Algorithms

```typescript
class HybridSolver<TState> {
  constructor(
    private saSolver: SimulatedAnnealing<TState>,
    private localSearch: LocalSearch<TState>
  ) {}
  
  solve(): Solution<TState> {
    // Phase 1: Simulated Annealing
    const saSolution = this.saSolver.solve();
    
    // Phase 2: Local Search refinement
    return this.localSearch.refine(saSolution);
  }
}
```

Implementasi ini menunjukkan bagaimana Timetable-SA package dapat digunakan untuk menyelesaikan masalah penjadwalan kompleks dengan berbagai constraints dan optimization strategies. Struktur modularnya memungkinkan ekstensi dan kustomisasi sesuai kebutuhan spesifik institusi.