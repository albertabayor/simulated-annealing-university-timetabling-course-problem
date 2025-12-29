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
  ⚠️  Skipping MM23RS03: No lecturers on class Research Seminar
  ⚠️  Skipping GS13PW02: No lecturers on class Kerja Praktik
  ⚠️  Skipping AC135343: No lecturers on class Skripsi
  ⚠️  Skipping GS13PW02: No lecturers on class Kerja Praktik
  ⚠️  Skipping GS13TH46: No lecturers on class Skripsi
  ⚠️  Skipping GS13IP12: No lecturers on class Proyek Interdisipliner
  ⚠️  Skipping GS13PW02: No lecturers on class KERJA PRAKTIK
  ⚠️  Skipping GS13IP12: No lecturers on class PROYEK INTERDISIPLIN
  ⚠️  Skipping GS13CZ02: No lecturers on class Kewarganegaraan
  ⚠️  Skipping GS13IP12: No lecturers on class Proyek Interdisiplin
  ⚠️  Skipping CE11UT46: No lecturers on class Skripsi
  ⚠️  Skipping GS13PW02: No lecturers on class Praktik Kerja Lapang
  ⚠️  Skipping GS13CZ02: No lecturers on class Kewarganegaraan
  ⚠️  Could not place IF13RP12: Rekayasa Perangkat Lunak
  ⚠️  Skipping GS13PW02: No lecturers on class Kerja Praktik/Magang
  ⚠️  Skipping GS13CZ02: No lecturers on class Kewarganegaraan
  ⚠️  Skipping GS13IP12: No lecturers on class Proyek Interdisipliner
  ⚠️  Skipping VD13KP02: No lecturers on class Kerja Praktik
  ⚠️  Could not place VD13BS53: Perencanaan Bisnis

✅ Initial solution generated:
   Successfully placed: 354/373
   Failed to place: 19/373


⚖️  Setting up constraints...
   Hard constraints: 11
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
[2025-12-29T16:11:57.564Z] [INFO] Simulated Annealing initialized {"hardConstraints":11,"softConstraints":8,"moveGenerators":10,"config":{"initialTemperature":100000,"minTemperature":1e-7,"coolingRate":0.9998,"maxIterations":60000}}
[2025-12-29T16:11:57.565Z] [INFO] Starting optimization...
[2025-12-29T16:11:57.565Z] [INFO] Phase 1: Eliminating hard constraint violations
[2025-12-29T16:11:57.600Z] [INFO] Initial state {"fitness":"341935.71","hardViolations":29}
[2025-12-29T16:12:05.569Z] [INFO] [Phase 1] Iteration 500: Temp = 94572.30, Hard violations = 12, Best = 12
[2025-12-29T16:12:24.694Z] [INFO] [Phase 1] Iteration 2000: Temp = 83944.23, Hard violations = 10, Best = 10
[2025-12-29T16:12:31.083Z] [INFO] [Phase 1] Iteration 2500: Temp = 80410.79, Hard violations = 10, Best = 10
[2025-12-29T16:12:36.875Z] [INFO] [Phase 1] Iteration 3000: Temp = 77582.73, Hard violations = 10, Best = 10
[2025-12-29T16:12:43.036Z] [INFO] [Phase 1] Iteration 3500: Temp = 74974.00, Hard violations = 9, Best = 9
[2025-12-29T16:12:49.877Z] [INFO] [Phase 1] Iteration 4000: Temp = 71660.30, Hard violations = 9, Best = 9
[2025-12-29T16:13:07.032Z] [INFO] [Phase 1] Iteration 5500: Temp = 63989.92, Hard violations = 8, Best = 8
[2025-12-29T16:13:27.740Z] [INFO] [Phase 1] Iteration 7000: Temp = 56436.32, Hard violations = 7, Best = 7
[2025-12-29T16:13:39.412Z] [INFO] [Phase 1] Iteration 8000: Temp = 52222.07, Hard violations = 7, Best = 7
[2025-12-29T16:15:04.023Z] [INFO] [Phase 1] Iteration 15000: Temp = 31213.60, Hard violations = 4, Best = 4
[2025-12-29T16:15:09.075Z] [INFO] [Phase 1] Iteration 15500: Temp = 30218.38, Hard violations = 4, Best = 4
[2025-12-29T16:15:25.014Z] [INFO] [Phase 1] Iteration 17000: Temp = 27304.20, Hard violations = 4, Best = 4
[2025-12-29T16:16:22.959Z] [INFO] [Phase 1] Iteration 21500: Temp = 19344.46, Hard violations = 2, Best = 2
[2025-12-29T16:16:29.190Z] [INFO] [Phase 1] Iteration 22000: Temp = 18548.74, Hard violations = 2, Best = 2
[2025-12-29T16:16:48.489Z] [INFO] [Phase 1] Iteration 23500: Temp = 16228.81, Hard violations = 2, Best = 2
[2025-12-29T16:16:56.412Z] [INFO] [Phase 1] Iteration 24000: Temp = 15443.43, Hard violations = 2, Best = 2
[2025-12-29T16:17:15.927Z] [INFO] [Phase 1] Iteration 25500: Temp = 13509.19, Hard violations = 2, Best = 2
[2025-12-29T16:17:22.377Z] [INFO] [Phase 1] Iteration 26000: Temp = 12950.91, Hard violations = 2, Best = 2
[2025-12-29T16:17:30.129Z] [INFO] [Phase 1] Iteration 26500: Temp = 12380.98, Hard violations = 1, Best = 1
[2025-12-29T16:17:51.476Z] [INFO] [Phase 1] Iteration 28000: Temp = 10664.78, Hard violations = 1, Best = 1
[2025-12-29T16:18:01.736Z] [INFO] Phase 1 complete: Hard violations = 1
[2025-12-29T16:18:01.736Z] [INFO] Phase 1.5: Intensification - targeting remaining hard violations
[2025-12-29T16:18:01.736Z] [INFO] [Intensification] Attempt 1/3
[2025-12-29T16:18:14.034Z] [INFO] [Intensification] Iter 500: Hard violations = 1, Best = 1
[2025-12-29T16:18:26.237Z] [INFO] [Intensification] Iter 1000: Hard violations = 1, Best = 1
[2025-12-29T16:18:38.388Z] [INFO] [Intensification] Iter 1500: Hard violations = 1, Best = 1
[2025-12-29T16:18:50.767Z] [INFO] [Intensification] Iter 2000: Hard violations = 1, Best = 1
[2025-12-29T16:18:50.767Z] [INFO] [Intensification] Attempt 2/3
[2025-12-29T16:19:03.698Z] [INFO] [Intensification] Iter 500: Hard violations = 1, Best = 1
[2025-12-29T16:19:16.065Z] [INFO] [Intensification] Iter 1000: Hard violations = 1, Best = 1
[2025-12-29T16:19:28.655Z] [INFO] [Intensification] Iter 1500: Hard violations = 1, Best = 1
[2025-12-29T16:19:41.270Z] [INFO] [Intensification] Iter 2000: Hard violations = 1, Best = 1
[2025-12-29T16:19:41.270Z] [INFO] [Intensification] Attempt 3/3
[2025-12-29T16:19:54.552Z] [INFO] [Intensification] Iter 500: Hard violations = 1, Best = 1
[2025-12-29T16:20:07.178Z] [INFO] [Intensification] Iter 1000: Hard violations = 1, Best = 1
[2025-12-29T16:20:19.336Z] [INFO] [Intensification] Iter 1500: Hard violations = 1, Best = 1
[2025-12-29T16:20:31.288Z] [INFO] [Intensification] Iter 2000: Hard violations = 1, Best = 1
[2025-12-29T16:20:31.288Z] [WARN] [Intensification] Could not eliminate all hard violations. Remaining: 1
[2025-12-29T16:20:31.288Z] [INFO] Phase 2: Optimizing soft constraints
[2025-12-29T16:20:45.495Z] [INFO] [Phase 2] Iteration 35500: Temp = 9071.43, Current = 26.92, Best = 26.91
[2025-12-29T16:20:52.846Z] [INFO] [Phase 2] Iteration 36000: Temp = 8582.49, Current = 27.01, Best = 26.91
[2025-12-29T16:21:08.120Z] [INFO] [Phase 2] Iteration 37000: Temp = 7660.78, Current = 27.27, Best = 26.91
[2025-12-29T16:21:24.768Z] [INFO] [Phase 2] Iteration 38000: Temp = 6814.83, Current = 27.38, Best = 26.91
[2025-12-29T16:21:32.468Z] [INFO] [Phase 2] Iteration 38500: Temp = 6435.93, Current = 27.40, Best = 26.91
[2025-12-29T16:21:40.121Z] [INFO] [Phase 2] Iteration 39000: Temp = 6081.74, Current = 27.28, Best = 26.91
[2025-12-29T16:22:04.572Z] [INFO] [Phase 2] Iteration 40500: Temp = 5051.43, Current = 27.25, Best = 26.91
[2025-12-29T16:22:21.860Z] [INFO] [Phase 2] Iteration 41500: Temp = 4466.74, Current = 27.32, Best = 26.91
[2025-12-29T16:22:30.065Z] [INFO] [Phase 2] Iteration 42000: Temp = 4203.23, Current = 27.31, Best = 26.91
[2025-12-29T16:22:38.459Z] [INFO] [Phase 2] Iteration 42500: Temp = 3946.57, Current = 27.31, Best = 26.91
[2025-12-29T16:22:46.324Z] [INFO] [Phase 2] Iteration 43000: Temp = 3713.75, Current = 27.27, Best = 26.91
[2025-12-29T16:23:02.811Z] [INFO] [Phase 2] Iteration 44000: Temp = 3283.23, Current = 27.35, Best = 26.91
[2025-12-29T16:23:19.540Z] [INFO] [Phase 2] Iteration 45000: Temp = 2920.10, Current = 27.32, Best = 26.91
[2025-12-29T16:23:43.490Z] [INFO] [Phase 2] Iteration 46500: Temp = 2437.56, Current = 27.34, Best = 26.91
[2025-12-29T16:23:51.591Z] [INFO] [Phase 2] Iteration 47000: Temp = 2296.06, Current = 27.41, Best = 26.91
[2025-12-29T16:24:00.023Z] [INFO] [Phase 2] Iteration 47500: Temp = 2159.74, Current = 27.18, Best = 26.91
[2025-12-29T16:24:08.172Z] [INFO] [Phase 2] Iteration 48000: Temp = 2034.36, Current = 27.16, Best = 26.91
[2025-12-29T16:24:16.571Z] [INFO] [Phase 2] Iteration 48500: Temp = 1909.75, Current = 27.24, Best = 26.91
[2025-12-29T16:24:24.604Z] [INFO] [Phase 2] Iteration 49000: Temp = 1799.61, Current = 27.25, Best = 26.91
[2025-12-29T16:24:48.252Z] [INFO] [Phase 2] Iteration 50500: Temp = 1513.39, Current = 27.28, Best = 26.91
[2025-12-29T16:24:56.533Z] [INFO] [Phase 2] Iteration 51000: Temp = 1421.55, Current = 27.23, Best = 26.91
[2025-12-29T16:25:13.584Z] [INFO] [Phase 2] Iteration 52000: Temp = 1259.27, Current = 27.02, Best = 26.91
[2025-12-29T16:25:21.403Z] [INFO] [Phase 2] Iteration 52500: Temp = 1189.97, Current = 27.08, Best = 26.91
[2025-12-29T16:25:30.091Z] [INFO] [Phase 2] Iteration 53000: Temp = 1115.07, Current = 27.27, Best = 26.91
[2025-12-29T16:25:37.620Z] [INFO] [Phase 2] Iteration 53500: Temp = 1053.08, Current = 27.39, Best = 26.91
[2025-12-29T16:25:44.301Z] [INFO] [Phase 2] Reheating #1: Temperature = 149986.45, Fitness = 26.91
[2025-12-29T16:25:45.144Z] [INFO] [Phase 2] Iteration 54000: Temp = 148969.90, Current = 27.26, Best = 26.91
[2025-12-29T16:25:53.629Z] [INFO] [Phase 2] Iteration 54500: Temp = 140209.57, Current = 27.25, Best = 26.91
[2025-12-29T16:26:01.468Z] [INFO] [Phase 2] Iteration 55000: Temp = 132572.89, Current = 27.41, Best = 26.91
[2025-12-29T16:26:19.209Z] [INFO] [Phase 2] Iteration 56000: Temp = 116830.01, Current = 27.50, Best = 26.91
[2025-12-29T16:26:35.294Z] [INFO] [Phase 2] Iteration 57000: Temp = 102977.17, Current = 27.49, Best = 26.91
[2025-12-29T16:26:44.627Z] [INFO] [Phase 2] Iteration 57500: Temp = 96843.98, Current = 27.48, Best = 26.91
[2025-12-29T16:26:53.109Z] [INFO] [Phase 2] Iteration 58000: Temp = 90857.72, Current = 27.54, Best = 26.91
[2025-12-29T16:27:25.574Z] [INFO] Optimization complete {"iterations":60000,"reheats":1,"finalTemperature":"71555.3252","fitness":"26.91","hardViolations":0,"softViolations":8}
[2025-12-29T16:27:25.574Z] [INFO] Operator Statistics:
[2025-12-29T16:27:25.574Z] [INFO]   Fix Friday Prayer Conflict: Attempts = 769, Improvements = 34, Accepted = 726, Success Rate = 4.42%
[2025-12-29T16:27:25.574Z] [INFO]   Swap Friday with Non-Friday: Attempts = 850, Improvements = 1, Accepted = 544, Success Rate = 0.12%
[2025-12-29T16:27:25.574Z] [INFO]   Fix Lecturer Conflict: Attempts = 29, Improvements = 1, Accepted = 29, Success Rate = 3.45%
[2025-12-29T16:27:25.574Z] [INFO]   Fix Room Conflict: Attempts = 3190, Improvements = 2, Accepted = 3190, Success Rate = 0.06%
[2025-12-29T16:27:25.574Z] [INFO]   Fix Max Daily Periods: Attempts = 349, Improvements = 7, Accepted = 349, Success Rate = 2.01%
[2025-12-29T16:27:25.574Z] [INFO]   Fix Room Capacity: Attempts = 0, Improvements = 0, Accepted = 0, Success Rate = 0.00%
[2025-12-29T16:27:25.574Z] [INFO]   Change Time Slot and Room: Attempts = 4060, Improvements = 520, Accepted = 3696, Success Rate = 12.81%
[2025-12-29T16:27:25.574Z] [INFO]   Change Time Slot: Attempts = 3252, Improvements = 259, Accepted = 2595, Success Rate = 7.96%
[2025-12-29T16:27:25.574Z] [INFO]   Change Room: Attempts = 6699, Improvements = 507, Accepted = 6699, Success Rate = 7.57%
[2025-12-29T16:27:25.574Z] [INFO]   Swap Classes: Attempts = 13526, Improvements = 127, Accepted = 788, Success Rate = 0.94%
======================================================================

