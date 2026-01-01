# Benchmarking Results for Timetable-SA Examples
In first trials, i use parallel evaluation to speed up the process. However, in subsequent trials, I disabled parallel evaluation to ensure consistent and comparable results across different runs.

# First Trial Results (with Parallel Evaluation)
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
  ⚠️  Skipping GS13CZ02: No lecturers on class Kewarganegaraan
  ⚠️  Skipping MM23RS03: No lecturers on class Research Seminar
  ⚠️  Skipping GS13IP12: No lecturers on class Proyek Interdisipliner
  ⚠️  Skipping GS13PW02: No lecturers on class Praktik Kerja Lapang
  ⚠️  Skipping GS13CZ02: No lecturers on class Kewarganegaraan
  ⚠️  Skipping CE11UT46: No lecturers on class Skripsi
  ⚠️  Skipping GS13IP12: No lecturers on class Proyek Interdisipliner
  ⚠️  Skipping AC135343: No lecturers on class Skripsi
  ⚠️  Skipping GS13IP12: No lecturers on class Proyek Interdisiplin
  ⚠️  Skipping VD13KP02: No lecturers on class Kerja Praktik
  ⚠️  Skipping GS13PW02: No lecturers on class Kerja Praktik
  ⚠️  Skipping GS13IP12: No lecturers on class PROYEK INTERDISIPLIN
  ⚠️  Skipping GS13PW02: No lecturers on class Kerja Praktik
  ⚠️  Skipping GS13PW02: No lecturers on class Kerja Praktik/Magang
  ⚠️  Skipping GS13TH46: No lecturers on class Skripsi
  ⚠️  Skipping GS13CZ02: No lecturers on class Kewarganegaraan
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
   Cooling rate: 0.9995
   Max iterations: 20000

🚀 Starting optimization...

======================================================================
[2026-01-01T18:22:39.125Z] [INFO] Simulated Annealing initialized {"hardConstraints":11,"softConstraints":8,"moveGenerators":10,"parallelEvaluation":true,"config":{"initialTemperature":100000,"minTemperature":1e-7,"coolingRate":0.9995,"maxIterations":20000}}
[2026-01-01T18:22:39.126Z] [INFO] Parallel evaluation enabled with auto workers
[2026-01-01T18:22:39.127Z] [INFO] Starting optimization...
[2026-01-01T18:22:39.127Z] [INFO] Phase 1: Eliminating hard constraint violations
[2026-01-01T18:22:39.139Z] [INFO] Initial state {"fitness":"173358.56","hardViolations":14}
[2026-01-01T18:22:40.504Z] [INFO] [Phase 1] Iteration 500: Temp = 83858.11, Hard violations = 3, Best = 3
[2026-01-01T18:22:43.117Z] [INFO] [Phase 1] Iteration 2000: Temp = 52773.56, Hard violations = 1, Best = 1
[2026-01-01T18:22:44.209Z] [INFO] [Phase 1] Iteration 2500: Temp = 45171.73, Hard violations = 1, Best = 1
[2026-01-01T18:22:46.349Z] [INFO] [Phase 1] Iteration 3500: Temp = 33578.88, Hard violations = 1, Best = 1
[2026-01-01T18:22:46.454Z] [INFO] Phase 1 complete: Hard violations = 0
[2026-01-01T18:22:46.455Z] [INFO] Phase 2: Optimizing soft constraints
[2026-01-01T18:22:47.450Z] [INFO] [Phase 2] Iteration 4000: Temp = 28842.77, Current = 26.60, Best = 26.54
[2026-01-01T18:22:48.516Z] [INFO] [Phase 2] Iteration 4500: Temp = 24998.69, Current = 26.87, Best = 26.54
[2026-01-01T18:22:49.574Z] [INFO] [Phase 2] Iteration 5000: Temp = 21634.46, Current = 26.82, Best = 26.54
[2026-01-01T18:22:50.611Z] [INFO] [Phase 2] Iteration 5500: Temp = 18826.26, Current = 26.70, Best = 26.54
[2026-01-01T18:22:51.715Z] [INFO] [Phase 2] Iteration 6000: Temp = 16098.30, Current = 26.64, Best = 26.54
[2026-01-01T18:22:52.771Z] [INFO] [Phase 2] Iteration 6500: Temp = 13862.34, Current = 26.70, Best = 26.54
[2026-01-01T18:22:53.950Z] [INFO] [Phase 2] Iteration 7000: Temp = 11824.06, Current = 26.87, Best = 26.54
[2026-01-01T18:23:00.436Z] [INFO] [Phase 2] Iteration 10000: Temp = 4847.26, Current = 26.77, Best = 26.54
[2026-01-01T18:23:01.465Z] [INFO] [Phase 2] Iteration 10500: Temp = 4228.64, Current = 26.75, Best = 26.54
[2026-01-01T18:23:04.711Z] [INFO] [Phase 2] Iteration 12000: Temp = 2714.94, Current = 26.85, Best = 26.54
[2026-01-01T18:23:05.823Z] [INFO] [Phase 2] Iteration 12500: Temp = 2329.68, Current = 26.83, Best = 26.54
[2026-01-01T18:23:06.967Z] [INFO] [Phase 2] Iteration 13000: Temp = 1988.12, Current = 26.94, Best = 26.54
[2026-01-01T18:23:09.155Z] [INFO] [Phase 2] Iteration 14000: Temp = 1463.91, Current = 26.94, Best = 26.54
[2026-01-01T18:23:10.267Z] [INFO] [Phase 2] Iteration 14500: Temp = 1243.06, Current = 26.90, Best = 26.54
[2026-01-01T18:23:11.864Z] [INFO] [Phase 2] Reheating #1: Temperature = 149927.82, Fitness = 26.54
[2026-01-01T18:23:12.423Z] [INFO] [Phase 2] Iteration 15500: Temp = 138675.19, Current = 26.80, Best = 26.54
[2026-01-01T18:23:12.852Z] [INFO] [Phase 2] Iteration 16000: Temp = 119414.08, Current = 26.90, Best = 26.54
[2026-01-01T18:23:16.127Z] [INFO] [Phase 2] Iteration 17500: Temp = 75677.66, Current = 26.88, Best = 26.54
[2026-01-01T18:23:17.232Z] [INFO] [Phase 2] Iteration 18000: Temp = 64485.67, Current = 26.97, Best = 26.54
[2026-01-01T18:23:21.573Z] [INFO] [Phase 2] Iteration 20000: Temp = 35402.88, Current = 26.86, Best = 26.54
[2026-01-01T18:23:21.575Z] [INFO] Optimization complete {"iterations":20000,"reheats":1,"finalTemperature":"35402.8775","fitness":"26.54","hardViolations":0,"softViolations":8}
[2026-01-01T18:23:21.576Z] [INFO] Operator Statistics:
[2026-01-01T18:23:21.576Z] [INFO]   Fix Friday Prayer Conflict: Attempts = 0, Improvements = 0, Accepted = 0, Success Rate = 0.00%
[2026-01-01T18:23:21.576Z] [INFO]   Swap Friday with Non-Friday: Attempts = 0, Improvements = 0, Accepted = 0, Success Rate = 0.00%
[2026-01-01T18:23:21.576Z] [INFO]   Fix Lecturer Conflict: Attempts = 0, Improvements = 0, Accepted = 0, Success Rate = 0.00%
[2026-01-01T18:23:21.576Z] [INFO]   Fix Room Conflict: Attempts = 0, Improvements = 0, Accepted = 0, Success Rate = 0.00%
[2026-01-01T18:23:21.576Z] [INFO]   Fix Max Daily Periods: Attempts = 10, Improvements = 9, Accepted = 10, Success Rate = 90.00%
[2026-01-01T18:23:21.576Z] [INFO]   Fix Room Capacity: Attempts = 0, Improvements = 0, Accepted = 0, Success Rate = 0.00%
[2026-01-01T18:23:21.576Z] [INFO]   Change Time Slot and Room: Attempts = 2185, Improvements = 253, Accepted = 1985, Success Rate = 11.58%
[2026-01-01T18:23:21.576Z] [INFO]   Change Time Slot: Attempts = 1714, Improvements = 117, Accepted = 1456, Success Rate = 6.83%
[2026-01-01T18:23:21.576Z] [INFO]   Change Room: Attempts = 3303, Improvements = 215, Accepted = 3303, Success Rate = 6.51%
[2026-01-01T18:23:21.576Z] [INFO]   Swap Classes: Attempts = 4883, Improvements = 32, Accepted = 223, Success Rate = 0.66%
======================================================================

✨ OPTIMIZATION COMPLETE!

Cache stats: {
  timeCache: {
    timeToMinutes: 20,
    minutesToTime: 17,
  },
  endTimeCache: 271,
  prayerOverlapCache: 271,
  totalEntries: 579,
}
📊 RESULTS:
   Final fitness: 26.54
   Hard constraint violations: 0
   Soft constraint violations: 8
   Total iterations: 20000
   Reheating events: 1
   Final temperature: 35402.8775
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
      Attempts: 10
      Improvements: 9
      Success rate: 90.00%
   Fix Room Capacity:
      Attempts: 0
      Improvements: 0
      Success rate: 0.00%
   Change Time Slot and Room:
      Attempts: 2185
      Improvements: 253
      Success rate: 11.58%
   Change Time Slot:
      Attempts: 1714
      Improvements: 117
      Success rate: 6.83%
   Change Room:
      Attempts: 3303
      Improvements: 215
      Success rate: 6.51%
   Swap Classes:
      Attempts: 4883
      Improvements: 32
      Success rate: 0.66%

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
  ⚠️  Skipping AC135343: No lecturers on class Skripsi
  ⚠️  Skipping GS13PW02: No lecturers on class KERJA PRAKTIK
  ⚠️  Skipping GS13PW02: No lecturers on class Praktik Kerja Lapang
  ⚠️  Skipping GS13PW02: No lecturers on class Kerja Praktik/Magang
  ⚠️  Skipping GS13PW02: No lecturers on class Kerja Praktik
  ⚠️  Skipping GS13CZ02: No lecturers on class Kewarganegaraan
  ⚠️  Skipping MM23RS03: No lecturers on class Research Seminar
  ⚠️  Skipping GS13IP12: No lecturers on class PROYEK INTERDISIPLIN
  ⚠️  Skipping GS13IP12: No lecturers on class Proyek Interdisipliner
  ⚠️  Skipping CE11UT46: No lecturers on class Skripsi
  ⚠️  Skipping GS13CZ02: No lecturers on class Kewarganegaraan
  ⚠️  Skipping GS13TH46: No lecturers on class Skripsi
  ⚠️  Skipping VD13KP02: No lecturers on class Kerja Praktik
  ⚠️  Skipping GS13IP12: No lecturers on class Proyek Interdisipliner
  ⚠️  Skipping GS13PW02: No lecturers on class Kerja Praktik
  ⚠️  Skipping GS13IP12: No lecturers on class Proyek Interdisiplin
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
   Cooling rate: 0.9995
   Max iterations: 20000

🚀 Starting optimization...

