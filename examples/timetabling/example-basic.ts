/**
 * Basic example: University course timetabling with v2 core
 *
 * This demonstrates how to use the generic timetable-sa v2 library
 * to solve university course timetabling problems.
 *
 * Run with: npm run example:timetabling
 */

import { SimulatedAnnealing } from 'timetable-sa';
import type { SAConfig, Constraint, MoveGenerator } from 'timetable-sa';
import type { TimetableState } from './types/index.js';
import { loadDataFromExcel } from './data/index.js';
import { generateInitialSolution } from './utils/initial-solution.js';
import {
  NoLecturerConflict,
  NoRoomConflict,
  RoomCapacity,
  NoProdiConflict,
} from './constraints/hard/index.js';
import {
  PreferredTime,
} from './constraints/soft/index.js';
import {
  ChangeTimeSlot,
  ChangeRoom,
  SwapClasses,
} from './moves/index.js';

console.log('='.repeat(70));
console.log('  UNIVERSITY COURSE TIMETABLING - Simulated Annealing v2.0');
console.log('='.repeat(70));

// 1. Load data from Excel
console.log('\n📂 Loading data from Excel file...');
const dataPath = './data_uisi.xlsx';
const data = loadDataFromExcel(dataPath);

console.log(`✅ Data loaded successfully!`);
console.log(`   Rooms: ${data.rooms.length}`);
console.log(`   Lecturers: ${data.lecturers.length}`);
console.log(`   Classes: ${data.classes.length}`);

// 2. Generate initial solution using greedy algorithm
console.log('\n🏗️  Generating initial timetable (greedy algorithm)...');
const initialState = generateInitialSolution(data);

// 3. Define constraints
console.log('\n⚖️  Setting up constraints...');

const constraints: Constraint<TimetableState>[] = [
  // Hard constraints (MUST be satisfied)
  new NoLecturerConflict(),
  new NoRoomConflict(),
  new RoomCapacity(),
  new NoProdiConflict(),

  // Soft constraints (preferences)
  new PreferredTime(10),  // weight = 10
];

console.log(`   Hard constraints: 4`);
console.log(`   Soft constraints: 1`);

// 4. Define move operators
console.log('\n🔄 Setting up move operators...');

const moveGenerators: MoveGenerator<TimetableState>[] = [
  new ChangeTimeSlot(),
  new ChangeRoom(),
  new SwapClasses(),
];

console.log(`   Move operators: ${moveGenerators.length}`);

// 5. Configure Simulated Annealing
console.log('\n⚙️  Configuring Simulated Annealing...');

const config: SAConfig<TimetableState> = {
  initialTemperature: 1000,
  minTemperature: 0.01,
  coolingRate: 0.995,
  maxIterations: 10000,  // Reduced for faster testing
  hardConstraintWeight: 10000,

  // State cloning function
  cloneState: (state) => JSON.parse(JSON.stringify(state)),

  // Reheating to escape local minima
  reheatingThreshold: 1000,
  reheatingFactor: 2.0,
  maxReheats: 3,

  // Logging
  logging: {
    enabled: true,
    level: 'info',
    logInterval: 500,
  },
};

console.log(`   Initial temperature: ${config.initialTemperature}`);
console.log(`   Cooling rate: ${config.coolingRate}`);
console.log(`   Max iterations: ${config.maxIterations}`);

// 6. Create solver and run optimization
console.log('\n🚀 Starting optimization...\n');
console.log('='.repeat(70));

const solver = new SimulatedAnnealing(
  initialState,
  constraints,
  moveGenerators,
  config
);

const solution = solver.solve();

console.log('='.repeat(70));
console.log('\n✨ OPTIMIZATION COMPLETE!\n');

// 7. Display results
console.log('📊 RESULTS:');
console.log(`   Final fitness: ${solution.fitness.toFixed(2)}`);
console.log(`   Hard constraint violations: ${solution.hardViolations}`);
console.log(`   Soft constraint violations: ${solution.softViolations}`);
console.log(`   Total iterations: ${solution.iterations}`);
console.log(`   Reheating events: ${solution.reheats}`);
console.log(`   Final temperature: ${solution.finalTemperature.toFixed(4)}`);
console.log(`   Classes scheduled: ${solution.state.schedule.length}/${data.classes.length}`);

console.log('\n📈 OPERATOR STATISTICS:');
for (const [operatorName, stats] of Object.entries(solution.operatorStats)) {
  console.log(`   ${operatorName}:`);
  console.log(`      Attempts: ${stats.attempts}`);
  console.log(`      Improvements: ${stats.improvements}`);
  console.log(`      Success rate: ${(stats.successRate * 100).toFixed(2)}%`);
}

if (solution.violations.length > 0) {
  console.log(`\n⚠️  VIOLATIONS (${solution.violations.length}):`);
  solution.violations.slice(0, 10).forEach(v => {
    console.log(`   - [${v.constraintType}] ${v.constraintName}: ${v.description || 'No description'}`);
  });
  if (solution.violations.length > 10) {
    console.log(`   ... and ${solution.violations.length - 10} more`);
  }
} else {
  console.log('\n🎉 NO VIOLATIONS - Perfect timetable!');
}

console.log('\n' + '='.repeat(70));
console.log('✅ Example completed successfully!');
console.log('='.repeat(70) + '\n');

// Optional: Save results to JSON
import fs from 'fs';
fs.writeFileSync(
  'timetable-result.json',
  JSON.stringify({
    fitness: solution.fitness,
    hardViolations: solution.hardViolations,
    softViolations: solution.softViolations,
    iterations: solution.iterations,
    schedule: solution.state.schedule,
  }, null, 2)
);

console.log('💾 Results saved to: timetable-result.json\n');