✨ OPTIMIZATION COMPLETE!

Cache stats: {
  timeCache: {
    timeToMinutes: 20,
    minutesToTime: 17,
  },
  endTimeCache: 281,
  prayerOverlapCache: 281,
  totalEntries: 599,
}
📊 RESULTS:
   Final fitness: 26.91
   Hard constraint violations: 0
   Soft constraint violations: 8
   Total iterations: 60000
   Reheating events: 1
   Final temperature: 71555.3252
   Classes scheduled: 354/373

📈 OPERATOR STATISTICS:
   Fix Friday Prayer Conflict:
      Attempts: 769
      Improvements: 34
      Success rate: 4.42%
   Swap Friday with Non-Friday:
      Attempts: 850
      Improvements: 1
      Success rate: 0.12%
   Fix Lecturer Conflict:
      Attempts: 29
      Improvements: 1
      Success rate: 3.45%
   Fix Room Conflict:
      Attempts: 3190
      Improvements: 2
      Success rate: 0.06%
   Fix Max Daily Periods:
      Attempts: 349
      Improvements: 7
      Success rate: 2.01%
   Fix Room Capacity:
      Attempts: 0
      Improvements: 0
      Success rate: 0.00%
   Change Time Slot and Room:
      Attempts: 4060
      Improvements: 520
      Success rate: 12.81%
   Change Time Slot:
      Attempts: 3252
      Improvements: 259
      Success rate: 7.96%
   Change Room:
      Attempts: 6699
      Improvements: 507
      Success rate: 7.57%
   Swap Classes:
      Attempts: 13526
      Improvements: 127
      Success rate: 0.94%

⚠️  VIOLATIONS (8):
   - [soft] Preferred Time: No description
   - [soft] Preferred Room: No description
   - [soft] Transit Time: No description
   - [soft] Compactness: No description
   - [soft] Prayer Time Overlap: No description
   - [soft] Evening Class Priority: No description
   - [soft] Research Day: No description
   - [soft] Overflow Penalty: No description

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
  ⚠️  Skipping MM23RS03: No lecturers on class Research Seminar
  ⚠️  Skipping GS13PW02: No lecturers on class Kerja Praktik
  ⚠️  Skipping AC135343: No lecturers on class Skripsi
  ⚠️  Skipping GS13PW02: No lecturers on class Kerja Praktik
  ⚠️  Skipping GS13TH46: No lecturers on class Skripsi
  ⚠️  Skipping GS13IP12: No lecturers on class Proyek Interdisipliner
  ⚠️  Skipping GS13PW02: No lecturers on class KERJA PRAKTIK
  ⚠️  Skipping GS13IP12: No lecturers on class PROYEK INTERDISIPLIN
  ⚠️  Skipping GS13CZ02: No lecturers on class Kewarganegaraan
  ⚠️  Skipping GS13IP12: No lecturers on class Proyek Interdisiplin
  ⚠️  Skipping CE11UT46: No lecturers on class Skripsi
  ⚠️  Skipping GS13PW02: No lecturers on class Praktik Kerja Lapang
  ⚠️  Skipping GS13CZ02: No lecturers on class Kewarganegaraan
  ⚠️  Could not place IF13RP12: Rekayasa Perangkat Lunak
  ⚠️  Skipping GS13PW02: No lecturers on class Kerja Praktik/Magang
  ⚠️  Skipping GS13CZ02: No lecturers on class Kewarganegaraan
  ⚠️  Skipping GS13IP12: No lecturers on class Proyek Interdisipliner
  ⚠️  Skipping VD13KP02: No lecturers on class Kerja Praktik
  ⚠️  Could not place VD13BS53: Perencanaan Bisnis

✅ Initial solution generated:
   Successfully placed: 354/373
   Failed to place: 19/373