======================================================================
[2026-01-01T18:24:24.461Z] [INFO] Simulated Annealing initialized {"hardConstraints":11,"softConstraints":8,"moveGenerators":10,"parallelEvaluation":true,"config":{"initialTemperature":100000,"minTemperature":1e-7,"coolingRate":0.9995,"maxIterations":20000}}
[2026-01-01T18:24:24.462Z] [INFO] Parallel evaluation enabled with auto workers
[2026-01-01T18:24:24.463Z] [INFO] Starting optimization...
[2026-01-01T18:24:24.463Z] [INFO] Phase 1: Eliminating hard constraint violations
[2026-01-01T18:24:24.479Z] [INFO] Initial state {"fitness":"222247.32","hardViolations":14}
[2026-01-01T18:24:26.054Z] [INFO] [Phase 1] Iteration 500: Temp = 82485.46, Hard violations = 5, Best = 5
[2026-01-01T18:24:27.334Z] [INFO] [Phase 1] Iteration 1000: Temp = 69691.61, Hard violations = 5, Best = 5
[2026-01-01T18:24:28.553Z] [INFO] [Phase 1] Iteration 1500: Temp = 59325.52, Hard violations = 4, Best = 4
[2026-01-01T18:24:29.789Z] [INFO] [Phase 1] Iteration 2000: Temp = 50577.14, Hard violations = 3, Best = 3
[2026-01-01T18:24:32.037Z] [INFO] [Phase 1] Iteration 3000: Temp = 37937.04, Hard violations = 2, Best = 2
[2026-01-01T18:24:32.994Z] [INFO] [Phase 1] Iteration 3500: Temp = 33730.37, Hard violations = 2, Best = 2
[2026-01-01T18:24:33.939Z] [INFO] [Phase 1] Iteration 4000: Temp = 29960.17, Hard violations = 2, Best = 2
[2026-01-01T18:24:36.824Z] [INFO] [Phase 1] Iteration 5500: Temp = 20994.91, Hard violations = 1, Best = 1
[2026-01-01T18:24:38.655Z] [INFO] [Phase 1] Iteration 6500: Temp = 16730.33, Hard violations = 1, Best = 1
[2026-01-01T18:24:40.533Z] [INFO] [Phase 1] Iteration 7500: Temp = 13186.11, Hard violations = 1, Best = 1
[2026-01-01T18:24:41.516Z] [INFO] [Phase 1] Iteration 8000: Temp = 11653.81, Hard violations = 1, Best = 1
[2026-01-01T18:24:42.751Z] [INFO] Phase 1 complete: Hard violations = 1
[2026-01-01T18:24:42.752Z] [INFO] Phase 1.5: Intensification - targeting remaining hard violations
[2026-01-01T18:24:42.752Z] [INFO] [Intensification] Attempt 1/3
[2026-01-01T18:24:44.136Z] [INFO] [Intensification] Iter 500: Hard violations = 3, Best = 1
[2026-01-01T18:24:45.591Z] [INFO] [Intensification] Iter 1000: Hard violations = 4, Best = 1
[2026-01-01T18:24:47.082Z] [INFO] [Intensification] Iter 1500: Hard violations = 3, Best = 1
[2026-01-01T18:24:47.920Z] [INFO] [Intensification] Iter 2000: Hard violations = 3, Best = 1
[2026-01-01T18:24:47.920Z] [INFO] [Intensification] Attempt 2/3
[2026-01-01T18:24:49.310Z] [INFO] [Intensification] Iter 500: Hard violations = 2, Best = 1
[2026-01-01T18:24:50.771Z] [INFO] [Intensification] Iter 1000: Hard violations = 2, Best = 1
[2026-01-01T18:24:52.332Z] [INFO] [Intensification] Iter 1500: Hard violations = 5, Best = 1
[2026-01-01T18:24:53.956Z] [INFO] [Intensification] Iter 2000: Hard violations = 12, Best = 1
[2026-01-01T18:24:53.957Z] [INFO] [Intensification] Attempt 3/3
[2026-01-01T18:24:55.267Z] [INFO] [Intensification] Iter 500: Hard violations = 3, Best = 1
[2026-01-01T18:24:56.861Z] [INFO] [Intensification] Iter 1000: Hard violations = 5, Best = 1
[2026-01-01T18:24:58.460Z] [INFO] [Intensification] Iter 1500: Hard violations = 5, Best = 1
[2026-01-01T18:24:59.999Z] [INFO] [Intensification] Iter 2000: Hard violations = 5, Best = 1
[2026-01-01T18:24:59.999Z] [WARN] [Intensification] Could not eliminate all hard violations. Remaining: 1
[2026-01-01T18:24:59.999Z] [INFO] Phase 2: Optimizing soft constraints
[2026-01-01T18:25:02.778Z] [INFO] [Phase 2] Iteration 16000: Temp = 6955.30, Current = 50026.77, Best = 50026.66
[2026-01-01T18:25:04.984Z] [INFO] [Phase 2] Iteration 17000: Temp = 5222.27, Current = 50026.77, Best = 50026.66
[2026-01-01T18:25:06.148Z] [INFO] [Phase 2] Iteration 17500: Temp = 4474.49, Current = 50026.84, Best = 50026.66
[2026-01-01T18:25:07.318Z] [INFO] [Phase 2] Iteration 18000: Temp = 3837.63, Current = 50026.95, Best = 50026.66
[2026-01-01T18:25:08.506Z] [INFO] [Phase 2] Iteration 18500: Temp = 3279.91, Current = 50026.97, Best = 50026.66
[2026-01-01T18:25:11.940Z] [INFO] [Phase 2] Iteration 20000: Temp = 2081.74, Current = 50026.90, Best = 50026.66
[2026-01-01T18:25:11.943Z] [INFO] Optimization complete {"iterations":20000,"reheats":0,"finalTemperature":"2081.7359","fitness":"50026.66","hardViolations":1,"softViolations":8}
[2026-01-01T18:25:11.943Z] [INFO] Operator Statistics:
[2026-01-01T18:25:11.943Z] [INFO]   Fix Friday Prayer Conflict: Attempts = 1, Improvements = 1, Accepted = 1, Success Rate = 100.00%
[2026-01-01T18:25:11.943Z] [INFO]   Swap Friday with Non-Friday: Attempts = 0, Improvements = 0, Accepted = 0, Success Rate = 0.00%
[2026-01-01T18:25:11.943Z] [INFO]   Fix Lecturer Conflict: Attempts = 815, Improvements = 136, Accepted = 758, Success Rate = 16.69%
[2026-01-01T18:25:11.943Z] [INFO]   Fix Room Conflict: Attempts = 4, Improvements = 3, Accepted = 4, Success Rate = 75.00%
[2026-01-01T18:25:11.943Z] [INFO]   Fix Max Daily Periods: Attempts = 1463, Improvements = 5, Accepted = 1463, Success Rate = 0.34%
[2026-01-01T18:25:11.943Z] [INFO]   Fix Room Capacity: Attempts = 161, Improvements = 4, Accepted = 161, Success Rate = 2.48%
[2026-01-01T18:25:11.943Z] [INFO]   Change Time Slot and Room: Attempts = 2351, Improvements = 215, Accepted = 2194, Success Rate = 9.15%
[2026-01-01T18:25:11.943Z] [INFO]   Change Time Slot: Attempts = 2092, Improvements = 96, Accepted = 1843, Success Rate = 4.59%
[2026-01-01T18:25:11.943Z] [INFO]   Change Room: Attempts = 2857, Improvements = 141, Accepted = 2857, Success Rate = 4.94%
[2026-01-01T18:25:11.943Z] [INFO]   Swap Classes: Attempts = 3998, Improvements = 15, Accepted = 191, Success Rate = 0.38%
======================================================================

✨ OPTIMIZATION COMPLETE!

Cache stats: {
  timeCache: {
    timeToMinutes: 20,
    minutesToTime: 17,
  },
  endTimeCache: 274,
  prayerOverlapCache: 274,
  totalEntries: 585,
}
📊 RESULTS:
   Final fitness: 50026.66
   Hard constraint violations: 1
   Soft constraint violations: 8
   Total iterations: 20000
   Reheating events: 0
   Final temperature: 2081.7359
   Classes scheduled: 356/373

📈 OPERATOR STATISTICS:
   Fix Friday Prayer Conflict:
      Attempts: 1
      Improvements: 1
      Success rate: 100.00%
   Swap Friday with Non-Friday:
      Attempts: 0
      Improvements: 0
      Success rate: 0.00%
   Fix Lecturer Conflict:
      Attempts: 815
      Improvements: 136
      Success rate: 16.69%
   Fix Room Conflict:
      Attempts: 4
      Improvements: 3
      Success rate: 75.00%
   Fix Max Daily Periods:
      Attempts: 1463
      Improvements: 5
      Success rate: 0.34%
   Fix Room Capacity:
      Attempts: 161
      Improvements: 4
      Success rate: 2.48%
   Change Time Slot and Room:
      Attempts: 2351
      Improvements: 215
      Success rate: 9.15%
   Change Time Slot:
      Attempts: 2092
      Improvements: 96
      Success rate: 4.59%
   Change Room:
      Attempts: 2857
      Improvements: 141
      Success rate: 4.94%
   Swap Classes:
      Attempts: 3998
      Improvements: 15
      Success rate: 0.38%

⚠️  VIOLATIONS (9):
   - [hard] Max Daily Periods: Lecturer ANW exceeds max daily periods (9) on Monday with 10 periods
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
  ⚠️  Skipping GS13PW02: No lecturers on class KERJA PRAKTIK
  ⚠️  Skipping GS13CZ02: No lecturers on class Kewarganegaraan
  ⚠️  Skipping GS13PW02: No lecturers on class Kerja Praktik/Magang
  ⚠️  Skipping GS13IP12: No lecturers on class PROYEK INTERDISIPLIN
  ⚠️  Skipping VD13KP02: No lecturers on class Kerja Praktik
  ⚠️  Skipping GS13CZ02: No lecturers on class Kewarganegaraan
  ⚠️  Skipping GS13IP12: No lecturers on class Proyek Interdisiplin
  ⚠️  Skipping MM23RS03: No lecturers on class Research Seminar
  ⚠️  Skipping GS13PW02: No lecturers on class Kerja Praktik
  ⚠️  Skipping GS13IP12: No lecturers on class Proyek Interdisipliner
  ⚠️  Skipping GS13TH46: No lecturers on class Skripsi
  ⚠️  Skipping AC135343: No lecturers on class Skripsi
  ⚠️  Skipping CE11UT46: No lecturers on class Skripsi
  ⚠️  Skipping GS13PW02: No lecturers on class Kerja Praktik
  ⚠️  Skipping GS13IP12: No lecturers on class Proyek Interdisipliner
  ⚠️  Skipping GS13CZ02: No lecturers on class Kewarganegaraan
  ⚠️  Skipping GS13PW02: No lecturers on class Praktik Kerja Lapang

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
   Cooling rate: 0.9995
   Max iterations: 20000

🚀 Starting optimization...

