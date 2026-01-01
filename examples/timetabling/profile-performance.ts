/**
 * Performance Profiler for Simulated Annealing
 * 
 * This script measures where time is spent in the SA optimization loop.
 * Run with: npx ts-node examples/timetabling/profile-performance.ts
 * Or with bun: bun examples/timetabling/profile-performance.ts
 */

import type { SAConfig, Constraint, MoveGenerator } from "../../src/index.js";
import type { TimetableState, ScheduleEntry } from "./types/index.js";
import { loadDataFromExcel } from "./data/index.js";
import { generateInitialSolution } from "./utils/initial-solution.js";
import { NoFridayPrayConflict } from "./constraints/hard/NoFridayPrayConflit.js";

import { NoLecturerConflict, NoRoomConflict, RoomCapacity, NoProdiConflict, MaxDailyPeriods, ClassTypeTime, SaturdayRestriction, FridayTimeRestriction, PrayerTimeStart, ExclusiveRoom } from "./constraints/hard/index.js";
import { Compactness, EveningClassPriority, OverflowPenalty, PrayerTimeOverlap, PreferredRoom, PreferredTime, ResearchDay, TransitTime } from "./constraints/soft/index.js";
import { ChangeTimeSlot, ChangeRoom, SwapClasses, ChangeTimeSlotAndRoom, FixFridayPrayerConflict, FixLecturerConflict, FixRoomConflict, FixMaxDailyPeriods, FixRoomCapacity } from "./moves/index.js";
import { SwapFridayWithNonFriday } from "./moves/SwapFridayWithNonFriday.js";

// ============================================
// PROFILING CONFIGURATION
// ============================================
const PROFILE_ITERATIONS = 2000; // Number of iterations to profile
const WARMUP_ITERATIONS = 100;   // Warmup iterations (not counted)

interface ProfileStats {
  totalTime: number;
  cloneTime: number;
  constraintTime: number;
  hardConstraintTime: number;
  moveGenerationTime: number;
  tabuCheckTime: number;
  acceptanceProbTime: number;
  otherTime: number;
  iterationCount: number;
  
  // Per-constraint breakdown
  constraintBreakdown: Map<string, { time: number; calls: number }>;
  // Per-operator breakdown
  operatorBreakdown: Map<string, { time: number; calls: number }>;
}

function createProfileStats(): ProfileStats {
  return {
    totalTime: 0,
    cloneTime: 0,
    constraintTime: 0,
    hardConstraintTime: 0,
    moveGenerationTime: 0,
    tabuCheckTime: 0,
    acceptanceProbTime: 0,
    otherTime: 0,
    iterationCount: 0,
    constraintBreakdown: new Map(),
    operatorBreakdown: new Map(),
  };
}

// ============================================
// PROFILED OPERATIONS
// ============================================

function profileClone(
  state: TimetableState,
  cloneFn: (s: TimetableState) => TimetableState,
  stats: ProfileStats
): TimetableState {
  const start = performance.now();
  const result = cloneFn(state);
  stats.cloneTime += performance.now() - start;
  return result;
}

function profileConstraints(
  state: TimetableState,
  constraints: Constraint<TimetableState>[],
  hardConstraintWeight: number,
  stats: ProfileStats
): { fitness: number; hardViolations: number } {
  const start = performance.now();
  let hardPenalty = 0;
  let softPenalty = 0;
  let hardViolationCount = 0;

  for (const constraint of constraints) {
    const constraintStart = performance.now();
    const score = constraint.evaluate(state);
    const constraintTime = performance.now() - constraintStart;

    // Track per-constraint time
    const key = constraint.name;
    const existing = stats.constraintBreakdown.get(key) ?? { time: 0, calls: 0 };
    existing.time += constraintTime;
    existing.calls += 1;
    stats.constraintBreakdown.set(key, existing);

    if (constraint.type === "hard") {
      if (score < 1) {
        hardPenalty += 1 - score;
        // Count violations
        if (constraint.getViolations) {
          hardViolationCount += constraint.getViolations(state).length;
        } else {
          hardViolationCount += Math.max(1, Math.round((1 / score) - 1));
        }
      }
    } else {
      if (score < 1) {
        softPenalty += (1 - score) * (constraint.weight ?? 10);
      }
    }
  }

  stats.constraintTime += performance.now() - start;

  return {
    fitness: hardPenalty * hardConstraintWeight + softPenalty,
    hardViolations: hardViolationCount,
  };
}