⚖️  Setting up constraints...
   Hard constraints: 11
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
[2025-12-29T17:23:35.507Z] [INFO] Simulated Annealing initialized {"hardConstraints":11,"softConstraints":8,"moveGenerators":10,"config":{"initialTemperature":100000,"minTemperature":1e-7,"coolingRate":0.9998,"maxIterations":60000}}
[2025-12-29T17:23:35.507Z] [INFO] Starting optimization...
[2025-12-29T17:23:35.507Z] [INFO] Phase 1: Eliminating hard constraint violations
[2025-12-29T17:23:35.545Z] [INFO] Initial state {"fitness":"341935.71","hardViolations":29}
[2025-12-29T17:23:48.518Z] [INFO] [Phase 1] Iteration 1000: Temp = 91575.28, Hard violations = 10, Best = 10
[2025-12-29T17:24:00.273Z] [INFO] [Phase 1] Iteration 2000: Temp = 84601.62, Hard violations = 8, Best = 8
[2025-12-29T17:24:05.713Z] [INFO] [Phase 1] Iteration 2500: Temp = 81675.16, Hard violations = 8, Best = 8
[2025-12-29T17:24:36.177Z] [INFO] [Phase 1] Iteration 5000: Temp = 67324.93, Hard violations = 6, Best = 6
[2025-12-29T17:24:44.431Z] [INFO] [Phase 1] Iteration 5500: Temp = 63951.53, Hard violations = 6, Best = 6
[2025-12-29T17:24:50.750Z] [INFO] [Phase 1] Iteration 6000: Temp = 61210.64, Hard violations = 6, Best = 6
[2025-12-29T17:24:57.260Z] [INFO] [Phase 1] Iteration 6500: Temp = 58423.40, Hard violations = 6, Best = 6
[2025-12-29T17:25:03.550Z] [INFO] [Phase 1] Iteration 7000: Temp = 55908.25, Hard violations = 6, Best = 6
[2025-12-29T17:25:10.157Z] [INFO] [Phase 1] Iteration 7500: Temp = 53426.53, Hard violations = 6, Best = 6
[2025-12-29T17:25:18.013Z] [INFO] [Phase 1] Iteration 8000: Temp = 50983.54, Hard violations = 6, Best = 6
[2025-12-29T17:25:47.033Z] [INFO] [Phase 1] Iteration 10000: Temp = 41724.26, Hard violations = 6, Best = 6
[2025-12-29T17:25:55.828Z] [INFO] [Phase 1] Iteration 10500: Temp = 39522.79, Hard violations = 6, Best = 6
[2025-12-29T17:26:03.759Z] [INFO] [Phase 1] Iteration 11000: Temp = 37355.18, Hard violations = 6, Best = 6
[2025-12-29T17:26:09.933Z] [INFO] [Phase 1] Iteration 11500: Temp = 35789.96, Hard violations = 6, Best = 6
[2025-12-29T17:26:30.269Z] [INFO] [Phase 1] Iteration 13000: Temp = 31101.42, Hard violations = 6, Best = 6
[2025-12-29T17:26:37.809Z] [INFO] [Phase 1] Iteration 13500: Temp = 29756.54, Hard violations = 5, Best = 5
[2025-12-29T17:26:50.797Z] [INFO] [Phase 1] Iteration 14500: Temp = 27178.87, Hard violations = 5, Best = 5
[2025-12-29T17:27:13.850Z] [INFO] [Phase 1] Iteration 16000: Temp = 23500.59, Hard violations = 5, Best = 5
[2025-12-29T17:27:20.678Z] [INFO] [Phase 1] Iteration 16500: Temp = 22475.39, Hard violations = 5, Best = 5
[2025-12-29T17:27:40.868Z] [INFO] [Phase 1] Iteration 18000: Temp = 19695.85, Hard violations = 5, Best = 5
[2025-12-29T17:27:47.855Z] [INFO] [Phase 1] Iteration 18500: Temp = 18829.09, Hard violations = 5, Best = 5
[2025-12-29T17:28:02.250Z] [INFO] [Phase 1] Iteration 19500: Temp = 17287.69, Hard violations = 5, Best = 5
[2025-12-29T17:28:42.933Z] [INFO] [Phase 1] Iteration 22500: Temp = 13385.46, Hard violations = 4, Best = 4
[2025-12-29T17:28:50.427Z] [INFO] [Phase 1] Iteration 23000: Temp = 12737.67, Hard violations = 4, Best = 4
[2025-12-29T17:29:24.146Z] [INFO] [Phase 1] Iteration 25500: Temp = 10271.19, Hard violations = 3, Best = 3
[2025-12-29T17:29:27.667Z] [INFO] Phase 1 complete: Hard violations = 1
[2025-12-29T17:29:27.667Z] [INFO] Phase 1.5: Intensification - targeting remaining hard violations
[2025-12-29T17:29:27.667Z] [INFO] [Intensification] Attempt 1/3
[2025-12-29T17:29:41.365Z] [INFO] [Intensification] Iter 500: Hard violations = 1, Best = 1
[2025-12-29T17:29:54.012Z] [INFO] [Intensification] Iter 1000: Hard violations = 1, Best = 1
[2025-12-29T17:30:06.561Z] [INFO] [Intensification] Iter 1500: Hard violations = 1, Best = 1
[2025-12-29T17:30:19.610Z] [INFO] [Intensification] Iter 2000: Hard violations = 1, Best = 1
[2025-12-29T17:30:19.611Z] [INFO] [Intensification] Attempt 2/3
[2025-12-29T17:30:33.574Z] [INFO] [Intensification] Iter 500: Hard violations = 1, Best = 1
[2025-12-29T17:30:46.198Z] [INFO] [Intensification] Iter 1000: Hard violations = 1, Best = 1
[2025-12-29T17:30:59.067Z] [INFO] [Intensification] Iter 1500: Hard violations = 1, Best = 1
[2025-12-29T17:31:12.901Z] [INFO] [Intensification] Iter 2000: Hard violations = 1, Best = 1
[2025-12-29T17:31:12.901Z] [INFO] [Intensification] Attempt 3/3
[2025-12-29T17:31:25.529Z] [INFO] [Intensification] Iter 500: Hard violations = 1, Best = 1
[2025-12-29T17:31:39.412Z] [INFO] [Intensification] Iter 1000: Hard violations = 1, Best = 1
[2025-12-29T17:31:51.924Z] [INFO] [Intensification] Iter 1500: Hard violations = 1, Best = 1
[2025-12-29T17:32:04.518Z] [INFO] [Intensification] Iter 2000: Hard violations = 1, Best = 1
[2025-12-29T17:32:04.518Z] [WARN] [Intensification] Could not eliminate all hard violations. Remaining: 1
[2025-12-29T17:32:04.518Z] [INFO] Phase 2: Optimizing soft constraints
[2025-12-29T17:32:09.058Z] [INFO] [Phase 2] Iteration 32000: Temp = 9651.72, Current = 50026.83, Best = 50026.70
[2025-12-29T17:32:25.429Z] [INFO] [Phase 2] Iteration 33000: Temp = 8551.65, Current = 50027.01, Best = 50026.70
[2025-12-29T17:32:33.448Z] [INFO] [Phase 2] Iteration 33500: Temp = 8056.81, Current = 50026.99, Best = 50026.70
[2025-12-29T17:32:41.958Z] [INFO] [Phase 2] Iteration 34000: Temp = 7564.85, Current = 50027.01, Best = 50026.70
[2025-12-29T17:32:50.796Z] [INFO] [Phase 2] Iteration 34500: Temp = 7129.96, Current = 50027.02, Best = 50026.70
[2025-12-29T17:33:05.843Z] [INFO] [Phase 2] Iteration 35500: Temp = 6375.71, Current = 50026.85, Best = 50026.70
[2025-12-29T17:33:13.691Z] [INFO] [Phase 2] Iteration 36000: Temp = 6013.99, Current = 50026.94, Best = 50026.70
[2025-12-29T17:33:22.241Z] [INFO] [Phase 2] Iteration 36500: Temp = 5690.99, Current = 50027.06, Best = 50026.70
[2025-12-29T17:33:30.061Z] [INFO] [Phase 2] Iteration 37000: Temp = 5374.57, Current = 50027.01, Best = 50026.70
[2025-12-29T17:33:37.222Z] [INFO] [Phase 2] Iteration 37500: Temp = 5077.77, Current = 50027.01, Best = 50026.70
[2025-12-29T17:33:44.189Z] [INFO] [Phase 2] Iteration 38000: Temp = 4822.38, Current = 50026.90, Best = 50026.70
[2025-12-29T17:33:52.671Z] [INFO] [Phase 2] Iteration 38500: Temp = 4525.19, Current = 50027.03, Best = 50026.70
[2025-12-29T17:34:00.632Z] [INFO] [Phase 2] Iteration 39000: Temp = 4265.05, Current = 50026.93, Best = 50026.70
[2025-12-29T17:34:18.737Z] [INFO] [Phase 2] Iteration 40000: Temp = 3764.60, Current = 27.19, Best = 27.11
[2025-12-29T17:34:26.305Z] [INFO] [Phase 2] Iteration 40500: Temp = 3543.22, Current = 27.29, Best = 27.11
[2025-12-29T17:34:34.314Z] [INFO] [Phase 2] Iteration 41000: Temp = 3334.86, Current = 27.14, Best = 27.11
[2025-12-29T17:34:58.737Z] [INFO] [Phase 2] Iteration 42500: Temp = 2790.48, Current = 27.11, Best = 27.11
[2025-12-29T17:35:06.678Z] [INFO] [Phase 2] Iteration 43000: Temp = 2627.96, Current = 27.17, Best = 27.11
[2025-12-29T17:35:15.021Z] [INFO] [Phase 2] Iteration 43500: Temp = 2460.59, Current = 27.09, Best = 27.04
[2025-12-29T17:35:22.698Z] [INFO] [Phase 2] Iteration 44000: Temp = 2325.64, Current = 27.10, Best = 27.04
[2025-12-29T17:35:37.597Z] [INFO] [Phase 2] Iteration 45000: Temp = 2077.54, Current = 27.27, Best = 27.04
[2025-12-29T17:35:52.896Z] [INFO] [Phase 2] Iteration 46000: Temp = 1863.34, Current = 27.27, Best = 27.04
[2025-12-29T17:36:00.527Z] [INFO] [Phase 2] Iteration 46500: Temp = 1763.26, Current = 27.20, Best = 27.04
[2025-12-29T17:36:09.362Z] [INFO] [Phase 2] Iteration 47000: Temp = 1660.57, Current = 27.22, Best = 27.04
[2025-12-29T17:36:16.510Z] [INFO] [Phase 2] Iteration 47500: Temp = 1570.75, Current = 27.24, Best = 27.04
[2025-12-29T17:36:23.941Z] [INFO] [Phase 2] Iteration 48000: Temp = 1479.86, Current = 27.39, Best = 27.04
[2025-12-29T17:36:40.116Z] [INFO] [Phase 2] Iteration 49000: Temp = 1320.67, Current = 27.33, Best = 27.04
[2025-12-29T17:36:47.641Z] [INFO] [Phase 2] Iteration 49500: Temp = 1247.74, Current = 27.22, Best = 27.04
[2025-12-29T17:37:11.998Z] [INFO] [Phase 2] Iteration 51000: Temp = 1047.61, Current = 27.28, Best = 27.04
[2025-12-29T17:37:18.374Z] [INFO] [Phase 2] Reheating #1: Temperature = 149986.45, Fitness = 27.04
[2025-12-29T17:37:20.374Z] [INFO] [Phase 2] Iteration 51500: Temp = 147605.52, Current = 27.35, Best = 27.04
[2025-12-29T17:37:27.947Z] [INFO] [Phase 2] Iteration 52000: Temp = 138897.64, Current = 27.54, Best = 27.04
[2025-12-29T17:38:08.732Z] [INFO] [Phase 2] Iteration 54500: Temp = 102750.85, Current = 27.38, Best = 27.04
[2025-12-29T17:38:16.921Z] [INFO] [Phase 2] Iteration 55000: Temp = 96766.52, Current = 27.47, Best = 27.04
[2025-12-29T17:38:25.478Z] [INFO] [Phase 2] Iteration 55500: Temp = 91094.29, Current = 27.40, Best = 27.04
[2025-12-29T17:38:50.457Z] [INFO] [Phase 2] Iteration 57000: Temp = 75405.19, Current = 27.63, Best = 27.04
[2025-12-29T17:38:58.849Z] [INFO] [Phase 2] Iteration 57500: Temp = 70744.15, Current = 27.54, Best = 27.04
[2025-12-29T17:39:07.922Z] [INFO] [Phase 2] Iteration 58000: Temp = 66663.92, Current = 27.41, Best = 27.04
[2025-12-29T17:39:32.442Z] [INFO] [Phase 2] Iteration 59500: Temp = 55248.71, Current = 27.46, Best = 27.04
[2025-12-29T17:39:41.580Z] [INFO] Optimization complete {"iterations":60000,"reheats":1,"finalTemperature":"51792.1506","fitness":"27.04","hardViolations":0,"softViolations":8}
[2025-12-29T17:39:41.581Z] [INFO] Operator Statistics:
[2025-12-29T17:39:41.581Z] [INFO]   Fix Friday Prayer Conflict: Attempts = 1006, Improvements = 19, Accepted = 822, Success Rate = 1.89%
[2025-12-29T17:39:41.581Z] [INFO]   Swap Friday with Non-Friday: Attempts = 879, Improvements = 1, Accepted = 682, Success Rate = 0.11%
[2025-12-29T17:39:41.581Z] [INFO]   Fix Lecturer Conflict: Attempts = 0, Improvements = 0, Accepted = 0, Success Rate = 0.00%
[2025-12-29T17:39:41.581Z] [INFO]   Fix Room Conflict: Attempts = 13, Improvements = 2, Accepted = 13, Success Rate = 15.38%
[2025-12-29T17:39:41.581Z] [INFO]   Fix Max Daily Periods: Attempts = 17, Improvements = 6, Accepted = 17, Success Rate = 35.29%
[2025-12-29T17:39:41.581Z] [INFO]   Fix Room Capacity: Attempts = 98, Improvements = 1, Accepted = 98, Success Rate = 1.02%
[2025-12-29T17:39:41.581Z] [INFO]   Change Time Slot and Room: Attempts = 4438, Improvements = 529, Accepted = 4092, Success Rate = 11.92%
[2025-12-29T17:39:41.581Z] [INFO]   Change Time Slot: Attempts = 3523, Improvements = 203, Accepted = 2888, Success Rate = 5.76%
[2025-12-29T17:39:41.581Z] [INFO]   Change Room: Attempts = 7216, Improvements = 515, Accepted = 7216, Success Rate = 7.14%
[2025-12-29T17:39:41.581Z] [INFO]   Swap Classes: Attempts = 17150, Improvements = 145, Accepted = 973, Success Rate = 0.85%
======================================================================

✨ OPTIMIZATION COMPLETE!