======================================================================
[2026-01-01T18:25:15.670Z] [INFO] Simulated Annealing initialized {"hardConstraints":11,"softConstraints":8,"moveGenerators":10,"parallelEvaluation":true,"config":{"initialTemperature":100000,"minTemperature":1e-7,"coolingRate":0.9995,"maxIterations":20000}}
[2026-01-01T18:25:15.671Z] [INFO] Parallel evaluation enabled with auto workers
[2026-01-01T18:25:15.672Z] [INFO] Starting optimization...
[2026-01-01T18:25:15.672Z] [INFO] Phase 1: Eliminating hard constraint violations
[2026-01-01T18:25:15.683Z] [INFO] Initial state {"fitness":"215739.05","hardViolations":11}
[2026-01-01T18:25:17.037Z] [INFO] [Phase 1] Iteration 500: Temp = 86326.22, Hard violations = 4, Best = 4
[2026-01-01T18:25:19.510Z] [INFO] [Phase 1] Iteration 1500: Temp = 64493.25, Hard violations = 4, Best = 4
[2026-01-01T18:25:21.271Z] [INFO] [Phase 1] Iteration 2500: Temp = 47204.18, Hard violations = 3, Best = 3
[2026-01-01T18:25:22.465Z] [INFO] [Phase 1] Iteration 3000: Temp = 40912.95, Hard violations = 3, Best = 3
[2026-01-01T18:25:23.774Z] [INFO] [Phase 1] Iteration 3500: Temp = 35195.18, Hard violations = 3, Best = 3
[2026-01-01T18:25:26.168Z] [INFO] [Phase 1] Iteration 4500: Temp = 26731.44, Hard violations = 3, Best = 3
[2026-01-01T18:25:27.408Z] [INFO] [Phase 1] Iteration 5000: Temp = 22961.12, Hard violations = 3, Best = 3
[2026-01-01T18:25:30.675Z] [INFO] [Phase 1] Iteration 6500: Temp = 16203.30, Hard violations = 3, Best = 3
[2026-01-01T18:25:34.441Z] [INFO] [Phase 1] Iteration 8500: Temp = 10974.98, Hard violations = 3, Best = 3
[2026-01-01T18:25:35.312Z] [INFO] Phase 1 complete: Hard violations = 3
[2026-01-01T18:25:35.312Z] [INFO] Phase 1.5: Intensification - targeting remaining hard violations
[2026-01-01T18:25:35.312Z] [INFO] [Intensification] Attempt 1/3
[2026-01-01T18:25:36.885Z] [INFO] [Intensification] Iter 500: Hard violations = 3, Best = 3
[2026-01-01T18:25:38.463Z] [INFO] [Intensification] Iter 1000: Hard violations = 8, Best = 3
[2026-01-01T18:25:40.084Z] [INFO] [Intensification] Iter 1500: Hard violations = 9, Best = 3
[2026-01-01T18:25:41.697Z] [INFO] [Intensification] Iter 2000: Hard violations = 9, Best = 3
[2026-01-01T18:25:41.697Z] [INFO] [Intensification] Attempt 2/3
[2026-01-01T18:25:43.377Z] [INFO] [Intensification] Iter 500: Hard violations = 14, Best = 3
[2026-01-01T18:25:45.072Z] [INFO] [Intensification] Iter 1000: Hard violations = 16, Best = 3
[2026-01-01T18:25:46.774Z] [INFO] [Intensification] Iter 1500: Hard violations = 19, Best = 3
[2026-01-01T18:25:48.474Z] [INFO] [Intensification] Iter 2000: Hard violations = 16, Best = 3
[2026-01-01T18:25:48.475Z] [INFO] [Intensification] Attempt 3/3
[2026-01-01T18:25:50.125Z] [INFO] [Intensification] Iter 500: Hard violations = 7, Best = 3
[2026-01-01T18:25:51.782Z] [INFO] [Intensification] Iter 1000: Hard violations = 10, Best = 3
[2026-01-01T18:25:52.727Z] [INFO] [Intensification] Iter 1500: Hard violations = 10, Best = 3
[2026-01-01T18:25:54.431Z] [INFO] [Intensification] Iter 2000: Hard violations = 10, Best = 3
[2026-01-01T18:25:54.431Z] [WARN] [Intensification] Could not eliminate all hard violations. Remaining: 3
[2026-01-01T18:25:54.431Z] [INFO] Phase 2: Optimizing soft constraints
[2026-01-01T18:25:54.514Z] [INFO] [Phase 2] Iteration 15000: Temp = 9880.78, Current = 150026.24, Best = 150026.21
[2026-01-01T18:25:57.632Z] [INFO] [Phase 2] Iteration 16500: Temp = 6924.06, Current = 100026.44, Best = 100026.35
[2026-01-01T18:25:58.576Z] [INFO] [Phase 2] Iteration 17000: Temp = 6258.73, Current = 50026.46, Best = 50026.46
[2026-01-01T18:25:59.501Z] [INFO] [Phase 2] Iteration 17500: Temp = 5646.02, Current = 50026.31, Best = 50026.31
[2026-01-01T18:26:01.351Z] [INFO] [Phase 2] Iteration 18500: Temp = 4615.41, Current = 50026.49, Best = 50026.25
[2026-01-01T18:26:02.303Z] [INFO] [Phase 2] Iteration 19000: Temp = 4155.26, Current = 50026.66, Best = 50026.25
[2026-01-01T18:26:04.151Z] [INFO] [Phase 2] Iteration 20000: Temp = 3389.98, Current = 50026.59, Best = 50026.25
[2026-01-01T18:26:04.154Z] [INFO] Optimization complete {"iterations":20000,"reheats":0,"finalTemperature":"3389.9800","fitness":"50026.25","hardViolations":1,"softViolations":8}
[2026-01-01T18:26:04.154Z] [INFO] Operator Statistics:
[2026-01-01T18:26:04.154Z] [INFO]   Fix Friday Prayer Conflict: Attempts = 1341, Improvements = 4, Accepted = 1194, Success Rate = 0.30%
[2026-01-01T18:26:04.154Z] [INFO]   Swap Friday with Non-Friday: Attempts = 1247, Improvements = 1, Accepted = 1245, Success Rate = 0.08%
[2026-01-01T18:26:04.154Z] [INFO]   Fix Lecturer Conflict: Attempts = 1630, Improvements = 216, Accepted = 1568, Success Rate = 13.25%
[2026-01-01T18:26:04.154Z] [INFO]   Fix Room Conflict: Attempts = 20, Improvements = 14, Accepted = 20, Success Rate = 70.00%
[2026-01-01T18:26:04.154Z] [INFO]   Fix Max Daily Periods: Attempts = 226, Improvements = 6, Accepted = 226, Success Rate = 2.65%
[2026-01-01T18:26:04.154Z] [INFO]   Fix Room Capacity: Attempts = 215, Improvements = 3, Accepted = 215, Success Rate = 1.40%
[2026-01-01T18:26:04.154Z] [INFO]   Change Time Slot and Room: Attempts = 1658, Improvements = 147, Accepted = 1572, Success Rate = 8.87%
[2026-01-01T18:26:04.154Z] [INFO]   Change Time Slot: Attempts = 1479, Improvements = 73, Accepted = 1317, Success Rate = 4.94%
[2026-01-01T18:26:04.154Z] [INFO]   Change Room: Attempts = 2095, Improvements = 134, Accepted = 2095, Success Rate = 6.40%
[2026-01-01T18:26:04.154Z] [INFO]   Swap Classes: Attempts = 2856, Improvements = 18, Accepted = 167, Success Rate = 0.63%
======================================================================

✨ OPTIMIZATION COMPLETE!

Cache stats: {
  timeCache: {
    timeToMinutes: 20,
    minutesToTime: 17,
  },
  endTimeCache: 266,
  prayerOverlapCache: 266,
  totalEntries: 569,
}
📊 RESULTS:
   Final fitness: 50026.25
   Hard constraint violations: 1
   Soft constraint violations: 8
   Total iterations: 20000
   Reheating events: 0
   Final temperature: 3389.9800
   Classes scheduled: 356/373

📈 OPERATOR STATISTICS:
   Fix Friday Prayer Conflict:
      Attempts: 1341
      Improvements: 4
      Success rate: 0.30%
   Swap Friday with Non-Friday:
      Attempts: 1247
      Improvements: 1
      Success rate: 0.08%
   Fix Lecturer Conflict:
      Attempts: 1630
      Improvements: 216
      Success rate: 13.25%
   Fix Room Conflict:
      Attempts: 20
      Improvements: 14
      Success rate: 70.00%
   Fix Max Daily Periods:
      Attempts: 226
      Improvements: 6
      Success rate: 2.65%
   Fix Room Capacity:
      Attempts: 215
      Improvements: 3
      Success rate: 1.40%
   Change Time Slot and Room:
      Attempts: 1658
      Improvements: 147
      Success rate: 8.87%
   Change Time Slot:
      Attempts: 1479
      Improvements: 73
      Success rate: 4.94%
   Change Room:
      Attempts: 2095
      Improvements: 134
      Success rate: 6.40%
   Swap Classes:
      Attempts: 2856
      Improvements: 18
      Success rate: 0.63%

⚠️  VIOLATIONS (9):
   - [hard] No Friday Pray Conflict: Class IF13RP12 (Rekayasa Perangkat Lunak) overlaps with Friday prayer time (11:40-13:10). Class time: 10:50-12:30
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
  ⚠️  Skipping CE11UT46: No lecturers on class Skripsi
  ⚠️  Skipping MM23RS03: No lecturers on class Research Seminar
  ⚠️  Skipping GS13CZ02: No lecturers on class Kewarganegaraan
  ⚠️  Skipping GS13IP12: No lecturers on class Proyek Interdisipliner
  ⚠️  Skipping AC135343: No lecturers on class Skripsi
  ⚠️  Skipping GS13CZ02: No lecturers on class Kewarganegaraan
  ⚠️  Skipping GS13PW02: No lecturers on class KERJA PRAKTIK
  ⚠️  Skipping GS13IP12: No lecturers on class Proyek Interdisipliner
  ⚠️  Skipping GS13PW02: No lecturers on class Praktik Kerja Lapang
  ⚠️  Skipping GS13IP12: No lecturers on class Proyek Interdisiplin
  ⚠️  Skipping VD13KP02: No lecturers on class Kerja Praktik
  ⚠️  Skipping GS13CZ02: No lecturers on class Kewarganegaraan
  ⚠️  Skipping GS13IP12: No lecturers on class PROYEK INTERDISIPLIN
  ⚠️  Skipping GS13TH46: No lecturers on class Skripsi
  ⚠️  Skipping GS13PW02: No lecturers on class Kerja Praktik/Magang
  ⚠️  Skipping GS13PW02: No lecturers on class Kerja Praktik
  ⚠️  Skipping GS13PW02: No lecturers on class Kerja Praktik

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
   Cooling rate: 0.9995
   Max iterations: 20000

🚀 Starting optimization...

======================================================================
[2026-01-01T18:26:07.633Z] [INFO] Simulated Annealing initialized {"hardConstraints":11,"softConstraints":8,"moveGenerators":10,"parallelEvaluation":true,"config":{"initialTemperature":100000,"minTemperature":1e-7,"coolingRate":0.9995,"maxIterations":20000}}
[2026-01-01T18:26:07.634Z] [INFO] Parallel evaluation enabled with auto workers
[2026-01-01T18:26:07.634Z] [INFO] Starting optimization...
[2026-01-01T18:26:07.634Z] [INFO] Phase 1: Eliminating hard constraint violations
[2026-01-01T18:26:07.646Z] [INFO] Initial state {"fitness":"162524.89","hardViolations":10}
[2026-01-01T18:26:08.925Z] [INFO] [Phase 1] Iteration 500: Temp = 86585.66, Hard violations = 3, Best = 3
[2026-01-01T18:26:09.900Z] [INFO] [Phase 1] Iteration 1000: Temp = 77023.06, Hard violations = 3, Best = 3
[2026-01-01T18:26:10.901Z] [INFO] [Phase 1] Iteration 1500: Temp = 68208.86, Hard violations = 3, Best = 3
[2026-01-01T18:26:11.916Z] [INFO] [Phase 1] Iteration 2000: Temp = 60312.76, Hard violations = 3, Best = 3
[2026-01-01T18:26:12.878Z] [INFO] [Phase 1] Iteration 2500: Temp = 54001.73, Hard violations = 3, Best = 3
[2026-01-01T18:26:15.799Z] [INFO] [Phase 1] Iteration 4000: Temp = 38165.40, Hard violations = 3, Best = 3
[2026-01-01T18:26:16.891Z] [INFO] [Phase 1] Iteration 4500: Temp = 32897.35, Hard violations = 3, Best = 3
[2026-01-01T18:26:17.907Z] [INFO] [Phase 1] Iteration 5000: Temp = 29147.29, Hard violations = 3, Best = 3
[2026-01-01T18:26:18.951Z] [INFO] [Phase 1] Iteration 5500: Temp = 25670.18, Hard violations = 2, Best = 2
[2026-01-01T18:26:21.925Z] [INFO] [Phase 1] Iteration 7000: Temp = 17809.62, Hard violations = 1, Best = 1
[2026-01-01T18:26:22.949Z] [INFO] [Phase 1] Iteration 7500: Temp = 15811.05, Hard violations = 1, Best = 1
[2026-01-01T18:26:24.465Z] [INFO] [Phase 1] Iteration 8500: Temp = 12062.98, Hard violations = 1, Best = 1
[2026-01-01T18:26:25.872Z] [INFO] Phase 1 complete: Hard violations = 1
[2026-01-01T18:26:25.872Z] [INFO] Phase 1.5: Intensification - targeting remaining hard violations
[2026-01-01T18:26:25.872Z] [INFO] [Intensification] Attempt 1/3
[2026-01-01T18:26:27.523Z] [INFO] [Intensification] Iter 500: Hard violations = 13, Best = 1
[2026-01-01T18:26:29.161Z] [INFO] [Intensification] Iter 1000: Hard violations = 12, Best = 1
[2026-01-01T18:26:30.811Z] [INFO] [Intensification] Iter 1500: Hard violations = 9, Best = 1
[2026-01-01T18:26:32.504Z] [INFO] [Intensification] Iter 2000: Hard violations = 11, Best = 1
[2026-01-01T18:26:32.504Z] [INFO] [Intensification] Attempt 2/3
[2026-01-01T18:26:34.000Z] [INFO] [Intensification] Iter 500: Hard violations = 2, Best = 1
[2026-01-01T18:26:35.602Z] [INFO] [Intensification] Iter 1000: Hard violations = 3, Best = 1
[2026-01-01T18:26:37.223Z] [INFO] [Intensification] Iter 1500: Hard violations = 3, Best = 1
[2026-01-01T18:26:38.840Z] [INFO] [Intensification] Iter 2000: Hard violations = 3, Best = 1
[2026-01-01T18:26:38.840Z] [INFO] [Intensification] Attempt 3/3
[2026-01-01T18:26:40.411Z] [INFO] [Intensification] Iter 500: Hard violations = 5, Best = 1
[2026-01-01T18:26:42.040Z] [INFO] [Intensification] Iter 1000: Hard violations = 5, Best = 1
[2026-01-01T18:26:43.668Z] [INFO] [Intensification] Iter 1500: Hard violations = 6, Best = 1
[2026-01-01T18:26:45.317Z] [INFO] [Intensification] Iter 2000: Hard violations = 5, Best = 1
[2026-01-01T18:26:45.317Z] [WARN] [Intensification] Could not eliminate all hard violations. Remaining: 1
[2026-01-01T18:26:45.317Z] [INFO] Phase 2: Optimizing soft constraints
[2026-01-01T18:26:47.220Z] [INFO] [Phase 2] Iteration 16000: Temp = 7869.82, Current = 50026.59, Best = 50026.46
[2026-01-01T18:26:48.211Z] [INFO] [Phase 2] Iteration 16500: Temp = 6934.46, Current = 50026.60, Best = 50026.45
[2026-01-01T18:26:50.172Z] [INFO] [Phase 2] Iteration 17500: Temp = 5378.66, Current = 50026.77, Best = 50026.45
[2026-01-01T18:26:52.184Z] [INFO] [Phase 2] Iteration 18500: Temp = 4165.66, Current = 26.79, Best = 26.76
[2026-01-01T18:26:54.498Z] [INFO] [Phase 2] Iteration 19500: Temp = 3053.53, Current = 26.85, Best = 26.73
[2026-01-01T18:26:55.600Z] [INFO] Optimization complete {"iterations":20000,"reheats":0,"finalTemperature":"2625.4705","fitness":"26.73","hardViolations":0,"softViolations":8}
[2026-01-01T18:26:55.600Z] [INFO] Operator Statistics:
[2026-01-01T18:26:55.600Z] [INFO]   Fix Friday Prayer Conflict: Attempts = 0, Improvements = 0, Accepted = 0, Success Rate = 0.00%
[2026-01-01T18:26:55.600Z] [INFO]   Swap Friday with Non-Friday: Attempts = 0, Improvements = 0, Accepted = 0, Success Rate = 0.00%
[2026-01-01T18:26:55.600Z] [INFO]   Fix Lecturer Conflict: Attempts = 777, Improvements = 33, Accepted = 753, Success Rate = 4.25%
[2026-01-01T18:26:55.600Z] [INFO]   Fix Room Conflict: Attempts = 119, Improvements = 3, Accepted = 119, Success Rate = 2.52%
[2026-01-01T18:26:55.600Z] [INFO]   Fix Max Daily Periods: Attempts = 1294, Improvements = 5, Accepted = 1294, Success Rate = 0.39%
[2026-01-01T18:26:55.600Z] [INFO]   Fix Room Capacity: Attempts = 263, Improvements = 5, Accepted = 263, Success Rate = 1.90%
[2026-01-01T18:26:55.600Z] [INFO]   Change Time Slot and Room: Attempts = 2178, Improvements = 227, Accepted = 2047, Success Rate = 10.42%
[2026-01-01T18:26:55.600Z] [INFO]   Change Time Slot: Attempts = 2011, Improvements = 112, Accepted = 1788, Success Rate = 5.57%
[2026-01-01T18:26:55.600Z] [INFO]   Change Room: Attempts = 2776, Improvements = 150, Accepted = 2776, Success Rate = 5.40%
[2026-01-01T18:26:55.600Z] [INFO]   Swap Classes: Attempts = 3860, Improvements = 28, Accepted = 194, Success Rate = 0.73%
======================================================================