function profileHardConstraintCount(
  state: TimetableState,
  hardConstraints: Constraint<TimetableState>[],
  stats: ProfileStats
): number {
  const start = performance.now();
  let count = 0;

  for (const constraint of hardConstraints) {
    const score = constraint.evaluate(state);
    if (score < 1) {
      if (constraint.getViolations) {
        count += constraint.getViolations(state).length;
      } else {
        count += Math.max(1, Math.round((1 / score) - 1));
      }
    }
  }

  stats.hardConstraintTime += performance.now() - start;
  return count;
}

function profileMoveGeneration(
  state: TimetableState,
  generators: MoveGenerator<TimetableState>[],
  temperature: number,
  cloneFn: (s: TimetableState) => TimetableState,
  stats: ProfileStats
): { newState: TimetableState | null; operatorName: string } {
  const start = performance.now();

  // Filter applicable generators
  const applicable = generators.filter((g) => g.canApply(state));
  if (applicable.length === 0) {
    stats.moveGenerationTime += performance.now() - start;
    return { newState: null, operatorName: "" };
  }

  // Random selection for profiling simplicity
  const selected = applicable[Math.floor(Math.random() * applicable.length)]!;
  
  const cloneStart = performance.now();
  const cloned = cloneFn(state);
  stats.cloneTime += performance.now() - cloneStart;

  const generateStart = performance.now();
  const newState = selected.generate(cloned, temperature);
  const generateTime = performance.now() - generateStart;

  // Track per-operator time
  const existing = stats.operatorBreakdown.get(selected.name) ?? { time: 0, calls: 0 };
  existing.time += generateTime;
  existing.calls += 1;
  stats.operatorBreakdown.set(selected.name, existing);

  stats.moveGenerationTime += performance.now() - start - (performance.now() - cloneStart);
  return { newState, operatorName: selected.name };
}

function profileTabuCheck(
  signature: string,
  tabuList: Map<string, number>,
  currentIteration: number,
  tabuTenure: number,
  stats: ProfileStats
): boolean {
  const start = performance.now();
  const addedAt = tabuList.get(signature);
  const isTabu = addedAt !== undefined && currentIteration - addedAt < tabuTenure;
  stats.tabuCheckTime += performance.now() - start;
  return isTabu;
}

function getStateSignature(state: TimetableState): string {
  const assignments: string[] = [];
  for (const entry of state.schedule) {
    if (entry.classId && entry.timeSlot && entry.room) {
      assignments.push(
        `${entry.classId}:${entry.timeSlot.day}:${entry.timeSlot.startTime}:${entry.room}`
      );
    }
  }
  return assignments.sort().join("|");
}

// ============================================
// RUN PROFILING
// ============================================

console.log("=".repeat(70));
console.log("  PERFORMANCE PROFILER - Simulated Annealing");
console.log("=".repeat(70));

// Load data
console.log("\n📂 Loading data...");
const dataPath = "./data_uisi.xlsx";
const data = loadDataFromExcel(dataPath);
console.log(`✅ Loaded: ${data.classes.length} classes, ${data.rooms.length} rooms, ${data.lecturers.length} lecturers`);

// Generate initial state  
console.log("\n🏗️  Generating initial solution...");
const initialState = generateInitialSolution(data, { randomize: true });

// Setup constraints and operators
const constraints: Constraint<TimetableState>[] = [
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
  new PreferredTime(10),
  new PreferredRoom(10),
  new TransitTime(5),
  new Compactness(15),
  new PrayerTimeOverlap(20),
  new EveningClassPriority(20),
  new ResearchDay(10),
  new OverflowPenalty(10),
];

const hardConstraints = constraints.filter((c) => c.type === "hard");
const softConstraints = constraints.filter((c) => c.type === "soft");

const moveGenerators: MoveGenerator<TimetableState>[] = [
  new FixFridayPrayerConflict(),
  new SwapFridayWithNonFriday(),
  new FixLecturerConflict(),
  new FixRoomConflict(),
  new FixMaxDailyPeriods(),
  new FixRoomCapacity(),
  new ChangeTimeSlotAndRoom(),
  new ChangeTimeSlot(),
  new ChangeRoom(),
  new SwapClasses(),
];