Cache stats: {
  timeCache: {
    timeToMinutes: 20,
    minutesToTime: 17,
  },
  endTimeCache: 286,
  prayerOverlapCache: 286,
  totalEntries: 609,
}
📊 RESULTS:
   Final fitness: 27.04
   Hard constraint violations: 0
   Soft constraint violations: 8
   Total iterations: 60000
   Reheating events: 1
   Final temperature: 51792.1506
   Classes scheduled: 354/373

📈 OPERATOR STATISTICS:
   Fix Friday Prayer Conflict:
      Attempts: 1006
      Improvements: 19
      Success rate: 1.89%
   Swap Friday with Non-Friday:
      Attempts: 879
      Improvements: 1
      Success rate: 0.11%
   Fix Lecturer Conflict:
      Attempts: 0
      Improvements: 0
      Success rate: 0.00%
   Fix Room Conflict:
      Attempts: 13
      Improvements: 2
      Success rate: 15.38%
   Fix Max Daily Periods:
      Attempts: 17
      Improvements: 6
      Success rate: 35.29%
   Fix Room Capacity:
      Attempts: 98
      Improvements: 1
      Success rate: 1.02%
   Change Time Slot and Room:
      Attempts: 4438
      Improvements: 529
      Success rate: 11.92%
   Change Time Slot:
      Attempts: 3523
      Improvements: 203
      Success rate: 5.76%
   Change Room:
      Attempts: 7216
      Improvements: 515
      Success rate: 7.14%
   Swap Classes:
      Attempts: 17150
      Improvements: 145
      Success rate: 0.85%

⚠️  VIOLATIONS (8):
   - [soft] Preferred Time: No description
   - [soft] Preferred Room: No description
   - [soft] Transit Time: No description
   - [soft] Compactness: No description
   - [soft] Prayer Time Overlap: No description
   - [soft] Evening Class Priority: No description
   - [soft] Research Day: No description
   - [soft] Overflow Penalty: No description

======================================================================
✅ Example completed successfully!
======================================================================

💾 Results saved to: timetable-result.json

emmanuelabayor@ade:~/projects/timetable-sa$
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
  ⚠️  Skipping MM23RS03: No lecturers on class Research Seminar
  ⚠️  Skipping GS13PW02: No lecturers on class Kerja Praktik
  ⚠️  Skipping AC135343: No lecturers on class Skripsi
  ⚠️  Skipping GS13PW02: No lecturers on class Kerja Praktik
  ⚠️  Skipping GS13TH46: No lecturers on class Skripsi
  ⚠️  Skipping GS13IP12: No lecturers on class Proyek Interdisipliner
  ⚠️  Skipping GS13PW02: No lecturers on class KERJA PRAKTIK
  ⚠️  Skipping GS13IP12: No lecturers on class PROYEK INTERDISIPLIN
  ⚠️  Skipping GS13CZ02: No lecturers on class Kewarganegaraan
  ⚠️  Skipping GS13IP12: No lecturers on class Proyek Interdisiplin
  ⚠️  Skipping CE11UT46: No lecturers on class Skripsi
  ⚠️  Skipping GS13PW02: No lecturers on class Praktik Kerja Lapang
  ⚠️  Skipping GS13CZ02: No lecturers on class Kewarganegaraan
  ⚠️  Could not place IF13RP12: Rekayasa Perangkat Lunak
  ⚠️  Skipping GS13PW02: No lecturers on class Kerja Praktik/Magang
  ⚠️  Skipping GS13CZ02: No lecturers on class Kewarganegaraan
  ⚠️  Skipping GS13IP12: No lecturers on class Proyek Interdisipliner
  ⚠️  Skipping VD13KP02: No lecturers on class Kerja Praktik
  ⚠️  Could not place VD13BS53: Perencanaan Bisnis

✅ Initial solution generated:
   Successfully placed: 354/373
   Failed to place: 19/373


⚖️  Setting up constraints...
   Hard constraints: 11
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
[2025-12-29T16:28:42.316Z] [INFO] Simulated Annealing initialized {"hardConstraints":11,"softConstraints":8,"moveGenerators":10,"config":{"initialTemperature":100000,"minTemperature":1e-7,"coolingRate":0.9998,"maxIterations":60000}}
[2025-12-29T16:28:42.317Z] [INFO] Starting optimization...
[2025-12-29T16:28:42.317Z] [INFO] Phase 1: Eliminating hard constraint violations
[2025-12-29T16:28:42.354Z] [INFO] Initial state {"fitness":"341935.71","hardViolations":29}
[2025-12-29T16:28:58.236Z] [INFO] [Phase 1] Iteration 1000: Temp = 89779.75, Hard violations = 10, Best = 10
[2025-12-29T16:29:24.025Z] [INFO] [Phase 1] Iteration 2500: Temp = 76995.27, Hard violations = 9, Best = 9
[2025-12-29T16:29:30.139Z] [INFO] [Phase 1] Iteration 3000: Temp = 73872.45, Hard violations = 8, Best = 8
[2025-12-29T16:29:36.787Z] [INFO] [Phase 1] Iteration 3500: Temp = 70579.19, Hard violations = 8, Best = 8
[2025-12-29T16:29:43.594Z] [INFO] [Phase 1] Iteration 4000: Temp = 67446.24, Hard violations = 8, Best = 8
[2025-12-29T16:30:05.461Z] [INFO] [Phase 1] Iteration 5500: Temp = 58458.46, Hard violations = 7, Best = 7
[2025-12-29T16:30:32.889Z] [INFO] [Phase 1] Iteration 7500: Temp = 48283.86, Hard violations = 7, Best = 7
[2025-12-29T16:30:59.648Z] [INFO] [Phase 1] Iteration 9500: Temp = 40604.55, Hard violations = 6, Best = 6
[2025-12-29T16:31:06.256Z] [INFO] [Phase 1] Iteration 10000: Temp = 38825.44, Hard violations = 6, Best = 6
[2025-12-29T16:31:12.541Z] [INFO] [Phase 1] Iteration 10500: Temp = 37280.54, Hard violations = 6, Best = 6
[2025-12-29T16:31:50.425Z] [INFO] [Phase 1] Iteration 13500: Temp = 29138.11, Hard violations = 5, Best = 5
[2025-12-29T16:32:22.781Z] [INFO] [Phase 1] Iteration 16000: Temp = 23613.67, Hard violations = 5, Best = 5
[2025-12-29T16:32:29.040Z] [INFO] [Phase 1] Iteration 16500: Temp = 22651.40, Hard violations = 5, Best = 5
[2025-12-29T16:32:35.807Z] [INFO] [Phase 1] Iteration 17000: Temp = 21837.27, Hard violations = 5, Best = 5
[2025-12-29T16:32:49.223Z] [INFO] [Phase 1] Iteration 18000: Temp = 19957.58, Hard violations = 5, Best = 5
[2025-12-29T16:33:22.688Z] [INFO] [Phase 1] Iteration 20500: Temp = 16464.22, Hard violations = 4, Best = 4
[2025-12-29T16:33:51.261Z] [INFO] [Phase 1] Iteration 22500: Temp = 14139.53, Hard violations = 3, Best = 3
[2025-12-29T16:33:58.010Z] [INFO] [Phase 1] Iteration 23000: Temp = 13606.81, Hard violations = 3, Best = 3
[2025-12-29T16:34:05.227Z] [INFO] [Phase 1] Iteration 23500: Temp = 13083.70, Hard violations = 3, Best = 3
[2025-12-29T16:34:12.776Z] [INFO] [Phase 1] Iteration 24000: Temp = 12548.02, Hard violations = 3, Best = 3
[2025-12-29T16:34:42.998Z] [INFO] [Phase 1] Iteration 26000: Temp = 10679.72, Hard violations = 3, Best = 3
[2025-12-29T16:34:55.092Z] [INFO] Phase 1 complete: Hard violations = 3
[2025-12-29T16:34:55.092Z] [INFO] Phase 1.5: Intensification - targeting remaining hard violations
[2025-12-29T16:34:55.092Z] [INFO] [Intensification] Attempt 1/3
[2025-12-29T16:35:09.849Z] [INFO] [Intensification] Iter 500: Hard violations = 3, Best = 3
[2025-12-29T16:35:23.206Z] [INFO] [Intensification] Iter 1000: Hard violations = 3, Best = 3
[2025-12-29T16:35:35.992Z] [INFO] [Intensification] Iter 1500: Hard violations = 3, Best = 3
[2025-12-29T16:35:47.669Z] [INFO] [Intensification] Iter 2000: Hard violations = 3, Best = 3
[2025-12-29T16:35:47.670Z] [INFO] [Intensification] Attempt 2/3
[2025-12-29T16:36:03.306Z] [INFO] [Intensification] Iter 500: Hard violations = 3, Best = 3
[2025-12-29T16:36:18.011Z] [INFO] [Intensification] Iter 1000: Hard violations = 3, Best = 3
[2025-12-29T16:36:33.609Z] [INFO] [Intensification] Iter 1500: Hard violations = 3, Best = 3
[2025-12-29T16:36:48.157Z] [INFO] [Intensification] Iter 2000: Hard violations = 3, Best = 3
[2025-12-29T16:36:48.157Z] [INFO] [Intensification] Attempt 3/3
[2025-12-29T16:37:03.019Z] [INFO] [Intensification] Iter 500: Hard violations = 3, Best = 3
[2025-12-29T16:37:17.952Z] [INFO] [Intensification] Iter 1000: Hard violations = 3, Best = 3
[2025-12-29T16:37:33.117Z] [INFO] [Intensification] Iter 1500: Hard violations = 3, Best = 3
[2025-12-29T16:37:48.768Z] [INFO] [Intensification] Iter 2000: Hard violations = 3, Best = 3
[2025-12-29T16:37:48.768Z] [WARN] [Intensification] Could not eliminate all hard violations. Remaining: 3
[2025-12-29T16:37:48.768Z] [INFO] Phase 2: Optimizing soft constraints
[2025-12-29T16:37:57.813Z] [INFO] [Phase 2] Iteration 33500: Temp = 9508.01, Current = 150027.29, Best = 150027.16
[2025-12-29T16:38:05.642Z] [INFO] [Phase 2] Iteration 34000: Temp = 9100.51, Current = 150027.36, Best = 150027.16
[2025-12-29T16:38:48.023Z] [INFO] [Phase 2] Iteration 37000: Temp = 7259.48, Current = 150027.48, Best = 150027.16
[2025-12-29T16:39:15.255Z] [INFO] [Phase 2] Iteration 39000: Temp = 6169.96, Current = 100027.57, Best = 100027.45
[2025-12-29T16:39:21.550Z] [INFO] [Phase 2] Iteration 39500: Temp = 5923.26, Current = 100027.54, Best = 100027.44
[2025-12-29T16:39:34.817Z] [INFO] [Phase 2] Iteration 40500: Temp = 5411.24, Current = 100027.40, Best = 100027.33
[2025-12-29T16:39:40.997Z] [INFO] [Phase 2] Iteration 41000: Temp = 5193.85, Current = 100027.37, Best = 100027.33
[2025-12-29T16:39:47.841Z] [INFO] [Phase 2] Iteration 41500: Temp = 4952.39, Current = 100027.36, Best = 100027.33
[2025-12-29T16:40:00.258Z] [INFO] [Phase 2] Iteration 42500: Temp = 4555.16, Current = 100027.47, Best = 100027.33
[2025-12-29T16:40:20.453Z] [INFO] [Phase 2] Iteration 44000: Temp = 3986.24, Current = 100027.67, Best = 100027.25
[2025-12-29T16:40:33.162Z] [INFO] [Phase 2] Iteration 45000: Temp = 3661.38, Current = 100027.58, Best = 100027.25
[2025-12-29T16:40:40.389Z] [INFO] [Phase 2] Iteration 45500: Temp = 3511.47, Current = 100027.52, Best = 100027.25
[2025-12-29T16:40:46.710Z] [INFO] [Phase 2] Iteration 46000: Temp = 3367.03, Current = 100027.55, Best = 100027.25
[2025-12-29T16:41:04.890Z] [INFO] [Phase 2] Iteration 47500: Temp = 2971.36, Current = 100027.59, Best = 100027.25
[2025-12-29T16:41:11.465Z] [INFO] [Phase 2] Iteration 48000: Temp = 2840.60, Current = 100027.61, Best = 100027.25
[2025-12-29T16:41:19.042Z] [INFO] [Phase 2] Iteration 48500: Temp = 2712.33, Current = 100027.71, Best = 100027.25
[2025-12-29T16:41:30.887Z] [INFO] [Phase 2] Iteration 49500: Temp = 2490.29, Current = 100027.71, Best = 100027.25
[2025-12-29T16:41:37.161Z] [INFO] [Phase 2] Iteration 50000: Temp = 2380.70, Current = 100027.59, Best = 100027.25
[2025-12-29T16:41:43.249Z] [INFO] [Phase 2] Iteration 50500: Temp = 2285.52, Current = 100027.42, Best = 100027.25
[2025-12-29T16:42:10.729Z] [INFO] [Phase 2] Iteration 52500: Temp = 1913.58, Current = 100027.64, Best = 100027.25
[2025-12-29T16:42:23.160Z] [INFO] [Phase 2] Iteration 53500: Temp = 1757.63, Current = 50027.76, Best = 50027.75
[2025-12-29T16:42:50.547Z] [INFO] [Phase 2] Iteration 55000: Temp = 1465.43, Current = 27.72, Best = 27.56
[2025-12-29T16:43:15.395Z] [INFO] [Phase 2] Iteration 56500: Temp = 1217.41, Current = 27.64, Best = 27.56
[2025-12-29T16:43:23.935Z] [INFO] [Phase 2] Iteration 57000: Temp = 1146.28, Current = 27.53, Best = 27.47
[2025-12-29T16:43:32.230Z] [INFO] [Phase 2] Iteration 57500: Temp = 1080.38, Current = 27.59, Best = 27.47
[2025-12-29T16:43:43.738Z] [INFO] [Phase 2] Reheating #1: Temperature = 149986.45, Fitness = 27.47
[2025-12-29T16:43:50.142Z] [INFO] [Phase 2] Iteration 58500: Temp = 142956.46, Current = 27.63, Best = 27.47
[2025-12-29T16:44:05.350Z] [INFO] [Phase 2] Iteration 59500: Temp = 127425.09, Current = 27.53, Best = 27.46
[2025-12-29T16:44:13.059Z] [INFO] [Phase 2] Iteration 60000: Temp = 119907.73, Current = 27.59, Best = 27.46
[2025-12-29T16:44:13.069Z] [INFO] Optimization complete {"iterations":60000,"reheats":1,"finalTemperature":"119907.7330","fitness":"27.46","hardViolations":0,"softViolations":8}
[2025-12-29T16:44:13.070Z] [INFO] Operator Statistics:
[2025-12-29T16:44:13.070Z] [INFO]   Fix Friday Prayer Conflict: Attempts = 3194, Improvements = 144, Accepted = 3172, Success Rate = 4.51%
[2025-12-29T16:44:13.070Z] [INFO]   Swap Friday with Non-Friday: Attempts = 3607, Improvements = 0, Accepted = 2626, Success Rate = 0.00%
[2025-12-29T16:44:13.070Z] [INFO]   Fix Lecturer Conflict: Attempts = 1638, Improvements = 7, Accepted = 1567, Success Rate = 0.43%
[2025-12-29T16:44:13.070Z] [INFO]   Fix Room Conflict: Attempts = 2, Improvements = 2, Accepted = 2, Success Rate = 100.00%
[2025-12-29T16:44:13.070Z] [INFO]   Fix Max Daily Periods: Attempts = 445, Improvements = 9, Accepted = 445, Success Rate = 2.02%
[2025-12-29T16:44:13.070Z] [INFO]   Fix Room Capacity: Attempts = 1, Improvements = 1, Accepted = 1, Success Rate = 100.00%
[2025-12-29T16:44:13.070Z] [INFO]   Change Time Slot and Room: Attempts = 3122, Improvements = 468, Accepted = 2926, Success Rate = 14.99%
[2025-12-29T16:44:13.070Z] [INFO]   Change Time Slot: Attempts = 2409, Improvements = 199, Accepted = 1913, Success Rate = 8.26%
[2025-12-29T16:44:13.070Z] [INFO]   Change Room: Attempts = 5566, Improvements = 397, Accepted = 5566, Success Rate = 7.13%
[2025-12-29T16:44:13.070Z] [INFO]   Swap Classes: Attempts = 10159, Improvements = 70, Accepted = 549, Success Rate = 0.69%
======================================================================