✨ OPTIMIZATION COMPLETE!

Cache stats: {
  timeCache: {
    timeToMinutes: 20,
    minutesToTime: 17,
  },
  endTimeCache: 272,
  prayerOverlapCache: 272,
  totalEntries: 581,
}
📊 RESULTS:
   Final fitness: 26.73
   Hard constraint violations: 0
   Soft constraint violations: 8
   Total iterations: 20000
   Reheating events: 0
   Final temperature: 2625.4705
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
      Attempts: 777
      Improvements: 33
      Success rate: 4.25%
   Fix Room Conflict:
      Attempts: 119
      Improvements: 3
      Success rate: 2.52%
   Fix Max Daily Periods:
      Attempts: 1294
      Improvements: 5
      Success rate: 0.39%
   Fix Room Capacity:
      Attempts: 263
      Improvements: 5
      Success rate: 1.90%
   Change Time Slot and Room:
      Attempts: 2178
      Improvements: 227
      Success rate: 10.42%
   Change Time Slot:
      Attempts: 2011
      Improvements: 112
      Success rate: 5.57%
   Change Room:
      Attempts: 2776
      Improvements: 150
      Success rate: 5.40%
   Swap Classes:
      Attempts: 3860
      Improvements: 28
      Success rate: 0.73%

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
  ⚠️  Skipping VD13KP02: No lecturers on class Kerja Praktik
  ⚠️  Skipping GS13PW02: No lecturers on class Praktik Kerja Lapang
  ⚠️  Skipping CE11UT46: No lecturers on class Skripsi
  ⚠️  Skipping GS13IP12: No lecturers on class Proyek Interdisipliner
  ⚠️  Skipping GS13IP12: No lecturers on class Proyek Interdisiplin
  ⚠️  Skipping AC135343: No lecturers on class Skripsi
  ⚠️  Skipping GS13PW02: No lecturers on class Kerja Praktik/Magang
  ⚠️  Skipping GS13TH46: No lecturers on class Skripsi
  ⚠️  Skipping MM23RS03: No lecturers on class Research Seminar
  ⚠️  Skipping GS13IP12: No lecturers on class Proyek Interdisipliner
  ⚠️  Skipping GS13PW02: No lecturers on class Kerja Praktik
  ⚠️  Skipping GS13PW02: No lecturers on class KERJA PRAKTIK
  ⚠️  Skipping GS13CZ02: No lecturers on class Kewarganegaraan
  ⚠️  Skipping GS13CZ02: No lecturers on class Kewarganegaraan
  ⚠️  Skipping GS13CZ02: No lecturers on class Kewarganegaraan
  ⚠️  Skipping GS13PW02: No lecturers on class Kerja Praktik
  ⚠️  Skipping GS13IP12: No lecturers on class PROYEK INTERDISIPLIN

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
   Cooling rate: 0.9995
   Max iterations: 20000

🚀 Starting optimization...

======================================================================
[2026-01-01T18:26:58.031Z] [INFO] Simulated Annealing initialized {"hardConstraints":11,"softConstraints":8,"moveGenerators":10,"parallelEvaluation":true,"config":{"initialTemperature":100000,"minTemperature":1e-7,"coolingRate":0.9995,"maxIterations":20000}}
[2026-01-01T18:26:58.032Z] [INFO] Parallel evaluation enabled with auto workers
[2026-01-01T18:26:58.033Z] [INFO] Starting optimization...
[2026-01-01T18:26:58.033Z] [INFO] Phase 1: Eliminating hard constraint violations
[2026-01-01T18:26:58.044Z] [INFO] Initial state {"fitness":"166691.67","hardViolations":10}
[2026-01-01T18:27:00.507Z] [INFO] [Phase 1] Iteration 1000: Temp = 72355.34, Hard violations = 4, Best = 4
[2026-01-01T18:27:02.830Z] [INFO] [Phase 1] Iteration 2000: Temp = 52720.80, Hard violations = 3, Best = 3
[2026-01-01T18:27:03.947Z] [INFO] [Phase 1] Iteration 2500: Temp = 45854.59, Hard violations = 3, Best = 3
[2026-01-01T18:27:05.018Z] [INFO] [Phase 1] Iteration 3000: Temp = 39942.49, Hard violations = 1, Best = 1
[2026-01-01T18:27:06.137Z] [INFO] [Phase 1] Iteration 3500: Temp = 34325.99, Hard violations = 1, Best = 1
[2026-01-01T18:27:07.260Z] [INFO] [Phase 1] Iteration 4000: Temp = 29440.30, Hard violations = 1, Best = 1
[2026-01-01T18:27:08.371Z] [INFO] [Phase 1] Iteration 4500: Temp = 25414.70, Hard violations = 1, Best = 1
[2026-01-01T18:27:09.480Z] [INFO] [Phase 1] Iteration 5000: Temp = 21884.76, Hard violations = 1, Best = 1
[2026-01-01T18:27:10.612Z] [INFO] [Phase 1] Iteration 5500: Temp = 18901.73, Hard violations = 1, Best = 1
[2026-01-01T18:27:11.743Z] [INFO] [Phase 1] Iteration 6000: Temp = 16195.20, Hard violations = 1, Best = 1
[2026-01-01T18:27:14.038Z] [INFO] [Phase 1] Iteration 7000: Temp = 11812.24, Hard violations = 1, Best = 1
[2026-01-01T18:27:15.274Z] [INFO] Phase 1 complete: Hard violations = 1
[2026-01-01T18:27:15.275Z] [INFO] Phase 1.5: Intensification - targeting remaining hard violations
[2026-01-01T18:27:15.275Z] [INFO] [Intensification] Attempt 1/3
[2026-01-01T18:27:15.501Z] [INFO] [Intensification] SUCCESS! All hard violations eliminated in attempt 1
[2026-01-01T18:27:15.501Z] [INFO] Phase 2: Optimizing soft constraints
[2026-01-01T18:27:17.319Z] [INFO] [Phase 2] Iteration 8500: Temp = 7885.57, Current = 26.82, Best = 26.57
[2026-01-01T18:27:18.404Z] [INFO] [Phase 2] Iteration 9000: Temp = 6834.61, Current = 26.79, Best = 26.57
[2026-01-01T18:27:19.505Z] [INFO] [Phase 2] Iteration 9500: Temp = 5861.82, Current = 27.01, Best = 26.57
[2026-01-01T18:27:21.597Z] [INFO] [Phase 2] Iteration 10500: Temp = 4379.30, Current = 27.14, Best = 26.57
[2026-01-01T18:27:23.764Z] [INFO] [Phase 2] Iteration 11500: Temp = 3252.14, Current = 26.85, Best = 26.57
[2026-01-01T18:27:29.352Z] [INFO] [Phase 2] Iteration 14500: Temp = 1386.94, Current = 26.92, Best = 26.57
[2026-01-01T18:27:30.377Z] [INFO] [Phase 2] Iteration 15000: Temp = 1207.52, Current = 26.91, Best = 26.57
[2026-01-01T18:27:31.759Z] [INFO] [Phase 2] Reheating #1: Temperature = 149927.82, Fitness = 26.57
[2026-01-01T18:27:33.545Z] [INFO] [Phase 2] Iteration 16500: Temp = 117341.99, Current = 27.10, Best = 26.57
[2026-01-01T18:27:34.645Z] [INFO] [Phase 2] Iteration 17000: Temp = 100640.45, Current = 27.02, Best = 26.57
[2026-01-01T18:27:35.722Z] [INFO] [Phase 2] Iteration 17500: Temp = 87227.40, Current = 26.95, Best = 26.57
[2026-01-01T18:27:36.888Z] [INFO] [Phase 2] Iteration 18000: Temp = 74438.92, Current = 26.98, Best = 26.57
[2026-01-01T18:27:37.956Z] [INFO] [Phase 2] Iteration 18500: Temp = 64550.20, Current = 26.98, Best = 26.57
[2026-01-01T18:27:41.328Z] [INFO] [Phase 2] Iteration 20000: Temp = 40846.82, Current = 27.08, Best = 26.57
[2026-01-01T18:27:41.331Z] [INFO] Optimization complete {"iterations":20000,"reheats":1,"finalTemperature":"40846.8155","fitness":"26.57","hardViolations":0,"softViolations":8}
[2026-01-01T18:27:41.331Z] [INFO] Operator Statistics:
[2026-01-01T18:27:41.331Z] [INFO]   Fix Friday Prayer Conflict: Attempts = 0, Improvements = 0, Accepted = 0, Success Rate = 0.00%
[2026-01-01T18:27:41.331Z] [INFO]   Swap Friday with Non-Friday: Attempts = 0, Improvements = 0, Accepted = 0, Success Rate = 0.00%
[2026-01-01T18:27:41.331Z] [INFO]   Fix Lecturer Conflict: Attempts = 0, Improvements = 0, Accepted = 0, Success Rate = 0.00%
[2026-01-01T18:27:41.331Z] [INFO]   Fix Room Conflict: Attempts = 0, Improvements = 0, Accepted = 0, Success Rate = 0.00%
[2026-01-01T18:27:41.331Z] [INFO]   Fix Max Daily Periods: Attempts = 7, Improvements = 5, Accepted = 7, Success Rate = 71.43%
[2026-01-01T18:27:41.331Z] [INFO]   Fix Room Capacity: Attempts = 0, Improvements = 0, Accepted = 0, Success Rate = 0.00%
[2026-01-01T18:27:41.331Z] [INFO]   Change Time Slot and Room: Attempts = 2101, Improvements = 262, Accepted = 1900, Success Rate = 12.47%
[2026-01-01T18:27:41.331Z] [INFO]   Change Time Slot: Attempts = 1739, Improvements = 123, Accepted = 1445, Success Rate = 7.07%
[2026-01-01T18:27:41.331Z] [INFO]   Change Room: Attempts = 3003, Improvements = 185, Accepted = 3003, Success Rate = 6.16%
[2026-01-01T18:27:41.331Z] [INFO]   Swap Classes: Attempts = 5042, Improvements = 38, Accepted = 228, Success Rate = 0.75%
======================================================================

✨ OPTIMIZATION COMPLETE!

Cache stats: {
  timeCache: {
    timeToMinutes: 20,
    minutesToTime: 17,
  },
  endTimeCache: 272,
  prayerOverlapCache: 272,
  totalEntries: 581,
}
📊 RESULTS:
   Final fitness: 26.57
   Hard constraint violations: 0
   Soft constraint violations: 8
   Total iterations: 20000
   Reheating events: 1
   Final temperature: 40846.8155
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
      Attempts: 7
      Improvements: 5
      Success rate: 71.43%
   Fix Room Capacity:
      Attempts: 0
      Improvements: 0
      Success rate: 0.00%
   Change Time Slot and Room:
      Attempts: 2101
      Improvements: 262
      Success rate: 12.47%
   Change Time Slot:
      Attempts: 1739
      Improvements: 123
      Success rate: 7.07%
   Change Room:
      Attempts: 3003
      Improvements: 185
      Success rate: 6.16%
   Swap Classes:
      Attempts: 5042
      Improvements: 38
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