const cloneState = (state: TimetableState): TimetableState => ({
  ...state,
  schedule: state.schedule.map((entry: ScheduleEntry) => ({ ...entry })),
});

const hardConstraintWeight = 100000;
const tabuTenure = 50;

// Initialize profiling stats
const stats = createProfileStats();
const tabuList = new Map<string, number>();

// Simulate SA loop
console.log(`\n🔬 Running profiler (${WARMUP_ITERATIONS} warmup + ${PROFILE_ITERATIONS} profiled iterations)...`);

let currentState = cloneState(initialState);
let temperature = 100000;
const coolingRate = 0.9995;

// Warmup
console.log("   Warming up...");
for (let i = 0; i < WARMUP_ITERATIONS; i++) {
  const { newState } = profileMoveGeneration(currentState, moveGenerators, temperature, cloneState, createProfileStats());
  if (newState) {
    currentState = newState;
  }
  temperature *= coolingRate;
}

// Reset for actual profiling
currentState = cloneState(initialState);
temperature = 100000;

// Profile
console.log("   Profiling...");
const overallStart = performance.now();

for (let i = 0; i < PROFILE_ITERATIONS; i++) {
  const iterStart = performance.now();

  // 1. Generate neighbor (includes one clone)
  const { newState, operatorName } = profileMoveGeneration(
    currentState, 
    moveGenerators, 
    temperature, 
    cloneState, 
    stats
  );

  if (!newState) {
    stats.iterationCount++;
    temperature *= coolingRate;
    continue;
  }

  // 2. Tabu check
  const newSignature = getStateSignature(newState);
  profileTabuCheck(newSignature, tabuList, i, tabuTenure, stats);

  // 3. Calculate fitness (evaluates ALL constraints)
  const { fitness: newFitness, hardViolations: newHardViolations } = profileConstraints(
    newState,
    constraints,
    hardConstraintWeight,
    stats
  );

  // NOTE: In the actual SA engine, hard violations are now computed TOGETHER
  // with fitness in calculateFitnessAndViolations(). This call is removed.

  // 5. Accept or reject
  const acceptStart = performance.now();
  const accept = Math.random() < 0.5; // Simplified for profiling
  stats.acceptanceProbTime += performance.now() - acceptStart;

  if (accept) {
    // 6. Clone for best state update
    currentState = profileClone(newState, cloneState, stats);
    
    // Add to tabu
    tabuList.set(getStateSignature(currentState), i);
  }

  temperature *= coolingRate;
  stats.iterationCount++;
  stats.totalTime += performance.now() - iterStart;

  if ((i + 1) % 500 === 0) {
    console.log(`   Progress: ${i + 1}/${PROFILE_ITERATIONS}`);
  }
}

const overallTime = performance.now() - overallStart;

// ============================================
// REPORT RESULTS
// ============================================

console.log("\n" + "=".repeat(70));
console.log("  📊 PROFILING RESULTS");
console.log("=".repeat(70));

console.log(`\n🕐 OVERALL TIMING:`);
console.log(`   Total wall time: ${overallTime.toFixed(2)} ms`);
console.log(`   Iterations: ${stats.iterationCount}`);
console.log(`   Avg per iteration: ${(overallTime / stats.iterationCount).toFixed(3)} ms`);
console.log(`   Projected for 20K iterations: ${((overallTime / stats.iterationCount) * 20000 / 1000).toFixed(1)} seconds`);

console.log(`\n⏱️  TIME BREAKDOWN:`);
const categorized = stats.cloneTime + stats.constraintTime + stats.hardConstraintTime + 
                    stats.moveGenerationTime + stats.tabuCheckTime + stats.acceptanceProbTime;
const other = overallTime - categorized;

const breakdown = [
  { name: "Constraint Evaluation", time: stats.constraintTime, pct: (stats.constraintTime / overallTime * 100) },
  // NOTE: Since SA engine now uses unified calculateFitnessAndViolations(), 
  // hard constraint count time should be 0 - keeping the metric for visibility
  { name: "Hard Constraint Count", time: stats.hardConstraintTime, pct: (stats.hardConstraintTime / overallTime * 100) },
  { name: "State Cloning", time: stats.cloneTime, pct: (stats.cloneTime / overallTime * 100) },
  { name: "Move Generation", time: stats.moveGenerationTime, pct: (stats.moveGenerationTime / overallTime * 100) },
  { name: "Tabu Check", time: stats.tabuCheckTime, pct: (stats.tabuCheckTime / overallTime * 100) },
  { name: "Acceptance Prob", time: stats.acceptanceProbTime, pct: (stats.acceptanceProbTime / overallTime * 100) },
  { name: "Other/Overhead", time: other, pct: (other / overallTime * 100) },
];