✨ OPTIMIZATION COMPLETE!

Cache stats: {
  timeCache: {
    timeToMinutes: 20,
    minutesToTime: 17,
  },
  endTimeCache: 288,
  prayerOverlapCache: 288,
  totalEntries: 613,
}
📊 RESULTS:
   Final fitness: 27.46
   Hard constraint violations: 0
   Soft constraint violations: 8
   Total iterations: 60000
   Reheating events: 1
   Final temperature: 119907.7330
   Classes scheduled: 354/373

📈 OPERATOR STATISTICS:
   Fix Friday Prayer Conflict:
      Attempts: 3194
      Improvements: 144
      Success rate: 4.51%
   Swap Friday with Non-Friday:
      Attempts: 3607
      Improvements: 0
      Success rate: 0.00%
   Fix Lecturer Conflict:
      Attempts: 1638
      Improvements: 7
      Success rate: 0.43%
   Fix Room Conflict:
      Attempts: 2
      Improvements: 2
      Success rate: 100.00%
   Fix Max Daily Periods:
      Attempts: 445
      Improvements: 9
      Success rate: 2.02%
   Fix Room Capacity:
      Attempts: 1
      Improvements: 1
      Success rate: 100.00%
   Change Time Slot and Room:
      Attempts: 3122
      Improvements: 468
      Success rate: 14.99%
   Change Time Slot:
      Attempts: 2409
      Improvements: 199
      Success rate: 8.26%
   Change Room:
      Attempts: 5566
      Improvements: 397
      Success rate: 7.13%
   Swap Classes:
      Attempts: 10159
      Improvements: 70
      Success rate: 0.69%

⚠️  VIOLATIONS (8):
   - [soft] Preferred Time: No description
   - [soft] Preferred Room: No description
   - [soft] Transit Time: No description
   - [soft] Compactness: No description
   - [soft] Prayer Time Overlap: No description
   - [soft] Evening Class Priority: No description
   - [soft] Research Day: No description
   - [soft] Overflow Penalty: No description

======================================================================
✅ Example completed successfully!
======================================================================

💾 Results saved to: timetable-result.json

emmanuelabayor@ade:~/projects/timetable-sa$
```
# Trial 4
```bash
emmanuelabayor@ade:~/projects/timetable-sa$ bun run examples/timetabling/example-basic.ts
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
  ⚠️  Skipping MM23RS03: No lecturers on class Research Seminar
  ⚠️  Skipping GS13PW02: No lecturers on class Kerja Praktik
  ⚠️  Skipping AC135343: No lecturers on class Skripsi
  ⚠️  Skipping GS13PW02: No lecturers on class Kerja Praktik
  ⚠️  Skipping GS13TH46: No lecturers on class Skripsi
  ⚠️  Skipping GS13IP12: No lecturers on class Proyek Interdisipliner
  ⚠️  Skipping GS13PW02: No lecturers on class KERJA PRAKTIK
  ⚠️  Skipping GS13IP12: No lecturers on class PROYEK INTERDISIPLIN
  ⚠️  Skipping GS13CZ02: No lecturers on class Kewarganegaraan
  ⚠️  Skipping GS13IP12: No lecturers on class Proyek Interdisiplin
  ⚠️  Skipping CE11UT46: No lecturers on class Skripsi
  ⚠️  Skipping GS13PW02: No lecturers on class Praktik Kerja Lapang
  ⚠️  Skipping GS13CZ02: No lecturers on class Kewarganegaraan
  ⚠️  Could not place IF13RP12: Rekayasa Perangkat Lunak
  ⚠️  Skipping GS13PW02: No lecturers on class Kerja Praktik/Magang
  ⚠️  Skipping GS13CZ02: No lecturers on class Kewarganegaraan
  ⚠️  Skipping GS13IP12: No lecturers on class Proyek Interdisipliner
  ⚠️  Skipping VD13KP02: No lecturers on class Kerja Praktik
  ⚠️  Could not place VD13BS53: Perencanaan Bisnis

✅ Initial solution generated:
   Successfully placed: 354/373
   Failed to place: 19/373


