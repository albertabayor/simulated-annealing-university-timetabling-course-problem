# Explanation
i run the algorithm 5 times at the same time, it might be could be fast if i only run one at a time, because cpu is used 100% more by this algorithm.
here i resume what the result is

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
  ⚠️  Skipping GS13CZ02: No lecturers on class Kewarganegaraan
  ⚠️  Skipping GS13PW02: No lecturers on class Kerja Praktik
  ⚠️  Skipping MM23RS03: No lecturers on class Research Seminar
  ⚠️  Skipping GS13PW02: No lecturers on class KERJA PRAKTIK
  ⚠️  Skipping GS13IP12: No lecturers on class PROYEK INTERDISIPLIN
  ⚠️  Skipping GS13PW02: No lecturers on class Kerja Praktik/Magang
  ⚠️  Skipping GS13TH46: No lecturers on class Skripsi
  ⚠️  Skipping GS13IP12: No lecturers on class Proyek Interdisipliner
  ⚠️  Skipping GS13CZ02: No lecturers on class Kewarganegaraan
  ⚠️  Skipping GS13IP12: No lecturers on class Proyek Interdisipliner
  ⚠️  Skipping VD13KP02: No lecturers on class Kerja Praktik
  ⚠️  Skipping GS13PW02: No lecturers on class Kerja Praktik
  ⚠️  Skipping GS13IP12: No lecturers on class Proyek Interdisiplin
  ⚠️  Skipping GS13PW02: No lecturers on class Praktik Kerja Lapang
  ⚠️  Skipping AC135343: No lecturers on class Skripsi
  ⚠️  Skipping GS13CZ02: No lecturers on class Kewarganegaraan
  ⚠️  Skipping CE11UT46: No lecturers on class Skripsi

✅ Initial solution generated:
   Successfully placed: 356/373
   Failed to place: 17/373


⚖️  Setting up constraints...
   Hard constraints: 11
   Soft constraints: 8

🔄 Setting up move operators...
   Targeted operators: 5 (FixFridayPrayerConflict, FixLecturerConflict, etc.)
   General operators: 4 (including high-success ChangeTimeSlotAndRoom)
   Total operators: 9

⚙️  Configuring Simulated Annealing...
   Initial temperature: 100000
   Cooling rate: 0.9998
   Max iterations: 60000

🚀 Starting optimization...

