# Explanation
i run the algorithm 5 times at the same time, it might be could be fast if i only run one at a time, because cpu is used 100% more by this algorithm.
here i resume what the result is

# Unit test
```bash
emmanuelabayor@ade:~/projects/timetable-sa$ bun test
bun test v1.3.3 (274e01c7)

tests/integration/simple-timetabling.test.ts:
✓ Simple Timetabling Integration Tests > Feasible Problem Solving > should solve a simple timetabling problem with conflicts [9.90ms]
✓ Simple Timetabling Integration Tests > Feasible Problem Solving > should maintain solution quality for already-feasible timetable [2.60ms]
✓ Simple Timetabling Integration Tests > Feasible Problem Solving > should optimize soft constraints after satisfying hard constraints [5.66ms]
✓ Simple Timetabling Integration Tests > Operator Effectiveness > should use all move operators during search [5.37ms]
✓ Simple Timetabling Integration Tests > Operator Effectiveness > should track operator success rates [5.60ms]
✓ Simple Timetabling Integration Tests > Constraint Satisfaction > should eliminate all room conflicts [4.02ms]
✓ Simple Timetabling Integration Tests > Constraint Satisfaction > should eliminate all lecturer conflicts [3.69ms]
✓ Simple Timetabling Integration Tests > Constraint Satisfaction > should respect both room AND lecturer constraints simultaneously [3.95ms]
✓ Simple Timetabling Integration Tests > Performance Characteristics > should converge faster with better initial state [7.57ms]
✓ Simple Timetabling Integration Tests > Performance Characteristics > should produce consistent results with same seed (deterministic cloning) [4.22ms]
✓ Simple Timetabling Integration Tests > Scalability > should handle larger timetabling problems [12.38ms]

tests/core/acceptance-probability.test.ts:
✓ Acceptance Probability Logic > Phase 1: Hard Constraint Elimination > should ALWAYS accept moves that reduce hard violations [0.45ms]
✓ Acceptance Probability Logic > Phase 1: Hard Constraint Elimination > should NEVER accept moves that increase hard violations in Phase 1 [8.11ms]
✓ Acceptance Probability Logic > Phase 1: Hard Constraint Elimination > should use Metropolis criterion for moves with same hard violations [0.59ms]
✓ Acceptance Probability Logic > Phase 1: Hard Constraint Elimination > should prioritize hard violations over soft in Phase 1 [0.36ms]
✓ Acceptance Probability Logic > Phase 2: Soft Constraint Optimization > should STRICTLY reject moves that increase hard violations in Phase 2 [0.41ms]
✓ Acceptance Probability Logic > Phase 2: Soft Constraint Optimization > should accept soft-improving moves in Phase 2 [0.19ms]
✓ Acceptance Probability Logic > Phase 2: Soft Constraint Optimization > should use Metropolis for soft-worsening moves (at high temp) [0.30ms]
✓ Acceptance Probability Logic > Phase 2: Soft Constraint Optimization > should maintain hard constraint satisfaction throughout Phase 2 [0.53ms]
✓ Acceptance Probability Logic > Temperature-Dependent Acceptance > should accept more worsening moves at high temperature [0.20ms]
✓ Acceptance Probability Logic > Temperature-Dependent Acceptance > should accept fewer worsening moves as temperature decreases [0.28ms]
✓ Acceptance Probability Logic > Acceptance Probability Edge Cases > should handle zero temperature gracefully [0.09ms]
✓ Acceptance Probability Logic > Acceptance Probability Edge Cases > should handle identical fitness values [0.18ms]
✓ Acceptance Probability Logic > Acceptance Probability Edge Cases > should handle very large fitness differences [0.56ms]
✓ Acceptance Probability Logic > Phase Transition > should transition from Phase 1 to Phase 2 when hard violations reach 0 [0.13ms]
✓ Acceptance Probability Logic > Phase Transition > should enforce stricter acceptance in Phase 2 than Phase 1 [0.03ms]

tests/core/SimulatedAnnealing.test.ts:
✓ SimulatedAnnealing Core Engine > Initialization > should initialize with valid configuration [0.49ms]
✓ SimulatedAnnealing Core Engine > Initialization > should separate hard and soft constraints [0.31ms]
✓ SimulatedAnnealing Core Engine > Initialization > should initialize operator statistics [0.95ms]
✓ SimulatedAnnealing Core Engine > Optimization Loop > should complete optimization within maxIterations [0.89ms]
✓ SimulatedAnnealing Core Engine > Optimization Loop > should respect minTemperature stopping condition [0.13ms]
✓ SimulatedAnnealing Core Engine > Optimization Loop > should stop early if Phase 1 eliminates all hard violations [1.40ms]
✓ SimulatedAnnealing Core Engine > Optimization Loop > should handle empty move generators gracefully [0.12ms]
✓ SimulatedAnnealing Core Engine > Optimization Loop > should handle all non-applicable move generators [0.24ms]
✓ SimulatedAnnealing Core Engine > Constraint Evaluation > should correctly evaluate hard constraints [2.11ms]
✓ SimulatedAnnealing Core Engine > Constraint Evaluation > should correctly count violations using getViolations() [1.08ms]
✓ SimulatedAnnealing Core Engine > Constraint Evaluation > should apply correct penalty weights for soft constraints [0.35ms]
✓ SimulatedAnnealing Core Engine > Constraint Evaluation > should heavily penalize hard constraints vs soft [1.08ms]
✓ SimulatedAnnealing Core Engine > Solution Quality > should find feasible solution for solvable problem [1.71ms]
✓ SimulatedAnnealing Core Engine > Solution Quality > should improve fitness over iterations [1.09ms]
✓ SimulatedAnnealing Core Engine > Solution Quality > should optimize soft constraints after hard constraints satisfied [0.94ms]
✓ SimulatedAnnealing Core Engine > Solution Quality > should handle unsolvable problems gracefully [31.46ms]
✓ SimulatedAnnealing Core Engine > Operator Statistics > should track operator attempts [0.66ms]
✓ SimulatedAnnealing Core Engine > Operator Statistics > should track operator success rates [0.52ms]
✓ SimulatedAnnealing Core Engine > Operator Statistics > should calculate success rate as improvements/attempts [0.57ms]
✓ SimulatedAnnealing Core Engine > Reheating Mechanism > should reheat when stuck in local minima [1.33ms]
✓ SimulatedAnnealing Core Engine > Reheating Mechanism > should not exceed maxReheats [32.99ms]
✓ SimulatedAnnealing Core Engine > Solution Output > should return complete solution object [0.70ms]
✓ SimulatedAnnealing Core Engine > Solution Output > should include violation details [0.25ms]
✓ SimulatedAnnealing Core Engine > Solution Output > should not mutate initial state [0.48ms]
✓ SimulatedAnnealing Core Engine > Edge Cases > should handle state with no assignments [0.17ms]
✓ SimulatedAnnealing Core Engine > Edge Cases > should handle single assignment state [0.17ms]
✓ SimulatedAnnealing Core Engine > Edge Cases > should handle very high temperature [0.53ms]
✓ SimulatedAnnealing Core Engine > Edge Cases > should handle very low cooling rate [0.30ms]

tests/core/fitness-calculation.test.ts:
✓ Fitness Calculation > Basic Fitness Calculation > should calculate 0 fitness for fully satisfied constraints [0.38ms]
✓ Fitness Calculation > Basic Fitness Calculation > should calculate high fitness for violated hard constraints [7.32ms]
✓ Fitness Calculation > Basic Fitness Calculation > should calculate fitness with soft constraint penalties [0.23ms]
✓ Fitness Calculation > Constraint Weighting > should weight hard constraints much higher than soft [6.56ms]
✓ Fitness Calculation > Constraint Weighting > should apply custom soft constraint weights correctly [0.23ms]
✓ Fitness Calculation > Constraint Weighting > should use default weight of 10 for soft constraints without explicit weight [0.10ms]
✓ Fitness Calculation > Partial Satisfaction > should handle partial constraint satisfaction (score = 0.5) [7.44ms]
✓ Fitness Calculation > Partial Satisfaction > should calculate fitness correctly for gradual improvements [21.63ms]
✓ Fitness Calculation > Multiple Constraints > should sum penalties from multiple hard constraints [6.05ms]
✓ Fitness Calculation > Multiple Constraints > should sum penalties from multiple soft constraints [0.29ms]
✓ Fitness Calculation > Multiple Constraints > should combine hard and soft penalties correctly [5.79ms]
✓ Fitness Calculation > Violation Counting > should count hard violations correctly using getViolations() [5.64ms]
✓ Fitness Calculation > Violation Counting > should count multiple violations from single constraint [5.20ms]
✓ Fitness Calculation > Violation Counting > should provide violation details [7.00ms]
✓ Fitness Calculation > Edge Cases > should handle constraint score = 0 (complete violation) [6.90ms]
✓ Fitness Calculation > Edge Cases > should handle constraint score = 1 (complete satisfaction) [0.28ms]
✓ Fitness Calculation > Edge Cases > should handle no constraints [0.15ms]
✓ Fitness Calculation > Edge Cases > should handle very large penalty values [5.28ms]
✓ Fitness Calculation > Edge Cases > should handle fractional scores correctly [9.53ms]

 73 pass
 0 fail
 133 expect() calls
Ran 73 tests across 4 files. [292.00ms]
```