⚖️  Setting up constraints...
   Hard constraints: 11
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
[2025-12-29T16:44:20.692Z] [INFO] Simulated Annealing initialized {"hardConstraints":11,"softConstraints":8,"moveGenerators":10,"config":{"initialTemperature":100000,"minTemperature":1e-7,"coolingRate":0.9998,"maxIterations":60000}}
[2025-12-29T16:44:20.692Z] [INFO] Starting optimization...
[2025-12-29T16:44:20.693Z] [INFO] Phase 1: Eliminating hard constraint violations
[2025-12-29T16:44:20.738Z] [INFO] Initial state {"fitness":"341935.71","hardViolations":29}
[2025-12-29T16:44:36.965Z] [INFO] [Phase 1] Iteration 1000: Temp = 90175.69, Hard violations = 14, Best = 14
[2025-12-29T16:44:43.254Z] [INFO] [Phase 1] Iteration 1500: Temp = 86847.71, Hard violations = 14, Best = 14
[2025-12-29T16:44:49.029Z] [INFO] [Phase 1] Iteration 2000: Temp = 84162.79, Hard violations = 14, Best = 14
[2025-12-29T16:45:01.138Z] [INFO] [Phase 1] Iteration 3000: Temp = 78944.62, Hard violations = 13, Best = 13
[2025-12-29T16:45:08.183Z] [INFO] [Phase 1] Iteration 3500: Temp = 75742.73, Hard violations = 11, Best = 11
[2025-12-29T16:45:35.821Z] [INFO] [Phase 1] Iteration 5000: Temp = 65139.25, Hard violations = 10, Best = 10
[2025-12-29T16:45:48.464Z] [INFO] [Phase 1] Iteration 6000: Temp = 59962.48, Hard violations = 10, Best = 10
[2025-12-29T16:45:55.786Z] [INFO] [Phase 1] Iteration 6500: Temp = 57072.03, Hard violations = 9, Best = 9
[2025-12-29T16:46:03.129Z] [INFO] [Phase 1] Iteration 7000: Temp = 54299.18, Hard violations = 8, Best = 8
[2025-12-29T16:46:10.099Z] [INFO] [Phase 1] Iteration 7500: Temp = 51826.65, Hard violations = 8, Best = 8
[2025-12-29T16:46:25.099Z] [INFO] [Phase 1] Iteration 8500: Temp = 47233.11, Hard violations = 8, Best = 8
[2025-12-29T16:46:38.324Z] [INFO] [Phase 1] Iteration 9500: Temp = 43314.46, Hard violations = 7, Best = 7
[2025-12-29T16:47:01.805Z] [INFO] [Phase 1] Iteration 11500: Temp = 37617.61, Hard violations = 6, Best = 6
[2025-12-29T16:47:21.337Z] [INFO] [Phase 1] Iteration 13000: Temp = 33719.00, Hard violations = 6, Best = 6
[2025-12-29T16:47:27.505Z] [INFO] [Phase 1] Iteration 13500: Temp = 32507.08, Hard violations = 6, Best = 6
[2025-12-29T16:47:47.625Z] [INFO] [Phase 1] Iteration 15000: Temp = 28830.84, Hard violations = 4, Best = 4
[2025-12-29T16:48:06.619Z] [INFO] [Phase 1] Iteration 16000: Temp = 25946.46, Hard violations = 4, Best = 4
[2025-12-29T16:48:17.557Z] [INFO] [Phase 1] Iteration 16500: Temp = 24577.46, Hard violations = 4, Best = 4
[2025-12-29T16:48:27.499Z] [INFO] [Phase 1] Iteration 17000: Temp = 23252.77, Hard violations = 4, Best = 4
[2025-12-29T16:48:49.070Z] [INFO] [Phase 1] Iteration 18000: Temp = 20714.06, Hard violations = 4, Best = 4
[2025-12-29T16:48:58.098Z] [INFO] [Phase 1] Iteration 18500: Temp = 19656.49, Hard violations = 3, Best = 3
[2025-12-29T16:49:07.967Z] [INFO] [Phase 1] Iteration 19000: Temp = 18597.03, Hard violations = 3, Best = 3
[2025-12-29T16:49:18.344Z] [INFO] [Phase 1] Iteration 19500: Temp = 17548.99, Hard violations = 3, Best = 3
[2025-12-29T16:49:39.266Z] [INFO] [Phase 1] Iteration 20500: Temp = 15705.09, Hard violations = 3, Best = 3
[2025-12-29T16:49:49.786Z] [INFO] [Phase 1] Iteration 21000: Temp = 14746.10, Hard violations = 2, Best = 2
[2025-12-29T16:49:58.217Z] [INFO] [Phase 1] Iteration 21500: Temp = 13906.73, Hard violations = 2, Best = 2
[2025-12-29T16:50:01.579Z] [INFO] Phase 1 complete: Hard violations = 0
[2025-12-29T16:50:01.579Z] [INFO] Phase 2: Optimizing soft constraints
[2025-12-29T16:50:15.920Z] [INFO] [Phase 2] Iteration 22500: Temp = 12301.99, Current = 27.22, Best = 27.20
[2025-12-29T16:50:40.946Z] [INFO] [Phase 2] Iteration 24000: Temp = 10203.61, Current = 27.29, Best = 27.09
[2025-12-29T16:50:49.296Z] [INFO] [Phase 2] Iteration 24500: Temp = 9574.81, Current = 27.37, Best = 27.09
[2025-12-29T16:51:05.943Z] [INFO] [Phase 2] Iteration 25500: Temp = 8429.38, Current = 27.11, Best = 27.09
[2025-12-29T16:51:13.823Z] [INFO] [Phase 2] Iteration 26000: Temp = 7938.44, Current = 27.26, Best = 27.05
[2025-12-29T16:51:22.323Z] [INFO] [Phase 2] Iteration 26500: Temp = 7494.06, Current = 27.27, Best = 27.05
[2025-12-29T16:51:39.222Z] [INFO] [Phase 2] Iteration 27500: Temp = 6653.21, Current = 27.21, Best = 27.01
[2025-12-29T16:51:47.292Z] [INFO] [Phase 2] Iteration 28000: Temp = 6250.70, Current = 27.37, Best = 27.01
[2025-12-29T16:51:54.900Z] [INFO] [Phase 2] Iteration 28500: Temp = 5912.61, Current = 27.42, Best = 27.01
[2025-12-29T16:52:11.261Z] [INFO] [Phase 2] Iteration 29500: Temp = 5279.74, Current = 27.57, Best = 27.01
[2025-12-29T16:52:19.312Z] [INFO] [Phase 2] Iteration 30000: Temp = 4967.27, Current = 27.42, Best = 27.01
[2025-12-29T16:52:27.903Z] [INFO] [Phase 2] Iteration 30500: Temp = 4643.48, Current = 27.53, Best = 27.01
[2025-12-29T16:52:35.702Z] [INFO] [Phase 2] Iteration 31000: Temp = 4379.16, Current = 27.56, Best = 27.01
[2025-12-29T16:52:53.756Z] [INFO] [Phase 2] Iteration 32000: Temp = 3857.60, Current = 27.78, Best = 27.01
[2025-12-29T16:53:01.802Z] [INFO] [Phase 2] Iteration 32500: Temp = 3635.11, Current = 27.76, Best = 27.01
[2025-12-29T16:53:18.276Z] [INFO] [Phase 2] Iteration 33500: Temp = 3222.08, Current = 27.68, Best = 27.01
[2025-12-29T16:53:34.732Z] [INFO] [Phase 2] Iteration 34500: Temp = 2857.69, Current = 27.42, Best = 27.01
[2025-12-29T16:53:51.312Z] [INFO] [Phase 2] Iteration 35500: Temp = 2527.43, Current = 27.37, Best = 27.01
[2025-12-29T16:53:59.903Z] [INFO] [Phase 2] Iteration 36000: Temp = 2370.73, Current = 27.38, Best = 27.01
[2025-12-29T16:54:08.410Z] [INFO] [Phase 2] Iteration 36500: Temp = 2229.08, Current = 27.31, Best = 27.01
[2025-12-29T16:54:33.943Z] [INFO] [Phase 2] Iteration 38000: Temp = 1852.19, Current = 27.41, Best = 27.01
[2025-12-29T16:54:42.990Z] [INFO] [Phase 2] Iteration 38500: Temp = 1744.32, Current = 27.55, Best = 27.01
[2025-12-29T16:54:50.556Z] [INFO] [Phase 2] Iteration 39000: Temp = 1647.34, Current = 27.52, Best = 27.01
[2025-12-29T16:54:58.501Z] [INFO] [Phase 2] Iteration 39500: Temp = 1551.08, Current = 27.58, Best = 27.01
[2025-12-29T16:55:33.086Z] [INFO] [Phase 2] Iteration 41500: Temp = 1214.01, Current = 27.62, Best = 27.01
[2025-12-29T16:55:41.160Z] [INFO] [Phase 2] Iteration 42000: Temp = 1145.82, Current = 27.48, Best = 27.01
[2025-12-29T16:55:59.535Z] [INFO] [Phase 2] Reheating #1: Temperature = 149986.45, Fitness = 27.01
[2025-12-29T16:56:05.444Z] [INFO] [Phase 2] Iteration 43500: Temp = 142842.13, Current = 27.67, Best = 27.01
[2025-12-29T16:56:14.027Z] [INFO] [Phase 2] Iteration 44000: Temp = 133985.78, Current = 27.85, Best = 27.01
[2025-12-29T16:56:24.008Z] [INFO] [Phase 2] Iteration 44500: Temp = 125879.79, Current = 27.69, Best = 27.01
[2025-12-29T16:56:32.367Z] [INFO] [Phase 2] Iteration 45000: Temp = 118240.56, Current = 27.70, Best = 27.01
[2025-12-29T16:56:41.587Z] [INFO] [Phase 2] Iteration 45500: Temp = 111554.73, Current = 27.67, Best = 27.01
[2025-12-29T16:57:00.704Z] [INFO] [Phase 2] Iteration 46500: Temp = 98642.58, Current = 27.61, Best = 27.01
[2025-12-29T16:57:09.214Z] [INFO] [Phase 2] Iteration 47000: Temp = 92656.28, Current = 27.57, Best = 27.01
[2025-12-29T16:57:35.523Z] [INFO] [Phase 2] Iteration 48500: Temp = 76897.87, Current = 27.49, Best = 27.01
[2025-12-29T16:57:43.645Z] [INFO] [Phase 2] Iteration 49000: Temp = 72202.29, Current = 27.75, Best = 27.01
[2025-12-29T16:58:17.333Z] [INFO] [Phase 2] Iteration 51000: Temp = 56308.58, Current = 27.71, Best = 27.01
[2025-12-29T16:58:25.783Z] [INFO] [Phase 2] Iteration 51500: Temp = 53050.33, Current = 27.72, Best = 27.01
[2025-12-29T16:58:34.043Z] [INFO] [Phase 2] Iteration 52000: Temp = 50000.60, Current = 27.58, Best = 27.01
[2025-12-29T16:58:59.995Z] [INFO] [Phase 2] Iteration 53500: Temp = 41455.33, Current = 27.71, Best = 27.01
[2025-12-29T16:59:08.125Z] [INFO] [Phase 2] Iteration 54000: Temp = 39001.90, Current = 27.60, Best = 27.01
[2025-12-29T16:59:17.342Z] [INFO] [Phase 2] Iteration 54500: Temp = 36723.04, Current = 27.42, Best = 27.01
[2025-12-29T16:59:25.096Z] [INFO] [Phase 2] Iteration 55000: Temp = 34695.10, Current = 27.40, Best = 27.01
[2025-12-29T16:59:59.307Z] [INFO] [Phase 2] Iteration 57000: Temp = 27128.20, Current = 27.64, Best = 27.01
[2025-12-29T17:00:07.698Z] [INFO] [Phase 2] Iteration 57500: Temp = 25497.18, Current = 27.69, Best = 27.01
[2025-12-29T17:00:15.806Z] [INFO] [Phase 2] Iteration 58000: Temp = 24017.00, Current = 27.73, Best = 27.01
[2025-12-29T17:00:32.141Z] [INFO] [Phase 2] Iteration 59000: Temp = 21254.09, Current = 27.58, Best = 27.01
[2025-12-29T17:00:40.741Z] [INFO] [Phase 2] Iteration 59500: Temp = 19996.22, Current = 27.62, Best = 27.01
[2025-12-29T17:00:50.890Z] [INFO] [Phase 2] Iteration 60000: Temp = 18543.81, Current = 27.66, Best = 27.01
[2025-12-29T17:00:50.902Z] [INFO] Optimization complete {"iterations":60000,"reheats":1,"finalTemperature":"18543.8072","fitness":"27.01","hardViolations":0,"softViolations":8}
[2025-12-29T17:00:50.902Z] [INFO] Operator Statistics:
[2025-12-29T17:00:50.902Z] [INFO]   Fix Friday Prayer Conflict: Attempts = 424, Improvements = 14, Accepted = 404, Success Rate = 3.30%
[2025-12-29T17:00:50.902Z] [INFO]   Swap Friday with Non-Friday: Attempts = 676, Improvements = 1, Accepted = 226, Success Rate = 0.15%
[2025-12-29T17:00:50.902Z] [INFO]   Fix Lecturer Conflict: Attempts = 920, Improvements = 72, Accepted = 372, Success Rate = 7.83%
[2025-12-29T17:00:50.902Z] [INFO]   Fix Room Conflict: Attempts = 560, Improvements = 2, Accepted = 560, Success Rate = 0.36%
[2025-12-29T17:00:50.902Z] [INFO]   Fix Max Daily Periods: Attempts = 62, Improvements = 7, Accepted = 62, Success Rate = 11.29%
[2025-12-29T17:00:50.902Z] [INFO]   Fix Room Capacity: Attempts = 0, Improvements = 0, Accepted = 0, Success Rate = 0.00%
[2025-12-29T17:00:50.902Z] [INFO]   Change Time Slot and Room: Attempts = 5342, Improvements = 638, Accepted = 4943, Success Rate = 11.94%
[2025-12-29T17:00:50.902Z] [INFO]   Change Time Slot: Attempts = 4232, Improvements = 237, Accepted = 3521, Success Rate = 5.60%
[2025-12-29T17:00:50.902Z] [INFO]   Change Room: Attempts = 8634, Improvements = 638, Accepted = 8634, Success Rate = 7.39%
[2025-12-29T17:00:50.902Z] [INFO]   Swap Classes: Attempts = 12625, Improvements = 91, Accepted = 672, Success Rate = 0.72%
======================================================================