# Second Trial Run

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
  ⚠️  Skipping GS13CZ02: No lecturers on class Kewarganegaraan
  ⚠️  Skipping GS13CZ02: No lecturers on class Kewarganegaraan
  ⚠️  Skipping GS13IP12: No lecturers on class Proyek Interdisiplin
  ⚠️  Skipping AC135343: No lecturers on class Skripsi
  ⚠️  Skipping GS13PW02: No lecturers on class Kerja Praktik
  ⚠️  Skipping VD13KP02: No lecturers on class Kerja Praktik
  ⚠️  Skipping CE11UT46: No lecturers on class Skripsi
  ⚠️  Skipping MM23RS03: No lecturers on class Research Seminar
  ⚠️  Skipping GS13IP12: No lecturers on class Proyek Interdisipliner
  ⚠️  Skipping GS13PW02: No lecturers on class KERJA PRAKTIK
  ⚠️  Skipping GS13IP12: No lecturers on class PROYEK INTERDISIPLIN
  ⚠️  Skipping GS13PW02: No lecturers on class Kerja Praktik
  ⚠️  Skipping GS13CZ02: No lecturers on class Kewarganegaraan
  ⚠️  Skipping GS13TH46: No lecturers on class Skripsi
  ⚠️  Skipping GS13PW02: No lecturers on class Kerja Praktik/Magang
  ⚠️  Skipping GS13PW02: No lecturers on class Praktik Kerja Lapang
  ⚠️  Skipping GS13IP12: No lecturers on class Proyek Interdisipliner

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
   Cooling rate: 0.9995
   Max iterations: 20000

🚀 Starting optimization...

======================================================================
[2026-01-01T18:30:57.534Z] [INFO] Simulated Annealing initialized {"hardConstraints":11,"softConstraints":8,"moveGenerators":10,"parallelEvaluation":false,"config":{"initialTemperature":100000,"minTemperature":1e-7,"coolingRate":0.9995,"maxIterations":20000}}
[2026-01-01T18:30:57.535Z] [INFO] Starting optimization...
[2026-01-01T18:30:57.535Z] [INFO] Phase 1: Eliminating hard constraint violations
[2026-01-01T18:30:57.546Z] [INFO] Initial state {"fitness":"217332.59","hardViolations":16}
[2026-01-01T18:31:01.980Z] [INFO] [Phase 1] Iteration 2000: Temp = 59652.80, Hard violations = 2, Best = 2
[2026-01-01T18:31:04.576Z] [INFO] [Phase 1] Iteration 3000: Temp = 42860.83, Hard violations = 2, Best = 2
[2026-01-01T18:31:05.901Z] [INFO] [Phase 1] Iteration 3500: Temp = 35960.26, Hard violations = 2, Best = 2
[2026-01-01T18:31:09.739Z] [INFO] [Phase 1] Iteration 5000: Temp = 22027.51, Hard violations = 2, Best = 2
[2026-01-01T18:31:13.853Z] [INFO] [Phase 1] Iteration 7000: Temp = 13048.34, Hard violations = 1, Best = 1
[2026-01-01T18:31:14.824Z] [INFO] [Phase 1] Iteration 7500: Temp = 11445.86, Hard violations = 1, Best = 1
[2026-01-01T18:31:15.877Z] [INFO] Phase 1 complete: Hard violations = 1
[2026-01-01T18:31:15.877Z] [INFO] Phase 1.5: Intensification - targeting remaining hard violations
[2026-01-01T18:31:15.877Z] [INFO] [Intensification] Attempt 1/3
[2026-01-01T18:31:17.212Z] [INFO] [Intensification] Iter 500: Hard violations = 1, Best = 1
[2026-01-01T18:31:18.780Z] [INFO] [Intensification] Iter 1000: Hard violations = 8, Best = 1
[2026-01-01T18:31:20.351Z] [INFO] [Intensification] Iter 1500: Hard violations = 8, Best = 1
[2026-01-01T18:31:21.837Z] [INFO] [Intensification] Iter 2000: Hard violations = 4, Best = 1
[2026-01-01T18:31:21.837Z] [INFO] [Intensification] Attempt 2/3
[2026-01-01T18:31:23.193Z] [INFO] [Intensification] Iter 500: Hard violations = 5, Best = 1
[2026-01-01T18:31:24.795Z] [INFO] [Intensification] Iter 1000: Hard violations = 6, Best = 1
[2026-01-01T18:31:26.410Z] [INFO] [Intensification] Iter 1500: Hard violations = 4, Best = 1
[2026-01-01T18:31:27.916Z] [INFO] [Intensification] Iter 2000: Hard violations = 3, Best = 1
[2026-01-01T18:31:27.916Z] [INFO] [Intensification] Attempt 3/3
[2026-01-01T18:31:29.136Z] [INFO] [Intensification] Iter 500: Hard violations = 1, Best = 1
[2026-01-01T18:31:30.358Z] [INFO] [Intensification] Iter 1000: Hard violations = 6, Best = 1
[2026-01-01T18:31:31.822Z] [INFO] [Intensification] Iter 1500: Hard violations = 7, Best = 1
[2026-01-01T18:31:33.391Z] [INFO] [Intensification] Iter 2000: Hard violations = 10, Best = 1
[2026-01-01T18:31:33.391Z] [WARN] [Intensification] Could not eliminate all hard violations. Remaining: 1
[2026-01-01T18:31:33.391Z] [INFO] Phase 2: Optimizing soft constraints
[2026-01-01T18:31:34.393Z] [INFO] [Phase 2] Iteration 14500: Temp = 8671.65, Current = 26.65, Best = 26.60
[2026-01-01T18:31:35.447Z] [INFO] [Phase 2] Iteration 15000: Temp = 7448.56, Current = 26.81, Best = 26.60
[2026-01-01T18:31:36.474Z] [INFO] [Phase 2] Iteration 15500: Temp = 6446.16, Current = 26.77, Best = 26.60
[2026-01-01T18:31:38.507Z] [INFO] [Phase 2] Iteration 16500: Temp = 4832.74, Current = 26.73, Best = 26.60
[2026-01-01T18:31:39.534Z] [INFO] [Phase 2] Iteration 17000: Temp = 4176.09, Current = 26.77, Best = 26.60
[2026-01-01T18:31:40.533Z] [INFO] [Phase 2] Iteration 17500: Temp = 3634.03, Current = 26.72, Best = 26.60
[2026-01-01T18:31:41.519Z] [INFO] [Phase 2] Iteration 18000: Temp = 3159.16, Current = 26.83, Best = 26.60
[2026-01-01T18:31:42.557Z] [INFO] [Phase 2] Iteration 18500: Temp = 2729.91, Current = 26.86, Best = 26.60
[2026-01-01T18:31:43.616Z] [INFO] [Phase 2] Iteration 19000: Temp = 2334.34, Current = 26.86, Best = 26.60
[2026-01-01T18:31:44.631Z] [INFO] [Phase 2] Iteration 19500: Temp = 2017.17, Current = 27.00, Best = 26.60
[2026-01-01T18:31:45.616Z] [INFO] [Phase 2] Iteration 20000: Temp = 1754.46, Current = 27.10, Best = 26.60
[2026-01-01T18:31:45.618Z] [INFO] Optimization complete {"iterations":20000,"reheats":0,"finalTemperature":"1754.4569","fitness":"26.60","hardViolations":0,"softViolations":8}
[2026-01-01T18:31:45.618Z] [INFO] Operator Statistics:
[2026-01-01T18:31:45.618Z] [INFO]   Fix Friday Prayer Conflict: Attempts = 1, Improvements = 1, Accepted = 1, Success Rate = 100.00%
[2026-01-01T18:31:45.618Z] [INFO]   Swap Friday with Non-Friday: Attempts = 2, Improvements = 0, Accepted = 0, Success Rate = 0.00%
[2026-01-01T18:31:45.618Z] [INFO]   Fix Lecturer Conflict: Attempts = 1296, Improvements = 155, Accepted = 1234, Success Rate = 11.96%
[2026-01-01T18:31:45.619Z] [INFO]   Fix Room Conflict: Attempts = 24, Improvements = 14, Accepted = 24, Success Rate = 58.33%
[2026-01-01T18:31:45.619Z] [INFO]   Fix Max Daily Periods: Attempts = 979, Improvements = 11, Accepted = 979, Success Rate = 1.12%
[2026-01-01T18:31:45.619Z] [INFO]   Fix Room Capacity: Attempts = 488, Improvements = 4, Accepted = 435, Success Rate = 0.82%
[2026-01-01T18:31:45.619Z] [INFO]   Change Time Slot and Room: Attempts = 2360, Improvements = 221, Accepted = 2254, Success Rate = 9.36%
[2026-01-01T18:31:45.619Z] [INFO]   Change Time Slot: Attempts = 2091, Improvements = 114, Accepted = 1895, Success Rate = 5.45%
[2026-01-01T18:31:45.619Z] [INFO]   Change Room: Attempts = 2877, Improvements = 163, Accepted = 2877, Success Rate = 5.67%
[2026-01-01T18:31:45.619Z] [INFO]   Swap Classes: Attempts = 3966, Improvements = 36, Accepted = 224, Success Rate = 0.91%
======================================================================

✨ OPTIMIZATION COMPLETE!

Cache stats: {
  timeCache: {
    timeToMinutes: 20,
    minutesToTime: 17,
  },
  endTimeCache: 271,
  prayerOverlapCache: 271,
  totalEntries: 579,
}
📊 RESULTS:
   Final fitness: 26.60
   Hard constraint violations: 0
   Soft constraint violations: 8
   Total iterations: 20000
   Reheating events: 0
   Final temperature: 1754.4569
   Classes scheduled: 356/373

📈 OPERATOR STATISTICS:
   Fix Friday Prayer Conflict:
      Attempts: 1
      Improvements: 1
      Success rate: 100.00%
   Swap Friday with Non-Friday:
      Attempts: 2
      Improvements: 0
      Success rate: 0.00%
   Fix Lecturer Conflict:
      Attempts: 1296
      Improvements: 155
      Success rate: 11.96%
   Fix Room Conflict:
      Attempts: 24
      Improvements: 14
      Success rate: 58.33%
   Fix Max Daily Periods:
      Attempts: 979
      Improvements: 11
      Success rate: 1.12%
   Fix Room Capacity:
      Attempts: 488
      Improvements: 4
      Success rate: 0.82%
   Change Time Slot and Room:
      Attempts: 2360
      Improvements: 221
      Success rate: 9.36%
   Change Time Slot:
      Attempts: 2091
      Improvements: 114
      Success rate: 5.45%
   Change Room:
      Attempts: 2877
      Improvements: 163
      Success rate: 5.67%
   Swap Classes:
      Attempts: 3966
      Improvements: 36
      Success rate: 0.91%

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
  ⚠️  Skipping GS13IP12: No lecturers on class Proyek Interdisiplin
  ⚠️  Skipping CE11UT46: No lecturers on class Skripsi
  ⚠️  Skipping GS13IP12: No lecturers on class Proyek Interdisipliner
  ⚠️  Skipping GS13TH46: No lecturers on class Skripsi
  ⚠️  Skipping GS13PW02: No lecturers on class Kerja Praktik
  ⚠️  Skipping GS13PW02: No lecturers on class KERJA PRAKTIK
  ⚠️  Skipping MM23RS03: No lecturers on class Research Seminar
  ⚠️  Skipping GS13PW02: No lecturers on class Praktik Kerja Lapang
  ⚠️  Skipping GS13CZ02: No lecturers on class Kewarganegaraan
  ⚠️  Skipping VD13KP02: No lecturers on class Kerja Praktik
  ⚠️  Skipping GS13IP12: No lecturers on class PROYEK INTERDISIPLIN
  ⚠️  Skipping GS13CZ02: No lecturers on class Kewarganegaraan
  ⚠️  Skipping GS13PW02: No lecturers on class Kerja Praktik/Magang
  ⚠️  Skipping GS13PW02: No lecturers on class Kerja Praktik
  ⚠️  Skipping GS13CZ02: No lecturers on class Kewarganegaraan
  ⚠️  Skipping GS13IP12: No lecturers on class Proyek Interdisipliner
  ⚠️  Skipping AC135343: No lecturers on class Skripsi

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
   Cooling rate: 0.9995
   Max iterations: 20000

🚀 Starting optimization...