======================================================================
[2025-12-29T18:35:14.247Z] [INFO] Simulated Annealing initialized {"hardConstraints":11,"softConstraints":8,"moveGenerators":9,"config":{"initialTemperature":100000,"minTemperature":1e-7,"coolingRate":0.9998,"maxIterations":60000}}
[2025-12-29T18:35:14.248Z] [INFO] Starting optimization...
[2025-12-29T18:35:14.248Z] [INFO] Phase 1: Eliminating hard constraint violations
[2025-12-29T18:35:14.285Z] [INFO] Initial state {"fitness":"165934.65","hardViolations":13}
[2025-12-29T18:35:47.297Z] [INFO] Phase 1 complete: Hard violations = 0
[2025-12-29T18:35:47.297Z] [INFO] Phase 2: Optimizing soft constraints
^[[H[2025-12-29T18:36:11.654Z] [INFO] [Phase 2] Iteration 3000: Temp = 71488.50, Current = 26.88, Best = 26.86
[2025-12-29T18:36:22.141Z] [INFO] [Phase 2] Iteration 3500: Temp = 67432.75, Current = 26.91, Best = 26.84
[2025-12-29T18:37:01.489Z] [INFO] [Phase 2] Iteration 5500: Temp = 54017.53, Current = 27.23, Best = 26.77
[2025-12-29T18:37:12.437Z] [INFO] [Phase 2] Iteration 6000: Temp = 50668.39, Current = 27.16, Best = 26.77
[2025-12-29T18:37:25.020Z] [INFO] [Phase 2] Iteration 6500: Temp = 47641.11, Current = 27.28, Best = 26.77
[2025-12-29T18:37:45.542Z] [INFO] [Phase 2] Iteration 7500: Temp = 42321.03, Current = 27.20, Best = 26.77
[2025-12-29T18:38:20.466Z] [INFO] [Phase 2] Iteration 9000: Temp = 35419.64, Current = 27.12, Best = 26.77
[2025-12-29T18:38:31.736Z] [INFO] [Phase 2] Iteration 9500: Temp = 33416.86, Current = 27.00, Best = 26.77
[2025-12-29T18:38:42.000Z] [INFO] [Phase 2] Iteration 10000: Temp = 31401.46, Current = 26.95, Best = 26.77
[2025-12-29T18:38:52.044Z] [INFO] [Phase 2] Iteration 10500: Temp = 29673.33, Current = 27.09, Best = 26.77
[2025-12-29T18:39:04.468Z] [INFO] [Phase 2] Iteration 11000: Temp = 27917.19, Current = 27.09, Best = 26.77
[2025-12-29T18:39:38.543Z] [INFO] [Phase 2] Iteration 12500: Temp = 23146.04, Current = 26.94, Best = 26.77
[2025-12-29T18:40:46.508Z] [INFO] [Phase 2] Iteration 15500: Temp = 16391.93, Current = 26.98, Best = 26.77
[2025-12-29T18:41:08.073Z] [INFO] [Phase 2] Iteration 16500: Temp = 14546.89, Current = 26.98, Best = 26.77
[2025-12-29T18:41:51.412Z] [INFO] [Phase 2] Iteration 18500: Temp = 11624.97, Current = 26.94, Best = 26.77
[2025-12-29T18:42:12.840Z] [INFO] [Phase 2] Iteration 19500: Temp = 10337.14, Current = 27.22, Best = 26.77
[2025-12-29T18:42:23.654Z] [INFO] [Phase 2] Iteration 20000: Temp = 9783.90, Current = 27.18, Best = 26.77
[2025-12-29T18:42:33.219Z] [INFO] [Phase 2] Iteration 20500: Temp = 9256.56, Current = 27.24, Best = 26.77
[2025-12-29T18:42:43.488Z] [INFO] [Phase 2] Iteration 21000: Temp = 8706.99, Current = 27.21, Best = 26.77
[2025-12-29T18:42:53.538Z] [INFO] [Phase 2] Iteration 21500: Temp = 8219.59, Current = 27.19, Best = 26.77
[2025-12-29T18:43:04.956Z] [INFO] [Phase 2] Iteration 22000: Temp = 7756.37, Current = 27.18, Best = 26.77
[2025-12-29T18:43:14.448Z] [INFO] [Phase 2] Iteration 22500: Temp = 7338.31, Current = 27.19, Best = 26.77
[2025-12-29T18:43:36.760Z] [INFO] [Phase 2] Iteration 23500: Temp = 6494.12, Current = 27.31, Best = 26.77
[2025-12-29T18:43:55.744Z] [INFO] [Phase 2] Iteration 24500: Temp = 5812.94, Current = 27.44, Best = 26.77
[2025-12-29T18:44:07.030Z] [INFO] [Phase 2] Iteration 25000: Temp = 5487.54, Current = 27.33, Best = 26.77
[2025-12-29T18:44:36.088Z] [INFO] [Phase 2] Iteration 26500: Temp = 4617.54, Current = 27.28, Best = 26.77
[2025-12-29T18:44:57.470Z] [INFO] [Phase 2] Iteration 27500: Temp = 4101.90, Current = 27.48, Best = 26.77
[2025-12-29T18:45:06.881Z] [INFO] [Phase 2] Iteration 28000: Temp = 3887.03, Current = 27.32, Best = 26.77
[2025-12-29T18:45:28.149Z] [INFO] [Phase 2] Iteration 29000: Temp = 3470.97, Current = 27.36, Best = 26.77
[2025-12-29T18:45:37.236Z] [INFO] [Phase 2] Iteration 29500: Temp = 3285.20, Current = 27.34, Best = 26.77
[2025-12-29T18:45:47.423Z] [INFO] [Phase 2] Iteration 30000: Temp = 3116.85, Current = 27.33, Best = 26.77
[2025-12-29T18:45:57.064Z] [INFO] [Phase 2] Iteration 30500: Temp = 2947.68, Current = 27.42, Best = 26.77
[2025-12-29T18:46:15.712Z] [INFO] [Phase 2] Iteration 31500: Temp = 2642.72, Current = 27.29, Best = 26.77
[2025-12-29T18:46:36.281Z] [INFO] [Phase 2] Iteration 32500: Temp = 2368.36, Current = 27.28, Best = 26.77
[2025-12-29T18:46:46.050Z] [INFO] [Phase 2] Iteration 33000: Temp = 2237.57, Current = 27.24, Best = 26.77
[2025-12-29T18:46:57.745Z] [INFO] [Phase 2] Iteration 33500: Temp = 2103.46, Current = 27.31, Best = 26.77
[2025-12-29T18:47:07.540Z] [INFO] [Phase 2] Iteration 34000: Temp = 1979.37, Current = 27.34, Best = 26.77
[2025-12-29T18:47:29.492Z] [INFO] [Phase 2] Iteration 35000: Temp = 1752.71, Current = 27.22, Best = 26.77
[2025-12-29T18:47:49.948Z] [INFO] [Phase 2] Iteration 36000: Temp = 1548.91, Current = 27.26, Best = 26.77
[2025-12-29T18:48:03.283Z] [INFO] [Phase 2] Iteration 36500: Temp = 1447.37, Current = 27.21, Best = 26.77
[2025-12-29T18:48:13.552Z] [INFO] [Phase 2] Iteration 37000: Temp = 1364.44, Current = 27.17, Best = 26.77
[2025-12-29T18:48:23.350Z] [INFO] [Phase 2] Iteration 37500: Temp = 1290.64, Current = 27.31, Best = 26.77
[2025-12-29T18:49:04.558Z] [INFO] [Phase 2] Iteration 39500: Temp = 1023.38, Current = 27.41, Best = 26.77
[2025-12-29T18:49:08.792Z] [INFO] [Phase 2] Reheating #1: Temperature = 149986.45, Fitness = 26.77
[2025-12-29T18:49:16.785Z] [INFO] [Phase 2] Iteration 40000: Temp = 144537.83, Current = 27.11, Best = 26.77
[2025-12-29T18:49:26.435Z] [INFO] [Phase 2] Iteration 40500: Temp = 136528.79, Current = 27.13, Best = 26.77
[2025-12-29T18:49:36.940Z] [INFO] [Phase 2] Iteration 41000: Temp = 128217.66, Current = 27.15, Best = 26.77
[2025-12-29T18:49:57.267Z] [INFO] [Phase 2] Iteration 42000: Temp = 113354.14, Current = 27.18, Best = 26.77
[2025-12-29T18:50:07.523Z] [INFO] [Phase 2] Iteration 42500: Temp = 106581.59, Current = 27.26, Best = 26.77
[2025-12-29T18:50:18.574Z] [INFO] [Phase 2] Iteration 43000: Temp = 100193.63, Current = 27.36, Best = 26.77
[2025-12-29T18:50:29.829Z] [INFO] [Phase 2] Iteration 43500: Temp = 94075.56, Current = 27.56, Best = 26.77
[2025-12-29T18:51:01.755Z] [INFO] [Phase 2] Iteration 45000: Temp = 78577.10, Current = 27.73, Best = 26.77
[2025-12-29T18:51:22.772Z] [INFO] [Phase 2] Iteration 46000: Temp = 69872.25, Current = 27.71, Best = 26.77
[2025-12-29T18:51:32.633Z] [INFO] [Phase 2] Iteration 46500: Temp = 65815.97, Current = 27.70, Best = 26.77
[2025-12-29T18:52:18.155Z] [INFO] [Phase 2] Iteration 48500: Temp = 51585.38, Current = 27.68, Best = 26.77
[2025-12-29T18:52:52.684Z] [INFO] [Phase 2] Iteration 50000: Temp = 42863.46, Current = 27.67, Best = 26.77
[2025-12-29T18:53:03.264Z] [INFO] [Phase 2] Iteration 50500: Temp = 40246.11, Current = 27.63, Best = 26.77
[2025-12-29T18:53:14.616Z] [INFO] [Phase 2] Iteration 51000: Temp = 38008.42, Current = 27.55, Best = 26.77
[2025-12-29T18:53:35.542Z] [INFO] [Phase 2] Iteration 52000: Temp = 33474.87, Current = 27.66, Best = 26.77
[2025-12-29T18:53:57.367Z] [INFO] [Phase 2] Iteration 53000: Temp = 29541.10, Current = 27.51, Best = 26.77
[2025-12-29T18:54:07.704Z] [INFO] [Phase 2] Iteration 53500: Temp = 27898.61, Current = 27.57, Best = 26.77
[2025-12-29T18:54:19.977Z] [INFO] [Phase 2] Iteration 54000: Temp = 26179.34, Current = 27.55, Best = 26.77
[2025-12-29T18:55:03.146Z] [INFO] [Phase 2] Iteration 56000: Temp = 20457.42, Current = 27.25, Best = 26.77
[2025-12-29T18:55:14.077Z] [INFO] [Phase 2] Iteration 56500: Temp = 19192.88, Current = 27.36, Best = 26.77
[2025-12-29T18:55:35.977Z] [INFO] [Phase 2] Iteration 57500: Temp = 17076.92, Current = 27.25, Best = 26.77
[2025-12-29T18:55:57.447Z] [INFO] [Phase 2] Iteration 58500: Temp = 15115.42, Current = 27.21, Best = 26.77
[2025-12-29T18:56:29.113Z] [INFO] [Phase 2] Iteration 60000: Temp = 12625.23, Current = 27.18, Best = 26.77
[2025-12-29T18:56:29.126Z] [INFO] Optimization complete {"iterations":60000,"reheats":1,"finalTemperature":"12625.2332","fitness":"26.77","hardViolations":0,"softViolations":8}
[2025-12-29T18:56:29.127Z] [INFO] Operator Statistics:
[2025-12-29T18:56:29.127Z] [INFO]   Fix Friday Prayer Conflict: Attempts = 0, Improvements = 0, Accepted = 0, Success Rate = 0.00%
[2025-12-29T18:56:29.127Z] [INFO]   Fix Lecturer Conflict: Attempts = 0, Improvements = 0, Accepted = 0, Success Rate = 0.00%
[2025-12-29T18:56:29.127Z] [INFO]   Fix Room Conflict: Attempts = 0, Improvements = 0, Accepted = 0, Success Rate = 0.00%
[2025-12-29T18:56:29.127Z] [INFO]   Fix Max Daily Periods: Attempts = 48, Improvements = 9, Accepted = 48, Success Rate = 18.75%
[2025-12-29T18:56:29.127Z] [INFO]   Fix Room Capacity: Attempts = 0, Improvements = 0, Accepted = 0, Success Rate = 0.00%
[2025-12-29T18:56:29.127Z] [INFO]   Change Time Slot and Room: Attempts = 6187, Improvements = 652, Accepted = 5719, Success Rate = 10.54%
[2025-12-29T18:56:29.127Z] [INFO]   Change Time Slot: Attempts = 4934, Improvements = 293, Accepted = 4134, Success Rate = 5.94%
[2025-12-29T18:56:29.127Z] [INFO]   Change Room: Attempts = 9631, Improvements = 723, Accepted = 9631, Success Rate = 7.51%
[2025-12-29T18:56:29.127Z] [INFO]   Swap Classes: Attempts = 14597, Improvements = 120, Accepted = 732, Success Rate = 0.82%
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
   Final fitness: 26.77
   Hard constraint violations: 0
   Soft constraint violations: 8
   Total iterations: 60000
   Reheating events: 1
   Final temperature: 12625.2332
   Classes scheduled: 356/373

📈 OPERATOR STATISTICS:
   Fix Friday Prayer Conflict:
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
      Attempts: 48
      Improvements: 9
      Success rate: 18.75%
   Fix Room Capacity:
      Attempts: 0
      Improvements: 0
      Success rate: 0.00%
   Change Time Slot and Room:
      Attempts: 6187
      Improvements: 652
      Success rate: 10.54%
   Change Time Slot:
      Attempts: 4934
      Improvements: 293
      Success rate: 5.94%
   Change Room:
      Attempts: 9631
      Improvements: 723
      Success rate: 7.51%
   Swap Classes:
      Attempts: 14597
      Improvements: 120
      Success rate: 0.82%

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
   🔀 Randomization enabled - shuffling class order
  ⚠️  Skipping GS13PW02: No lecturers on class KERJA PRAKTIK
  ⚠️  Skipping AC135343: No lecturers on class Skripsi
  ⚠️  Skipping GS13CZ02: No lecturers on class Kewarganegaraan
  ⚠️  Skipping GS13TH46: No lecturers on class Skripsi
  ⚠️  Skipping GS13CZ02: No lecturers on class Kewarganegaraan
  ⚠️  Skipping VD13KP02: No lecturers on class Kerja Praktik
  ⚠️  Skipping GS13PW02: No lecturers on class Kerja Praktik
  ⚠️  Skipping GS13CZ02: No lecturers on class Kewarganegaraan
  ⚠️  Skipping GS13IP12: No lecturers on class Proyek Interdisiplin
  ⚠️  Skipping GS13IP12: No lecturers on class Proyek Interdisipliner
  ⚠️  Skipping GS13IP12: No lecturers on class Proyek Interdisipliner
  ⚠️  Skipping CE11UT46: No lecturers on class Skripsi
  ⚠️  Skipping GS13PW02: No lecturers on class Kerja Praktik/Magang
  ⚠️  Skipping GS13PW02: No lecturers on class Praktik Kerja Lapang
  ⚠️  Skipping GS13PW02: No lecturers on class Kerja Praktik
  ⚠️  Skipping GS13IP12: No lecturers on class PROYEK INTERDISIPLIN
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
   Total operators: 9

⚙️  Configuring Simulated Annealing...
   Initial temperature: 100000
   Cooling rate: 0.9998
   Max iterations: 60000

🚀 Starting optimization...

======================================================================
[2025-12-29T18:35:29.172Z] [INFO] Simulated Annealing initialized {"hardConstraints":11,"softConstraints":8,"moveGenerators":9,"config":{"initialTemperature":100000,"minTemperature":1e-7,"coolingRate":0.9998,"maxIterations":60000}}
[2025-12-29T18:35:29.172Z] [INFO] Starting optimization...
[2025-12-29T18:35:29.172Z] [INFO] Phase 1: Eliminating hard constraint violations
[2025-12-29T18:35:29.211Z] [INFO] Initial state {"fitness":"163913.88","hardViolations":11}
[2025-12-29T18:35:54.970Z] [INFO] Phase 1 complete: Hard violations = 0
[2025-12-29T18:35:54.970Z] [INFO] Phase 2: Optimizing soft constraints
[2025-12-29T18:36:00.513Z] [INFO] [Phase 2] Iteration 1500: Temp = 82893.07, Current = 26.49, Best = 26.36
[2025-12-29T18:36:13.724Z] [INFO] [Phase 2] Iteration 2000: Temp = 77738.06, Current = 26.64, Best = 26.36
[2025-12-29T18:36:34.643Z] [INFO] [Phase 2] Iteration 3000: Temp = 68534.17, Current = 26.58, Best = 26.36
[2025-12-29T18:37:06.531Z] [INFO] [Phase 2] Iteration 4500: Temp = 57232.07, Current = 26.58, Best = 26.36
[2025-12-29T18:38:13.422Z] [INFO] [Phase 2] Iteration 7500: Temp = 40555.85, Current = 26.73, Best = 26.36
[2025-12-29T18:38:25.572Z] [INFO] [Phase 2] Iteration 8000: Temp = 38155.65, Current = 27.00, Best = 26.36
[2025-12-29T18:38:34.735Z] [INFO] [Phase 2] Iteration 8500: Temp = 36142.46, Current = 26.88, Best = 26.36
[2025-12-29T18:38:45.472Z] [INFO] [Phase 2] Iteration 9000: Temp = 33942.30, Current = 26.80, Best = 26.36
[2025-12-29T18:38:55.906Z] [INFO] [Phase 2] Iteration 9500: Temp = 31952.68, Current = 26.95, Best = 26.36
[2025-12-29T18:39:07.689Z] [INFO] [Phase 2] Iteration 10000: Temp = 30206.30, Current = 26.95, Best = 26.36
[2025-12-29T18:39:17.587Z] [INFO] [Phase 2] Iteration 10500: Temp = 28538.24, Current = 26.98, Best = 26.36
[2025-12-29T18:39:27.838Z] [INFO] [Phase 2] Iteration 11000: Temp = 26967.68, Current = 26.75, Best = 26.36
[2025-12-29T18:39:40.066Z] [INFO] [Phase 2] Iteration 11500: Temp = 25397.05, Current = 26.85, Best = 26.36
[2025-12-29T18:39:50.161Z] [INFO] [Phase 2] Iteration 12000: Temp = 23870.11, Current = 26.76, Best = 26.36
[2025-12-29T18:40:02.351Z] [INFO] [Phase 2] Iteration 12500: Temp = 22331.99, Current = 26.84, Best = 26.36
[2025-12-29T18:40:15.291Z] [INFO] [Phase 2] Iteration 13000: Temp = 21001.93, Current = 27.05, Best = 26.36
[2025-12-29T18:40:26.624Z] [INFO] [Phase 2] Iteration 13500: Temp = 19735.28, Current = 27.09, Best = 26.36
[2025-12-29T18:40:41.540Z] [INFO] [Phase 2] Iteration 14000: Temp = 18456.22, Current = 27.06, Best = 26.36
[2025-12-29T18:40:53.346Z] [INFO] [Phase 2] Iteration 14500: Temp = 17409.14, Current = 27.05, Best = 26.36
[2025-12-29T18:41:25.430Z] [INFO] [Phase 2] Iteration 16000: Temp = 14581.85, Current = 27.36, Best = 26.36
[2025-12-29T18:41:36.061Z] [INFO] [Phase 2] Iteration 16500: Temp = 13680.50, Current = 27.31, Best = 26.36
[2025-12-29T18:42:00.676Z] [INFO] [Phase 2] Iteration 17500: Temp = 12135.79, Current = 27.22, Best = 26.36
[2025-12-29T18:42:35.399Z] [INFO] [Phase 2] Iteration 19000: Temp = 9969.59, Current = 27.28, Best = 26.36
[2025-12-29T18:42:54.822Z] [INFO] [Phase 2] Iteration 20000: Temp = 8898.91, Current = 27.34, Best = 26.36
[2025-12-29T18:43:28.003Z] [INFO] [Phase 2] Iteration 21500: Temp = 7372.15, Current = 27.16, Best = 26.36
[2025-12-29T18:43:39.930Z] [INFO] [Phase 2] Iteration 22000: Temp = 6924.76, Current = 27.18, Best = 26.36
[2025-12-29T18:44:00.616Z] [INFO] [Phase 2] Iteration 23000: Temp = 6120.79, Current = 27.18, Best = 26.36
[2025-12-29T18:44:21.993Z] [INFO] [Phase 2] Iteration 24000: Temp = 5441.63, Current = 27.19, Best = 26.36
[2025-12-29T18:44:42.874Z] [INFO] [Phase 2] Iteration 25000: Temp = 4833.00, Current = 27.13, Best = 26.36
[2025-12-29T18:45:02.366Z] [INFO] [Phase 2] Iteration 26000: Temp = 4312.23, Current = 27.29, Best = 26.36
[2025-12-29T18:45:43.533Z] [INFO] [Phase 2] Iteration 28000: Temp = 3396.79, Current = 27.20, Best = 26.36
[2025-12-29T18:46:04.409Z] [INFO] [Phase 2] Iteration 29000: Temp = 3028.36, Current = 27.11, Best = 26.36
[2025-12-29T18:46:14.240Z] [INFO] [Phase 2] Iteration 29500: Temp = 2855.98, Current = 27.15, Best = 26.36
[2025-12-29T18:46:25.746Z] [INFO] [Phase 2] Iteration 30000: Temp = 2691.80, Current = 27.19, Best = 26.36
[2025-12-29T18:46:46.055Z] [INFO] [Phase 2] Iteration 31000: Temp = 2392.16, Current = 27.18, Best = 26.36
[2025-12-29T18:47:26.301Z] [INFO] [Phase 2] Iteration 33000: Temp = 1902.89, Current = 27.22, Best = 26.36
[2025-12-29T18:47:37.314Z] [INFO] [Phase 2] Iteration 33500: Temp = 1799.61, Current = 27.04, Best = 26.36
[2025-12-29T18:47:47.266Z] [INFO] [Phase 2] Iteration 34000: Temp = 1695.81, Current = 27.15, Best = 26.36
[2025-12-29T18:48:11.449Z] [INFO] [Phase 2] Iteration 35000: Temp = 1493.54, Current = 27.22, Best = 26.36
[2025-12-29T18:48:21.494Z] [INFO] [Phase 2] Iteration 35500: Temp = 1409.37, Current = 27.16, Best = 26.36
[2025-12-29T18:48:31.322Z] [INFO] [Phase 2] Iteration 36000: Temp = 1331.28, Current = 27.14, Best = 26.36
[2025-12-29T18:48:43.068Z] [INFO] [Phase 2] Iteration 36500: Temp = 1250.24, Current = 27.11, Best = 26.36
[2025-12-29T18:48:54.251Z] [INFO] [Phase 2] Iteration 37000: Temp = 1167.10, Current = 27.14, Best = 26.36
[2025-12-29T18:49:04.862Z] [INFO] [Phase 2] Iteration 37500: Temp = 1095.84, Current = 27.21, Best = 26.36
[2025-12-29T18:49:22.476Z] [INFO] [Phase 2] Reheating #1: Temperature = 149986.45, Fitness = 26.36
[2025-12-29T18:49:26.904Z] [INFO] [Phase 2] Iteration 38500: Temp = 145757.18, Current = 27.31, Best = 26.36
[2025-12-29T18:49:47.793Z] [INFO] [Phase 2] Iteration 39500: Temp = 128422.99, Current = 27.26, Best = 26.36
[2025-12-29T18:49:58.239Z] [INFO] [Phase 2] Iteration 40000: Temp = 120750.12, Current = 27.21, Best = 26.36
[2025-12-29T18:50:08.880Z] [INFO] [Phase 2] Iteration 40500: Temp = 113490.26, Current = 27.19, Best = 26.36
[2025-12-29T18:50:21.449Z] [INFO] [Phase 2] Iteration 41000: Temp = 106475.05, Current = 27.29, Best = 26.36
[2025-12-29T18:50:31.680Z] [INFO] [Phase 2] Iteration 41500: Temp = 100093.47, Current = 27.51, Best = 26.36
[2025-12-29T18:50:42.175Z] [INFO] [Phase 2] Iteration 42000: Temp = 93962.73, Current = 27.38, Best = 26.36
[2025-12-29T18:50:54.463Z] [INFO] [Phase 2] Iteration 42500: Temp = 88189.85, Current = 27.37, Best = 26.36
[2025-12-29T18:51:15.960Z] [INFO] [Phase 2] Iteration 43500: Temp = 77904.17, Current = 27.24, Best = 26.36
[2025-12-29T18:51:37.377Z] [INFO] [Phase 2] Iteration 44500: Temp = 68804.35, Current = 27.27, Best = 26.36
[2025-12-29T18:51:48.436Z] [INFO] [Phase 2] Iteration 45000: Temp = 64771.19, Current = 27.45, Best = 26.36
[2025-12-29T18:52:02.948Z] [INFO] [Phase 2] Iteration 45500: Temp = 60621.79, Current = 27.33, Best = 26.36
[2025-12-29T18:52:14.417Z] [INFO] [Phase 2] Iteration 46000: Temp = 57068.27, Current = 27.42, Best = 26.36
[2025-12-29T18:53:55.881Z] [INFO] [Phase 2] Iteration 50500: Temp = 32609.13, Current = 27.25, Best = 26.36
[2025-12-29T18:54:20.116Z] [INFO] [Phase 2] Iteration 51500: Temp = 28679.41, Current = 27.37, Best = 26.36
[2025-12-29T18:54:30.324Z] [INFO] [Phase 2] Iteration 52000: Temp = 26987.49, Current = 27.26, Best = 26.36
[2025-12-29T18:54:40.532Z] [INFO] [Phase 2] Iteration 52500: Temp = 25436.05, Current = 27.34, Best = 26.36
[2025-12-29T18:55:03.036Z] [INFO] [Phase 2] Iteration 53500: Temp = 22554.97, Current = 27.48, Best = 26.36
[2025-12-29T18:55:13.118Z] [INFO] [Phase 2] Iteration 54000: Temp = 21330.75, Current = 27.49, Best = 26.36
[2025-12-29T18:55:25.292Z] [INFO] [Phase 2] Iteration 54500: Temp = 20048.29, Current = 27.31, Best = 26.36
[2025-12-29T18:55:36.439Z] [INFO] [Phase 2] Iteration 55000: Temp = 18786.47, Current = 27.29, Best = 26.36
[2025-12-29T18:55:46.809Z] [INFO] [Phase 2] Iteration 55500: Temp = 17667.58, Current = 27.24, Best = 26.36
[2025-12-29T18:55:57.949Z] [INFO] [Phase 2] Iteration 56000: Temp = 16655.24, Current = 27.32, Best = 26.36
[2025-12-29T18:56:29.701Z] [INFO] [Phase 2] Iteration 57500: Temp = 13928.08, Current = 27.53, Best = 26.36
[2025-12-29T18:56:39.614Z] [INFO] [Phase 2] Iteration 58000: Temp = 13093.31, Current = 27.54, Best = 26.36
[2025-12-29T18:56:48.867Z] [INFO] [Phase 2] Iteration 58500: Temp = 12335.67, Current = 27.55, Best = 26.36
[2025-12-29T18:56:59.258Z] [INFO] [Phase 2] Iteration 59000: Temp = 11591.70, Current = 27.55, Best = 26.36
[2025-12-29T18:57:10.027Z] [INFO] [Phase 2] Iteration 59500: Temp = 10923.13, Current = 27.43, Best = 26.36
[2025-12-29T18:57:20.511Z] [INFO] [Phase 2] Iteration 60000: Temp = 10301.37, Current = 27.12, Best = 26.36
[2025-12-29T18:57:20.529Z] [INFO] Optimization complete {"iterations":60000,"reheats":1,"finalTemperature":"10301.3721","fitness":"26.36","hardViolations":0,"softViolations":8}
[2025-12-29T18:57:20.529Z] [INFO] Operator Statistics:
[2025-12-29T18:57:20.529Z] [INFO]   Fix Friday Prayer Conflict: Attempts = 0, Improvements = 0, Accepted = 0, Success Rate = 0.00%
[2025-12-29T18:57:20.529Z] [INFO]   Fix Lecturer Conflict: Attempts = 0, Improvements = 0, Accepted = 0, Success Rate = 0.00%
[2025-12-29T18:57:20.529Z] [INFO]   Fix Room Conflict: Attempts = 0, Improvements = 0, Accepted = 0, Success Rate = 0.00%
[2025-12-29T18:57:20.529Z] [INFO]   Fix Max Daily Periods: Attempts = 8, Improvements = 7, Accepted = 8, Success Rate = 87.50%
[2025-12-29T18:57:20.529Z] [INFO]   Fix Room Capacity: Attempts = 0, Improvements = 0, Accepted = 0, Success Rate = 0.00%
[2025-12-29T18:57:20.529Z] [INFO]   Change Time Slot and Room: Attempts = 6380, Improvements = 708, Accepted = 6019, Success Rate = 11.10%
[2025-12-29T18:57:20.529Z] [INFO]   Change Time Slot: Attempts = 5131, Improvements = 269, Accepted = 4432, Success Rate = 5.24%
[2025-12-29T18:57:20.529Z] [INFO]   Change Room: Attempts = 10179, Improvements = 724, Accepted = 10179, Success Rate = 7.11%
[2025-12-29T18:57:20.529Z] [INFO]   Swap Classes: Attempts = 14716, Improvements = 115, Accepted = 781, Success Rate = 0.78%
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
   Final fitness: 26.36
   Hard constraint violations: 0
   Soft constraint violations: 8
   Total iterations: 60000
   Reheating events: 1
   Final temperature: 10301.3721
   Classes scheduled: 356/373

📈 OPERATOR STATISTICS:
   Fix Friday Prayer Conflict:
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
      Improvements: 7
      Success rate: 87.50%
   Fix Room Capacity:
      Attempts: 0
      Improvements: 0
      Success rate: 0.00%
   Change Time Slot and Room:
      Attempts: 6380
      Improvements: 708
      Success rate: 11.10%
   Change Time Slot:
      Attempts: 5131
      Improvements: 269
      Success rate: 5.24%
   Change Room:
      Attempts: 10179
      Improvements: 724
      Success rate: 7.11%
   Swap Classes:
      Attempts: 14716
      Improvements: 115
      Success rate: 0.78%

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
   🔀 Randomization enabled - shuffling class order
  ⚠️  Skipping GS13IP12: No lecturers on class PROYEK INTERDISIPLIN
  ⚠️  Skipping GS13PW02: No lecturers on class Praktik Kerja Lapang
  ⚠️  Skipping GS13IP12: No lecturers on class Proyek Interdisipliner
  ⚠️  Skipping GS13IP12: No lecturers on class Proyek Interdisiplin
  ⚠️  Skipping MM23RS03: No lecturers on class Research Seminar
  ⚠️  Skipping GS13CZ02: No lecturers on class Kewarganegaraan
  ⚠️  Skipping GS13IP12: No lecturers on class Proyek Interdisipliner
  ⚠️  Skipping GS13TH46: No lecturers on class Skripsi
  ⚠️  Skipping GS13PW02: No lecturers on class Kerja Praktik/Magang
  ⚠️  Skipping GS13PW02: No lecturers on class Kerja Praktik
  ⚠️  Skipping VD13KP02: No lecturers on class Kerja Praktik
  ⚠️  Skipping GS13CZ02: No lecturers on class Kewarganegaraan
  ⚠️  Skipping CE11UT46: No lecturers on class Skripsi
  ⚠️  Skipping AC135343: No lecturers on class Skripsi
  ⚠️  Skipping GS13CZ02: No lecturers on class Kewarganegaraan
  ⚠️  Skipping GS13PW02: No lecturers on class Kerja Praktik
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
   Total operators: 9

⚙️  Configuring Simulated Annealing...
   Initial temperature: 100000
   Cooling rate: 0.9998
   Max iterations: 60000

🚀 Starting optimization...

======================================================================
[2025-12-29T18:35:37.097Z] [INFO] Simulated Annealing initialized {"hardConstraints":11,"softConstraints":8,"moveGenerators":9,"config":{"initialTemperature":100000,"minTemperature":1e-7,"coolingRate":0.9998,"maxIterations":60000}}
[2025-12-29T18:35:37.098Z] [INFO] Starting optimization...
[2025-12-29T18:35:37.098Z] [INFO] Phase 1: Eliminating hard constraint violations
[2025-12-29T18:35:37.145Z] [INFO] Initial state {"fitness":"172247.36","hardViolations":13}
[2025-12-29T18:36:26.058Z] [INFO] [Phase 1] Iteration 2500: Temp = 77489.67, Hard violations = 5, Best = 5
[2025-12-29T18:36:34.805Z] [INFO] [Phase 1] Iteration 3000: Temp = 73680.61, Hard violations = 5, Best = 5
[2025-12-29T18:37:04.148Z] [INFO] [Phase 1] Iteration 4500: Temp = 63429.22, Hard violations = 5, Best = 5
[2025-12-29T18:37:24.282Z] [INFO] [Phase 1] Iteration 5500: Temp = 57335.19, Hard violations = 5, Best = 5
[2025-12-29T18:38:13.703Z] [INFO] [Phase 1] Iteration 8000: Temp = 44938.29, Hard violations = 3, Best = 3
[2025-12-29T18:38:24.462Z] [INFO] [Phase 1] Iteration 8500: Temp = 42720.77, Hard violations = 3, Best = 3
[2025-12-29T18:39:04.460Z] [INFO] [Phase 1] Iteration 10500: Temp = 34538.13, Hard violations = 3, Best = 3
[2025-12-29T18:39:16.495Z] [INFO] [Phase 1] Iteration 11000: Temp = 32286.76, Hard violations = 3, Best = 3
[2025-12-29T18:39:38.659Z] [INFO] [Phase 1] Iteration 12000: Temp = 28813.55, Hard violations = 2, Best = 2
[2025-12-29T18:39:48.862Z] [INFO] [Phase 1] Iteration 12500: Temp = 27037.89, Hard violations = 2, Best = 2
[2025-12-29T18:40:14.236Z] [INFO] [Phase 1] Iteration 13500: Temp = 23760.55, Hard violations = 1, Best = 1
[2025-12-29T18:40:37.925Z] [INFO] [Phase 1] Iteration 14500: Temp = 20964.15, Hard violations = 1, Best = 1
[2025-12-29T18:40:52.541Z] [INFO] [Phase 1] Iteration 15000: Temp = 19632.91, Hard violations = 1, Best = 1
[2025-12-29T18:41:02.198Z] [INFO] [Phase 1] Iteration 15500: Temp = 18578.44, Hard violations = 1, Best = 1
[2025-12-29T18:41:24.809Z] [INFO] [Phase 1] Iteration 16500: Temp = 16437.90, Hard violations = 1, Best = 1
[2025-12-29T18:42:00.123Z] [INFO] [Phase 1] Iteration 18000: Temp = 13669.56, Hard violations = 1, Best = 1
[2025-12-29T18:42:20.043Z] [INFO] [Phase 1] Iteration 19000: Temp = 12194.19, Hard violations = 1, Best = 1
[2025-12-29T18:42:30.835Z] [INFO] [Phase 1] Iteration 19500: Temp = 11516.19, Hard violations = 1, Best = 1
[2025-12-29T18:42:40.955Z] [INFO] [Phase 1] Iteration 20000: Temp = 10862.84, Hard violations = 1, Best = 1
[2025-12-29T18:42:54.636Z] [INFO] Phase 1 complete: Hard violations = 1
[2025-12-29T18:42:54.636Z] [INFO] Phase 1.5: Intensification - targeting remaining hard violations
[2025-12-29T18:42:54.636Z] [INFO] [Intensification] Attempt 1/3
[2025-12-29T18:43:15.733Z] [INFO] [Intensification] Iter 500: Hard violations = 7, Best = 1
[2025-12-29T18:43:36.745Z] [INFO] [Intensification] Iter 1000: Hard violations = 12, Best = 1
[2025-12-29T18:43:56.242Z] [INFO] [Intensification] Iter 1500: Hard violations = 13, Best = 1
[2025-12-29T18:44:17.277Z] [INFO] [Intensification] Iter 2000: Hard violations = 20, Best = 1
[2025-12-29T18:44:17.277Z] [INFO] [Intensification] Attempt 2/3
[2025-12-29T18:44:35.733Z] [INFO] [Intensification] Iter 500: Hard violations = 8, Best = 1
[2025-12-29T18:44:56.360Z] [INFO] [Intensification] Iter 1000: Hard violations = 16, Best = 1
[2025-12-29T18:45:17.282Z] [INFO] [Intensification] Iter 1500: Hard violations = 16, Best = 1
[2025-12-29T18:45:36.678Z] [INFO] [Intensification] Iter 2000: Hard violations = 20, Best = 1
[2025-12-29T18:45:36.678Z] [INFO] [Intensification] Attempt 3/3
[2025-12-29T18:45:52.344Z] [INFO] [Intensification] Iter 500: Hard violations = 4, Best = 1
[2025-12-29T18:46:07.695Z] [INFO] [Intensification] Iter 1000: Hard violations = 6, Best = 1
[2025-12-29T18:46:28.242Z] [INFO] [Intensification] Iter 1500: Hard violations = 12, Best = 1
[2025-12-29T18:46:47.926Z] [INFO] [Intensification] Iter 2000: Hard violations = 11, Best = 1
[2025-12-29T18:46:47.926Z] [WARN] [Intensification] Could not eliminate all hard violations. Remaining: 1
[2025-12-29T18:46:47.926Z] [INFO] Phase 2: Optimizing soft constraints
[2025-12-29T18:46:55.924Z] [INFO] [Phase 2] Iteration 27000: Temp = 9607.42, Current = 50026.98, Best = 50026.91
[2025-12-29T18:47:05.692Z] [INFO] [Phase 2] Iteration 27500: Temp = 9037.02, Current = 50027.05, Best = 50026.91
[2025-12-29T18:47:28.433Z] [INFO] [Phase 2] Iteration 28500: Temp = 7983.02, Current = 50027.22, Best = 50026.91
[2025-12-29T18:48:00.443Z] [INFO] [Phase 2] Iteration 30000: Temp = 6657.20, Current = 50027.38, Best = 50026.91
[2025-12-29T18:48:12.946Z] [INFO] [Phase 2] Iteration 30500: Temp = 6246.95, Current = 50027.21, Best = 50026.91
[2025-12-29T18:48:33.262Z] [INFO] [Phase 2] Iteration 31500: Temp = 5543.80, Current = 50027.24, Best = 50026.91
[2025-12-29T18:48:44.542Z] [INFO] [Phase 2] Iteration 32000: Temp = 5234.52, Current = 50027.29, Best = 50026.91
[2025-12-29T18:48:55.276Z] [INFO] [Phase 2] Iteration 32500: Temp = 4911.94, Current = 50027.30, Best = 50026.91
[2025-12-29T18:49:18.474Z] [INFO] [Phase 2] Iteration 33500: Temp = 4343.40, Current = 50027.25, Best = 50026.91
[2025-12-29T18:49:38.587Z] [INFO] [Phase 2] Iteration 34500: Temp = 3875.39, Current = 50027.17, Best = 50026.91
[2025-12-29T18:49:48.777Z] [INFO] [Phase 2] Iteration 35000: Temp = 3652.60, Current = 50027.31, Best = 50026.91
[2025-12-29T18:49:59.104Z] [INFO] [Phase 2] Iteration 35500: Temp = 3439.87, Current = 50027.29, Best = 50026.91
[2025-12-29T18:50:21.289Z] [INFO] [Phase 2] Iteration 36500: Temp = 3060.63, Current = 50027.23, Best = 50026.91
[2025-12-29T18:50:31.080Z] [INFO] [Phase 2] Iteration 37000: Temp = 2890.46, Current = 50027.23, Best = 50026.91
[2025-12-29T18:50:53.447Z] [INFO] [Phase 2] Iteration 38000: Temp = 2565.63, Current = 50027.26, Best = 50026.91
[2025-12-29T18:51:03.734Z] [INFO] [Phase 2] Iteration 38500: Temp = 2424.43, Current = 50027.34, Best = 50026.91
[2025-12-29T18:51:14.693Z] [INFO] [Phase 2] Iteration 39000: Temp = 2283.23, Current = 50027.44, Best = 50026.91
[2025-12-29T18:51:35.533Z] [INFO] [Phase 2] Iteration 40000: Temp = 2026.64, Current = 50027.29, Best = 50026.91
[2025-12-29T18:51:56.869Z] [INFO] [Phase 2] Iteration 41000: Temp = 1807.91, Current = 27.43, Best = 27.30
[2025-12-29T18:52:10.760Z] [INFO] [Phase 2] Iteration 41500: Temp = 1707.04, Current = 27.43, Best = 27.30
[2025-12-29T18:52:20.353Z] [INFO] [Phase 2] Iteration 42000: Temp = 1609.88, Current = 27.42, Best = 27.30
[2025-12-29T18:52:30.867Z] [INFO] [Phase 2] Iteration 42500: Temp = 1515.81, Current = 27.47, Best = 27.30
[2025-12-29T18:53:27.566Z] [INFO] [Phase 2] Iteration 45000: Temp = 1117.08, Current = 27.37, Best = 27.30
[2025-12-29T18:53:48.345Z] [INFO] [Phase 2] Reheating #1: Temperature = 149986.45, Fitness = 27.30
[2025-12-29T18:53:58.973Z] [INFO] [Phase 2] Iteration 46500: Temp = 140743.43, Current = 27.42, Best = 27.30
[2025-12-29T18:54:09.658Z] [INFO] [Phase 2] Iteration 47000: Temp = 132705.54, Current = 27.38, Best = 27.30
[2025-12-29T18:54:22.082Z] [INFO] [Phase 2] Iteration 47500: Temp = 124652.07, Current = 27.46, Best = 27.30
[2025-12-29T18:54:55.420Z] [INFO] [Phase 2] Iteration 49000: Temp = 103534.81, Current = 27.44, Best = 27.24
[2025-12-29T18:55:05.865Z] [INFO] [Phase 2] Iteration 49500: Temp = 97368.40, Current = 27.53, Best = 27.24
[2025-12-29T18:55:16.586Z] [INFO] [Phase 2] Iteration 50000: Temp = 91752.60, Current = 27.52, Best = 27.24
[2025-12-29T18:55:39.185Z] [INFO] [Phase 2] Iteration 51000: Temp = 81197.43, Current = 27.52, Best = 27.24
[2025-12-29T18:55:49.748Z] [INFO] [Phase 2] Iteration 51500: Temp = 76376.68, Current = 27.67, Best = 27.24
[2025-12-29T18:56:01.292Z] [INFO] [Phase 2] Iteration 52000: Temp = 71799.05, Current = 27.64, Best = 27.24
[2025-12-29T18:56:11.131Z] [INFO] [Phase 2] Iteration 52500: Temp = 67807.01, Current = 27.57, Best = 27.24
[2025-12-29T18:56:22.068Z] [INFO] [Phase 2] Iteration 53000: Temp = 63590.18, Current = 27.55, Best = 27.24
[2025-12-29T18:56:33.507Z] [INFO] [Phase 2] Iteration 53500: Temp = 59695.27, Current = 27.56, Best = 27.24
[2025-12-29T18:56:43.423Z] [INFO] [Phase 2] Iteration 54000: Temp = 56106.22, Current = 27.81, Best = 27.24
[2025-12-29T18:56:53.502Z] [INFO] [Phase 2] Iteration 54500: Temp = 52606.53, Current = 27.77, Best = 27.24
[2025-12-29T18:57:15.300Z] [INFO] [Phase 2] Iteration 55500: Temp = 46480.26, Current = 27.81, Best = 27.24
[2025-12-29T18:58:02.098Z] [INFO] [Phase 2] Iteration 57500: Temp = 36190.72, Current = 28.06, Best = 27.24
[2025-12-29T18:58:22.496Z] [INFO] [Phase 2] Iteration 58500: Temp = 32020.95, Current = 27.96, Best = 27.24
[2025-12-29T18:58:32.129Z] [INFO] [Phase 2] Iteration 59000: Temp = 30023.61, Current = 27.93, Best = 27.24
[2025-12-29T18:58:50.930Z] [INFO] [Phase 2] Iteration 60000: Temp = 26490.11, Current = 27.73, Best = 27.24
[2025-12-29T18:58:50.943Z] [INFO] Optimization complete {"iterations":60000,"reheats":1,"finalTemperature":"26490.1126","fitness":"27.24","hardViolations":0,"softViolations":8}
[2025-12-29T18:58:50.944Z] [INFO] Operator Statistics:
[2025-12-29T18:58:50.944Z] [INFO]   Fix Friday Prayer Conflict: Attempts = 0, Improvements = 0, Accepted = 0, Success Rate = 0.00%
[2025-12-29T18:58:50.944Z] [INFO]   Fix Lecturer Conflict: Attempts = 726, Improvements = 10, Accepted = 712, Success Rate = 1.38%
[2025-12-29T18:58:50.944Z] [INFO]   Fix Room Conflict: Attempts = 128, Improvements = 20, Accepted = 128, Success Rate = 15.63%
[2025-12-29T18:58:50.944Z] [INFO]   Fix Max Daily Periods: Attempts = 689, Improvements = 6, Accepted = 689, Success Rate = 0.87%
[2025-12-29T18:58:50.944Z] [INFO]   Fix Room Capacity: Attempts = 810, Improvements = 11, Accepted = 769, Success Rate = 1.36%
[2025-12-29T18:58:50.944Z] [INFO]   Change Time Slot and Room: Attempts = 6400, Improvements = 647, Accepted = 5989, Success Rate = 10.11%
[2025-12-29T18:58:50.944Z] [INFO]   Change Time Slot: Attempts = 5343, Improvements = 271, Accepted = 4619, Success Rate = 5.07%
[2025-12-29T18:58:50.944Z] [INFO]   Change Room: Attempts = 9823, Improvements = 735, Accepted = 9823, Success Rate = 7.48%
[2025-12-29T18:58:50.945Z] [INFO]   Swap Classes: Attempts = 13773, Improvements = 111, Accepted = 793, Success Rate = 0.81%
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
   Final fitness: 27.24
   Hard constraint violations: 0
   Soft constraint violations: 8
   Total iterations: 60000
   Reheating events: 1
   Final temperature: 26490.1126
   Classes scheduled: 356/373

📈 OPERATOR STATISTICS:
   Fix Friday Prayer Conflict:
      Attempts: 0
      Improvements: 0
      Success rate: 0.00%
   Fix Lecturer Conflict:
      Attempts: 726
      Improvements: 10
      Success rate: 1.38%
   Fix Room Conflict:
      Attempts: 128
      Improvements: 20
      Success rate: 15.63%
   Fix Max Daily Periods:
      Attempts: 689
      Improvements: 6
      Success rate: 0.87%
   Fix Room Capacity:
      Attempts: 810
      Improvements: 11
      Success rate: 1.36%
   Change Time Slot and Room:
      Attempts: 6400
      Improvements: 647
      Success rate: 10.11%
   Change Time Slot:
      Attempts: 5343
      Improvements: 271
      Success rate: 5.07%
   Change Room:
      Attempts: 9823
      Improvements: 735
      Success rate: 7.48%
   Swap Classes:
      Attempts: 13773
      Improvements: 111
      Success rate: 0.81%

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
  ⚠️  Skipping VD13KP02: No lecturers on class Kerja Praktik
  ⚠️  Skipping GS13PW02: No lecturers on class Kerja Praktik
  ⚠️  Skipping GS13IP12: No lecturers on class Proyek Interdisipliner
  ⚠️  Skipping GS13CZ02: No lecturers on class Kewarganegaraan
  ⚠️  Skipping GS13IP12: No lecturers on class PROYEK INTERDISIPLIN
  ⚠️  Skipping GS13IP12: No lecturers on class Proyek Interdisiplin
  ⚠️  Skipping CE11UT46: No lecturers on class Skripsi
  ⚠️  Skipping GS13IP12: No lecturers on class Proyek Interdisipliner
  ⚠️  Skipping GS13CZ02: No lecturers on class Kewarganegaraan
  ⚠️  Skipping GS13CZ02: No lecturers on class Kewarganegaraan
  ⚠️  Skipping GS13TH46: No lecturers on class Skripsi
  ⚠️  Skipping MM23RS03: No lecturers on class Research Seminar
  ⚠️  Skipping GS13PW02: No lecturers on class Kerja Praktik/Magang
  ⚠️  Skipping AC135343: No lecturers on class Skripsi
  ⚠️  Skipping GS13PW02: No lecturers on class Praktik Kerja Lapang
  ⚠️  Skipping GS13PW02: No lecturers on class KERJA PRAKTIK
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
   Total operators: 9

⚙️  Configuring Simulated Annealing...
   Initial temperature: 100000
   Cooling rate: 0.9998
   Max iterations: 60000

🚀 Starting optimization...

======================================================================
[2025-12-29T18:35:40.404Z] [INFO] Simulated Annealing initialized {"hardConstraints":11,"softConstraints":8,"moveGenerators":9,"config":{"initialTemperature":100000,"minTemperature":1e-7,"coolingRate":0.9998,"maxIterations":60000}}
[2025-12-29T18:35:40.405Z] [INFO] Starting optimization...
[2025-12-29T18:35:40.405Z] [INFO] Phase 1: Eliminating hard constraint violations
[2025-12-29T18:35:40.450Z] [INFO] Initial state {"fitness":"173774.76","hardViolations":19}
[2025-12-29T18:35:55.265Z] [INFO] [Phase 1] Iteration 500: Temp = 93108.27, Hard violations = 7, Best = 7
[2025-12-29T18:36:09.870Z] [INFO] [Phase 1] Iteration 1000: Temp = 87545.34, Hard violations = 6, Best = 6
[2025-12-29T18:36:23.121Z] [INFO] [Phase 1] Iteration 1500: Temp = 82314.78, Hard violations = 6, Best = 6
[2025-12-29T18:36:34.403Z] [INFO] [Phase 1] Iteration 2000: Temp = 77722.51, Hard violations = 6, Best = 6
[2025-12-29T18:37:31.869Z] [INFO] [Phase 1] Iteration 4000: Temp = 59782.84, Hard violations = 3, Best = 3
[2025-12-29T18:37:50.555Z] [INFO] [Phase 1] Iteration 4500: Temp = 55141.94, Hard violations = 3, Best = 3
[2025-12-29T18:38:54.513Z] [INFO] [Phase 1] Iteration 6500: Temp = 40693.98, Hard violations = 2, Best = 2
[2025-12-29T18:39:11.745Z] [INFO] [Phase 1] Iteration 7000: Temp = 37602.57, Hard violations = 2, Best = 2
[2025-12-29T18:39:27.091Z] [INFO] [Phase 1] Iteration 7500: Temp = 34801.64, Hard violations = 1, Best = 1
[2025-12-29T18:39:43.417Z] [INFO] [Phase 1] Iteration 8000: Temp = 32293.22, Hard violations = 1, Best = 1
[2025-12-29T18:39:58.416Z] [INFO] [Phase 1] Iteration 8500: Temp = 29953.60, Hard violations = 1, Best = 1
[2025-12-29T18:40:16.680Z] [INFO] [Phase 1] Iteration 9000: Temp = 27716.89, Hard violations = 1, Best = 1
[2025-12-29T18:40:57.380Z] [INFO] Phase 1 complete: Hard violations = 0
[2025-12-29T18:40:57.380Z] [INFO] Phase 2: Optimizing soft constraints
[2025-12-29T18:41:05.214Z] [INFO] [Phase 2] Iteration 10500: Temp = 22251.73, Current = 27.23, Best = 27.18
[2025-12-29T18:41:17.940Z] [INFO] [Phase 2] Iteration 11000: Temp = 20855.41, Current = 27.15, Best = 27.15
[2025-12-29T18:41:27.800Z] [INFO] [Phase 2] Iteration 11500: Temp = 19625.06, Current = 27.09, Best = 27.07
[2025-12-29T18:41:38.778Z] [INFO] [Phase 2] Iteration 12000: Temp = 18378.85, Current = 26.99, Best = 26.99
[2025-12-29T18:42:03.811Z] [INFO] [Phase 2] Iteration 13000: Temp = 16258.06, Current = 27.01, Best = 26.86
[2025-12-29T18:42:15.406Z] [INFO] [Phase 2] Iteration 13500: Temp = 15186.12, Current = 26.99, Best = 26.86
[2025-12-29T18:42:26.523Z] [INFO] [Phase 2] Iteration 14000: Temp = 14298.80, Current = 27.06, Best = 26.86
[2025-12-29T18:42:46.648Z] [INFO] [Phase 2] Iteration 15000: Temp = 12709.68, Current = 26.99, Best = 26.86
[2025-12-29T18:44:25.725Z] [INFO] [Phase 2] Iteration 19500: Temp = 7195.87, Current = 27.31, Best = 26.86
[2025-12-29T18:44:35.838Z] [INFO] [Phase 2] Iteration 20000: Temp = 6744.32, Current = 27.32, Best = 26.86
[2025-12-29T18:44:47.480Z] [INFO] [Phase 2] Iteration 20500: Temp = 6323.63, Current = 27.36, Best = 26.86
[2025-12-29T18:45:06.999Z] [INFO] [Phase 2] Iteration 21500: Temp = 5635.48, Current = 27.38, Best = 26.86
[2025-12-29T18:45:18.582Z] [INFO] [Phase 2] Iteration 22000: Temp = 5299.84, Current = 27.43, Best = 26.86
[2025-12-29T18:45:28.812Z] [INFO] [Phase 2] Iteration 22500: Temp = 4993.17, Current = 27.31, Best = 26.86
[2025-12-29T18:45:38.367Z] [INFO] [Phase 2] Iteration 23000: Temp = 4699.54, Current = 27.17, Best = 26.86
[2025-12-29T18:46:08.798Z] [INFO] [Phase 2] Iteration 24500: Temp = 3949.73, Current = 27.47, Best = 26.86
[2025-12-29T18:46:18.732Z] [INFO] [Phase 2] Iteration 25000: Temp = 3724.16, Current = 27.39, Best = 26.86
[2025-12-29T18:46:40.147Z] [INFO] [Phase 2] Iteration 26000: Temp = 3312.26, Current = 27.49, Best = 26.86
[2025-12-29T18:47:01.997Z] [INFO] [Phase 2] Iteration 27000: Temp = 2921.85, Current = 27.58, Best = 26.86
[2025-12-29T18:47:33.642Z] [INFO] [Phase 2] Iteration 28500: Temp = 2434.64, Current = 27.27, Best = 26.86
[2025-12-29T18:47:43.651Z] [INFO] [Phase 2] Iteration 29000: Temp = 2296.97, Current = 27.46, Best = 26.86
[2025-12-29T18:47:53.503Z] [INFO] [Phase 2] Iteration 29500: Temp = 2172.30, Current = 27.40, Best = 26.86
[2025-12-29T18:48:26.217Z] [INFO] [Phase 2] Iteration 31000: Temp = 1811.53, Current = 27.43, Best = 26.86
[2025-12-29T18:48:47.721Z] [INFO] [Phase 2] Iteration 32000: Temp = 1602.17, Current = 27.55, Best = 26.86
[2025-12-29T18:48:58.174Z] [INFO] [Phase 2] Iteration 32500: Temp = 1501.93, Current = 27.35, Best = 26.86
[2025-12-29T18:49:40.391Z] [INFO] [Phase 2] Iteration 34500: Temp = 1180.72, Current = 27.59, Best = 26.86
[2025-12-29T18:50:00.315Z] [INFO] [Phase 2] Iteration 35500: Temp = 1047.40, Current = 27.47, Best = 26.86
[2025-12-29T18:50:08.089Z] [INFO] [Phase 2] Reheating #1: Temperature = 149986.45, Fitness = 26.86
[2025-12-29T18:50:22.148Z] [INFO] [Phase 2] Iteration 36500: Temp = 139342.87, Current = 27.56, Best = 26.86
[2025-12-29T18:50:32.067Z] [INFO] [Phase 2] Iteration 37000: Temp = 131096.21, Current = 27.52, Best = 26.86
[2025-12-29T18:50:42.891Z] [INFO] [Phase 2] Iteration 37500: Temp = 122796.06, Current = 27.44, Best = 26.86
[2025-12-29T18:51:05.556Z] [INFO] [Phase 2] Iteration 38500: Temp = 108279.12, Current = 27.65, Best = 26.86
[2025-12-29T18:51:16.842Z] [INFO] [Phase 2] Iteration 39000: Temp = 101586.02, Current = 27.67, Best = 26.86
[2025-12-29T18:51:27.427Z] [INFO] [Phase 2] Iteration 39500: Temp = 95535.68, Current = 27.59, Best = 26.86
[2025-12-29T18:52:23.155Z] [INFO] [Phase 2] Iteration 42000: Temp = 70082.20, Current = 27.47, Best = 26.86
[2025-12-29T18:52:34.821Z] [INFO] [Phase 2] Iteration 42500: Temp = 65789.65, Current = 27.53, Best = 26.86
[2025-12-29T18:52:46.444Z] [INFO] [Phase 2] Iteration 43000: Temp = 61920.82, Current = 27.53, Best = 26.86
[2025-12-29T18:52:57.118Z] [INFO] [Phase 2] Iteration 43500: Temp = 58431.24, Current = 27.46, Best = 26.86
[2025-12-29T18:53:08.483Z] [INFO] [Phase 2] Iteration 44000: Temp = 55017.13, Current = 27.47, Best = 26.86
[2025-12-29T18:53:28.829Z] [INFO] [Phase 2] Iteration 45000: Temp = 48551.84, Current = 27.40, Best = 26.86
[2025-12-29T18:54:00.692Z] [INFO] [Phase 2] Iteration 46500: Temp = 40439.78, Current = 27.69, Best = 26.86
[2025-12-29T18:54:11.247Z] [INFO] [Phase 2] Iteration 47000: Temp = 38031.23, Current = 27.71, Best = 26.86
[2025-12-29T18:54:23.620Z] [INFO] [Phase 2] Iteration 47500: Temp = 35673.26, Current = 27.40, Best = 26.86
[2025-12-29T18:54:44.402Z] [INFO] [Phase 2] Iteration 48500: Temp = 31506.34, Current = 27.52, Best = 26.86
[2025-12-29T18:54:56.181Z] [INFO] [Phase 2] Iteration 49000: Temp = 29671.38, Current = 27.39, Best = 26.86
[2025-12-29T18:55:06.396Z] [INFO] [Phase 2] Iteration 49500: Temp = 27870.72, Current = 27.33, Best = 26.86
[2025-12-29T18:55:16.520Z] [INFO] [Phase 2] Iteration 50000: Temp = 26315.84, Current = 27.44, Best = 26.86
[2025-12-29T18:55:27.597Z] [INFO] [Phase 2] Iteration 50500: Temp = 24947.30, Current = 27.47, Best = 26.86
[2025-12-29T18:55:37.710Z] [INFO] [Phase 2] Iteration 51000: Temp = 23433.33, Current = 27.52, Best = 26.86
[2025-12-29T18:55:48.137Z] [INFO] [Phase 2] Iteration 51500: Temp = 22002.43, Current = 27.52, Best = 26.86
[2025-12-29T18:56:00.044Z] [INFO] [Phase 2] Iteration 52000: Temp = 20568.20, Current = 27.47, Best = 26.86
[2025-12-29T18:56:10.202Z] [INFO] [Phase 2] Iteration 52500: Temp = 19389.67, Current = 27.41, Best = 26.86
[2025-12-29T18:56:31.445Z] [INFO] [Phase 2] Iteration 53500: Temp = 17162.52, Current = 27.59, Best = 26.86
[2025-12-29T18:56:41.009Z] [INFO] [Phase 2] Iteration 54000: Temp = 16098.43, Current = 27.64, Best = 26.86
[2025-12-29T18:57:12.390Z] [INFO] [Phase 2] Iteration 55500: Temp = 13174.74, Current = 27.58, Best = 26.86
[2025-12-29T18:57:34.374Z] [INFO] [Phase 2] Iteration 56500: Temp = 11614.90, Current = 27.55, Best = 26.86
[2025-12-29T18:57:47.273Z] [INFO] [Phase 2] Iteration 57000: Temp = 10910.03, Current = 27.71, Best = 26.86
[2025-12-29T18:57:57.897Z] [INFO] [Phase 2] Iteration 57500: Temp = 10254.09, Current = 27.71, Best = 26.86
[2025-12-29T18:58:17.505Z] [INFO] [Phase 2] Iteration 58500: Temp = 9085.36, Current = 27.62, Best = 26.86
[2025-12-29T18:58:25.996Z] [INFO] [Phase 2] Iteration 59000: Temp = 8557.93, Current = 27.61, Best = 26.86
[2025-12-29T18:58:34.711Z] [INFO] [Phase 2] Iteration 59500: Temp = 8059.51, Current = 27.62, Best = 26.86
[2025-12-29T18:58:43.996Z] [INFO] Optimization complete {"iterations":60000,"reheats":1,"finalTemperature":"7594.6695","fitness":"26.86","hardViolations":0,"softViolations":8}
[2025-12-29T18:58:43.996Z] [INFO] Operator Statistics:
[2025-12-29T18:58:43.996Z] [INFO]   Fix Friday Prayer Conflict: Attempts = 0, Improvements = 0, Accepted = 0, Success Rate = 0.00%
[2025-12-29T18:58:43.996Z] [INFO]   Fix Lecturer Conflict: Attempts = 1773, Improvements = 363, Accepted = 1494, Success Rate = 20.47%
[2025-12-29T18:58:43.996Z] [INFO]   Fix Room Conflict: Attempts = 0, Improvements = 0, Accepted = 0, Success Rate = 0.00%
[2025-12-29T18:58:43.996Z] [INFO]   Fix Max Daily Periods: Attempts = 142, Improvements = 11, Accepted = 142, Success Rate = 7.75%
[2025-12-29T18:58:43.996Z] [INFO]   Fix Room Capacity: Attempts = 0, Improvements = 0, Accepted = 0, Success Rate = 0.00%
[2025-12-29T18:58:43.996Z] [INFO]   Change Time Slot and Room: Attempts = 6446, Improvements = 681, Accepted = 6023, Success Rate = 10.56%
[2025-12-29T18:58:43.996Z] [INFO]   Change Time Slot: Attempts = 5379, Improvements = 280, Accepted = 4598, Success Rate = 5.21%
[2025-12-29T18:58:43.996Z] [INFO]   Change Room: Attempts = 10018, Improvements = 716, Accepted = 10018, Success Rate = 7.15%
[2025-12-29T18:58:43.996Z] [INFO]   Swap Classes: Attempts = 14180, Improvements = 129, Accepted = 836, Success Rate = 0.91%
======================================================================

✨ OPTIMIZATION COMPLETE!

Cache stats: {
  timeCache: {
    timeToMinutes: 20,
    minutesToTime: 17,
  },
  endTimeCache: 277,
  prayerOverlapCache: 277,
  totalEntries: 591,
}
📊 RESULTS:
   Final fitness: 26.86
   Hard constraint violations: 0
   Soft constraint violations: 8
   Total iterations: 60000
   Reheating events: 1
   Final temperature: 7594.6695
   Classes scheduled: 356/373

📈 OPERATOR STATISTICS:
   Fix Friday Prayer Conflict:
      Attempts: 0
      Improvements: 0
      Success rate: 0.00%
   Fix Lecturer Conflict:
      Attempts: 1773
      Improvements: 363
      Success rate: 20.47%
   Fix Room Conflict:
      Attempts: 0
      Improvements: 0
      Success rate: 0.00%
   Fix Max Daily Periods:
      Attempts: 142
      Improvements: 11
      Success rate: 7.75%
   Fix Room Capacity:
      Attempts: 0
      Improvements: 0
      Success rate: 0.00%
   Change Time Slot and Room:
      Attempts: 6446
      Improvements: 681
      Success rate: 10.56%
   Change Time Slot:
      Attempts: 5379
      Improvements: 280
      Success rate: 5.21%
   Change Room:
      Attempts: 10018
      Improvements: 716
      Success rate: 7.15%
   Swap Classes:
      Attempts: 14180
      Improvements: 129
      Success rate: 0.91%

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
  ⚠️  Skipping MM23RS03: No lecturers on class Research Seminar
  ⚠️  Skipping GS13CZ02: No lecturers on class Kewarganegaraan
  ⚠️  Skipping AC135343: No lecturers on class Skripsi
  ⚠️  Skipping GS13PW02: No lecturers on class Kerja Praktik
  ⚠️  Skipping GS13CZ02: No lecturers on class Kewarganegaraan
  ⚠️  Skipping GS13IP12: No lecturers on class Proyek Interdisipliner
  ⚠️  Skipping GS13IP12: No lecturers on class Proyek Interdisipliner
  ⚠️  Skipping GS13TH46: No lecturers on class Skripsi
  ⚠️  Skipping VD13KP02: No lecturers on class Kerja Praktik
  ⚠️  Skipping GS13IP12: No lecturers on class Proyek Interdisiplin
  ⚠️  Skipping CE11UT46: No lecturers on class Skripsi
  ⚠️  Skipping GS13CZ02: No lecturers on class Kewarganegaraan
  ⚠️  Skipping GS13PW02: No lecturers on class Kerja Praktik
  ⚠️  Skipping GS13PW02: No lecturers on class Kerja Praktik/Magang
  ⚠️  Skipping GS13IP12: No lecturers on class PROYEK INTERDISIPLIN
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
   Total operators: 9

⚙️  Configuring Simulated Annealing...
   Initial temperature: 100000
   Cooling rate: 0.9998
   Max iterations: 60000

🚀 Starting optimization...

======================================================================
[2025-12-29T18:35:44.164Z] [INFO] Simulated Annealing initialized {"hardConstraints":11,"softConstraints":8,"moveGenerators":9,"config":{"initialTemperature":100000,"minTemperature":1e-7,"coolingRate":0.9998,"maxIterations":60000}}
[2025-12-29T18:35:44.165Z] [INFO] Starting optimization...
[2025-12-29T18:35:44.165Z] [INFO] Phase 1: Eliminating hard constraint violations
[2025-12-29T18:35:44.231Z] [INFO] Initial state {"fitness":"237525.12","hardViolations":13}
[2025-12-29T18:35:54.274Z] [INFO] [Phase 1] Iteration 500: Temp = 94629.06, Hard violations = 5, Best = 5
[2025-12-29T18:36:14.120Z] [INFO] [Phase 1] Iteration 1500: Temp = 85863.17, Hard violations = 3, Best = 3
[2025-12-29T18:36:23.030Z] [INFO] [Phase 1] Iteration 2000: Temp = 81822.32, Hard violations = 3, Best = 3
[2025-12-29T18:36:41.885Z] [INFO] [Phase 1] Iteration 3000: Temp = 73813.37, Hard violations = 2, Best = 2
[2025-12-29T18:37:09.909Z] [INFO] [Phase 1] Iteration 4500: Temp = 63441.91, Hard violations = 2, Best = 2
[2025-12-29T18:37:48.342Z] [INFO] [Phase 1] Iteration 6500: Temp = 52169.87, Hard violations = 2, Best = 2
[2025-12-29T18:38:01.477Z] [INFO] [Phase 1] Iteration 7000: Temp = 49367.86, Hard violations = 2, Best = 2
[2025-12-29T18:38:20.300Z] [INFO] [Phase 1] Iteration 8000: Temp = 44812.63, Hard violations = 2, Best = 2
[2025-12-29T18:38:41.199Z] [INFO] [Phase 1] Iteration 9000: Temp = 40031.98, Hard violations = 2, Best = 2
[2025-12-29T18:38:51.088Z] [INFO] [Phase 1] Iteration 9500: Temp = 37881.89, Hard violations = 2, Best = 2
[2025-12-29T18:39:19.935Z] [INFO] [Phase 1] Iteration 11000: Temp = 32559.13, Hard violations = 2, Best = 2
[2025-12-29T18:39:29.081Z] [INFO] [Phase 1] Iteration 11500: Temp = 30977.25, Hard violations = 2, Best = 2
[2025-12-29T18:39:48.712Z] [INFO] [Phase 1] Iteration 12500: Temp = 27984.28, Hard violations = 2, Best = 2
[2025-12-29T18:40:09.686Z] [INFO] [Phase 1] Iteration 13500: Temp = 25412.30, Hard violations = 2, Best = 2
[2025-12-29T18:40:19.125Z] [INFO] [Phase 1] Iteration 14000: Temp = 24167.97, Hard violations = 2, Best = 2
[2025-12-29T18:40:54.151Z] [INFO] [Phase 1] Iteration 15500: Temp = 20590.14, Hard violations = 2, Best = 2
[2025-12-29T18:41:03.659Z] [INFO] [Phase 1] Iteration 16000: Temp = 19519.36, Hard violations = 2, Best = 2
[2025-12-29T18:41:23.585Z] [INFO] [Phase 1] Iteration 17000: Temp = 17636.96, Hard violations = 2, Best = 2
[2025-12-29T18:42:03.063Z] [INFO] [Phase 1] Iteration 19000: Temp = 14442.52, Hard violations = 2, Best = 2
[2025-12-29T18:43:02.154Z] [INFO] [Phase 1] Iteration 22000: Temp = 10545.99, Hard violations = 2, Best = 2
[2025-12-29T18:43:11.757Z] [INFO] Phase 1 complete: Hard violations = 2
[2025-12-29T18:43:11.757Z] [INFO] Phase 1.5: Intensification - targeting remaining hard violations
[2025-12-29T18:43:11.757Z] [INFO] [Intensification] Attempt 1/3
[2025-12-29T18:43:32.807Z] [INFO] [Intensification] Iter 500: Hard violations = 5, Best = 2
[2025-12-29T18:43:52.503Z] [INFO] [Intensification] Iter 1000: Hard violations = 7, Best = 2
[2025-12-29T18:44:14.002Z] [INFO] [Intensification] Iter 1500: Hard violations = 11, Best = 2
[2025-12-29T18:44:33.468Z] [INFO] [Intensification] Iter 2000: Hard violations = 15, Best = 2
[2025-12-29T18:44:33.469Z] [INFO] [Intensification] Attempt 2/3
[2025-12-29T18:44:49.083Z] [INFO] [Intensification] Iter 500: Hard violations = 2, Best = 2
[2025-12-29T18:45:05.619Z] [INFO] [Intensification] Iter 1000: Hard violations = 10, Best = 2
[2025-12-29T18:45:27.159Z] [INFO] [Intensification] Iter 1500: Hard violations = 10, Best = 2
[2025-12-29T18:45:47.693Z] [INFO] [Intensification] Iter 2000: Hard violations = 15, Best = 2
[2025-12-29T18:45:47.693Z] [INFO] [Intensification] Attempt 3/3
[2025-12-29T18:46:04.859Z] [INFO] [Intensification] Iter 500: Hard violations = 8, Best = 2
[2025-12-29T18:46:25.582Z] [INFO] [Intensification] Iter 1000: Hard violations = 8, Best = 2
[2025-12-29T18:46:44.942Z] [INFO] [Intensification] Iter 1500: Hard violations = 13, Best = 2
[2025-12-29T18:47:05.049Z] [INFO] [Intensification] Iter 2000: Hard violations = 13, Best = 2
[2025-12-29T18:47:05.049Z] [WARN] [Intensification] Could not eliminate all hard violations. Remaining: 2
[2025-12-29T18:47:05.049Z] [INFO] Phase 2: Optimizing soft constraints
[2025-12-29T18:47:13.940Z] [INFO] [Phase 2] Iteration 29000: Temp = 9489.01, Current = 50026.71, Best = 50026.71
[2025-12-29T18:47:45.879Z] [INFO] [Phase 2] Iteration 30500: Temp = 7928.92, Current = 50026.79, Best = 50026.62
[2025-12-29T18:47:56.683Z] [INFO] [Phase 2] Iteration 31000: Temp = 7456.68, Current = 50026.81, Best = 50026.62
[2025-12-29T18:48:09.763Z] [INFO] [Phase 2] Iteration 31500: Temp = 6983.18, Current = 50026.77, Best = 50026.62
[2025-12-29T18:48:29.252Z] [INFO] [Phase 2] Iteration 32500: Temp = 6223.25, Current = 50026.82, Best = 50026.62
[2025-12-29T18:49:22.306Z] [INFO] [Phase 2] Iteration 35000: Temp = 4631.42, Current = 50026.83, Best = 50026.62
[2025-12-29T18:49:32.041Z] [INFO] [Phase 2] Iteration 35500: Temp = 4368.66, Current = 50026.90, Best = 50026.62
[2025-12-29T18:50:01.353Z] [INFO] [Phase 2] Iteration 37000: Temp = 3685.62, Current = 50026.99, Best = 50026.62
[2025-12-29T18:50:22.839Z] [INFO] [Phase 2] Iteration 38000: Temp = 3290.46, Current = 50026.98, Best = 50026.62
[2025-12-29T18:50:43.047Z] [INFO] [Phase 2] Iteration 39000: Temp = 2909.60, Current = 50027.01, Best = 50026.62
[2025-12-29T18:50:54.631Z] [INFO] [Phase 2] Iteration 39500: Temp = 2737.95, Current = 50026.94, Best = 50026.62
[2025-12-29T18:51:25.208Z] [INFO] [Phase 2] Iteration 41000: Temp = 2313.11, Current = 50027.12, Best = 50026.62
[2025-12-29T18:51:35.421Z] [INFO] [Phase 2] Iteration 41500: Temp = 2173.61, Current = 50027.04, Best = 50026.62
[2025-12-29T18:51:57.985Z] [INFO] [Phase 2] Iteration 42500: Temp = 1920.10, Current = 50026.97, Best = 50026.62
[2025-12-29T18:52:12.284Z] [INFO] [Phase 2] Iteration 43000: Temp = 1804.65, Current = 50027.11, Best = 50026.62
[2025-12-29T18:52:22.264Z] [INFO] [Phase 2] Iteration 43500: Temp = 1693.44, Current = 50027.11, Best = 50026.62
[2025-12-29T18:52:33.024Z] [INFO] [Phase 2] Iteration 44000: Temp = 1601.85, Current = 50027.16, Best = 50026.62
[2025-12-29T18:52:55.712Z] [INFO] [Phase 2] Iteration 45000: Temp = 1418.42, Current = 27.13, Best = 27.09
[2025-12-29T18:53:07.219Z] [INFO] [Phase 2] Iteration 45500: Temp = 1335.28, Current = 27.18, Best = 27.09
[2025-12-29T18:53:17.477Z] [INFO] [Phase 2] Iteration 46000: Temp = 1259.27, Current = 27.12, Best = 27.05
[2025-12-29T18:53:37.086Z] [INFO] [Phase 2] Iteration 47000: Temp = 1124.71, Current = 27.03, Best = 26.99
[2025-12-29T18:53:58.186Z] [INFO] [Phase 2] Iteration 48000: Temp = 1001.11, Current = 27.08, Best = 26.99
[2025-12-29T18:54:01.095Z] [INFO] [Phase 2] Reheating #1: Temperature = 147989.84, Fitness = 26.99
[2025-12-29T18:54:20.672Z] [INFO] [Phase 2] Iteration 49000: Temp = 133317.45, Current = 27.03, Best = 26.96
[2025-12-29T18:54:40.609Z] [INFO] [Phase 2] Iteration 50000: Temp = 118145.99, Current = 27.00, Best = 26.88
[2025-12-29T18:54:52.849Z] [INFO] [Phase 2] Iteration 50500: Temp = 110976.09, Current = 27.06, Best = 26.88
[2025-12-29T18:55:03.822Z] [INFO] [Phase 2] Iteration 51000: Temp = 104095.47, Current = 26.99, Best = 26.88
[2025-12-29T18:55:14.947Z] [INFO] [Phase 2] Iteration 51500: Temp = 97660.97, Current = 27.09, Best = 26.88
[2025-12-29T18:55:27.554Z] [INFO] [Phase 2] Iteration 52000: Temp = 91697.56, Current = 27.14, Best = 26.88
[2025-12-29T18:55:38.216Z] [INFO] [Phase 2] Iteration 52500: Temp = 85943.43, Current = 27.18, Best = 26.88
[2025-12-29T18:55:48.298Z] [INFO] [Phase 2] Iteration 53000: Temp = 80954.18, Current = 27.18, Best = 26.88
[2025-12-29T18:55:59.203Z] [INFO] [Phase 2] Iteration 53500: Temp = 76376.68, Current = 27.21, Best = 26.88
[2025-12-29T18:56:41.238Z] [INFO] [Phase 2] Iteration 55500: Temp = 59564.07, Current = 27.28, Best = 26.88
[2025-12-29T18:56:50.325Z] [INFO] [Phase 2] Iteration 56000: Temp = 56196.07, Current = 27.14, Best = 26.88
[2025-12-29T18:57:00.418Z] [INFO] [Phase 2] Iteration 56500: Temp = 52923.14, Current = 27.13, Best = 26.88
[2025-12-29T18:57:23.371Z] [INFO] [Phase 2] Iteration 57500: Temp = 46322.48, Current = 27.23, Best = 26.88
[2025-12-29T18:57:47.214Z] [INFO] [Phase 2] Iteration 58500: Temp = 40903.47, Current = 27.43, Best = 26.88
[2025-12-29T18:57:57.743Z] [INFO] [Phase 2] Iteration 59000: Temp = 38498.10, Current = 27.39, Best = 26.88
[2025-12-29T18:58:08.419Z] [INFO] [Phase 2] Iteration 59500: Temp = 36010.20, Current = 27.42, Best = 26.88
[2025-12-29T18:58:19.307Z] [INFO] Optimization complete {"iterations":60000,"reheats":1,"finalTemperature":"33683.0781","fitness":"26.88","hardViolations":0,"softViolations":8}
[2025-12-29T18:58:19.307Z] [INFO] Operator Statistics:
[2025-12-29T18:58:19.307Z] [INFO]   Fix Friday Prayer Conflict: Attempts = 2144, Improvements = 12, Accepted = 1794, Success Rate = 0.56%
[2025-12-29T18:58:19.307Z] [INFO]   Fix Lecturer Conflict: Attempts = 692, Improvements = 25, Accepted = 670, Success Rate = 3.61%
[2025-12-29T18:58:19.307Z] [INFO]   Fix Room Conflict: Attempts = 350, Improvements = 15, Accepted = 350, Success Rate = 4.29%
[2025-12-29T18:58:19.307Z] [INFO]   Fix Max Daily Periods: Attempts = 187, Improvements = 6, Accepted = 187, Success Rate = 3.21%
[2025-12-29T18:58:19.307Z] [INFO]   Fix Room Capacity: Attempts = 315, Improvements = 4, Accepted = 315, Success Rate = 1.27%
[2025-12-29T18:58:19.307Z] [INFO]   Change Time Slot and Room: Attempts = 6059, Improvements = 611, Accepted = 5648, Success Rate = 10.08%
[2025-12-29T18:58:19.308Z] [INFO]   Change Time Slot: Attempts = 4862, Improvements = 242, Accepted = 4143, Success Rate = 4.98%
[2025-12-29T18:58:19.308Z] [INFO]   Change Room: Attempts = 8873, Improvements = 593, Accepted = 8873, Success Rate = 6.68%
[2025-12-29T18:58:19.308Z] [INFO]   Swap Classes: Attempts = 13009, Improvements = 102, Accepted = 659, Success Rate = 0.78%
======================================================================

✨ OPTIMIZATION COMPLETE!

Cache stats: {
  timeCache: {
    timeToMinutes: 20,
    minutesToTime: 17,
  },
  endTimeCache: 284,
  prayerOverlapCache: 284,
  totalEntries: 605,
}
📊 RESULTS:
   Final fitness: 26.88
   Hard constraint violations: 0
   Soft constraint violations: 8
   Total iterations: 60000
   Reheating events: 1
   Final temperature: 33683.0781
   Classes scheduled: 356/373

📈 OPERATOR STATISTICS:
   Fix Friday Prayer Conflict:
      Attempts: 2144
      Improvements: 12
      Success rate: 0.56%
   Fix Lecturer Conflict:
      Attempts: 692
      Improvements: 25
      Success rate: 3.61%
   Fix Room Conflict:
      Attempts: 350
      Improvements: 15
      Success rate: 4.29%
   Fix Max Daily Periods:
      Attempts: 187
      Improvements: 6
      Success rate: 3.21%
   Fix Room Capacity:
      Attempts: 315
      Improvements: 4
      Success rate: 1.27%
   Change Time Slot and Room:
      Attempts: 6059
      Improvements: 611
      Success rate: 10.08%
   Change Time Slot:
      Attempts: 4862
      Improvements: 242
      Success rate: 4.98%
   Change Room:
      Attempts: 8873
      Improvements: 593
      Success rate: 6.68%
   Swap Classes:
      Attempts: 13009
      Improvements: 102
      Success rate: 0.78%

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

# result of bun test command
```bash
emmanuelabayor@ade:~/projects/timetable-sa$ bun test
bun test v1.3.3 (274e01c7)

tests/integration/simple-timetabling.test.ts:
✓ Simple Timetabling Integration Tests > Feasible Problem Solving > should solve a simple timetabling problem with conflicts [20.36ms]
✓ Simple Timetabling Integration Tests > Feasible Problem Solving > should maintain solution quality for already-feasible timetable [2.74ms]
✓ Simple Timetabling Integration Tests > Feasible Problem Solving > should optimize soft constraints after satisfying hard constraints [8.62ms]
✓ Simple Timetabling Integration Tests > Operator Effectiveness > should use all move operators during search [4.84ms]
✓ Simple Timetabling Integration Tests > Operator Effectiveness > should track operator success rates [4.15ms]
✓ Simple Timetabling Integration Tests > Constraint Satisfaction > should eliminate all room conflicts [3.85ms]
✓ Simple Timetabling Integration Tests > Constraint Satisfaction > should eliminate all lecturer conflicts [3.74ms]
✓ Simple Timetabling Integration Tests > Constraint Satisfaction > should respect both room AND lecturer constraints simultaneously [3.72ms]
✓ Simple Timetabling Integration Tests > Performance Characteristics > should converge faster with better initial state [7.29ms]
✓ Simple Timetabling Integration Tests > Performance Characteristics > should produce consistent results with same seed (deterministic cloning) [4.36ms]
✓ Simple Timetabling Integration Tests > Scalability > should handle larger timetabling problems [11.75ms]

tests/core/acceptance-probability.test.ts:
✓ Acceptance Probability Logic > Phase 1: Hard Constraint Elimination > should ALWAYS accept moves that reduce hard violations [0.41ms]
✓ Acceptance Probability Logic > Phase 1: Hard Constraint Elimination > should NEVER accept moves that increase hard violations in Phase 1 [8.63ms]
✓ Acceptance Probability Logic > Phase 1: Hard Constraint Elimination > should use Metropolis criterion for moves with same hard violations [0.64ms]
✓ Acceptance Probability Logic > Phase 1: Hard Constraint Elimination > should prioritize hard violations over soft in Phase 1 [0.33ms]
✓ Acceptance Probability Logic > Phase 2: Soft Constraint Optimization > should STRICTLY reject moves that increase hard violations in Phase 2 [0.42ms]
✓ Acceptance Probability Logic > Phase 2: Soft Constraint Optimization > should accept soft-improving moves in Phase 2 [0.13ms]
✓ Acceptance Probability Logic > Phase 2: Soft Constraint Optimization > should use Metropolis for soft-worsening moves (at high temp) [0.40ms]
✓ Acceptance Probability Logic > Phase 2: Soft Constraint Optimization > should maintain hard constraint satisfaction throughout Phase 2 [0.61ms]
✓ Acceptance Probability Logic > Temperature-Dependent Acceptance > should accept more worsening moves at high temperature [0.28ms]
✓ Acceptance Probability Logic > Temperature-Dependent Acceptance > should accept fewer worsening moves as temperature decreases [0.33ms]
✓ Acceptance Probability Logic > Acceptance Probability Edge Cases > should handle zero temperature gracefully [1.26ms]
✓ Acceptance Probability Logic > Acceptance Probability Edge Cases > should handle identical fitness values [0.21ms]
✓ Acceptance Probability Logic > Acceptance Probability Edge Cases > should handle very large fitness differences [0.75ms]
✓ Acceptance Probability Logic > Phase Transition > should transition from Phase 1 to Phase 2 when hard violations reach 0 [0.17ms]
✓ Acceptance Probability Logic > Phase Transition > should enforce stricter acceptance in Phase 2 than Phase 1 [0.03ms]

tests/core/SimulatedAnnealing.test.ts:
✓ SimulatedAnnealing Core Engine > Initialization > should initialize with valid configuration [0.26ms]
✓ SimulatedAnnealing Core Engine > Initialization > should separate hard and soft constraints [0.67ms]
✓ SimulatedAnnealing Core Engine > Initialization > should initialize operator statistics [0.99ms]
✓ SimulatedAnnealing Core Engine > Optimization Loop > should complete optimization within maxIterations [0.81ms]
✓ SimulatedAnnealing Core Engine > Optimization Loop > should respect minTemperature stopping condition [0.15ms]
✓ SimulatedAnnealing Core Engine > Optimization Loop > should stop early if Phase 1 eliminates all hard violations [2.81ms]
✓ SimulatedAnnealing Core Engine > Optimization Loop > should handle empty move generators gracefully [0.20ms]
✓ SimulatedAnnealing Core Engine > Optimization Loop > should handle all non-applicable move generators [0.21ms]
✓ SimulatedAnnealing Core Engine > Constraint Evaluation > should correctly evaluate hard constraints [2.02ms]
✓ SimulatedAnnealing Core Engine > Constraint Evaluation > should correctly count violations using getViolations() [1.23ms]
✓ SimulatedAnnealing Core Engine > Constraint Evaluation > should apply correct penalty weights for soft constraints [0.34ms]
✓ SimulatedAnnealing Core Engine > Constraint Evaluation > should heavily penalize hard constraints vs soft [1.30ms]
✓ SimulatedAnnealing Core Engine > Solution Quality > should find feasible solution for solvable problem [1.58ms]
✓ SimulatedAnnealing Core Engine > Solution Quality > should improve fitness over iterations [1.28ms]
✓ SimulatedAnnealing Core Engine > Solution Quality > should optimize soft constraints after hard constraints satisfied [1.09ms]
440 |       const solver = new SimulatedAnnealing(state, constraints, moves, config);
441 |       const solution = solver.solve();
442 |
443 |       // Should complete without crashing
444 |       expect(solution.hardViolations).toBeGreaterThan(0);
445 |       expect(solution.iterations).toBeLessThanOrEqual(100);
                                        ^
error: expect(received).toBeLessThanOrEqual(expected)

Expected: <= 100
Received: 6045

      at <anonymous> (/home/emmanuelabayor/projects/timetable-sa/tests/core/SimulatedAnnealing.test.ts:445:35)
✗ SimulatedAnnealing Core Engine > Solution Quality > should handle unsolvable problems gracefully [32.85ms]
✓ SimulatedAnnealing Core Engine > Operator Statistics > should track operator attempts [0.61ms]
✓ SimulatedAnnealing Core Engine > Operator Statistics > should track operator success rates [0.56ms]
✓ SimulatedAnnealing Core Engine > Operator Statistics > should calculate success rate as improvements/attempts [0.56ms]
✓ SimulatedAnnealing Core Engine > Reheating Mechanism > should reheat when stuck in local minima [1.98ms]
✓ SimulatedAnnealing Core Engine > Reheating Mechanism > should not exceed maxReheats [32.40ms]
✓ SimulatedAnnealing Core Engine > Solution Output > should return complete solution object [0.78ms]
✓ SimulatedAnnealing Core Engine > Solution Output > should include violation details [0.45ms]
✓ SimulatedAnnealing Core Engine > Solution Output > should not mutate initial state [1.42ms]
✓ SimulatedAnnealing Core Engine > Edge Cases > should handle state with no assignments [0.18ms]
✓ SimulatedAnnealing Core Engine > Edge Cases > should handle single assignment state [0.11ms]
✓ SimulatedAnnealing Core Engine > Edge Cases > should handle very high temperature [0.39ms]
✓ SimulatedAnnealing Core Engine > Edge Cases > should handle very low cooling rate [0.17ms]

tests/core/fitness-calculation.test.ts:
✓ Fitness Calculation > Basic Fitness Calculation > should calculate 0 fitness for fully satisfied constraints [0.51ms]
✓ Fitness Calculation > Basic Fitness Calculation > should calculate high fitness for violated hard constraints [6.80ms]
✓ Fitness Calculation > Basic Fitness Calculation > should calculate fitness with soft constraint penalties [0.34ms]
✓ Fitness Calculation > Constraint Weighting > should weight hard constraints much higher than soft [6.42ms]
✓ Fitness Calculation > Constraint Weighting > should apply custom soft constraint weights correctly [0.16ms]
✓ Fitness Calculation > Constraint Weighting > should use default weight of 10 for soft constraints without explicit weight [0.09ms]
✓ Fitness Calculation > Partial Satisfaction > should handle partial constraint satisfaction (score = 0.5) [6.21ms]
✓ Fitness Calculation > Partial Satisfaction > should calculate fitness correctly for gradual improvements [20.48ms]
✓ Fitness Calculation > Multiple Constraints > should sum penalties from multiple hard constraints [4.79ms]
✓ Fitness Calculation > Multiple Constraints > should sum penalties from multiple soft constraints [0.19ms]
✓ Fitness Calculation > Multiple Constraints > should combine hard and soft penalties correctly [4.98ms]
✓ Fitness Calculation > Violation Counting > should count hard violations correctly using getViolations() [6.05ms]
✓ Fitness Calculation > Violation Counting > should count multiple violations from single constraint [5.43ms]
✓ Fitness Calculation > Violation Counting > should provide violation details [6.01ms]
✓ Fitness Calculation > Edge Cases > should handle constraint score = 0 (complete violation) [5.83ms]
✓ Fitness Calculation > Edge Cases > should handle constraint score = 1 (complete satisfaction) [0.23ms]
✓ Fitness Calculation > Edge Cases > should handle no constraints [0.12ms]
✓ Fitness Calculation > Edge Cases > should handle very large penalty values [5.32ms]
✓ Fitness Calculation > Edge Cases > should handle fractional scores correctly [6.03ms]

1 tests failed:
✗ SimulatedAnnealing Core Engine > Solution Quality > should handle unsolvable problems gracefully [32.85ms]

 72 pass
 1 fail
 133 expect() calls
Ran 73 tests across 4 files. [431.00ms]
```