✨ OPTIMIZATION COMPLETE!

Cache stats: {
  timeCache: {
    timeToMinutes: 20,
    minutesToTime: 17,
  },
  endTimeCache: 285,
  prayerOverlapCache: 285,
  totalEntries: 607,
}
📊 RESULTS:
   Final fitness: 27.01
   Hard constraint violations: 0
   Soft constraint violations: 8
   Total iterations: 60000
   Reheating events: 1
   Final temperature: 18543.8072
   Classes scheduled: 354/373

📈 OPERATOR STATISTICS:
   Fix Friday Prayer Conflict:
      Attempts: 424
      Improvements: 14
      Success rate: 3.30%
   Swap Friday with Non-Friday:
      Attempts: 676
      Improvements: 1
      Success rate: 0.15%
   Fix Lecturer Conflict:
      Attempts: 920
      Improvements: 72
      Success rate: 7.83%
   Fix Room Conflict:
      Attempts: 560
      Improvements: 2
      Success rate: 0.36%
   Fix Max Daily Periods:
      Attempts: 62
      Improvements: 7
      Success rate: 11.29%
   Fix Room Capacity:
      Attempts: 0
      Improvements: 0
      Success rate: 0.00%
   Change Time Slot and Room:
      Attempts: 5342
      Improvements: 638
      Success rate: 11.94%
   Change Time Slot:
      Attempts: 4232
      Improvements: 237
      Success rate: 5.60%
   Change Room:
      Attempts: 8634
      Improvements: 638
      Success rate: 7.39%
   Swap Classes:
      Attempts: 12625
      Improvements: 91
      Success rate: 0.72%

⚠️  VIOLATIONS (8):
   - [soft] Preferred Time: No description
   - [soft] Preferred Room: No description
   - [soft] Transit Time: No description
   - [soft] Compactness: No description
   - [soft] Prayer Time Overlap: No description
   - [soft] Evening Class Priority: No description
   - [soft] Research Day: No description
   - [soft] Overflow Penalty: No description

======================================================================
✅ Example completed successfully!
======================================================================

💾 Results saved to: timetable-result.json
```
# Trial 5
```bash
emmanuelabayor@ade:~/projects/timetable-sa$ bun run examples/timetabling/example-basic.ts
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
  ⚠️  Skipping MM23RS03: No lecturers on class Research Seminar
  ⚠️  Skipping GS13PW02: No lecturers on class Kerja Praktik
  ⚠️  Skipping AC135343: No lecturers on class Skripsi
  ⚠️  Skipping GS13PW02: No lecturers on class Kerja Praktik
  ⚠️  Skipping GS13TH46: No lecturers on class Skripsi
  ⚠️  Skipping GS13IP12: No lecturers on class Proyek Interdisipliner
  ⚠️  Skipping GS13PW02: No lecturers on class KERJA PRAKTIK
  ⚠️  Skipping GS13IP12: No lecturers on class PROYEK INTERDISIPLIN
  ⚠️  Skipping GS13CZ02: No lecturers on class Kewarganegaraan
  ⚠️  Skipping GS13IP12: No lecturers on class Proyek Interdisiplin
  ⚠️  Skipping CE11UT46: No lecturers on class Skripsi
  ⚠️  Skipping GS13PW02: No lecturers on class Praktik Kerja Lapang
  ⚠️  Skipping GS13CZ02: No lecturers on class Kewarganegaraan
  ⚠️  Could not place IF13RP12: Rekayasa Perangkat Lunak
  ⚠️  Skipping GS13PW02: No lecturers on class Kerja Praktik/Magang
  ⚠️  Skipping GS13CZ02: No lecturers on class Kewarganegaraan
  ⚠️  Skipping GS13IP12: No lecturers on class Proyek Interdisipliner
  ⚠️  Skipping VD13KP02: No lecturers on class Kerja Praktik
  ⚠️  Could not place VD13BS53: Perencanaan Bisnis

✅ Initial solution generated:
   Successfully placed: 354/373
   Failed to place: 19/373