======================================================================
[2026-01-01T18:31:48.282Z] [INFO] Simulated Annealing initialized {"hardConstraints":11,"softConstraints":8,"moveGenerators":10,"parallelEvaluation":false,"config":{"initialTemperature":100000,"minTemperature":1e-7,"coolingRate":0.9995,"maxIterations":20000}}
[2026-01-01T18:31:48.282Z] [INFO] Starting optimization...
[2026-01-01T18:31:48.282Z] [INFO] Phase 1: Eliminating hard constraint violations
[2026-01-01T18:31:48.293Z] [INFO] Initial state {"fitness":"223358.39","hardViolations":19}
[2026-01-01T18:31:49.591Z] [INFO] [Phase 1] Iteration 500: Temp = 85981.52, Hard violations = 7, Best = 7
[2026-01-01T18:31:51.622Z] [INFO] [Phase 1] Iteration 1500: Temp = 66958.29, Hard violations = 5, Best = 5
[2026-01-01T18:31:55.863Z] [INFO] [Phase 1] Iteration 3500: Temp = 40022.48, Hard violations = 3, Best = 3
[2026-01-01T18:31:58.983Z] [INFO] [Phase 1] Iteration 5000: Temp = 27504.44, Hard violations = 3, Best = 3
[2026-01-01T18:31:59.980Z] [INFO] [Phase 1] Iteration 5500: Temp = 24688.08, Hard violations = 3, Best = 3
[2026-01-01T18:32:01.030Z] [INFO] [Phase 1] Iteration 6000: Temp = 21841.02, Hard violations = 3, Best = 3
[2026-01-01T18:32:02.087Z] [INFO] [Phase 1] Iteration 6500: Temp = 19322.29, Hard violations = 2, Best = 2
[2026-01-01T18:32:04.399Z] [INFO] [Phase 1] Iteration 7500: Temp = 15069.86, Hard violations = 1, Best = 1
[2026-01-01T18:32:05.677Z] [INFO] [Phase 1] Iteration 8000: Temp = 12970.27, Hard violations = 1, Best = 1
[2026-01-01T18:32:07.744Z] [INFO] Phase 1 complete: Hard violations = 1
[2026-01-01T18:32:07.744Z] [INFO] Phase 1.5: Intensification - targeting remaining hard violations
[2026-01-01T18:32:07.744Z] [INFO] [Intensification] Attempt 1/3
[2026-01-01T18:32:09.375Z] [INFO] [Intensification] Iter 500: Hard violations = 5, Best = 1
[2026-01-01T18:32:11.108Z] [INFO] [Intensification] Iter 1000: Hard violations = 10, Best = 1
[2026-01-01T18:32:12.845Z] [INFO] [Intensification] Iter 1500: Hard violations = 11, Best = 1
[2026-01-01T18:32:14.548Z] [INFO] [Intensification] Iter 2000: Hard violations = 16, Best = 1
[2026-01-01T18:32:14.548Z] [INFO] [Intensification] Attempt 2/3
[2026-01-01T18:32:16.137Z] [INFO] [Intensification] Iter 500: Hard violations = 8, Best = 1
[2026-01-01T18:32:17.912Z] [INFO] [Intensification] Iter 1000: Hard violations = 8, Best = 1
[2026-01-01T18:32:19.738Z] [INFO] [Intensification] Iter 1500: Hard violations = 10, Best = 1
[2026-01-01T18:32:21.553Z] [INFO] [Intensification] Iter 2000: Hard violations = 7, Best = 1
[2026-01-01T18:32:21.553Z] [INFO] [Intensification] Attempt 3/3
[2026-01-01T18:32:23.187Z] [INFO] [Intensification] Iter 500: Hard violations = 5, Best = 1
[2026-01-01T18:32:24.949Z] [INFO] [Intensification] Iter 1000: Hard violations = 9, Best = 1
[2026-01-01T18:32:26.793Z] [INFO] [Intensification] Iter 1500: Hard violations = 13, Best = 1
[2026-01-01T18:32:28.643Z] [INFO] [Intensification] Iter 2000: Hard violations = 13, Best = 1
[2026-01-01T18:32:28.643Z] [WARN] [Intensification] Could not eliminate all hard violations. Remaining: 1
[2026-01-01T18:32:28.643Z] [INFO] Phase 2: Optimizing soft constraints
[2026-01-01T18:32:28.965Z] [INFO] [Phase 2] Iteration 15000: Temp = 9593.48, Current = 50026.77, Best = 50026.74
[2026-01-01T18:32:31.330Z] [INFO] [Phase 2] Iteration 16000: Temp = 7160.01, Current = 50026.85, Best = 50026.73
[2026-01-01T18:32:33.622Z] [INFO] [Phase 2] Iteration 17000: Temp = 5343.80, Current = 50026.81, Best = 50026.71
[2026-01-01T18:32:34.810Z] [INFO] [Phase 2] Iteration 17500: Temp = 4560.34, Current = 50026.98, Best = 50026.71
[2026-01-01T18:32:35.954Z] [INFO] [Phase 2] Iteration 18000: Temp = 3956.51, Current = 50027.00, Best = 50026.71
[2026-01-01T18:32:37.140Z] [INFO] [Phase 2] Iteration 18500: Temp = 3413.80, Current = 50026.89, Best = 50026.71
[2026-01-01T18:32:38.364Z] [INFO] [Phase 2] Iteration 19000: Temp = 2914.76, Current = 50026.98, Best = 50026.71
[2026-01-01T18:32:40.834Z] [INFO] [Phase 2] Iteration 20000: Temp = 2145.15, Current = 50027.14, Best = 50026.71
[2026-01-01T18:32:40.837Z] [INFO] Optimization complete {"iterations":20000,"reheats":0,"finalTemperature":"2145.1503","fitness":"50026.71","hardViolations":1,"softViolations":8}
[2026-01-01T18:32:40.837Z] [INFO] Operator Statistics:
[2026-01-01T18:32:40.837Z] [INFO]   Fix Friday Prayer Conflict: Attempts = 1, Improvements = 1, Accepted = 1, Success Rate = 100.00%
[2026-01-01T18:32:40.837Z] [INFO]   Swap Friday with Non-Friday: Attempts = 2, Improvements = 0, Accepted = 2, Success Rate = 0.00%
[2026-01-01T18:32:40.837Z] [INFO]   Fix Lecturer Conflict: Attempts = 817, Improvements = 8, Accepted = 810, Success Rate = 0.98%
[2026-01-01T18:32:40.837Z] [INFO]   Fix Room Conflict: Attempts = 46, Improvements = 14, Accepted = 46, Success Rate = 30.43%
[2026-01-01T18:32:40.837Z] [INFO]   Fix Max Daily Periods: Attempts = 820, Improvements = 10, Accepted = 820, Success Rate = 1.22%
[2026-01-01T18:32:40.837Z] [INFO]   Fix Room Capacity: Attempts = 637, Improvements = 2, Accepted = 637, Success Rate = 0.31%
[2026-01-01T18:32:40.837Z] [INFO]   Change Time Slot and Room: Attempts = 2308, Improvements = 214, Accepted = 2189, Success Rate = 9.27%
[2026-01-01T18:32:40.837Z] [INFO]   Change Time Slot: Attempts = 2018, Improvements = 79, Accepted = 1792, Success Rate = 3.91%
[2026-01-01T18:32:40.837Z] [INFO]   Change Room: Attempts = 2942, Improvements = 182, Accepted = 2942, Success Rate = 6.19%
[2026-01-01T18:32:40.837Z] [INFO]   Swap Classes: Attempts = 4091, Improvements = 34, Accepted = 263, Success Rate = 0.83%
======================================================================

✨ OPTIMIZATION COMPLETE!

Cache stats: {
  timeCache: {
    timeToMinutes: 19,
    minutesToTime: 16,
  },
  endTimeCache: 270,
  prayerOverlapCache: 270,
  totalEntries: 575,
}
📊 RESULTS:
   Final fitness: 50026.71
   Hard constraint violations: 1
   Soft constraint violations: 8
   Total iterations: 20000
   Reheating events: 0
   Final temperature: 2145.1503
   Classes scheduled: 356/373

📈 OPERATOR STATISTICS:
   Fix Friday Prayer Conflict:
      Attempts: 1
      Improvements: 1
      Success rate: 100.00%
   Swap Friday with Non-Friday:
      Attempts: 2
      Improvements: 0
      Success rate: 0.00%
   Fix Lecturer Conflict:
      Attempts: 817
      Improvements: 8
      Success rate: 0.98%
   Fix Room Conflict:
      Attempts: 46
      Improvements: 14
      Success rate: 30.43%
   Fix Max Daily Periods:
      Attempts: 820
      Improvements: 10
      Success rate: 1.22%
   Fix Room Capacity:
      Attempts: 637
      Improvements: 2
      Success rate: 0.31%
   Change Time Slot and Room:
      Attempts: 2308
      Improvements: 214
      Success rate: 9.27%
   Change Time Slot:
      Attempts: 2018
      Improvements: 79
      Success rate: 3.91%
   Change Room:
      Attempts: 2942
      Improvements: 182
      Success rate: 6.19%
   Swap Classes:
      Attempts: 4091
      Improvements: 34
      Success rate: 0.83%

⚠️  VIOLATIONS (9):
   - [hard] No Prodi Conflict: Prodi MANAJEMEN has overlapping classes MG12RP53 (MG-7A, Tuesday 12:30) and MG12MK53 (MG-7A, Tuesday 14:10)
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
  ⚠️  Skipping GS13PW02: No lecturers on class Kerja Praktik/Magang
  ⚠️  Skipping GS13PW02: No lecturers on class Praktik Kerja Lapang
  ⚠️  Skipping GS13IP12: No lecturers on class Proyek Interdisiplin
  ⚠️  Skipping GS13CZ02: No lecturers on class Kewarganegaraan
  ⚠️  Skipping MM23RS03: No lecturers on class Research Seminar
  ⚠️  Skipping GS13PW02: No lecturers on class KERJA PRAKTIK
  ⚠️  Skipping GS13PW02: No lecturers on class Kerja Praktik
  ⚠️  Skipping VD13KP02: No lecturers on class Kerja Praktik
  ⚠️  Skipping GS13CZ02: No lecturers on class Kewarganegaraan
  ⚠️  Skipping GS13IP12: No lecturers on class Proyek Interdisipliner
  ⚠️  Skipping GS13CZ02: No lecturers on class Kewarganegaraan
  ⚠️  Skipping GS13PW02: No lecturers on class Kerja Praktik
  ⚠️  Skipping CE11UT46: No lecturers on class Skripsi
  ⚠️  Skipping GS13TH46: No lecturers on class Skripsi
  ⚠️  Skipping GS13IP12: No lecturers on class PROYEK INTERDISIPLIN
  ⚠️  Skipping AC135343: No lecturers on class Skripsi
  ⚠️  Skipping GS13IP12: No lecturers on class Proyek Interdisipliner

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
   Cooling rate: 0.9995
   Max iterations: 20000

🚀 Starting optimization...