# Trial 1
```bash
emmanuelabayor@ade:~/projects/timetable-sa$ bun examples/timetabling/example-basic.ts
======================================================================
  UNIVERSITY COURSE TIMETABLING - Simulated Annealing v2.0
======================================================================

📂 Loading data from Excel file...
✅ Data loaded successfully!
   Rooms: 33
   Lecturers: 99
   Classes: 373

🏗️  Generating initial timetable (greedy algorithm)...

Generating initial solution for 373 classes...
   🔀 Randomization enabled - shuffling class order
  ⚠️  Skipping GS13TH46: No lecturers on class Skripsi
  ⚠️  Skipping GS13CZ02: No lecturers on class Kewarganegaraan
  ⚠️  Skipping GS13CZ02: No lecturers on class Kewarganegaraan
  ⚠️  Skipping CE11UT46: No lecturers on class Skripsi
  ⚠️  Skipping AC135343: No lecturers on class Skripsi
  ⚠️  Skipping GS13IP12: No lecturers on class PROYEK INTERDISIPLIN
  ⚠️  Skipping GS13IP12: No lecturers on class Proyek Interdisipliner
  ⚠️  Skipping VD13KP02: No lecturers on class Kerja Praktik
  ⚠️  Skipping GS13IP12: No lecturers on class Proyek Interdisiplin
  ⚠️  Skipping GS13PW02: No lecturers on class Kerja Praktik
  ⚠️  Skipping GS13PW02: No lecturers on class Praktik Kerja Lapang
  ⚠️  Skipping GS13PW02: No lecturers on class Kerja Praktik/Magang
  ⚠️  Skipping GS13IP12: No lecturers on class Proyek Interdisipliner
  ⚠️  Skipping MM23RS03: No lecturers on class Research Seminar
  ⚠️  Skipping GS13PW02: No lecturers on class Kerja Praktik
  ⚠️  Skipping GS13PW02: No lecturers on class KERJA PRAKTIK
  ⚠️  Skipping GS13CZ02: No lecturers on class Kewarganegaraan

✅ Initial solution generated:
   Successfully placed: 356/373
   Failed to place: 17/373


⚖️  Setting up constraints...
   Hard constraints: 11
   Soft constraints: 8

🔄 Setting up move operators...
   Targeted operators: 5 (FixFridayPrayerConflict, FixLecturerConflict, etc.)
   General operators: 4 (including high-success ChangeTimeSlotAndRoom)
   Total operators: 10

⚙️  Configuring Simulated Annealing...
   Initial temperature: 100000
   Cooling rate: 0.9998
   Max iterations: 60000

🚀 Starting optimization...

======================================================================
[2025-12-29T21:34:45.651Z] [INFO] Simulated Annealing initialized {"hardConstraints":11,"softConstraints":8,"moveGenerators":10,"config":{"initialTemperature":100000,"minTemperature":1e-7,"coolingRate":0.9998,"maxIterations":60000}}
[2025-12-29T21:34:45.652Z] [INFO] Starting optimization...
[2025-12-29T21:34:45.652Z] [INFO] Phase 1: Eliminating hard constraint violations
[2025-12-29T21:34:45.687Z] [INFO] Initial state {"fitness":"155580.84","hardViolations":10}
[2025-12-29T21:34:53.314Z] [INFO] Phase 1 complete: Hard violations = 0
[2025-12-29T21:34:53.314Z] [INFO] Phase 2: Optimizing soft constraints
[2025-12-29T21:34:57.180Z] [INFO] [Phase 2] Iteration 500: Temp = 93294.69, Current = 25.95, Best = 25.84
[2025-12-29T21:35:16.620Z] [INFO] [Phase 2] Iteration 1500: Temp = 83358.62, Current = 26.42, Best = 25.84
[2025-12-29T21:35:47.114Z] [INFO] [Phase 2] Iteration 3000: Temp = 70409.99, Current = 26.56, Best = 25.84
[2025-12-29T21:35:56.514Z] [INFO] [Phase 2] Iteration 3500: Temp = 66721.67, Current = 26.60, Best = 25.84
[2025-12-29T21:36:06.182Z] [INFO] [Phase 2] Iteration 4000: Temp = 62961.53, Current = 26.54, Best = 25.84
[2025-12-29T21:36:28.566Z] [INFO] [Phase 2] Iteration 5000: Temp = 55975.39, Current = 26.65, Best = 25.84
[2025-12-29T21:36:49.417Z] [INFO] [Phase 2] Iteration 6000: Temp = 50164.18, Current = 26.64, Best = 25.84
[2025-12-29T21:37:09.214Z] [INFO] [Phase 2] Iteration 7000: Temp = 44526.71, Current = 26.80, Best = 25.84
[2025-12-29T21:37:19.237Z] [INFO] [Phase 2] Iteration 7500: Temp = 41858.01, Current = 26.79, Best = 25.84
[2025-12-29T21:37:50.688Z] [INFO] [Phase 2] Iteration 9000: Temp = 35032.12, Current = 26.70, Best = 25.84
[2025-12-29T21:38:02.501Z] [INFO] [Phase 2] Iteration 9500: Temp = 32879.82, Current = 26.89, Best = 25.84
[2025-12-29T21:38:13.422Z] [INFO] [Phase 2] Iteration 10000: Temp = 30724.25, Current = 27.08, Best = 25.84
[2025-12-29T21:38:23.848Z] [INFO] [Phase 2] Iteration 10500: Temp = 28784.75, Current = 27.23, Best = 25.84
[2025-12-29T21:38:55.894Z] [INFO] [Phase 2] Iteration 12000: Temp = 23946.62, Current = 27.26, Best = 25.84
[2025-12-29T21:39:17.577Z] [INFO] [Phase 2] Iteration 13000: Temp = 21276.76, Current = 27.28, Best = 25.84
[2025-12-29T21:39:27.492Z] [INFO] [Phase 2] Iteration 13500: Temp = 19981.55, Current = 27.25, Best = 25.84
[2025-12-29T21:39:49.387Z] [INFO] [Phase 2] Iteration 14500: Temp = 17601.72, Current = 27.18, Best = 25.84
[2025-12-29T21:40:09.435Z] [INFO] [Phase 2] Iteration 15500: Temp = 15592.41, Current = 27.16, Best = 25.84
[2025-12-29T21:40:30.705Z] [INFO] [Phase 2] Iteration 16500: Temp = 13840.13, Current = 27.22, Best = 25.84
[2025-12-29T21:40:52.594Z] [INFO] [Phase 2] Iteration 17500: Temp = 12230.83, Current = 27.35, Best = 25.84
[2025-12-29T21:41:11.613Z] [INFO] [Phase 2] Iteration 18500: Temp = 10897.66, Current = 27.50, Best = 25.84
[2025-12-29T21:41:33.155Z] [INFO] [Phase 2] Iteration 19500: Temp = 9661.38, Current = 27.45, Best = 25.84
[2025-12-29T21:42:04.673Z] [INFO] [Phase 2] Iteration 21000: Temp = 8056.81, Current = 27.40, Best = 25.84
[2025-12-29T21:42:13.858Z] [INFO] [Phase 2] Iteration 21500: Temp = 7608.85, Current = 27.44, Best = 25.84
[2025-12-29T21:42:23.705Z] [INFO] [Phase 2] Iteration 22000: Temp = 7165.71, Current = 27.58, Best = 25.84
[2025-12-29T21:42:45.278Z] [INFO] [Phase 2] Iteration 23000: Temp = 6361.69, Current = 27.64, Best = 25.84
[2025-12-29T21:42:54.478Z] [INFO] [Phase 2] Iteration 23500: Temp = 6003.18, Current = 27.56, Best = 25.84
[2025-12-29T21:43:04.021Z] [INFO] [Phase 2] Iteration 24000: Temp = 5660.33, Current = 27.37, Best = 25.84
[2025-12-29T21:43:15.527Z] [INFO] [Phase 2] Iteration 24500: Temp = 5338.14, Current = 27.43, Best = 25.84
[2025-12-29T21:43:24.979Z] [INFO] [Phase 2] Iteration 25000: Temp = 5035.29, Current = 27.57, Best = 25.84
[2025-12-29T21:43:34.718Z] [INFO] [Phase 2] Iteration 25500: Temp = 4748.67, Current = 27.57, Best = 25.84
[2025-12-29T21:44:16.582Z] [INFO] [Phase 2] Iteration 27500: Temp = 3763.10, Current = 27.41, Best = 25.84
[2025-12-29T21:44:35.088Z] [INFO] [Phase 2] Iteration 28500: Temp = 3366.36, Current = 27.51, Best = 25.84
[2025-12-29T21:44:44.813Z] [INFO] [Phase 2] Iteration 29000: Temp = 3172.83, Current = 27.40, Best = 25.84
[2025-12-29T21:44:56.778Z] [INFO] [Phase 2] Iteration 29500: Temp = 2979.69, Current = 27.25, Best = 25.84
[2025-12-29T21:45:05.838Z] [INFO] [Phase 2] Iteration 30000: Temp = 2822.47, Current = 27.27, Best = 25.84
[2025-12-29T21:45:15.096Z] [INFO] [Phase 2] Iteration 30500: Temp = 2671.41, Current = 27.30, Best = 25.84
[2025-12-29T21:45:35.482Z] [INFO] [Phase 2] Iteration 31500: Temp = 2393.60, Current = 27.47, Best = 25.84
[2025-12-29T21:45:54.442Z] [INFO] [Phase 2] Iteration 32500: Temp = 2126.30, Current = 27.35, Best = 25.84
[2025-12-29T21:46:06.045Z] [INFO] [Phase 2] Iteration 33000: Temp = 2004.07, Current = 27.28, Best = 25.84
[2025-12-29T21:46:14.787Z] [INFO] [Phase 2] Iteration 33500: Temp = 1902.13, Current = 27.39, Best = 25.84
[2025-12-29T21:46:35.874Z] [INFO] [Phase 2] Iteration 34500: Temp = 1689.72, Current = 27.42, Best = 25.84
[2025-12-29T21:46:45.758Z] [INFO] [Phase 2] Iteration 35000: Temp = 1592.26, Current = 27.46, Best = 25.84
[2025-12-29T21:47:18.006Z] [INFO] [Phase 2] Iteration 36500: Temp = 1324.90, Current = 27.47, Best = 25.84
[2025-12-29T21:47:27.744Z] [INFO] [Phase 2] Iteration 37000: Temp = 1247.24, Current = 27.52, Best = 25.84
[2025-12-29T21:47:36.977Z] [INFO] [Phase 2] Iteration 37500: Temp = 1179.54, Current = 27.72, Best = 25.84
[2025-12-29T21:47:48.551Z] [INFO] [Phase 2] Iteration 38000: Temp = 1113.29, Current = 27.65, Best = 25.84
[2025-12-29T21:47:58.000Z] [INFO] [Phase 2] Iteration 38500: Temp = 1049.50, Current = 27.62, Best = 25.84
[2025-12-29T21:48:05.683Z] [INFO] [Phase 2] Reheating #1: Temperature = 149986.45, Fitness = 25.84
[2025-12-29T21:48:19.859Z] [INFO] [Phase 2] Iteration 39500: Temp = 138786.56, Current = 27.68, Best = 25.84
[2025-12-29T21:48:29.802Z] [INFO] [Phase 2] Iteration 40000: Temp = 130285.85, Current = 27.60, Best = 25.84
[2025-12-29T21:48:51.589Z] [INFO] [Phase 2] Iteration 41000: Temp = 115274.77, Current = 27.76, Best = 25.84
[2025-12-29T21:49:01.589Z] [INFO] [Phase 2] Iteration 41500: Temp = 108192.52, Current = 27.75, Best = 25.84
[2025-12-29T21:49:11.659Z] [INFO] [Phase 2] Iteration 42000: Temp = 101504.78, Current = 27.73, Best = 25.84
[2025-12-29T21:49:34.593Z] [INFO] [Phase 2] Iteration 43000: Temp = 88791.64, Current = 27.84, Best = 25.84
[2025-12-29T21:50:17.934Z] [INFO] [Phase 2] Iteration 45000: Temp = 68474.85, Current = 27.63, Best = 25.84
[2025-12-29T21:50:39.458Z] [INFO] [Phase 2] Iteration 46000: Temp = 60646.04, Current = 27.66, Best = 25.84
[2025-12-29T21:50:48.741Z] [INFO] [Phase 2] Iteration 46500: Temp = 57216.86, Current = 27.66, Best = 25.84
[2025-12-29T21:50:58.711Z] [INFO] [Phase 2] Iteration 47000: Temp = 53680.09, Current = 27.52, Best = 25.84
[2025-12-29T21:51:10.267Z] [INFO] [Phase 2] Iteration 47500: Temp = 50644.79, Current = 27.62, Best = 25.84
[2025-12-29T21:51:40.705Z] [INFO] [Phase 2] Iteration 49000: Temp = 41696.49, Current = 27.58, Best = 25.84
[2025-12-29T21:51:53.538Z] [INFO] [Phase 2] Iteration 49500: Temp = 39017.50, Current = 27.56, Best = 25.84
[2025-12-29T21:52:03.737Z] [INFO] [Phase 2] Iteration 50000: Temp = 36656.99, Current = 27.67, Best = 25.84
[2025-12-29T21:52:14.008Z] [INFO] [Phase 2] Iteration 50500: Temp = 34329.24, Current = 27.61, Best = 25.84
[2025-12-29T21:52:26.284Z] [INFO] [Phase 2] Iteration 51000: Temp = 32142.88, Current = 27.63, Best = 25.84
[2025-12-29T21:52:36.123Z] [INFO] [Phase 2] Iteration 51500: Temp = 30228.49, Current = 27.61, Best = 25.84
[2025-12-29T21:52:57.660Z] [INFO] [Phase 2] Iteration 52500: Temp = 26718.93, Current = 27.55, Best = 25.84
[2025-12-29T21:53:07.636Z] [INFO] [Phase 2] Iteration 53000: Temp = 25112.51, Current = 27.72, Best = 25.84
[2025-12-29T21:53:29.601Z] [INFO] [Phase 2] Iteration 54000: Temp = 22170.30, Current = 27.60, Best = 25.84
[2025-12-29T21:53:58.554Z] [INFO] [Phase 2] Iteration 55500: Temp = 18521.57, Current = 27.74, Best = 25.84
[2025-12-29T21:54:29.474Z] [INFO] [Phase 2] Iteration 57000: Temp = 15448.59, Current = 27.47, Best = 25.84
[2025-12-29T21:54:52.155Z] [INFO] [Phase 2] Iteration 58000: Temp = 13516.41, Current = 27.61, Best = 25.84
[2025-12-29T21:55:01.961Z] [INFO] [Phase 2] Iteration 58500: Temp = 12688.52, Current = 27.58, Best = 25.84
[2025-12-29T21:55:14.559Z] [INFO] [Phase 2] Iteration 59000: Temp = 11923.27, Current = 27.61, Best = 25.84
[2025-12-29T21:55:24.751Z] [INFO] [Phase 2] Iteration 59500: Temp = 11186.25, Current = 27.51, Best = 25.84
[2025-12-29T21:55:34.817Z] [INFO] [Phase 2] Iteration 60000: Temp = 10524.22, Current = 27.47, Best = 25.84
[2025-12-29T21:55:34.831Z] [INFO] Optimization complete {"iterations":60000,"reheats":1,"finalTemperature":"10524.2197","fitness":"25.84","hardViolations":0,"softViolations":8}
[2025-12-29T21:55:34.831Z] [INFO] Operator Statistics:
[2025-12-29T21:55:34.831Z] [INFO]   Fix Friday Prayer Conflict: Attempts = 0, Improvements = 0, Accepted = 0, Success Rate = 0.00%
[2025-12-29T21:55:34.831Z] [INFO]   Swap Friday with Non-Friday: Attempts = 0, Improvements = 0, Accepted = 0, Success Rate = 0.00%
[2025-12-29T21:55:34.831Z] [INFO]   Fix Lecturer Conflict: Attempts = 0, Improvements = 0, Accepted = 0, Success Rate = 0.00%
[2025-12-29T21:55:34.831Z] [INFO]   Fix Room Conflict: Attempts = 1, Improvements = 1, Accepted = 1, Success Rate = 100.00%
[2025-12-29T21:55:34.832Z] [INFO]   Fix Max Daily Periods: Attempts = 7, Improvements = 6, Accepted = 7, Success Rate = 85.71%
[2025-12-29T21:55:34.832Z] [INFO]   Fix Room Capacity: Attempts = 0, Improvements = 0, Accepted = 0, Success Rate = 0.00%
[2025-12-29T21:55:34.832Z] [INFO]   Change Time Slot and Room: Attempts = 6331, Improvements = 695, Accepted = 5986, Success Rate = 10.98%
[2025-12-29T21:55:34.832Z] [INFO]   Change Time Slot: Attempts = 4996, Improvements = 252, Accepted = 4351, Success Rate = 5.04%
[2025-12-29T21:55:34.832Z] [INFO]   Change Room: Attempts = 10293, Improvements = 783, Accepted = 10293, Success Rate = 7.61%
[2025-12-29T21:55:34.832Z] [INFO]   Swap Classes: Attempts = 14679, Improvements = 110, Accepted = 783, Success Rate = 0.75%
======================================================================

✨ OPTIMIZATION COMPLETE!

Cache stats: {
  timeCache: {
    timeToMinutes: 20,
    minutesToTime: 17,
  },
  endTimeCache: 287,
  prayerOverlapCache: 287,
  totalEntries: 611,
}
📊 RESULTS:
   Final fitness: 25.84
   Hard constraint violations: 0
   Soft constraint violations: 8
   Total iterations: 60000
   Reheating events: 1
   Final temperature: 10524.2197
   Classes scheduled: 356/373

📈 OPERATOR STATISTICS:
   Fix Friday Prayer Conflict:
      Attempts: 0
      Improvements: 0
      Success rate: 0.00%
   Swap Friday with Non-Friday:
      Attempts: 0
      Improvements: 0
      Success rate: 0.00%
   Fix Lecturer Conflict:
      Attempts: 0
      Improvements: 0
      Success rate: 0.00%
   Fix Room Conflict:
      Attempts: 1
      Improvements: 1
      Success rate: 100.00%
   Fix Max Daily Periods:
      Attempts: 7
      Improvements: 6
      Success rate: 85.71%
   Fix Room Capacity:
      Attempts: 0
      Improvements: 0
      Success rate: 0.00%
   Change Time Slot and Room:
      Attempts: 6331
      Improvements: 695
      Success rate: 10.98%
   Change Time Slot:
      Attempts: 4996
      Improvements: 252
      Success rate: 5.04%
   Change Room:
      Attempts: 10293
      Improvements: 783
      Success rate: 7.61%
   Swap Classes:
      Attempts: 14679
      Improvements: 110
      Success rate: 0.75%

⚠️  VIOLATIONS (8):
   - [soft] Preferred Time: Classes not scheduled in lecturer's preferred time slots
   - [soft] Preferred Room: Classes not assigned to lecturer's preferred room
   - [soft] Transit Time: Insufficient transit time between consecutive classes for lecturers
   - [soft] Compactness: Large gaps (>60 min) between consecutive classes for same prodi
   - [soft] Prayer Time Overlap: Classes overlapping with prayer times (especially Friday 12:00-13:00)
   - [soft] Evening Class Priority: Evening classes (sore) not starting at optimal time (18:30)
   - [soft] Research Day: Classes scheduled on lecturer's designated research day
   - [soft] Overflow Penalty: Lab/room type mismatch (non-lab class in lab room, or lab class not in lab)

======================================================================
✅ Example completed successfully!
======================================================================

💾 Results saved to: timetable-result.json
```