⚖️  Setting up constraints...
   Hard constraints: 11
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
[2025-12-29T17:01:15.137Z] [INFO] Simulated Annealing initialized {"hardConstraints":11,"softConstraints":8,"moveGenerators":10,"config":{"initialTemperature":100000,"minTemperature":1e-7,"coolingRate":0.9998,"maxIterations":60000}}
[2025-12-29T17:01:15.137Z] [INFO] Starting optimization...
[2025-12-29T17:01:15.137Z] [INFO] Phase 1: Eliminating hard constraint violations
[2025-12-29T17:01:15.175Z] [INFO] Initial state {"fitness":"341935.71","hardViolations":29}
[2025-12-29T17:01:28.160Z] [INFO] [Phase 1] Iteration 1000: Temp = 92181.74, Hard violations = 12, Best = 12
[2025-12-29T17:01:41.755Z] [INFO] [Phase 1] Iteration 2000: Temp = 84872.81, Hard violations = 11, Best = 11
[2025-12-29T17:01:57.039Z] [INFO] [Phase 1] Iteration 3000: Temp = 77365.78, Hard violations = 10, Best = 10
[2025-12-29T17:02:05.432Z] [INFO] [Phase 1] Iteration 3500: Temp = 73401.12, Hard violations = 9, Best = 9
[2025-12-29T17:02:13.919Z] [INFO] [Phase 1] Iteration 4000: Temp = 69528.30, Hard violations = 8, Best = 8
[2025-12-29T17:02:22.462Z] [INFO] [Phase 1] Iteration 4500: Temp = 65912.53, Hard violations = 8, Best = 8
[2025-12-29T17:02:30.638Z] [INFO] [Phase 1] Iteration 5000: Temp = 62497.29, Hard violations = 8, Best = 8
[2025-12-29T17:02:39.485Z] [INFO] [Phase 1] Iteration 5500: Temp = 59081.48, Hard violations = 8, Best = 8
[2025-12-29T17:02:55.271Z] [INFO] [Phase 1] Iteration 6500: Temp = 53801.87, Hard violations = 8, Best = 8
[2025-12-29T17:03:08.599Z] [INFO] [Phase 1] Iteration 7500: Temp = 49437.03, Hard violations = 7, Best = 7
[2025-12-29T17:03:15.175Z] [INFO] [Phase 1] Iteration 8000: Temp = 47469.89, Hard violations = 7, Best = 7
[2025-12-29T17:03:21.988Z] [INFO] [Phase 1] Iteration 8500: Temp = 45562.80, Hard violations = 7, Best = 7
[2025-12-29T17:03:37.388Z] [INFO] [Phase 1] Iteration 9500: Temp = 41574.31, Hard violations = 7, Best = 7
[2025-12-29T17:03:44.037Z] [INFO] [Phase 1] Iteration 10000: Temp = 39784.52, Hard violations = 7, Best = 7
[2025-12-29T17:03:51.488Z] [INFO] [Phase 1] Iteration 10500: Temp = 37904.63, Hard violations = 5, Best = 5
[2025-12-29T17:04:10.454Z] [INFO] [Phase 1] Iteration 11500: Temp = 33989.86, Hard violations = 4, Best = 4
[2025-12-29T17:04:19.375Z] [INFO] [Phase 1] Iteration 12000: Temp = 32299.68, Hard violations = 4, Best = 4
[2025-12-29T17:04:29.264Z] [INFO] [Phase 1] Iteration 12500: Temp = 30497.70, Hard violations = 4, Best = 4
[2025-12-29T17:04:58.342Z] [INFO] [Phase 1] Iteration 14000: Temp = 25972.42, Hard violations = 3, Best = 3
[2025-12-29T17:05:22.996Z] [INFO] [Phase 1] Iteration 15000: Temp = 22323.06, Hard violations = 3, Best = 3
[2025-12-29T17:05:34.657Z] [INFO] [Phase 1] Iteration 15500: Temp = 20780.46, Hard violations = 3, Best = 3
[2025-12-29T17:05:59.521Z] [INFO] [Phase 1] Iteration 16500: Temp = 17896.37, Hard violations = 3, Best = 3
[2025-12-29T17:06:48.925Z] [INFO] [Phase 1] Iteration 18500: Temp = 13278.79, Hard violations = 3, Best = 3
[2025-12-29T17:07:00.859Z] [INFO] [Phase 1] Iteration 19000: Temp = 12331.55, Hard violations = 3, Best = 3
[2025-12-29T17:07:22.346Z] [INFO] [Phase 1] Iteration 20000: Temp = 10843.31, Hard violations = 3, Best = 3
[2025-12-29T17:07:37.747Z] [INFO] Phase 1 complete: Hard violations = 2
[2025-12-29T17:07:37.747Z] [INFO] Phase 1.5: Intensification - targeting remaining hard violations
[2025-12-29T17:07:37.747Z] [INFO] [Intensification] Attempt 1/3
[2025-12-29T17:07:54.994Z] [INFO] [Intensification] Iter 500: Hard violations = 2, Best = 2
[2025-12-29T17:08:10.812Z] [INFO] [Intensification] Iter 1000: Hard violations = 2, Best = 2
[2025-12-29T17:08:26.399Z] [INFO] [Intensification] Iter 1500: Hard violations = 2, Best = 2
[2025-12-29T17:08:42.524Z] [INFO] [Intensification] Iter 2000: Hard violations = 2, Best = 2
[2025-12-29T17:08:42.524Z] [INFO] [Intensification] Attempt 2/3
[2025-12-29T17:08:57.440Z] [INFO] [Intensification] Iter 500: Hard violations = 2, Best = 2
[2025-12-29T17:09:13.897Z] [INFO] [Intensification] Iter 1000: Hard violations = 2, Best = 2
[2025-12-29T17:09:28.642Z] [INFO] [Intensification] Iter 1500: Hard violations = 2, Best = 2
[2025-12-29T17:09:44.078Z] [INFO] [Intensification] Iter 2000: Hard violations = 2, Best = 2
[2025-12-29T17:09:44.078Z] [INFO] [Intensification] Attempt 3/3
[2025-12-29T17:10:00.449Z] [INFO] [Intensification] Iter 500: Hard violations = 2, Best = 2
[2025-12-29T17:10:17.171Z] [INFO] [Intensification] Iter 1000: Hard violations = 2, Best = 2
[2025-12-29T17:10:32.346Z] [INFO] [Intensification] Iter 1500: Hard violations = 1, Best = 1
[2025-12-29T17:10:46.794Z] [INFO] [Intensification] Iter 2000: Hard violations = 1, Best = 1
[2025-12-29T17:10:46.794Z] [WARN] [Intensification] Could not eliminate all hard violations. Remaining: 1
[2025-12-29T17:10:46.794Z] [INFO] Phase 2: Optimizing soft constraints
[2025-12-29T17:11:08.181Z] [INFO] [Phase 2] Iteration 28000: Temp = 8668.76, Current = 50027.35, Best = 50027.10
[2025-12-29T17:11:16.976Z] [INFO] [Phase 2] Iteration 28500: Temp = 8142.68, Current = 50027.41, Best = 50027.10
[2025-12-29T17:11:26.097Z] [INFO] [Phase 2] Iteration 29000: Temp = 7673.04, Current = 50027.34, Best = 50027.10
[2025-12-29T17:12:23.669Z] [INFO] [Phase 2] Iteration 32500: Temp = 5063.57, Current = 27.45, Best = 27.18
[2025-12-29T17:12:32.143Z] [INFO] [Phase 2] Iteration 33000: Temp = 4778.21, Current = 27.23, Best = 27.18
[2025-12-29T17:12:40.129Z] [INFO] [Phase 2] Iteration 33500: Temp = 4494.52, Current = 27.12, Best = 27.05
[2025-12-29T17:12:47.590Z] [INFO] [Phase 2] Iteration 34000: Temp = 4236.15, Current = 27.22, Best = 27.05
[2025-12-29T17:13:04.607Z] [INFO] [Phase 2] Iteration 35000: Temp = 3743.58, Current = 27.37, Best = 27.05
[2025-12-29T17:13:13.046Z] [INFO] [Phase 2] Iteration 35500: Temp = 3512.88, Current = 27.36, Best = 27.05
[2025-12-29T17:13:21.096Z] [INFO] [Phase 2] Iteration 36000: Temp = 3284.55, Current = 27.28, Best = 27.05
[2025-12-29T17:13:29.863Z] [INFO] [Phase 2] Iteration 36500: Temp = 3073.52, Current = 27.22, Best = 27.05
[2025-12-29T17:13:38.875Z] [INFO] [Phase 2] Iteration 37000: Temp = 2893.35, Current = 27.22, Best = 27.05
[2025-12-29T17:13:55.078Z] [INFO] [Phase 2] Iteration 38000: Temp = 2550.28, Current = 27.20, Best = 27.05
[2025-12-29T17:14:11.311Z] [INFO] [Phase 2] Iteration 39000: Temp = 2254.19, Current = 27.19, Best = 27.05
[2025-12-29T17:14:36.693Z] [INFO] [Phase 2] Iteration 40500: Temp = 1877.18, Current = 27.24, Best = 27.05
[2025-12-29T17:14:44.397Z] [INFO] [Phase 2] Iteration 41000: Temp = 1767.50, Current = 27.36, Best = 27.05
[2025-12-29T17:14:51.872Z] [INFO] [Phase 2] Iteration 41500: Temp = 1675.25, Current = 27.38, Best = 27.05
[2025-12-29T17:14:59.520Z] [INFO] [Phase 2] Iteration 42000: Temp = 1581.47, Current = 27.36, Best = 27.05
[2025-12-29T17:15:07.582Z] [INFO] [Phase 2] Iteration 42500: Temp = 1490.26, Current = 27.40, Best = 27.05
[2025-12-29T17:15:16.886Z] [INFO] [Phase 2] Iteration 43000: Temp = 1400.94, Current = 27.21, Best = 27.05
[2025-12-29T17:15:25.568Z] [INFO] [Phase 2] Iteration 43500: Temp = 1312.24, Current = 27.31, Best = 27.05
[2025-12-29T17:15:32.931Z] [INFO] [Phase 2] Iteration 44000: Temp = 1236.56, Current = 27.34, Best = 27.05
[2025-12-29T17:15:40.179Z] [INFO] [Phase 2] Iteration 44500: Temp = 1168.97, Current = 27.34, Best = 27.05
[2025-12-29T17:15:57.366Z] [INFO] [Phase 2] Iteration 45500: Temp = 1034.91, Current = 27.22, Best = 27.05
[2025-12-29T17:16:01.631Z] [INFO] [Phase 2] Reheating #1: Temperature = 149986.45, Fitness = 27.05
[2025-12-29T17:16:13.843Z] [INFO] [Phase 2] Iteration 46500: Temp = 136392.32, Current = 27.39, Best = 27.05
[2025-12-29T17:16:22.308Z] [INFO] [Phase 2] Iteration 47000: Temp = 127935.86, Current = 27.51, Best = 27.05
[2025-12-29T17:16:30.295Z] [INFO] [Phase 2] Iteration 47500: Temp = 120605.29, Current = 27.50, Best = 27.05
[2025-12-29T17:16:38.972Z] [INFO] [Phase 2] Iteration 48000: Temp = 114241.85, Current = 27.65, Best = 27.05
[2025-12-29T17:16:54.087Z] [INFO] [Phase 2] Iteration 49000: Temp = 101870.89, Current = 27.77, Best = 27.05
[2025-12-29T17:17:02.054Z] [INFO] [Phase 2] Iteration 49500: Temp = 95822.75, Current = 27.67, Best = 27.05
[2025-12-29T17:17:27.977Z] [INFO] [Phase 2] Iteration 51000: Temp = 79192.46, Current = 27.73, Best = 27.05
[2025-12-29T17:17:36.422Z] [INFO] [Phase 2] Iteration 51500: Temp = 74237.89, Current = 27.66, Best = 27.05
[2025-12-29T17:17:44.704Z] [INFO] [Phase 2] Iteration 52000: Temp = 69482.02, Current = 27.70, Best = 27.05
[2025-12-29T17:18:41.778Z] [INFO] [Phase 2] Iteration 55500: Temp = 45733.28, Current = 27.72, Best = 27.05
[2025-12-29T17:19:06.909Z] [INFO] [Phase 2] Iteration 57000: Temp = 37705.53, Current = 27.67, Best = 27.05
[2025-12-29T17:19:33.249Z] [INFO] [Phase 2] Iteration 58500: Temp = 31292.81, Current = 27.73, Best = 27.05
[2025-12-29T17:19:49.328Z] [INFO] [Phase 2] Iteration 59500: Temp = 27648.62, Current = 27.68, Best = 27.05
[2025-12-29T17:19:59.154Z] [INFO] [Phase 2] Iteration 60000: Temp = 25918.82, Current = 27.64, Best = 27.05
[2025-12-29T17:19:59.165Z] [INFO] Optimization complete {"iterations":60000,"reheats":1,"finalTemperature":"25918.8208","fitness":"27.05","hardViolations":0,"softViolations":8}
[2025-12-29T17:19:59.165Z] [INFO] Operator Statistics:
[2025-12-29T17:19:59.165Z] [INFO]   Fix Friday Prayer Conflict: Attempts = 452, Improvements = 18, Accepted = 367, Success Rate = 3.98%
[2025-12-29T17:19:59.165Z] [INFO]   Swap Friday with Non-Friday: Attempts = 560, Improvements = 0, Accepted = 255, Success Rate = 0.00%
[2025-12-29T17:19:59.165Z] [INFO]   Fix Lecturer Conflict: Attempts = 3908, Improvements = 223, Accepted = 3695, Success Rate = 5.71%
[2025-12-29T17:19:59.165Z] [INFO]   Fix Room Conflict: Attempts = 46, Improvements = 1, Accepted = 46, Success Rate = 2.17%
[2025-12-29T17:19:59.165Z] [INFO]   Fix Max Daily Periods: Attempts = 30, Improvements = 7, Accepted = 30, Success Rate = 23.33%
[2025-12-29T17:19:59.165Z] [INFO]   Fix Room Capacity: Attempts = 0, Improvements = 0, Accepted = 0, Success Rate = 0.00%
[2025-12-29T17:19:59.165Z] [INFO]   Change Time Slot and Room: Attempts = 5177, Improvements = 618, Accepted = 4894, Success Rate = 11.94%
[2025-12-29T17:19:59.165Z] [INFO]   Change Time Slot: Attempts = 4152, Improvements = 246, Accepted = 3560, Success Rate = 5.92%
[2025-12-29T17:19:59.165Z] [INFO]   Change Room: Attempts = 8278, Improvements = 613, Accepted = 8278, Success Rate = 7.41%
[2025-12-29T17:19:59.165Z] [INFO]   Swap Classes: Attempts = 15198, Improvements = 143, Accepted = 867, Success Rate = 0.94%
======================================================================

✨ OPTIMIZATION COMPLETE!

Cache stats: {
  timeCache: {
    timeToMinutes: 20,
    minutesToTime: 17,
  },
  endTimeCache: 285,
  prayerOverlapCache: 285,
  totalEntries: 607,
}
📊 RESULTS:
   Final fitness: 27.05
   Hard constraint violations: 0
   Soft constraint violations: 8
   Total iterations: 60000
   Reheating events: 1
   Final temperature: 25918.8208
   Classes scheduled: 354/373

📈 OPERATOR STATISTICS:
   Fix Friday Prayer Conflict:
      Attempts: 452
      Improvements: 18
      Success rate: 3.98%
   Swap Friday with Non-Friday:
      Attempts: 560
      Improvements: 0
      Success rate: 0.00%
   Fix Lecturer Conflict:
      Attempts: 3908
      Improvements: 223
      Success rate: 5.71%
   Fix Room Conflict:
      Attempts: 46
      Improvements: 1
      Success rate: 2.17%
   Fix Max Daily Periods:
      Attempts: 30
      Improvements: 7
      Success rate: 23.33%
   Fix Room Capacity:
      Attempts: 0
      Improvements: 0
      Success rate: 0.00%
   Change Time Slot and Room:
      Attempts: 5177
      Improvements: 618
      Success rate: 11.94%
   Change Time Slot:
      Attempts: 4152
      Improvements: 246
      Success rate: 5.92%
   Change Room:
      Attempts: 8278
      Improvements: 613
      Success rate: 7.41%
   Swap Classes:
      Attempts: 15198
      Improvements: 143
      Success rate: 0.94%

⚠️  VIOLATIONS (8):
   - [soft] Preferred Time: No description
   - [soft] Preferred Room: No description
   - [soft] Transit Time: No description
   - [soft] Compactness: No description
   - [soft] Prayer Time Overlap: No description
   - [soft] Evening Class Priority: No description
   - [soft] Research Day: No description
   - [soft] Overflow Penalty: No description

======================================================================
✅ Example completed successfully!
======================================================================

💾 Results saved to: timetable-result.json
```