breakdown.sort((a, b) => b.time - a.time);

for (const item of breakdown) {
  const bar = "█".repeat(Math.round(item.pct / 2));
  console.log(`   ${item.name.padEnd(22)} ${item.time.toFixed(1).padStart(8)} ms  (${item.pct.toFixed(1).padStart(5)}%) ${bar}`);
}

console.log(`\n🔍 PER-CONSTRAINT BREAKDOWN (top 10 by time):`);
const constraintArr = [...stats.constraintBreakdown.entries()]
  .map(([name, data]) => ({ name, ...data, avgMs: data.time / data.calls }))
  .sort((a, b) => b.time - a.time)
  .slice(0, 10);

console.log(`   ${"Constraint".padEnd(25)} ${"Total(ms)".padStart(10)} ${"Calls".padStart(8)} ${"Avg(ms)".padStart(10)}`);
for (const c of constraintArr) {
  console.log(`   ${c.name.padEnd(25)} ${c.time.toFixed(1).padStart(10)} ${c.calls.toString().padStart(8)} ${c.avgMs.toFixed(4).padStart(10)}`);
}

console.log(`\n🔄 PER-OPERATOR BREAKDOWN:`);
const operatorArr = [...stats.operatorBreakdown.entries()]
  .map(([name, data]) => ({ name, ...data, avgMs: data.time / data.calls }))
  .sort((a, b) => b.time - a.time);

console.log(`   ${"Operator".padEnd(25)} ${"Total(ms)".padStart(10)} ${"Calls".padStart(8)} ${"Avg(ms)".padStart(10)}`);
for (const o of operatorArr) {
  console.log(`   ${o.name.padEnd(25)} ${o.time.toFixed(1).padStart(10)} ${o.calls.toString().padStart(8)} ${o.avgMs.toFixed(4).padStart(10)}`);
}

console.log("\n" + "=".repeat(70));
console.log("  💡 ANALYSIS & RECOMMENDATIONS");
console.log("=".repeat(70));

// Automated analysis
const constraintPct = (stats.constraintTime + stats.hardConstraintTime) / overallTime * 100;
const clonePct = stats.cloneTime / overallTime * 100;
const movePct = stats.moveGenerationTime / overallTime * 100;

console.log(`\n📈 Top bottlenecks:`);

if (constraintPct > 50) {
  console.log(`   🔴 CONSTRAINT EVALUATION is ${constraintPct.toFixed(1)}% of time - parallelization WOULD help`);
} else if (constraintPct > 30) {
  console.log(`   🟡 CONSTRAINT EVALUATION is ${constraintPct.toFixed(1)}% of time - parallelization might help`);
} else {
  console.log(`   🟢 CONSTRAINT EVALUATION is only ${constraintPct.toFixed(1)}% of time - parallelization won't help much`);
}

if (clonePct > 20) {
  console.log(`   🔴 STATE CLONING is ${clonePct.toFixed(1)}% of time - consider incremental updates or copy-on-write`);
} else {
  console.log(`   🟢 STATE CLONING is only ${clonePct.toFixed(1)}% of time - acceptable`);
}

if (movePct > 30) {
  console.log(`   🔴 MOVE GENERATION is ${movePct.toFixed(1)}% of time - optimize operator implementations`);
} else {
  console.log(`   🟢 MOVE GENERATION is only ${movePct.toFixed(1)}% of time - acceptable`);
}

// Check for duplicate evaluation (should be 0 now after optimization)
if (stats.hardConstraintTime > 0) {
  console.log(`\n   ⚠️  Note: Hard constraints evaluated separately:`);
  console.log(`      - In calculateFitness(): ${stats.constraintTime.toFixed(1)} ms total`);
  console.log(`      - In countHardViolations(): ${stats.hardConstraintTime.toFixed(1)} ms total`);
} else {
  console.log(`\n   ✅ Unified constraint evaluation: No redundant hard constraint calls!`);
}

console.log("\n" + "=".repeat(70));
console.log("✅ Profiling complete!");
console.log("=".repeat(70) + "\n");