# Trial 2
```bash
emmanuelabayor@ade:~/projects/timetable-sa$ bun examples/timetabling/example-basic.ts
======================================================================
  UNIVERSITY COURSE TIMETABLING - Simulated Annealing v2.0
======================================================================

📂 Loading data from Excel file...
✅ Data loaded successfully!
   Rooms: 33
   Lecturers: 99
   Classes: 373

🏗️  Generating initial timetable (greedy algorithm)...

Generating initial solution for 373 classes...
   🔀 Randomization enabled - shuffling class order
  ⚠️  Skipping GS13PW02: No lecturers on class Kerja Praktik
  ⚠️  Skipping GS13PW02: No lecturers on class KERJA PRAKTIK
  ⚠️  Skipping GS13TH46: No lecturers on class Skripsi
  ⚠️  Skipping GS13PW02: No lecturers on class Praktik Kerja Lapang
  ⚠️  Skipping CE11UT46: No lecturers on class Skripsi
  ⚠️  Skipping GS13CZ02: No lecturers on class Kewarganegaraan
  ⚠️  Skipping VD13KP02: No lecturers on class Kerja Praktik
  ⚠️  Skipping GS13IP12: No lecturers on class Proyek Interdisipliner
  ⚠️  Skipping GS13IP12: No lecturers on class PROYEK INTERDISIPLIN
  ⚠️  Skipping GS13PW02: No lecturers on class Kerja Praktik/Magang
  ⚠️  Skipping GS13IP12: No lecturers on class Proyek Interdisiplin
  ⚠️  Skipping GS13CZ02: No lecturers on class Kewarganegaraan
  ⚠️  Skipping GS13PW02: No lecturers on class Kerja Praktik
  ⚠️  Skipping AC135343: No lecturers on class Skripsi
  ⚠️  Skipping GS13CZ02: No lecturers on class Kewarganegaraan
  ⚠️  Skipping GS13IP12: No lecturers on class Proyek Interdisipliner
  ⚠️  Skipping MM23RS03: No lecturers on class Research Seminar

✅ Initial solution generated:
   Successfully placed: 356/373
   Failed to place: 17/373


⚖️  Setting up constraints...
   Hard constraints: 11
   Soft constraints: 8

🔄 Setting up move operators...
   Targeted operators: 5 (FixFridayPrayerConflict, FixLecturerConflict, etc.)
   General operators: 4 (including high-success ChangeTimeSlotAndRoom)
   Total operators: 10

⚙️  Configuring Simulated Annealing...
   Initial temperature: 100000
   Cooling rate: 0.9998
   Max iterations: 60000

🚀 Starting optimization...

======================================================================
[2025-12-29T21:34:55.419Z] [INFO] Simulated Annealing initialized {"hardConstraints":11,"softConstraints":8,"moveGenerators":10,"config":{"initialTemperature":100000,"minTemperature":1e-7,"coolingRate":0.9998,"maxIterations":60000}}
[2025-12-29T21:34:55.420Z] [INFO] Starting optimization...
[2025-12-29T21:34:55.420Z] [INFO] Phase 1: Eliminating hard constraint violations
[2025-12-29T21:34:55.460Z] [INFO] Initial state {"fitness":"238120.81","hardViolations":14}
[2025-12-29T21:35:12.130Z] [INFO] [Phase 1] Iteration 1000: Temp = 91630.25, Hard violations = 6, Best = 6
[2025-12-29T21:35:29.945Z] [INFO] [Phase 1] Iteration 2000: Temp = 84483.25, Hard violations = 4, Best = 4
[2025-12-29T21:35:49.880Z] [INFO] [Phase 1] Iteration 3000: Temp = 75939.93, Hard violations = 3, Best = 3
[2025-12-29T21:36:00.971Z] [INFO] [Phase 1] Iteration 3500: Temp = 71345.65, Hard violations = 3, Best = 3
[2025-12-29T21:36:14.191Z] [INFO] [Phase 1] Iteration 4000: Temp = 67271.09, Hard violations = 2, Best = 2
[2025-12-29T21:36:25.047Z] [INFO] [Phase 1] Iteration 4500: Temp = 63201.26, Hard violations = 2, Best = 2
[2025-12-29T21:36:36.123Z] [INFO] [Phase 1] Iteration 5000: Temp = 59413.30, Hard violations = 2, Best = 2
[2025-12-29T21:36:59.641Z] [INFO] [Phase 1] Iteration 6000: Temp = 52694.24, Hard violations = 2, Best = 2
[2025-12-29T21:37:23.971Z] [INFO] [Phase 1] Iteration 7000: Temp = 46325.53, Hard violations = 2, Best = 2
[2025-12-29T21:37:34.705Z] [INFO] [Phase 1] Iteration 7500: Temp = 43540.30, Hard violations = 1, Best = 1
[2025-12-29T21:38:07.171Z] [INFO] [Phase 1] Iteration 9000: Temp = 36156.92, Hard violations = 1, Best = 1
[2025-12-29T21:38:17.509Z] [INFO] [Phase 1] Iteration 9500: Temp = 34037.48, Hard violations = 1, Best = 1
[2025-12-29T21:38:34.131Z] [INFO] Phase 1 complete: Hard violations = 0
[2025-12-29T21:38:34.131Z] [INFO] Phase 2: Optimizing soft constraints
[2025-12-29T21:38:39.489Z] [INFO] [Phase 2] Iteration 10500: Temp = 30212.34, Current = 27.50, Best = 27.49
[2025-12-29T21:39:11.303Z] [INFO] [Phase 2] Iteration 12000: Temp = 25336.17, Current = 27.44, Best = 27.43
[2025-12-29T21:39:22.038Z] [INFO] [Phase 2] Iteration 12500: Temp = 23789.08, Current = 27.49, Best = 27.34
[2025-12-29T21:39:33.116Z] [INFO] [Phase 2] Iteration 13000: Temp = 22225.04, Current = 27.23, Best = 27.22
[2025-12-29T21:39:45.703Z] [INFO] [Phase 2] Iteration 13500: Temp = 20826.23, Current = 27.25, Best = 27.18
[2025-12-29T21:39:55.472Z] [INFO] [Phase 2] Iteration 14000: Temp = 19644.70, Current = 27.27, Best = 27.18
[2025-12-29T21:40:17.181Z] [INFO] [Phase 2] Iteration 15000: Temp = 17444.00, Current = 27.38, Best = 27.18
[2025-12-29T21:40:36.595Z] [INFO] [Phase 2] Iteration 16000: Temp = 15530.16, Current = 27.37, Best = 27.18
[2025-12-29T21:41:08.001Z] [INFO] [Phase 2] Iteration 17500: Temp = 12997.62, Current = 27.45, Best = 27.18
[2025-12-29T21:41:29.400Z] [INFO] [Phase 2] Iteration 18500: Temp = 11539.25, Current = 27.39, Best = 27.18
[2025-12-29T21:41:39.323Z] [INFO] [Phase 2] Iteration 19000: Temp = 10858.50, Current = 27.34, Best = 27.18
[2025-12-29T21:41:49.208Z] [INFO] [Phase 2] Iteration 19500: Temp = 10199.53, Current = 27.39, Best = 27.18
[2025-12-29T21:42:01.097Z] [INFO] [Phase 2] Iteration 20000: Temp = 9615.11, Current = 27.47, Best = 27.18
[2025-12-29T21:42:11.399Z] [INFO] [Phase 2] Iteration 20500: Temp = 9015.36, Current = 27.26, Best = 27.18
[2025-12-29T21:42:21.605Z] [INFO] [Phase 2] Iteration 21000: Temp = 8476.72, Current = 27.29, Best = 27.18
[2025-12-29T21:42:33.388Z] [INFO] [Phase 2] Iteration 21500: Temp = 8000.61, Current = 27.32, Best = 27.18
[2025-12-29T21:42:43.006Z] [INFO] [Phase 2] Iteration 22000: Temp = 7549.73, Current = 27.44, Best = 27.18
[2025-12-29T21:43:01.692Z] [INFO] [Phase 2] Iteration 23000: Temp = 6748.37, Current = 27.36, Best = 27.18
[2025-12-29T21:43:13.475Z] [INFO] [Phase 2] Iteration 23500: Temp = 6357.88, Current = 27.49, Best = 27.18
[2025-12-29T21:43:33.073Z] [INFO] [Phase 2] Iteration 24500: Temp = 5625.35, Current = 27.51, Best = 27.18
[2025-12-29T21:43:45.586Z] [INFO] [Phase 2] Iteration 25000: Temp = 5269.19, Current = 27.45, Best = 27.18
[2025-12-29T21:44:17.134Z] [INFO] [Phase 2] Iteration 26500: Temp = 4400.23, Current = 27.45, Best = 27.18
[2025-12-29T21:44:26.401Z] [INFO] [Phase 2] Iteration 27000: Temp = 4163.07, Current = 27.51, Best = 27.18
[2025-12-29T21:44:35.991Z] [INFO] [Phase 2] Iteration 27500: Temp = 3932.39, Current = 27.46, Best = 27.18
[2025-12-29T21:44:45.419Z] [INFO] [Phase 2] Iteration 28000: Temp = 3715.23, Current = 27.48, Best = 27.18
[2025-12-29T21:44:57.285Z] [INFO] [Phase 2] Iteration 28500: Temp = 3493.26, Current = 27.45, Best = 27.18
[2025-12-29T21:45:06.934Z] [INFO] [Phase 2] Iteration 29000: Temp = 3293.76, Current = 27.43, Best = 27.18
[2025-12-29T21:45:27.764Z] [INFO] [Phase 2] Iteration 30000: Temp = 2941.79, Current = 27.48, Best = 27.18
[2025-12-29T21:46:50.534Z] [INFO] [Phase 2] Iteration 34000: Temp = 1824.62, Current = 27.74, Best = 27.18
[2025-12-29T21:47:12.817Z] [INFO] [Phase 2] Iteration 35000: Temp = 1613.10, Current = 27.67, Best = 27.18
[2025-12-29T21:47:44.303Z] [INFO] [Phase 2] Iteration 36500: Temp = 1352.75, Current = 27.61, Best = 27.18
[2025-12-29T21:47:54.108Z] [INFO] [Phase 2] Iteration 37000: Temp = 1272.69, Current = 27.57, Best = 27.18
[2025-12-29T21:48:03.882Z] [INFO] [Phase 2] Iteration 37500: Temp = 1199.77, Current = 27.64, Best = 27.18
[2025-12-29T21:48:35.198Z] [INFO] [Phase 2] Iteration 39000: Temp = 1006.93, Current = 27.57, Best = 27.18
[2025-12-29T21:48:36.353Z] [INFO] [Phase 2] Reheating #1: Temperature = 149986.45, Fitness = 27.18
[2025-12-29T21:48:45.022Z] [INFO] [Phase 2] Iteration 39500: Temp = 142214.95, Current = 27.65, Best = 27.18
[2025-12-29T21:48:56.826Z] [INFO] [Phase 2] Iteration 40000: Temp = 133744.80, Current = 27.67, Best = 27.18
[2025-12-29T21:49:47.563Z] [INFO] [Phase 2] Iteration 42500: Temp = 99494.65, Current = 27.63, Best = 27.18
[2025-12-29T21:50:08.101Z] [INFO] [Phase 2] Iteration 43500: Temp = 88862.71, Current = 27.71, Best = 27.18
[2025-12-29T21:50:28.178Z] [INFO] [Phase 2] Iteration 44500: Temp = 78404.40, Current = 27.78, Best = 27.18
[2025-12-29T21:50:39.952Z] [INFO] [Phase 2] Iteration 45000: Temp = 73764.23, Current = 27.76, Best = 27.18
[2025-12-29T21:50:50.064Z] [INFO] [Phase 2] Iteration 45500: Temp = 69176.94, Current = 27.67, Best = 27.18
[2025-12-29T21:51:00.271Z] [INFO] [Phase 2] Iteration 46000: Temp = 64797.11, Current = 27.67, Best = 27.18
[2025-12-29T21:51:12.368Z] [INFO] [Phase 2] Iteration 46500: Temp = 61023.25, Current = 27.79, Best = 27.18
[2025-12-29T21:52:04.823Z] [INFO] [Phase 2] Iteration 49000: Temp = 44773.84, Current = 22.85, Best = 22.65
[2025-12-29T21:52:45.949Z] [INFO] [Phase 2] Iteration 51000: Temp = 35184.30, Current = 22.85, Best = 22.65
[2025-12-29T21:52:57.622Z] [INFO] [Phase 2] Iteration 51500: Temp = 33141.75, Current = 22.84, Best = 22.65
[2025-12-29T21:53:17.804Z] [INFO] [Phase 2] Iteration 52500: Temp = 29241.28, Current = 22.83, Best = 22.65
[2025-12-29T21:53:39.693Z] [INFO] [Phase 2] Iteration 53500: Temp = 25810.18, Current = 22.96, Best = 22.65
[2025-12-29T21:53:49.828Z] [INFO] [Phase 2] Iteration 54000: Temp = 24200.24, Current = 22.94, Best = 22.65
[2025-12-29T21:54:12.148Z] [INFO] [Phase 2] Iteration 55000: Temp = 21339.29, Current = 22.99, Best = 22.65
[2025-12-29T21:54:34.065Z] [INFO] [Phase 2] Iteration 56000: Temp = 18644.22, Current = 22.97, Best = 22.65
[2025-12-29T21:55:18.827Z] [INFO] [Phase 2] Iteration 58000: Temp = 14548.85, Current = 22.97, Best = 22.65
[2025-12-29T21:55:28.909Z] [INFO] [Phase 2] Iteration 58500: Temp = 13671.39, Current = 23.01, Best = 22.65
[2025-12-29T21:55:38.615Z] [INFO] [Phase 2] Iteration 59000: Temp = 12846.86, Current = 22.87, Best = 22.65
[2025-12-29T21:55:50.540Z] [INFO] [Phase 2] Iteration 59500: Temp = 12038.29, Current = 22.93, Best = 22.65
[2025-12-29T21:55:59.625Z] [INFO] Optimization complete {"iterations":60000,"reheats":1,"finalTemperature":"11343.9748","fitness":"22.65","hardViolations":0,"softViolations":7}
[2025-12-29T21:55:59.626Z] [INFO] Operator Statistics:
[2025-12-29T21:55:59.626Z] [INFO]   Fix Friday Prayer Conflict: Attempts = 60, Improvements = 1, Accepted = 60, Success Rate = 1.67%
[2025-12-29T21:55:59.626Z] [INFO]   Swap Friday with Non-Friday: Attempts = 152, Improvements = 1, Accepted = 31, Success Rate = 0.66%
[2025-12-29T21:55:59.626Z] [INFO]   Fix Lecturer Conflict: Attempts = 0, Improvements = 0, Accepted = 0, Success Rate = 0.00%
[2025-12-29T21:55:59.626Z] [INFO]   Fix Room Conflict: Attempts = 71, Improvements = 1, Accepted = 71, Success Rate = 1.41%
[2025-12-29T21:55:59.626Z] [INFO]   Fix Max Daily Periods: Attempts = 16, Improvements = 4, Accepted = 16, Success Rate = 25.00%
[2025-12-29T21:55:59.626Z] [INFO]   Fix Room Capacity: Attempts = 0, Improvements = 0, Accepted = 0, Success Rate = 0.00%
[2025-12-29T21:55:59.626Z] [INFO]   Change Time Slot and Room: Attempts = 6166, Improvements = 705, Accepted = 5769, Success Rate = 11.43%
[2025-12-29T21:55:59.626Z] [INFO]   Change Time Slot: Attempts = 5037, Improvements = 264, Accepted = 4321, Success Rate = 5.24%
[2025-12-29T21:55:59.626Z] [INFO]   Change Room: Attempts = 9963, Improvements = 720, Accepted = 9963, Success Rate = 7.23%
[2025-12-29T21:55:59.626Z] [INFO]   Swap Classes: Attempts = 14467, Improvements = 103, Accepted = 703, Success Rate = 0.71%
======================================================================

✨ OPTIMIZATION COMPLETE!

Cache stats: {
  timeCache: {
    timeToMinutes: 20,
    minutesToTime: 17,
  },
  endTimeCache: 279,
  prayerOverlapCache: 279,
  totalEntries: 595,
}
📊 RESULTS:
   Final fitness: 22.65
   Hard constraint violations: 0
   Soft constraint violations: 7
   Total iterations: 60000
   Reheating events: 1
   Final temperature: 11343.9748
   Classes scheduled: 356/373

📈 OPERATOR STATISTICS:
   Fix Friday Prayer Conflict:
      Attempts: 60
      Improvements: 1
      Success rate: 1.67%
   Swap Friday with Non-Friday:
      Attempts: 152
      Improvements: 1
      Success rate: 0.66%
   Fix Lecturer Conflict:
      Attempts: 0
      Improvements: 0
      Success rate: 0.00%
   Fix Room Conflict:
      Attempts: 71
      Improvements: 1
      Success rate: 1.41%
   Fix Max Daily Periods:
      Attempts: 16
      Improvements: 4
      Success rate: 25.00%
   Fix Room Capacity:
      Attempts: 0
      Improvements: 0
      Success rate: 0.00%
   Change Time Slot and Room:
      Attempts: 6166
      Improvements: 705
      Success rate: 11.43%
   Change Time Slot:
      Attempts: 5037
      Improvements: 264
      Success rate: 5.24%
   Change Room:
      Attempts: 9963
      Improvements: 720
      Success rate: 7.23%
   Swap Classes:
      Attempts: 14467
      Improvements: 103
      Success rate: 0.71%

⚠️  VIOLATIONS (7):
   - [soft] Preferred Time: Classes not scheduled in lecturer's preferred time slots
   - [soft] Preferred Room: Classes not assigned to lecturer's preferred room
   - [soft] Compactness: Large gaps (>60 min) between consecutive classes for same prodi
   - [soft] Prayer Time Overlap: Classes overlapping with prayer times (especially Friday 12:00-13:00)
   - [soft] Evening Class Priority: Evening classes (sore) not starting at optimal time (18:30)
   - [soft] Research Day: Classes scheduled on lecturer's designated research day
   - [soft] Overflow Penalty: Lab/room type mismatch (non-lab class in lab room, or lab class not in lab)

======================================================================
✅ Example completed successfully!
======================================================================

💾 Results saved to: timetable-result.json

```