======================================================================
[2026-01-01T18:33:15.205Z] [INFO] Simulated Annealing initialized {"hardConstraints":11,"softConstraints":8,"moveGenerators":10,"parallelEvaluation":false,"config":{"initialTemperature":100000,"minTemperature":1e-7,"coolingRate":0.9995,"maxIterations":20000}}
[2026-01-01T18:33:15.206Z] [INFO] Starting optimization...
[2026-01-01T18:33:15.206Z] [INFO] Phase 1: Eliminating hard constraint violations
[2026-01-01T18:33:15.217Z] [INFO] Initial state {"fitness":"222332.91","hardViolations":17}
[2026-01-01T18:33:16.463Z] [INFO] [Phase 1] Iteration 500: Temp = 87194.04, Hard violations = 3, Best = 3
[2026-01-01T18:33:19.326Z] [INFO] [Phase 1] Iteration 2000: Temp = 61500.71, Hard violations = 2, Best = 2
[2026-01-01T18:33:20.392Z] [INFO] [Phase 1] Iteration 2500: Temp = 53813.01, Hard violations = 2, Best = 2
[2026-01-01T18:33:22.386Z] [INFO] [Phase 1] Iteration 3500: Temp = 41823.24, Hard violations = 2, Best = 2
[2026-01-01T18:33:24.396Z] [INFO] [Phase 1] Iteration 4500: Temp = 32197.44, Hard violations = 2, Best = 2
[2026-01-01T18:33:25.353Z] [INFO] [Phase 1] Iteration 5000: Temp = 28541.43, Hard violations = 2, Best = 2
[2026-01-01T18:33:26.307Z] [INFO] [Phase 1] Iteration 5500: Temp = 25250.00, Hard violations = 2, Best = 2
[2026-01-01T18:33:28.297Z] [INFO] [Phase 1] Iteration 6500: Temp = 19565.39, Hard violations = 1, Best = 1
[2026-01-01T18:33:30.352Z] [INFO] [Phase 1] Iteration 7500: Temp = 15032.23, Hard violations = 1, Best = 1
[2026-01-01T18:33:31.348Z] [INFO] [Phase 1] Iteration 8000: Temp = 13272.12, Hard violations = 1, Best = 1
[2026-01-01T18:33:32.330Z] [INFO] [Phase 1] Iteration 8500: Temp = 11812.24, Hard violations = 1, Best = 1
[2026-01-01T18:33:33.341Z] [INFO] [Phase 1] Iteration 9000: Temp = 10392.71, Hard violations = 1, Best = 1
[2026-01-01T18:33:33.664Z] [INFO] Phase 1 complete: Hard violations = 1
[2026-01-01T18:33:33.664Z] [INFO] Phase 1.5: Intensification - targeting remaining hard violations
[2026-01-01T18:33:33.664Z] [INFO] [Intensification] Attempt 1/3
[2026-01-01T18:33:35.190Z] [INFO] [Intensification] Iter 500: Hard violations = 6, Best = 1
[2026-01-01T18:33:36.829Z] [INFO] [Intensification] Iter 1000: Hard violations = 7, Best = 1
[2026-01-01T18:33:38.488Z] [INFO] [Intensification] Iter 1500: Hard violations = 10, Best = 1
[2026-01-01T18:33:40.140Z] [INFO] [Intensification] Iter 2000: Hard violations = 11, Best = 1
[2026-01-01T18:33:40.140Z] [INFO] [Intensification] Attempt 2/3
[2026-01-01T18:33:41.473Z] [INFO] [Intensification] Iter 500: Hard violations = 1, Best = 1
[2026-01-01T18:33:42.827Z] [INFO] [Intensification] Iter 1000: Hard violations = 1, Best = 1
[2026-01-01T18:33:44.186Z] [INFO] [Intensification] Iter 1500: Hard violations = 3, Best = 1
[2026-01-01T18:33:45.821Z] [INFO] [Intensification] Iter 2000: Hard violations = 4, Best = 1
[2026-01-01T18:33:45.821Z] [INFO] [Intensification] Attempt 3/3
[2026-01-01T18:33:47.259Z] [INFO] [Intensification] Iter 500: Hard violations = 2, Best = 1
[2026-01-01T18:33:48.712Z] [INFO] [Intensification] Iter 1000: Hard violations = 2, Best = 1
[2026-01-01T18:33:50.162Z] [INFO] [Intensification] Iter 1500: Hard violations = 2, Best = 1
[2026-01-01T18:33:51.636Z] [INFO] [Intensification] Iter 2000: Hard violations = 6, Best = 1
[2026-01-01T18:33:51.636Z] [WARN] [Intensification] Could not eliminate all hard violations. Remaining: 1
[2026-01-01T18:33:51.636Z] [INFO] Phase 2: Optimizing soft constraints
[2026-01-01T18:33:53.362Z] [INFO] [Phase 2] Iteration 16000: Temp = 8089.29, Current = 50026.90, Best = 50026.81
[2026-01-01T18:33:55.290Z] [INFO] [Phase 2] Iteration 17000: Temp = 6417.21, Current = 50027.16, Best = 50026.81
[2026-01-01T18:33:58.161Z] [INFO] [Phase 2] Iteration 18500: Temp = 4542.14, Current = 50027.16, Best = 50026.81
[2026-01-01T18:33:59.167Z] [INFO] [Phase 2] Iteration 19000: Temp = 3984.31, Current = 50027.14, Best = 50026.81
[2026-01-01T18:34:01.073Z] [INFO] Optimization complete {"iterations":20000,"reheats":0,"finalTemperature":"3140.2578","fitness":"50026.81","hardViolations":1,"softViolations":8}
[2026-01-01T18:34:01.074Z] [INFO] Operator Statistics:
[2026-01-01T18:34:01.074Z] [INFO]   Fix Friday Prayer Conflict: Attempts = 0, Improvements = 0, Accepted = 0, Success Rate = 0.00%
[2026-01-01T18:34:01.074Z] [INFO]   Swap Friday with Non-Friday: Attempts = 46, Improvements = 7, Accepted = 11, Success Rate = 15.22%
[2026-01-01T18:34:01.074Z] [INFO]   Fix Lecturer Conflict: Attempts = 656, Improvements = 3, Accepted = 656, Success Rate = 0.46%
[2026-01-01T18:34:01.074Z] [INFO]   Fix Room Conflict: Attempts = 52, Improvements = 4, Accepted = 52, Success Rate = 7.69%
[2026-01-01T18:34:01.074Z] [INFO]   Fix Max Daily Periods: Attempts = 1612, Improvements = 9, Accepted = 1612, Success Rate = 0.56%
[2026-01-01T18:34:01.074Z] [INFO]   Fix Room Capacity: Attempts = 18, Improvements = 1, Accepted = 18, Success Rate = 5.56%
[2026-01-01T18:34:01.074Z] [INFO]   Change Time Slot and Room: Attempts = 2093, Improvements = 196, Accepted = 1990, Success Rate = 9.36%
[2026-01-01T18:34:01.074Z] [INFO]   Change Time Slot: Attempts = 1936, Improvements = 75, Accepted = 1721, Success Rate = 3.87%
[2026-01-01T18:34:01.074Z] [INFO]   Change Room: Attempts = 2696, Improvements = 171, Accepted = 2696, Success Rate = 6.34%
[2026-01-01T18:34:01.074Z] [INFO]   Swap Classes: Attempts = 3811, Improvements = 27, Accepted = 193, Success Rate = 0.71%
======================================================================

✨ OPTIMIZATION COMPLETE!

Cache stats: {
  timeCache: {
    timeToMinutes: 20,
    minutesToTime: 17,
  },
  endTimeCache: 273,
  prayerOverlapCache: 273,
  totalEntries: 583,
}
📊 RESULTS:
   Final fitness: 50026.81
   Hard constraint violations: 1
   Soft constraint violations: 8
   Total iterations: 20000
   Reheating events: 0
   Final temperature: 3140.2578
   Classes scheduled: 356/373

📈 OPERATOR STATISTICS:
   Fix Friday Prayer Conflict:
      Attempts: 0
      Improvements: 0
      Success rate: 0.00%
   Swap Friday with Non-Friday:
      Attempts: 46
      Improvements: 7
      Success rate: 15.22%
   Fix Lecturer Conflict:
      Attempts: 656
      Improvements: 3
      Success rate: 0.46%
   Fix Room Conflict:
      Attempts: 52
      Improvements: 4
      Success rate: 7.69%
   Fix Max Daily Periods:
      Attempts: 1612
      Improvements: 9
      Success rate: 0.56%
   Fix Room Capacity:
      Attempts: 18
      Improvements: 1
      Success rate: 5.56%
   Change Time Slot and Room:
      Attempts: 2093
      Improvements: 196
      Success rate: 9.36%
   Change Time Slot:
      Attempts: 1936
      Improvements: 75
      Success rate: 3.87%
   Change Room:
      Attempts: 2696
      Improvements: 171
      Success rate: 6.34%
   Swap Classes:
      Attempts: 3811
      Improvements: 27
      Success rate: 0.71%

⚠️  VIOLATIONS (9):
   - [hard] Max Daily Periods: Lecturer NGT exceeds max daily periods (9) on Monday with 10 periods
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
  ⚠️  Skipping MM23RS03: No lecturers on class Research Seminar
  ⚠️  Skipping VD13KP02: No lecturers on class Kerja Praktik
  ⚠️  Skipping GS13IP12: No lecturers on class Proyek Interdisiplin
  ⚠️  Skipping GS13IP12: No lecturers on class Proyek Interdisipliner
  ⚠️  Skipping GS13IP12: No lecturers on class Proyek Interdisipliner
  ⚠️  Skipping CE11UT46: No lecturers on class Skripsi
  ⚠️  Skipping GS13PW02: No lecturers on class Kerja Praktik
  ⚠️  Skipping GS13PW02: No lecturers on class Kerja Praktik/Magang
  ⚠️  Skipping GS13PW02: No lecturers on class KERJA PRAKTIK
  ⚠️  Skipping GS13TH46: No lecturers on class Skripsi
  ⚠️  Skipping AC135343: No lecturers on class Skripsi
  ⚠️  Skipping GS13PW02: No lecturers on class Kerja Praktik
  ⚠️  Skipping GS13IP12: No lecturers on class PROYEK INTERDISIPLIN
  ⚠️  Skipping GS13CZ02: No lecturers on class Kewarganegaraan
  ⚠️  Skipping GS13CZ02: No lecturers on class Kewarganegaraan
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
   Cooling rate: 0.9995
   Max iterations: 20000

🚀 Starting optimization...

======================================================================
[2026-01-01T18:34:06.975Z] [INFO] Simulated Annealing initialized {"hardConstraints":11,"softConstraints":8,"moveGenerators":10,"parallelEvaluation":false,"config":{"initialTemperature":100000,"minTemperature":1e-7,"coolingRate":0.9995,"maxIterations":20000}}
[2026-01-01T18:34:06.976Z] [INFO] Starting optimization...
[2026-01-01T18:34:06.976Z] [INFO] Phase 1: Eliminating hard constraint violations
[2026-01-01T18:34:06.987Z] [INFO] Initial state {"fitness":"168913.88","hardViolations":12}
[2026-01-01T18:34:08.293Z] [INFO] [Phase 1] Iteration 500: Temp = 85253.60, Hard violations = 3, Best = 3
[2026-01-01T18:34:09.359Z] [INFO] [Phase 1] Iteration 1000: Temp = 74113.32, Hard violations = 3, Best = 3
[2026-01-01T18:34:12.401Z] [INFO] Phase 1 complete: Hard violations = 0
[2026-01-01T18:34:12.401Z] [INFO] Phase 2: Optimizing soft constraints
[2026-01-01T18:34:12.595Z] [INFO] [Phase 2] Iteration 2500: Temp = 46945.21, Current = 26.87, Best = 26.86
[2026-01-01T18:34:14.564Z] [INFO] [Phase 2] Iteration 3500: Temp = 35780.86, Current = 26.96, Best = 26.77
[2026-01-01T18:34:15.580Z] [INFO] [Phase 2] Iteration 4000: Temp = 31043.14, Current = 26.94, Best = 26.77
[2026-01-01T18:34:16.567Z] [INFO] [Phase 2] Iteration 4500: Temp = 27135.53, Current = 26.86, Best = 26.74
[2026-01-01T18:34:17.671Z] [INFO] [Phase 2] Iteration 5000: Temp = 23122.45, Current = 26.86, Best = 26.74
[2026-01-01T18:34:18.693Z] [INFO] [Phase 2] Iteration 5500: Temp = 20040.76, Current = 26.96, Best = 26.74
[2026-01-01T18:34:19.768Z] [INFO] [Phase 2] Iteration 6000: Temp = 17231.35, Current = 27.03, Best = 26.74
[2026-01-01T18:34:20.789Z] [INFO] [Phase 2] Iteration 6500: Temp = 14942.28, Current = 27.24, Best = 26.74
[2026-01-01T18:34:21.796Z] [INFO] [Phase 2] Iteration 7000: Temp = 13028.78, Current = 27.17, Best = 26.74
[2026-01-01T18:34:25.081Z] [INFO] [Phase 2] Iteration 8500: Temp = 8298.28, Current = 27.08, Best = 26.74
[2026-01-01T18:34:28.225Z] [INFO] [Phase 2] Iteration 10000: Temp = 5261.59, Current = 26.93, Best = 26.74
[2026-01-01T18:34:29.283Z] [INFO] [Phase 2] Iteration 10500: Temp = 4474.49, Current = 26.91, Best = 26.74
[2026-01-01T18:34:31.332Z] [INFO] [Phase 2] Iteration 11500: Temp = 3347.86, Current = 27.29, Best = 26.74
[2026-01-01T18:34:32.374Z] [INFO] [Phase 2] Iteration 12000: Temp = 2913.30, Current = 27.33, Best = 26.74
[2026-01-01T18:34:33.425Z] [INFO] [Phase 2] Iteration 12500: Temp = 2498.64, Current = 27.37, Best = 26.74
[2026-01-01T18:34:35.664Z] [INFO] [Phase 2] Iteration 13500: Temp = 1811.52, Current = 27.25, Best = 26.74
[2026-01-01T18:34:36.746Z] [INFO] [Phase 2] Iteration 14000: Temp = 1567.73, Current = 27.27, Best = 26.74
[2026-01-01T18:34:39.951Z] [INFO] [Phase 2] Reheating #1: Temperature = 149927.82, Fitness = 26.74
[2026-01-01T18:34:43.387Z] [INFO] [Phase 2] Iteration 17000: Temp = 95110.58, Current = 27.35, Best = 26.74
[2026-01-01T18:34:44.527Z] [INFO] [Phase 2] Iteration 17500: Temp = 81900.31, Current = 27.20, Best = 26.74
[2026-01-01T18:34:45.632Z] [INFO] [Phase 2] Iteration 18000: Temp = 70067.83, Current = 27.04, Best = 26.74
[2026-01-01T18:34:48.887Z] [INFO] [Phase 2] Iteration 19500: Temp = 45620.47, Current = 27.09, Best = 26.74
[2026-01-01T18:34:49.953Z] [INFO] [Phase 2] Iteration 20000: Temp = 39639.31, Current = 27.27, Best = 26.74
[2026-01-01T18:34:49.956Z] [INFO] Optimization complete {"iterations":20000,"reheats":1,"finalTemperature":"39639.3123","fitness":"26.74","hardViolations":0,"softViolations":8}
[2026-01-01T18:34:49.956Z] [INFO] Operator Statistics:
[2026-01-01T18:34:49.956Z] [INFO]   Fix Friday Prayer Conflict: Attempts = 0, Improvements = 0, Accepted = 0, Success Rate = 0.00%
[2026-01-01T18:34:49.956Z] [INFO]   Swap Friday with Non-Friday: Attempts = 0, Improvements = 0, Accepted = 0, Success Rate = 0.00%
[2026-01-01T18:34:49.956Z] [INFO]   Fix Lecturer Conflict: Attempts = 0, Improvements = 0, Accepted = 0, Success Rate = 0.00%
[2026-01-01T18:34:49.956Z] [INFO]   Fix Room Conflict: Attempts = 1, Improvements = 1, Accepted = 1, Success Rate = 100.00%
[2026-01-01T18:34:49.956Z] [INFO]   Fix Max Daily Periods: Attempts = 31, Improvements = 4, Accepted = 31, Success Rate = 12.90%
[2026-01-01T18:34:49.956Z] [INFO]   Fix Room Capacity: Attempts = 0, Improvements = 0, Accepted = 0, Success Rate = 0.00%
[2026-01-01T18:34:49.956Z] [INFO]   Change Time Slot and Room: Attempts = 2218, Improvements = 243, Accepted = 2036, Success Rate = 10.96%
[2026-01-01T18:34:49.956Z] [INFO]   Change Time Slot: Attempts = 1688, Improvements = 126, Accepted = 1437, Success Rate = 7.46%
[2026-01-01T18:34:49.956Z] [INFO]   Change Room: Attempts = 3164, Improvements = 214, Accepted = 3164, Success Rate = 6.76%
[2026-01-01T18:34:49.956Z] [INFO]   Swap Classes: Attempts = 4767, Improvements = 28, Accepted = 189, Success Rate = 0.59%
======================================================================