# Trial 3
```bash
emmanuelabayor@ade:~/projects/timetable-sa$ bun examples/timetabling/example-basic.ts
======================================================================
  UNIVERSITY COURSE TIMETABLING - Simulated Annealing v2.0
======================================================================

📂 Loading data from Excel file...
✅ Data loaded successfully!
   Rooms: 33
   Lecturers: 99
   Classes: 373

🏗️  Generating initial timetable (greedy algorithm)...

Generating initial solution for 373 classes...
   🔀 Randomization enabled - shuffling class order
  ⚠️  Skipping GS13PW02: No lecturers on class Praktik Kerja Lapang
  ⚠️  Skipping GS13IP12: No lecturers on class Proyek Interdisipliner
  ⚠️  Skipping GS13PW02: No lecturers on class KERJA PRAKTIK
  ⚠️  Skipping AC135343: No lecturers on class Skripsi
  ⚠️  Skipping GS13PW02: No lecturers on class Kerja Praktik
  ⚠️  Skipping GS13CZ02: No lecturers on class Kewarganegaraan
  ⚠️  Skipping GS13PW02: No lecturers on class Kerja Praktik
  ⚠️  Skipping GS13CZ02: No lecturers on class Kewarganegaraan
  ⚠️  Skipping GS13CZ02: No lecturers on class Kewarganegaraan
  ⚠️  Skipping GS13IP12: No lecturers on class PROYEK INTERDISIPLIN
  ⚠️  Skipping CE11UT46: No lecturers on class Skripsi
  ⚠️  Skipping GS13TH46: No lecturers on class Skripsi
  ⚠️  Skipping MM23RS03: No lecturers on class Research Seminar
  ⚠️  Skipping GS13IP12: No lecturers on class Proyek Interdisipliner
  ⚠️  Skipping VD13KP02: No lecturers on class Kerja Praktik
  ⚠️  Skipping GS13PW02: No lecturers on class Kerja Praktik/Magang
  ⚠️  Skipping GS13IP12: No lecturers on class Proyek Interdisiplin

✅ Initial solution generated:
   Successfully placed: 356/373
   Failed to place: 17/373


⚖️  Setting up constraints...
   Hard constraints: 11
   Soft constraints: 8

🔄 Setting up move operators...
   Targeted operators: 5 (FixFridayPrayerConflict, FixLecturerConflict, etc.)
   General operators: 4 (including high-success ChangeTimeSlotAndRoom)
   Total operators: 10

⚙️  Configuring Simulated Annealing...
   Initial temperature: 100000
   Cooling rate: 0.9998
   Max iterations: 60000

🚀 Starting optimization...

======================================================================
[2025-12-29T21:34:58.066Z] [INFO] Simulated Annealing initialized {"hardConstraints":11,"softConstraints":8,"moveGenerators":10,"config":{"initialTemperature":100000,"minTemperature":1e-7,"coolingRate":0.9998,"maxIterations":60000}}
[2025-12-29T21:34:58.067Z] [INFO] Starting optimization...
[2025-12-29T21:34:58.067Z] [INFO] Phase 1: Eliminating hard constraint violations
[2025-12-29T21:34:58.110Z] [INFO] Initial state {"fitness":"175024.97","hardViolations":16}
[2025-12-29T21:35:18.842Z] [INFO] [Phase 1] Iteration 1000: Temp = 89725.89, Hard violations = 5, Best = 5
[2025-12-29T21:35:57.983Z] [INFO] [Phase 1] Iteration 2500: Temp = 75244.42, Hard violations = 3, Best = 3
[2025-12-29T21:36:10.620Z] [INFO] [Phase 1] Iteration 3000: Temp = 70777.11, Hard violations = 3, Best = 3
[2025-12-29T21:36:39.343Z] [INFO] [Phase 1] Iteration 4000: Temp = 62222.88, Hard violations = 3, Best = 3
[2025-12-29T21:36:54.312Z] [INFO] [Phase 1] Iteration 4500: Temp = 58376.67, Hard violations = 3, Best = 3
[2025-12-29T21:37:07.028Z] [INFO] [Phase 1] Iteration 5000: Temp = 54987.75, Hard violations = 3, Best = 3
[2025-12-29T21:37:19.480Z] [INFO] [Phase 1] Iteration 5500: Temp = 51805.92, Hard violations = 3, Best = 3
[2025-12-29T21:37:46.544Z] [INFO] [Phase 1] Iteration 6500: Temp = 45910.43, Hard violations = 3, Best = 3
[2025-12-29T21:38:00.553Z] [INFO] [Phase 1] Iteration 7000: Temp = 43236.56, Hard violations = 3, Best = 3
[2025-12-29T21:38:26.635Z] [INFO] [Phase 1] Iteration 8000: Temp = 38132.76, Hard violations = 3, Best = 3
[2025-12-29T21:38:41.066Z] [INFO] [Phase 1] Iteration 8500: Temp = 35747.03, Hard violations = 2, Best = 2
[2025-12-29T21:38:52.616Z] [INFO] [Phase 1] Iteration 9000: Temp = 33490.47, Hard violations = 2, Best = 2
[2025-12-29T21:39:17.577Z] [INFO] [Phase 1] Iteration 10000: Temp = 29507.61, Hard violations = 1, Best = 1
[2025-12-29T21:39:28.578Z] [INFO] [Phase 1] Iteration 10500: Temp = 27744.62, Hard violations = 1, Best = 1
[2025-12-29T21:39:41.365Z] [INFO] [Phase 1] Iteration 11000: Temp = 26118.29, Hard violations = 1, Best = 1
[2025-12-29T21:39:52.613Z] [INFO] [Phase 1] Iteration 11500: Temp = 24494.03, Hard violations = 1, Best = 1
[2025-12-29T21:40:16.335Z] [INFO] [Phase 1] Iteration 12500: Temp = 21641.59, Hard violations = 1, Best = 1
[2025-12-29T21:40:27.105Z] [INFO] [Phase 1] Iteration 13000: Temp = 20364.86, Hard violations = 1, Best = 1
[2025-12-29T21:40:37.710Z] [INFO] [Phase 1] Iteration 13500: Temp = 19209.50, Hard violations = 1, Best = 1
[2025-12-29T21:41:24.880Z] [INFO] [Phase 1] Iteration 15500: Temp = 15074.14, Hard violations = 1, Best = 1
[2025-12-29T21:41:32.057Z] [INFO] Phase 1 complete: Hard violations = 0
[2025-12-29T21:41:32.058Z] [INFO] Phase 2: Optimizing soft constraints
[2025-12-29T21:41:35.403Z] [INFO] [Phase 2] Iteration 16000: Temp = 14196.21, Current = 27.24, Best = 27.20
[2025-12-29T21:41:55.454Z] [INFO] [Phase 2] Iteration 17000: Temp = 12563.08, Current = 27.11, Best = 26.99
[2025-12-29T21:42:27.341Z] [INFO] [Phase 2] Iteration 18500: Temp = 10520.70, Current = 27.13, Best = 26.86
[2025-12-29T21:42:40.013Z] [INFO] [Phase 2] Iteration 19000: Temp = 9886.19, Current = 27.20, Best = 26.86
[2025-12-29T21:42:50.166Z] [INFO] [Phase 2] Iteration 19500: Temp = 9288.09, Current = 27.19, Best = 26.86
[2025-12-29T21:42:59.777Z] [INFO] [Phase 2] Iteration 20000: Temp = 8775.18, Current = 27.12, Best = 26.86
[2025-12-29T21:43:22.054Z] [INFO] [Phase 2] Iteration 21000: Temp = 7754.82, Current = 27.42, Best = 26.86
[2025-12-29T21:43:52.596Z] [INFO] [Phase 2] Iteration 22500: Temp = 6547.59, Current = 27.25, Best = 26.86
[2025-12-29T21:44:24.665Z] [INFO] [Phase 2] Iteration 24000: Temp = 5471.10, Current = 27.32, Best = 26.86
[2025-12-29T21:44:34.511Z] [INFO] [Phase 2] Iteration 24500: Temp = 5156.58, Current = 27.30, Best = 26.86
[2025-12-29T21:44:55.607Z] [INFO] [Phase 2] Iteration 25500: Temp = 4596.35, Current = 27.21, Best = 26.86
[2025-12-29T21:45:35.931Z] [INFO] [Phase 2] Iteration 27500: Temp = 3654.06, Current = 27.14, Best = 26.86
[2025-12-29T21:45:55.252Z] [INFO] [Phase 2] Iteration 28500: Temp = 3253.81, Current = 27.26, Best = 26.86
[2025-12-29T21:46:40.721Z] [INFO] [Phase 2] Iteration 30500: Temp = 2539.59, Current = 27.30, Best = 26.86
[2025-12-29T21:46:51.310Z] [INFO] [Phase 2] Iteration 31000: Temp = 2381.18, Current = 27.21, Best = 26.86
[2025-12-29T21:47:01.820Z] [INFO] [Phase 2] Iteration 31500: Temp = 2239.36, Current = 27.37, Best = 26.86
[2025-12-29T21:47:24.107Z] [INFO] [Phase 2] Iteration 32500: Temp = 1981.35, Current = 27.29, Best = 26.86
[2025-12-29T21:47:34.094Z] [INFO] [Phase 2] Iteration 33000: Temp = 1868.57, Current = 27.31, Best = 26.86
[2025-12-29T21:47:46.579Z] [INFO] [Phase 2] Iteration 33500: Temp = 1758.68, Current = 27.18, Best = 26.86
[2025-12-29T21:48:19.474Z] [INFO] [Phase 2] Iteration 35000: Temp = 1464.26, Current = 27.35, Best = 26.86
[2025-12-29T21:49:27.136Z] [INFO] [Phase 2] Reheating #1: Temperature = 149986.45, Fitness = 26.86
[2025-12-29T21:49:33.078Z] [INFO] [Phase 2] Iteration 38500: Temp = 145030.14, Current = 26.85, Best = 26.85
[2025-12-29T21:49:53.944Z] [INFO] [Phase 2] Iteration 39500: Temp = 127680.22, Current = 27.03, Best = 26.84
[2025-12-29T21:50:05.961Z] [INFO] [Phase 2] Iteration 40000: Temp = 120219.93, Current = 27.02, Best = 26.84
[2025-12-29T21:50:38.115Z] [INFO] [Phase 2] Iteration 41500: Temp = 100013.42, Current = 27.02, Best = 26.84
[2025-12-29T21:50:58.655Z] [INFO] [Phase 2] Iteration 42500: Temp = 88084.07, Current = 27.12, Best = 26.84
[2025-12-29T21:51:20.901Z] [INFO] [Phase 2] Iteration 43500: Temp = 78153.88, Current = 27.17, Best = 26.84
[2025-12-29T21:51:31.062Z] [INFO] [Phase 2] Iteration 44000: Temp = 73455.04, Current = 27.19, Best = 26.84
[2025-12-29T21:51:41.522Z] [INFO] [Phase 2] Iteration 44500: Temp = 69052.52, Current = 27.18, Best = 26.84
[2025-12-29T21:52:13.285Z] [INFO] [Phase 2] Iteration 46000: Temp = 57919.25, Current = 27.10, Best = 26.84
[2025-12-29T21:52:25.176Z] [INFO] [Phase 2] Iteration 46500: Temp = 54469.65, Current = 27.10, Best = 26.84
[2025-12-29T21:52:34.839Z] [INFO] [Phase 2] Iteration 47000: Temp = 51430.84, Current = 27.06, Best = 26.84
[2025-12-29T21:52:45.101Z] [INFO] [Phase 2] Iteration 47500: Temp = 48300.00, Current = 27.01, Best = 26.84
[2025-12-29T21:52:57.206Z] [INFO] [Phase 2] Iteration 48000: Temp = 45432.40, Current = 27.06, Best = 26.84
[2025-12-29T21:53:07.194Z] [INFO] [Phase 2] Iteration 48500: Temp = 42872.03, Current = 27.05, Best = 26.84
[2025-12-29T21:53:17.370Z] [INFO] [Phase 2] Iteration 49000: Temp = 40342.83, Current = 26.97, Best = 26.84
[2025-12-29T21:53:29.294Z] [INFO] [Phase 2] Iteration 49500: Temp = 37947.65, Current = 26.87, Best = 26.84
[2025-12-29T21:53:38.802Z] [INFO] [Phase 2] Iteration 50000: Temp = 35852.09, Current = 27.05, Best = 26.84
[2025-12-29T21:53:48.741Z] [INFO] [Phase 2] Iteration 50500: Temp = 33764.02, Current = 27.06, Best = 26.84
[2025-12-29T21:53:58.591Z] [INFO] [Phase 2] Iteration 51000: Temp = 31880.36, Current = 27.05, Best = 26.84
[2025-12-29T21:54:10.436Z] [INFO] [Phase 2] Iteration 51500: Temp = 30017.61, Current = 27.01, Best = 26.84
[2025-12-29T21:54:20.229Z] [INFO] [Phase 2] Iteration 52000: Temp = 28286.31, Current = 27.05, Best = 26.84
[2025-12-29T21:54:30.605Z] [INFO] [Phase 2] Iteration 52500: Temp = 26553.77, Current = 27.03, Best = 26.84
[2025-12-29T21:54:53.191Z] [INFO] [Phase 2] Iteration 53500: Temp = 23442.70, Current = 27.24, Best = 26.84
[2025-12-29T21:55:14.289Z] [INFO] [Phase 2] Iteration 54500: Temp = 21017.35, Current = 27.37, Best = 26.84
[2025-12-29T21:55:33.822Z] [INFO] [Phase 2] Iteration 55500: Temp = 18726.45, Current = 27.41, Best = 26.84
[2025-12-29T21:56:03.155Z] [INFO] [Phase 2] Iteration 57000: Temp = 15625.73, Current = 27.54, Best = 26.84
[2025-12-29T21:56:23.186Z] [INFO] [Phase 2] Iteration 58000: Temp = 13748.17, Current = 27.60, Best = 26.84
[2025-12-29T21:56:31.590Z] [INFO] [Phase 2] Iteration 58500: Temp = 12931.94, Current = 27.38, Best = 26.84
[2025-12-29T21:56:40.266Z] [INFO] [Phase 2] Iteration 59000: Temp = 12135.00, Current = 27.50, Best = 26.84
[2025-12-29T21:56:48.673Z] [INFO] [Phase 2] Iteration 59500: Temp = 11375.79, Current = 27.58, Best = 26.84
[2025-12-29T21:56:58.663Z] [INFO] [Phase 2] Iteration 60000: Temp = 10713.25, Current = 27.49, Best = 26.84
[2025-12-29T21:56:58.674Z] [INFO] Optimization complete {"iterations":60000,"reheats":1,"finalTemperature":"10713.2471","fitness":"26.84","hardViolations":0,"softViolations":8}
[2025-12-29T21:56:58.674Z] [INFO] Operator Statistics:
[2025-12-29T21:56:58.674Z] [INFO]   Fix Friday Prayer Conflict: Attempts = 0, Improvements = 0, Accepted = 0, Success Rate = 0.00%
[2025-12-29T21:56:58.674Z] [INFO]   Swap Friday with Non-Friday: Attempts = 0, Improvements = 0, Accepted = 0, Success Rate = 0.00%
[2025-12-29T21:56:58.674Z] [INFO]   Fix Lecturer Conflict: Attempts = 1073, Improvements = 125, Accepted = 788, Success Rate = 11.65%
[2025-12-29T21:56:58.674Z] [INFO]   Fix Room Conflict: Attempts = 1, Improvements = 1, Accepted = 1, Success Rate = 100.00%
[2025-12-29T21:56:58.674Z] [INFO]   Fix Max Daily Periods: Attempts = 399, Improvements = 9, Accepted = 399, Success Rate = 2.26%
[2025-12-29T21:56:58.674Z] [INFO]   Fix Room Capacity: Attempts = 0, Improvements = 0, Accepted = 0, Success Rate = 0.00%
[2025-12-29T21:56:58.674Z] [INFO]   Change Time Slot and Room: Attempts = 5932, Improvements = 646, Accepted = 5559, Success Rate = 10.89%
[2025-12-29T21:56:58.674Z] [INFO]   Change Time Slot: Attempts = 4987, Improvements = 247, Accepted = 4294, Success Rate = 4.95%
[2025-12-29T21:56:58.674Z] [INFO]   Change Room: Attempts = 9730, Improvements = 679, Accepted = 9730, Success Rate = 6.98%
[2025-12-29T21:56:58.674Z] [INFO]   Swap Classes: Attempts = 14096, Improvements = 117, Accepted = 711, Success Rate = 0.83%
======================================================================

✨ OPTIMIZATION COMPLETE!

Cache stats: {
  timeCache: {
    timeToMinutes: 20,
    minutesToTime: 17,
  },
  endTimeCache: 282,
  prayerOverlapCache: 282,
  totalEntries: 601,
}
📊 RESULTS:
   Final fitness: 26.84
   Hard constraint violations: 0
   Soft constraint violations: 8
   Total iterations: 60000
   Reheating events: 1
   Final temperature: 10713.2471
   Classes scheduled: 356/373

📈 OPERATOR STATISTICS:
   Fix Friday Prayer Conflict:
      Attempts: 0
      Improvements: 0
      Success rate: 0.00%
   Swap Friday with Non-Friday:
      Attempts: 0
      Improvements: 0
      Success rate: 0.00%
   Fix Lecturer Conflict:
      Attempts: 1073
      Improvements: 125
      Success rate: 11.65%
   Fix Room Conflict:
      Attempts: 1
      Improvements: 1
      Success rate: 100.00%
   Fix Max Daily Periods:
      Attempts: 399
      Improvements: 9
      Success rate: 2.26%
   Fix Room Capacity:
      Attempts: 0
      Improvements: 0
      Success rate: 0.00%
   Change Time Slot and Room:
      Attempts: 5932
      Improvements: 646
      Success rate: 10.89%
   Change Time Slot:
      Attempts: 4987
      Improvements: 247
      Success rate: 4.95%
   Change Room:
      Attempts: 9730
      Improvements: 679
      Success rate: 6.98%
   Swap Classes:
      Attempts: 14096
      Improvements: 117
      Success rate: 0.83%

⚠️  VIOLATIONS (8):
   - [soft] Preferred Time: Classes not scheduled in lecturer's preferred time slots
   - [soft] Preferred Room: Classes not assigned to lecturer's preferred room
   - [soft] Transit Time: Insufficient transit time between consecutive classes for lecturers
   - [soft] Compactness: Large gaps (>60 min) between consecutive classes for same prodi
   - [soft] Prayer Time Overlap: Classes overlapping with prayer times (especially Friday 12:00-13:00)
   - [soft] Evening Class Priority: Evening classes (sore) not starting at optimal time (18:30)
   - [soft] Research Day: Classes scheduled on lecturer's designated research day
   - [soft] Overflow Penalty: Lab/room type mismatch (non-lab class in lab room, or lab class not in lab)

======================================================================
✅ Example completed successfully!
======================================================================

💾 Results saved to: timetable-result.json

```