✨ OPTIMIZATION COMPLETE!

Cache stats: {
  timeCache: {
    timeToMinutes: 20,
    minutesToTime: 17,
  },
  endTimeCache: 268,
  prayerOverlapCache: 268,
  totalEntries: 573,
}
📊 RESULTS:
   Final fitness: 26.74
   Hard constraint violations: 0
   Soft constraint violations: 8
   Total iterations: 20000
   Reheating events: 1
   Final temperature: 39639.3123
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
      Attempts: 31
      Improvements: 4
      Success rate: 12.90%
   Fix Room Capacity:
      Attempts: 0
      Improvements: 0
      Success rate: 0.00%
   Change Time Slot and Room:
      Attempts: 2218
      Improvements: 243
      Success rate: 10.96%
   Change Time Slot:
      Attempts: 1688
      Improvements: 126
      Success rate: 7.46%
   Change Room:
      Attempts: 3164
      Improvements: 214
      Success rate: 6.76%
   Swap Classes:
      Attempts: 4767
      Improvements: 28
      Success rate: 0.59%

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
  ⚠️  Skipping GS13IP12: No lecturers on class PROYEK INTERDISIPLIN
  ⚠️  Skipping GS13PW02: No lecturers on class Praktik Kerja Lapang
  ⚠️  Skipping GS13IP12: No lecturers on class Proyek Interdisipliner
  ⚠️  Skipping GS13IP12: No lecturers on class Proyek Interdisipliner
  ⚠️  Skipping GS13PW02: No lecturers on class Kerja Praktik
  ⚠️  Skipping GS13CZ02: No lecturers on class Kewarganegaraan
  ⚠️  Skipping GS13CZ02: No lecturers on class Kewarganegaraan
  ⚠️  Skipping VD13KP02: No lecturers on class Kerja Praktik
  ⚠️  Skipping AC135343: No lecturers on class Skripsi
  ⚠️  Skipping CE11UT46: No lecturers on class Skripsi
  ⚠️  Skipping GS13CZ02: No lecturers on class Kewarganegaraan
  ⚠️  Skipping GS13TH46: No lecturers on class Skripsi
  ⚠️  Skipping GS13PW02: No lecturers on class Kerja Praktik
  ⚠️  Skipping MM23RS03: No lecturers on class Research Seminar
  ⚠️  Skipping GS13PW02: No lecturers on class KERJA PRAKTIK
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
   Cooling rate: 0.9995
   Max iterations: 20000

🚀 Starting optimization...

======================================================================
[2026-01-01T18:34:57.481Z] [INFO] Simulated Annealing initialized {"hardConstraints":11,"softConstraints":8,"moveGenerators":10,"parallelEvaluation":false,"config":{"initialTemperature":100000,"minTemperature":1e-7,"coolingRate":0.9995,"maxIterations":20000}}
[2026-01-01T18:34:57.482Z] [INFO] Starting optimization...
[2026-01-01T18:34:57.482Z] [INFO] Phase 1: Eliminating hard constraint violations
[2026-01-01T18:34:57.493Z] [INFO] Initial state {"fitness":"177406.32","hardViolations":17}
[2026-01-01T18:34:58.860Z] [INFO] [Phase 1] Iteration 500: Temp = 85681.04, Hard violations = 4, Best = 4
[2026-01-01T18:34:59.795Z] [INFO] [Phase 1] Iteration 1000: Temp = 76294.63, Hard violations = 4, Best = 4
[2026-01-01T18:35:00.740Z] [INFO] [Phase 1] Iteration 1500: Temp = 68004.49, Hard violations = 3, Best = 3
[2026-01-01T18:35:01.635Z] [INFO] [Phase 1] Iteration 2000: Temp = 61500.71, Hard violations = 3, Best = 3
[2026-01-01T18:35:02.627Z] [INFO] [Phase 1] Iteration 2500: Temp = 54299.64, Hard violations = 2, Best = 2
[2026-01-01T18:35:04.590Z] [INFO] [Phase 1] Iteration 3500: Temp = 42561.78, Hard violations = 2, Best = 2
[2026-01-01T18:35:06.551Z] [INFO] Phase 1 complete: Hard violations = 0
[2026-01-01T18:35:06.551Z] [INFO] Phase 2: Optimizing soft constraints
[2026-01-01T18:35:09.902Z] [INFO] [Phase 2] Iteration 6000: Temp = 20952.95, Current = 27.11, Best = 26.78
[2026-01-01T18:35:11.026Z] [INFO] [Phase 2] Iteration 6500: Temp = 17863.14, Current = 27.07, Best = 26.78
[2026-01-01T18:35:12.130Z] [INFO] [Phase 2] Iteration 7000: Temp = 15297.67, Current = 27.19, Best = 26.78
[2026-01-01T18:35:14.273Z] [INFO] [Phase 2] Iteration 8000: Temp = 11400.16, Current = 27.13, Best = 26.78
[2026-01-01T18:35:18.465Z] [INFO] [Phase 2] Iteration 10000: Temp = 6439.72, Current = 27.33, Best = 26.78
[2026-01-01T18:35:19.691Z] [INFO] [Phase 2] Iteration 10500: Temp = 5470.90, Current = 27.36, Best = 26.78
[2026-01-01T18:35:21.900Z] [INFO] [Phase 2] Iteration 11500: Temp = 4046.56, Current = 27.44, Best = 26.78
[2026-01-01T18:35:25.214Z] [INFO] [Phase 2] Iteration 13000: Temp = 2634.68, Current = 27.65, Best = 26.78
[2026-01-01T18:35:26.291Z] [INFO] [Phase 2] Iteration 13500: Temp = 2288.11, Current = 27.66, Best = 26.78
[2026-01-01T18:35:27.333Z] [INFO] [Phase 2] Iteration 14000: Temp = 1984.15, Current = 27.74, Best = 26.78
[2026-01-01T18:35:29.512Z] [INFO] [Phase 2] Iteration 15000: Temp = 1488.28, Current = 27.46, Best = 26.78
[2026-01-01T18:35:30.606Z] [INFO] [Phase 2] Iteration 15500: Temp = 1282.85, Current = 27.27, Best = 26.78
[2026-01-01T18:35:31.728Z] [INFO] [Phase 2] Iteration 16000: Temp = 1089.31, Current = 27.39, Best = 26.78
[2026-01-01T18:35:32.340Z] [INFO] [Phase 2] Reheating #1: Temperature = 149927.82, Fitness = 26.78
[2026-01-01T18:35:32.786Z] [INFO] [Phase 2] Iteration 16500: Temp = 140982.90, Current = 27.23, Best = 26.78
[2026-01-01T18:35:33.824Z] [INFO] [Phase 2] Iteration 17000: Temp = 121948.93, Current = 27.35, Best = 26.78
[2026-01-01T18:35:34.921Z] [INFO] [Phase 2] Iteration 17500: Temp = 104226.15, Current = 27.36, Best = 26.78
[2026-01-01T18:35:37.076Z] [INFO] [Phase 2] Iteration 18500: Temp = 77477.60, Current = 27.41, Best = 26.78
[2026-01-01T18:35:38.266Z] [INFO] [Phase 2] Iteration 19000: Temp = 65199.11, Current = 27.66, Best = 26.78
[2026-01-01T18:35:39.415Z] [INFO] [Phase 2] Iteration 19500: Temp = 55418.04, Current = 27.62, Best = 26.78
[2026-01-01T18:35:40.540Z] [INFO] [Phase 2] Iteration 20000: Temp = 47057.22, Current = 27.52, Best = 26.78
[2026-01-01T18:35:40.542Z] [INFO] Optimization complete {"iterations":20000,"reheats":1,"finalTemperature":"47057.2173","fitness":"26.78","hardViolations":0,"softViolations":8}
[2026-01-01T18:35:40.542Z] [INFO] Operator Statistics:
[2026-01-01T18:35:40.542Z] [INFO]   Fix Friday Prayer Conflict: Attempts = 0, Improvements = 0, Accepted = 0, Success Rate = 0.00%
[2026-01-01T18:35:40.542Z] [INFO]   Swap Friday with Non-Friday: Attempts = 0, Improvements = 0, Accepted = 0, Success Rate = 0.00%
[2026-01-01T18:35:40.542Z] [INFO]   Fix Lecturer Conflict: Attempts = 0, Improvements = 0, Accepted = 0, Success Rate = 0.00%
[2026-01-01T18:35:40.542Z] [INFO]   Fix Room Conflict: Attempts = 102, Improvements = 1, Accepted = 102, Success Rate = 0.98%
[2026-01-01T18:35:40.542Z] [INFO]   Fix Max Daily Periods: Attempts = 86, Improvements = 9, Accepted = 85, Success Rate = 10.47%
[2026-01-01T18:35:40.542Z] [INFO]   Fix Room Capacity: Attempts = 0, Improvements = 0, Accepted = 0, Success Rate = 0.00%
[2026-01-01T18:35:40.542Z] [INFO]   Change Time Slot and Room: Attempts = 2051, Improvements = 275, Accepted = 1886, Success Rate = 13.41%
[2026-01-01T18:35:40.542Z] [INFO]   Change Time Slot: Attempts = 1615, Improvements = 105, Accepted = 1347, Success Rate = 6.50%
[2026-01-01T18:35:40.542Z] [INFO]   Change Room: Attempts = 2865, Improvements = 191, Accepted = 2865, Success Rate = 6.67%
[2026-01-01T18:35:40.542Z] [INFO]   Swap Classes: Attempts = 4807, Improvements = 37, Accepted = 213, Success Rate = 0.77%
======================================================================

✨ OPTIMIZATION COMPLETE!

Cache stats: {
  timeCache: {
    timeToMinutes: 20,
    minutesToTime: 17,
  },
  endTimeCache: 275,
  prayerOverlapCache: 275,
  totalEntries: 587,
}
📊 RESULTS:
   Final fitness: 26.78
   Hard constraint violations: 0
   Soft constraint violations: 8
   Total iterations: 20000
   Reheating events: 1
   Final temperature: 47057.2173
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
      Attempts: 102
      Improvements: 1
      Success rate: 0.98%
   Fix Max Daily Periods:
      Attempts: 86
      Improvements: 9
      Success rate: 10.47%
   Fix Room Capacity:
      Attempts: 0
      Improvements: 0
      Success rate: 0.00%
   Change Time Slot and Room:
      Attempts: 2051
      Improvements: 275
      Success rate: 13.41%
   Change Time Slot:
      Attempts: 1615
      Improvements: 105
      Success rate: 6.50%
   Change Room:
      Attempts: 2865
      Improvements: 191
      Success rate: 6.67%
   Swap Classes:
      Attempts: 4807
      Improvements: 37
      Success rate: 0.77%

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