# Trial 4
```bash
emmanuelabayor@ade:~/projects/timetable-sa$ bun examples/timetabling/example-basic.ts
======================================================================
  UNIVERSITY COURSE TIMETABLING - Simulated Annealing v2.0
======================================================================

📂 Loading data from Excel file...
✅ Data loaded successfully!
   Rooms: 33
   Lecturers: 99
   Classes: 373

🏗️  Generating initial timetable (greedy algorithm)...

Generating initial solution for 373 classes...
   🔀 Randomization enabled - shuffling class order
  ⚠️  Skipping GS13IP12: No lecturers on class Proyek Interdisipliner
  ⚠️  Skipping MM23RS03: No lecturers on class Research Seminar
  ⚠️  Skipping GS13PW02: No lecturers on class Kerja Praktik
  ⚠️  Skipping GS13TH46: No lecturers on class Skripsi
  ⚠️  Skipping AC135343: No lecturers on class Skripsi
  ⚠️  Skipping GS13PW02: No lecturers on class Praktik Kerja Lapang
  ⚠️  Skipping GS13PW02: No lecturers on class Kerja Praktik/Magang
  ⚠️  Skipping GS13PW02: No lecturers on class Kerja Praktik
  ⚠️  Skipping GS13IP12: No lecturers on class Proyek Interdisipliner
  ⚠️  Skipping CE11UT46: No lecturers on class Skripsi
  ⚠️  Skipping GS13IP12: No lecturers on class PROYEK INTERDISIPLIN
  ⚠️  Skipping GS13CZ02: No lecturers on class Kewarganegaraan
  ⚠️  Skipping GS13CZ02: No lecturers on class Kewarganegaraan
  ⚠️  Skipping VD13KP02: No lecturers on class Kerja Praktik
  ⚠️  Skipping GS13CZ02: No lecturers on class Kewarganegaraan
  ⚠️  Skipping GS13IP12: No lecturers on class Proyek Interdisiplin
  ⚠️  Skipping GS13PW02: No lecturers on class KERJA PRAKTIK

✅ Initial solution generated:
   Successfully placed: 356/373
   Failed to place: 17/373


⚖️  Setting up constraints...
   Hard constraints: 11
   Soft constraints: 8

🔄 Setting up move operators...
   Targeted operators: 5 (FixFridayPrayerConflict, FixLecturerConflict, etc.)
   General operators: 4 (including high-success ChangeTimeSlotAndRoom)
   Total operators: 10

⚙️  Configuring Simulated Annealing...
   Initial temperature: 100000
   Cooling rate: 0.9998
   Max iterations: 60000

🚀 Starting optimization...

======================================================================
[2025-12-29T21:35:03.265Z] [INFO] Simulated Annealing initialized {"hardConstraints":11,"softConstraints":8,"moveGenerators":10,"config":{"initialTemperature":100000,"minTemperature":1e-7,"coolingRate":0.9998,"maxIterations":60000}}
[2025-12-29T21:35:03.267Z] [INFO] Starting optimization...
[2025-12-29T21:35:03.267Z] [INFO] Phase 1: Eliminating hard constraint violations
[2025-12-29T21:35:03.319Z] [INFO] Initial state {"fitness":"163913.57","hardViolations":11}
[2025-12-29T21:35:35.990Z] [INFO] [Phase 1] Iteration 1500: Temp = 83009.21, Hard violations = 2, Best = 2
[2025-12-29T21:35:45.908Z] [INFO] [Phase 1] Iteration 2000: Temp = 78174.66, Hard violations = 2, Best = 2
[2025-12-29T21:35:55.530Z] [INFO] [Phase 1] Iteration 2500: Temp = 73887.22, Hard violations = 2, Best = 2
[2025-12-29T21:35:59.306Z] [INFO] Phase 1 complete: Hard violations = 0
[2025-12-29T21:35:59.307Z] [INFO] Phase 2: Optimizing soft constraints
[2025-12-29T21:36:04.682Z] [INFO] [Phase 2] Iteration 3000: Temp = 69904.80, Current = 26.39, Best = 26.31
[2025-12-29T21:36:28.060Z] [INFO] [Phase 2] Iteration 4000: Temp = 61616.01, Current = 26.34, Best = 26.26
[2025-12-29T21:36:38.637Z] [INFO] [Phase 2] Iteration 4500: Temp = 57749.53, Current = 26.36, Best = 26.25
[2025-12-29T21:36:50.495Z] [INFO] [Phase 2] Iteration 5000: Temp = 54342.64, Current = 26.41, Best = 26.25
[2025-12-29T21:37:01.163Z] [INFO] [Phase 2] Iteration 5500: Temp = 50963.15, Current = 26.38, Best = 26.25
[2025-12-29T21:37:11.901Z] [INFO] [Phase 2] Iteration 6000: Temp = 47803.38, Current = 26.63, Best = 26.25
[2025-12-29T21:37:23.587Z] [INFO] [Phase 2] Iteration 6500: Temp = 45118.42, Current = 26.68, Best = 26.25
[2025-12-29T21:37:34.271Z] [INFO] [Phase 2] Iteration 7000: Temp = 42329.50, Current = 26.71, Best = 26.25
[2025-12-29T21:37:44.323Z] [INFO] [Phase 2] Iteration 7500: Temp = 39896.09, Current = 26.80, Best = 26.25
[2025-12-29T21:37:54.267Z] [INFO] [Phase 2] Iteration 8000: Temp = 37587.53, Current = 26.93, Best = 26.25
[2025-12-29T21:38:25.554Z] [INFO] [Phase 2] Iteration 9500: Temp = 31666.37, Current = 26.96, Best = 26.25
[2025-12-29T21:38:47.608Z] [INFO] [Phase 2] Iteration 10500: Temp = 28102.07, Current = 26.81, Best = 26.25
[2025-12-29T21:39:31.273Z] [INFO] [Phase 2] Iteration 12500: Temp = 21977.49, Current = 26.87, Best = 26.25
[2025-12-29T21:39:43.682Z] [INFO] [Phase 2] Iteration 13000: Temp = 20623.11, Current = 26.82, Best = 26.25
[2025-12-29T21:40:03.384Z] [INFO] [Phase 2] Iteration 14000: Temp = 18331.13, Current = 26.76, Best = 26.25
[2025-12-29T21:40:34.911Z] [INFO] [Phase 2] Iteration 15500: Temp = 15372.54, Current = 26.78, Best = 26.25
[2025-12-29T21:40:45.211Z] [INFO] [Phase 2] Iteration 16000: Temp = 14459.86, Current = 26.80, Best = 26.25
[2025-12-29T21:40:57.861Z] [INFO] [Phase 2] Iteration 16500: Temp = 13560.63, Current = 26.75, Best = 26.25
[2025-12-29T21:41:40.327Z] [INFO] [Phase 2] Iteration 18500: Temp = 10624.32, Current = 26.76, Best = 26.25
[2025-12-29T21:41:49.938Z] [INFO] [Phase 2] Iteration 19000: Temp = 10011.56, Current = 26.84, Best = 26.25
[2025-12-29T21:42:21.801Z] [INFO] [Phase 2] Iteration 20500: Temp = 8350.50, Current = 26.94, Best = 26.25
[2025-12-29T21:42:44.037Z] [INFO] [Phase 2] Iteration 21500: Temp = 7404.66, Current = 27.08, Best = 26.25
[2025-12-29T21:43:03.655Z] [INFO] [Phase 2] Iteration 22500: Temp = 6558.08, Current = 26.93, Best = 26.25
[2025-12-29T21:43:16.108Z] [INFO] [Phase 2] Iteration 23000: Temp = 6139.18, Current = 26.81, Best = 26.25
[2025-12-29T21:43:25.622Z] [INFO] [Phase 2] Iteration 23500: Temp = 5800.16, Current = 27.01, Best = 26.25
[2025-12-29T21:43:46.390Z] [INFO] [Phase 2] Iteration 24500: Temp = 5199.04, Current = 26.93, Best = 26.25
[2025-12-29T21:44:26.416Z] [INFO] [Phase 2] Iteration 26500: Temp = 4112.58, Current = 26.98, Best = 26.25
[2025-12-29T21:44:35.940Z] [INFO] [Phase 2] Iteration 27000: Temp = 3886.25, Current = 26.93, Best = 26.25
[2025-12-29T21:44:45.769Z] [INFO] [Phase 2] Iteration 27500: Temp = 3657.72, Current = 26.87, Best = 26.25
[2025-12-29T21:45:17.806Z] [INFO] [Phase 2] Iteration 29000: Temp = 3044.15, Current = 22.14, Best = 21.82
[2025-12-29T21:45:39.091Z] [INFO] [Phase 2] Iteration 30000: Temp = 2708.54, Current = 22.10, Best = 21.82
[2025-12-29T21:45:49.682Z] [INFO] [Phase 2] Iteration 30500: Temp = 2534.01, Current = 22.27, Best = 21.82
[2025-12-29T21:46:33.830Z] [INFO] [Phase 2] Iteration 32500: Temp = 1981.75, Current = 22.24, Best = 21.82
[2025-12-29T21:46:44.030Z] [INFO] [Phase 2] Iteration 33000: Temp = 1863.72, Current = 22.24, Best = 21.82
[2025-12-29T21:46:54.097Z] [INFO] [Phase 2] Iteration 33500: Temp = 1759.39, Current = 22.34, Best = 21.82
[2025-12-29T21:47:26.955Z] [INFO] [Phase 2] Iteration 35000: Temp = 1458.99, Current = 22.27, Best = 21.82
[2025-12-29T21:47:48.804Z] [INFO] [Phase 2] Iteration 36000: Temp = 1298.40, Current = 27.17, Best = 21.82
[2025-12-29T21:47:59.129Z] [INFO] [Phase 2] Iteration 36500: Temp = 1221.32, Current = 27.33, Best = 21.82
[2025-12-29T21:48:09.691Z] [INFO] [Phase 2] Iteration 37000: Temp = 1146.28, Current = 27.36, Best = 21.82
[2025-12-29T21:48:34.295Z] [INFO] [Phase 2] Reheating #1: Temperature = 149986.45, Fitness = 21.82
[2025-12-29T21:48:43.743Z] [INFO] [Phase 2] Iteration 38500: Temp = 141533.88, Current = 27.29, Best = 21.82
[2025-12-29T21:49:06.719Z] [INFO] [Phase 2] Iteration 39500: Temp = 124328.37, Current = 27.15, Best = 21.82
[2025-12-29T21:49:39.118Z] [INFO] [Phase 2] Iteration 41000: Temp = 103493.40, Current = 27.13, Best = 21.82
[2025-12-29T21:49:48.684Z] [INFO] [Phase 2] Iteration 41500: Temp = 97719.59, Current = 27.03, Best = 21.82
[2025-12-29T21:50:01.229Z] [INFO] [Phase 2] Iteration 42000: Temp = 91514.33, Current = 27.14, Best = 21.82
[2025-12-29T21:50:10.762Z] [INFO] [Phase 2] Iteration 42500: Temp = 86443.40, Current = 27.11, Best = 21.82
[2025-12-29T21:50:30.303Z] [INFO] [Phase 2] Iteration 43500: Temp = 76774.92, Current = 27.46, Best = 21.82
[2025-12-29T21:50:42.323Z] [INFO] [Phase 2] Iteration 44000: Temp = 72187.85, Current = 27.57, Best = 21.82
[2025-12-29T21:50:52.115Z] [INFO] [Phase 2] Iteration 44500: Temp = 67956.36, Current = 27.71, Best = 21.82
[2025-12-29T21:51:02.702Z] [INFO] [Phase 2] Iteration 45000: Temp = 63628.35, Current = 27.62, Best = 21.82
[2025-12-29T21:51:25.260Z] [INFO] [Phase 2] Iteration 46000: Temp = 55994.10, Current = 27.58, Best = 21.82
[2025-12-29T21:51:35.641Z] [INFO] [Phase 2] Iteration 46500: Temp = 52522.41, Current = 27.58, Best = 21.82
[2025-12-29T21:51:48.015Z] [INFO] [Phase 2] Iteration 47000: Temp = 49354.74, Current = 27.56, Best = 21.82
[2025-12-29T21:51:58.132Z] [INFO] [Phase 2] Iteration 47500: Temp = 46331.75, Current = 27.50, Best = 21.82
[2025-12-29T21:52:30.463Z] [INFO] [Phase 2] Iteration 49000: Temp = 38306.07, Current = 27.33, Best = 21.82
[2025-12-29T21:53:13.248Z] [INFO] [Phase 2] Iteration 51000: Temp = 29879.83, Current = 27.37, Best = 21.82
[2025-12-29T21:53:34.550Z] [INFO] [Phase 2] Iteration 52000: Temp = 26569.71, Current = 27.33, Best = 21.82
[2025-12-29T21:53:54.911Z] [INFO] [Phase 2] Iteration 53000: Temp = 23414.59, Current = 22.37, Best = 21.82
[2025-12-29T21:54:07.234Z] [INFO] [Phase 2] Iteration 53500: Temp = 21962.86, Current = 22.36, Best = 21.82
[2025-12-29T21:54:17.156Z] [INFO] [Phase 2] Iteration 54000: Temp = 20679.58, Current = 22.41, Best = 21.82
[2025-12-29T21:54:27.809Z] [INFO] [Phase 2] Iteration 54500: Temp = 19354.79, Current = 22.28, Best = 21.82
[2025-12-29T21:54:39.983Z] [INFO] [Phase 2] Iteration 55000: Temp = 18183.85, Current = 22.34, Best = 21.82
[2025-12-29T21:54:50.538Z] [INFO] [Phase 2] Iteration 55500: Temp = 16991.74, Current = 27.37, Best = 21.82
[2025-12-29T21:55:00.518Z] [INFO] [Phase 2] Iteration 56000: Temp = 15976.53, Current = 27.47, Best = 21.82
[2025-12-29T21:55:12.944Z] [INFO] [Phase 2] Iteration 56500: Temp = 15034.01, Current = 27.45, Best = 21.82
[2025-12-29T21:55:23.332Z] [INFO] [Phase 2] Iteration 57000: Temp = 14104.71, Current = 27.57, Best = 21.82
[2025-12-29T21:55:33.510Z] [INFO] [Phase 2] Iteration 57500: Temp = 13240.79, Current = 27.47, Best = 21.82
[2025-12-29T21:55:54.104Z] [INFO] [Phase 2] Iteration 58500: Temp = 11705.86, Current = 27.65, Best = 21.82
[2025-12-29T21:56:02.885Z] [INFO] [Phase 2] Iteration 59000: Temp = 11026.31, Current = 27.50, Best = 21.82
[2025-12-29T21:56:12.154Z] [INFO] [Phase 2] Iteration 59500: Temp = 10330.26, Current = 27.46, Best = 21.82
[2025-12-29T21:56:22.937Z] [INFO] Optimization complete {"iterations":60000,"reheats":1,"finalTemperature":"9689.7728","fitness":"21.82","hardViolations":0,"softViolations":7}
[2025-12-29T21:56:22.937Z] [INFO] Operator Statistics:
[2025-12-29T21:56:22.937Z] [INFO]   Fix Friday Prayer Conflict: Attempts = 0, Improvements = 0, Accepted = 0, Success Rate = 0.00%
[2025-12-29T21:56:22.937Z] [INFO]   Swap Friday with Non-Friday: Attempts = 0, Improvements = 0, Accepted = 0, Success Rate = 0.00%
[2025-12-29T21:56:22.937Z] [INFO]   Fix Lecturer Conflict: Attempts = 0, Improvements = 0, Accepted = 0, Success Rate = 0.00%
[2025-12-29T21:56:22.937Z] [INFO]   Fix Room Conflict: Attempts = 0, Improvements = 0, Accepted = 0, Success Rate = 0.00%
[2025-12-29T21:56:22.937Z] [INFO]   Fix Max Daily Periods: Attempts = 8, Improvements = 8, Accepted = 8, Success Rate = 100.00%
[2025-12-29T21:56:22.937Z] [INFO]   Fix Room Capacity: Attempts = 0, Improvements = 0, Accepted = 0, Success Rate = 0.00%
[2025-12-29T21:56:22.937Z] [INFO]   Change Time Slot and Room: Attempts = 6457, Improvements = 683, Accepted = 5917, Success Rate = 10.58%
[2025-12-29T21:56:22.937Z] [INFO]   Change Time Slot: Attempts = 5378, Improvements = 281, Accepted = 4507, Success Rate = 5.22%
[2025-12-29T21:56:22.937Z] [INFO]   Change Room: Attempts = 10224, Improvements = 755, Accepted = 10224, Success Rate = 7.38%
[2025-12-29T21:56:22.937Z] [INFO]   Swap Classes: Attempts = 14653, Improvements = 136, Accepted = 778, Success Rate = 0.93%
======================================================================

✨ OPTIMIZATION COMPLETE!

Cache stats: {
  timeCache: {
    timeToMinutes: 20,
    minutesToTime: 17,
  },
  endTimeCache: 282,
  prayerOverlapCache: 282,
  totalEntries: 601,
}
📊 RESULTS:
   Final fitness: 21.82
   Hard constraint violations: 0
   Soft constraint violations: 7
   Total iterations: 60000
   Reheating events: 1
   Final temperature: 9689.7728
   Classes scheduled: 356/373

📈 OPERATOR STATISTICS:
   Fix Friday Prayer Conflict:
      Attempts: 0
      Improvements: 0
      Success rate: 0.00%
   Swap Friday with Non-Friday:
      Attempts: 0
      Improvements: 0
      Success rate: 0.00%
   Fix Lecturer Conflict:
      Attempts: 0
      Improvements: 0
      Success rate: 0.00%
   Fix Room Conflict:
      Attempts: 0
      Improvements: 0
      Success rate: 0.00%
   Fix Max Daily Periods:
      Attempts: 8
      Improvements: 8
      Success rate: 100.00%
   Fix Room Capacity:
      Attempts: 0
      Improvements: 0
      Success rate: 0.00%
   Change Time Slot and Room:
      Attempts: 6457
      Improvements: 683
      Success rate: 10.58%
   Change Time Slot:
      Attempts: 5378
      Improvements: 281
      Success rate: 5.22%
   Change Room:
      Attempts: 10224
      Improvements: 755
      Success rate: 7.38%
   Swap Classes:
      Attempts: 14653
      Improvements: 136
      Success rate: 0.93%

⚠️  VIOLATIONS (7):
   - [soft] Preferred Time: Classes not scheduled in lecturer's preferred time slots
   - [soft] Preferred Room: Classes not assigned to lecturer's preferred room
   - [soft] Compactness: Large gaps (>60 min) between consecutive classes for same prodi
   - [soft] Prayer Time Overlap: Classes overlapping with prayer times (especially Friday 12:00-13:00)
   - [soft] Evening Class Priority: Evening classes (sore) not starting at optimal time (18:30)
   - [soft] Research Day: Classes scheduled on lecturer's designated research day
   - [soft] Overflow Penalty: Lab/room type mismatch (non-lab class in lab room, or lab class not in lab)

======================================================================
✅ Example completed successfully!
======================================================================

💾 Results saved to: timetable-result.json

```

# Trial 5
```bash

```
