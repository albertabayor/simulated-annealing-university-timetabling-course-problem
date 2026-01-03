# Analisis Paper: A General Mathematical Model for University Courses Timetabling

## Informasi Publikasi

- **Judul:** A General Mathematical Model for University Courses Timetabling: Implementation to a Public University in Malaysia
- **Penulis:** Zahidah Mohd Zaulir, Nurul Liyana Abdul Aziz, Nur Aidya Hanum Aizam*
- **Affiliasi:**
  - Faculty of Ocean Engineering Technology and Informatics, Universiti Malaysia Terengganu
  - Faculty of Computer and Mathematical Sciences, Universiti Teknologi MARA Cawangan Negeri Sembilan
- **Jurnal:** Malaysian Journal of Fundamental and Applied Sciences
- **Volume/Tahun:** Vol. 18 (2022), Halaman 82-94
- **Email:** aidya@umt.edu.my
- **License:** Creative Commons Attribution License
- **Status:** Published, Peer-reviewed

---

## Abstrak

Paper ini menyajikan **general mathematical model** untuk University Course Timetabling Problem (UCTP) yang mengakomodasi **various demands dan user preferences**.

**Masalah yang dihadapi:**
- Published articles mainly on improved solution approaches
- Different constraints used, ignoring human preferences
- Limited model application ke other universities

**Kontribusi:**
- Comprehensive requirements dari literature dan surveys
- General mathematical model dengan superset of constraints
- Termasuk user preferences
- Validasi dengan real data dari Malaysian university

**Keywords:** University course timetabling problem, Scheduling, Management problem, Integer programming, Mathematical model

---

## Latar Belakang

### University Course Timetabling Problem (UCTP)

**Definisi:**
Assigning courses taken oleh student groups, taught oleh lecturers, ke limited timeslots dalam appropriate classrooms.

**Constraints:**
- No conflicts antara rooms, students, dan lecturers
- Fulfill range of requirements/constraints

### Kategori Constraints

| Tipe | Deskripsi | Penalty |
|------|-----------|---------|
| **Hard** | Wajib dipenuhi, tidak boleh ada violation | Infeasible solution |
| **Soft** | Bisa violated tetapi mengurangi quality | Lower acceptance/satisfaction |

### 5 Main Requirements dalam Literatur

1. **Completeness** - Semua events assigned
2. **Conflict of resources** - Tidak ada conflict di timeslot
3. **Workload** - Batasan teaching/learning hours
4. **Availability** - Ketersediaan resources
5. **Meeting patterns** - Bagaimana classes di-assigned

---

## Survey-Based Requirements

### Requirements yang Dikumpulkan (a-v)

**Basic Requirements:**
- a) Completeness
- b) Room size limitation
- c) Availability of resources
- d) Conflict of resources (student groups, rooms, lecturers)
- e) Workload per day
- f) Maximum consecutive per day
- g-v) Various meeting patterns

### Requirements yang Dihapus (I-IV)

Paper ini menghapus 4 requirements yang dianggap contradicts/redundant/illogical:

| Dihapus | Alasan |
|---------|--------|
| **s) Max events/semester** | Lecturer programs sudah didesain sebelumnya |
| **t) Room capacity duplicate** | Sama dengan (b) |
| **u) Minimum events/day** | Irrelevant untuk large datasets |
| **v) Monotonically decreases** | Tidak dapat fulfilled dengan limited resources |

---

## Mathematical Model

### Notasi

**Sets:**
- C = Courses offered
- R = Rooms (different capacities and facilities)
- T = Timeslots available
- L = Lecturers
- G = Student groups
- D = Days of the week

**Subsets:**
- Cb = Laboratory courses
- Cl = Courses taught oleh lecturer l
- Cg = Courses dengan student group g
- Tlunch = Lunch break timeslots
- Teve = Evening sessions
- Tmorn = Morning sessions
- Tlate = Late evening sessions
- Tl = Unavailable timeslots untuk certain lecturers
- Cprac = Practical lectures
- Ctheo = Theory lectures

### Pairs untuk Meeting Patterns

| Symbol | Deskripsi |
|--------|-----------|
| **H** | Courses yang harus assigned simultaneously |
| **I** | Courses yang harus assigned consecutively, same day |
| **I'** | Courses yang tidak boleh consecutively, same day |
| **O** | Courses di same day |
| **O'** | Courses tidak di same day |
| **J** | Courses one after another (precedence) |
| **K** | Courses di morning dan afternoon sessions |

### Parameters

| Parameter | Deskripsi |
|-----------|-----------|
| RCr | Capacity of room r |
| CSc | Size of course c (student count) |
| Umax | Max courses/day untuk lecturer l |
| Vmax | Max courses/day untuk student group g |
| MCl | Max consecutive lectures/day untuk lecturer l |
| MCg | Max consecutive lectures/day untuk student group g |
| Pc,t,r | Lecturer preference (1=least, 5=most preferred) |
| Qc,r | Course c dapat assigned di room r |

### Decision Variables

$$
X_{c,t,r} = \begin{cases}
1, & \text{jika course c di timeslot t di room r} \\
0, & \text{otherwise}
\end{cases}
$$

### Objective Function

**Maximize lecturer preferences:**

$$
\max Z = \sum_{c} \sum_{t} \sum_{r} (P_{c,t,r} \times X_{c,t,r})
$$

**Preference scale:**
- 5 = Most preferred
- 4 = Preferred
- 3 = Neutral
- 2 = Not preferred
- 1 = Least preferred

---

## Constraints Formulation

### Table 1: Constraints in General Model

| Eq | Requirement | Mathematical Formulation |
|----|-------------|--------------------------|
| **(1)** | Completeness | $\sum_t \sum_r X_{c,t,r} = 1, \forall c$ |
| **(2)** | Room capacity | $C_{Sc} \times X_{c,t,r} \le R_{Cr}, \forall c, t, r$ |
| **(3)** | Timeslot unavailable | $\sum_c \sum_r X_{c,t,r} = 0, \forall t \in T_{un}$ |
| **(4)** | Room unavailable | $\sum_t X_{c,t,r} = 0, \forall (c,r) \in Q_{c,r}$ |
| **(5)** | Lecturer unavailable | $\sum_c X_{c,t,r} = 0, \forall r, t \in T_l$ |
| **(6)** | Student conflict | $\sum_c X_{c,t,r} \le 1, \forall t, g$ |
| **(7)** | Room conflict | $\sum_t X_{c,t,r} \le 1, \forall t, r$ |
| **(8)** | Lecturer conflict | $\sum_c \sum_r X_{c,t,r} \le 1, \forall t, l$ |
| **(9)** | Lecturer workload/day | $\sum_d \sum_t \sum_r X_{c,t,r} \le U^{max}, \forall d, l$ |
| **(10)** | Student workload/day | $\sum_d \sum_t \sum_r X_{c,t,r} \le V^{max}, \forall d, g$ |
| **(11)** | Lecturer consecutive | $\sum_r \sum_c (X_{c,t,r} + ... + X_{c,t+MC_l,r}) \le MC_l$ |
| **(12)** | Student consecutive | $\sum_r \sum_c (X_{c,t,r} + ... + X_{c,t+MC_g,r}) \le MC_g$ |
| **(13)** | Same day | $\sum_t \sum_r (X_{c_m,t,r} - X_{c_n,t,r}) = 0, \forall (c_m,c_n) \in O$ |
| **(14)** | Not same day | $\sum_t (X_{c_m,t,r} + X_{c_n,t,r}) \le 1, \forall (c_m,c_n) \in O'$ |
| **(15)** | Consecutive | $X_{c_m,t,r} - X_{c_n,t+1,r} = 0, \forall (c_m,c_n) \in I$ |
| **(16)** | Non-consecutive | $\sum_t (X_{c_m,t,r} + X_{c_n,t+1,r}) \le 1, \forall (c_m,c_n) \in I'$ |
| **(17)** | Morning-afternoon | $\sum_t X_{c_m,t,r} = \sum_t X_{c_n,t,r}, \forall (c_m,c_n) \in K$ |
| **(18)** | Simultaneous | $\sum_r (X_{c_m,t,r} - X_{c_n,t,r}) = 0, \forall (c_m,c_n) \in H$ |
| **(19)** | Avoid late evening | $\sum_c \sum_r X_{c,t,r} = 0, \forall t \in T_{late}$ |
| **(20)** | Precedence | $X_{c_m,t,r} - \sum_t X_{c_n,t,r} = 0, \forall (c_m,c_n) \in J$ |
| **(21)** | Gap (day off) | $\sum_t X_{c_i,t,r} + \sum_t X_{c_j,t,r} \le 1, \forall (c_m,c_n) \in O', d, r$ |
| **(22)** | Prayer times | $\sum_c X_{c,t,r} = 0, \forall t \in T_{lunch}$ |
| **(23)** | Theory in morning | $\sum_c \sum_r X_{c,t,r} = 0, \forall c \in C_{theo}, t \in T_{eve}$ |
| **(24)** | Practical in evening | $\sum_c \sum_r X_{c,t,r} = 0, \forall c \in C_{prac}, t \in T_{morn}$ |

---

## Hasil Eksperimen

### Dataset: Malaysian University

**Scale:**
- **1,098 lectures** (courses broken oleh credit hours)
- **141 rooms** (72 lecture + 69 laboratory)
- **55 timeslots** (11 per day + lunch)
- **194 lecturers**
- **124 student groups**

### Computational Results

**Hardware:**
- Core i7, 3.40 GHz
- 16GB RAM

**Software:**
- AIMMS optimization software
- CPLEX 12.9 solver

**Results:**
| Metric | Value |
|--------|-------|
| **Objective value** | 5,353 |
| **Maximum possible** | 5,490 |
| **Iterations** | 19,085 |
| **Time** | 1,340.19 seconds (~22 minutes) |
| **Relative gap** | 0% (optimal) |

### Lecturer Preferences Distribution

| Preference Level | Count | Percentage |
|-----------------|-------|------------|
| **5 (Most preferred)** | 1,006 | 91.8% |
| **4 (Second preferred)** | 60 | 5.5% |
| **3 (No preference)** | 19 | 1.7% |
| **2 (Not preferred)** | 7 | 0.6% |
| **1 (Least preferred)** | 4 | 0.4% |
| **Total** | 1,098 | 100% |

---

## Literature Review Summary

### Approaches untuk UCTP

| Peneliti | Metode | Kontribusi |
|----------|--------|-----------|
| **Lawrie** | Integer Programming | Earliest IP untuk timetabling |
| **Daskalaki et al.** | 0-1 IP | Minimize linear cost function |
| **Daskalaki & Birbas** | Two-stage relaxation | Time reduction + additional features |
| **Ribić & Konjicija** | Two-phase | Days → Slots |
| **Samarasekara** | Graph coloring | Alternative approach |
| **Gunawan & Ng** | Simulated Annealing | Metaheuristic approach |
| **Modibbo et al.** | Genetic Algorithm | Population-based |
| **Chen et al.** | Tabu Search | Memory-based |
| **Mahmud** | Ant Colony Optimization | Swarm intelligence |
| **Junn et al.** | Constraint Programming | Logic-based |

---

## Implikasi untuk Proyek Ini

### Relevansi

Paper ini sangat relevan karena:

1. **Comprehensive constraint list** - 24 constraints berbeda
2. **Survey-based requirements** - User preferences integration
3. **MILP formulation** - Mathematical foundation
4. **Real-world validation** - Malaysian university data
5. **Preference-based objective** - Lecturer preferences optimization

### Rekomendasi untuk Proyek

#### 1. Constraint Implementation

```javascript
/**
 * Comprehensive Constraints untuk UCTP
 * Berdasarkan 24 constraints dari Zaulir et al. (2022)
 */

class UCTPConstraints {
  /**
   * Eq (1): Completeness - All courses must be assigned
   */
  static checkCompleteness(solution) {
    const assignedCourses = new Set();

    for (const day of solution.days) {
      for (const timeslot of day.timeslots) {
        for (const room of timeslot.assignments) {
          assignedCourses.add(room.courseId);
        }
      }
    }

    const missing = solution.courses.filter(c => !assignedCourses.has(c.id));
    return {
      satisfied: missing.length === 0,
      missing: missing
    };
  }

  /**
   * Eq (2): Room capacity - Students tidak exceed room capacity
   */
  static checkRoomCapacity(solution) {
    const violations = [];

    for (const assignment of solution.allAssignments) {
      const room = solution.rooms.find(r => r.id === assignment.roomId);
      const course = solution.courses.find(c => c.id === assignment.courseId);

      if (course.studentCount > room.capacity) {
        violations.push({
          assignment: assignment,
          roomCapacity: room.capacity,
          studentCount: course.studentCount,
          excess: course.studentCount - room.capacity
        });
      }
    }

    return {
      satisfied: violations.length === 0,
      violations: violations
    };
  }

  /**
   * Eq (6-8): Conflict checks
   */
  static checkConflicts(solution) {
    const conflicts = {
      student: [],
      room: [],
      lecturer: []
    };

    // Check each timeslot
    for (const day of solution.days) {
      for (const timeslot of day.timeslots) {
        const studentMap = new Map(); // student group → assignments
        const roomMap = new Map(); // room → assignments
        const lecturerMap = new Map(); // lecturer → assignments

        for (const assignment of timeslot.assignments) {
          const course = solution.courses.find(c => c.id === assignment.courseId);

          // Check student conflicts
          for (const groupId of course.studentGroups) {
            if (studentMap.has(groupId)) {
              conflicts.student.push({
                timeslot: timeslot,
                group: groupId,
                existing: studentMap.get(groupId),
                new: assignment
              });
            } else {
              studentMap.set(groupId, assignment);
            }
          }

          // Check room conflicts
          if (roomMap.has(assignment.roomId)) {
            conflicts.room.push({
              timeslot: timeslot,
              room: assignment.roomId,
              existing: roomMap.get(assignment.roomId),
              new: assignment
            });
          } else {
            roomMap.set(assignment.roomId, assignment);
          }

          // Check lecturer conflicts
          if (lecturerMap.has(course.lecturerId)) {
            conflicts.lecturer.push({
              timeslot: timeslot,
              lecturer: course.lecturerId,
              existing: lecturerMap.get(course.lecturerId),
              new: assignment
            });
          } else {
            lecturerMap.set(course.lecturerId, assignment);
          }
        }
      }
    }

    return {
      satisfied: conflicts.student.length === 0 &&
                conflicts.room.length === 0 &&
                conflicts.lecturer.length === 0,
      conflicts: conflicts
    };
  }

  /**
   * Eq (9-10): Workload constraints
   */
  static checkWorkload(solution) {
    const violations = {
      lecturer: [],
      student: []
    };

    // Lecturer workload
    for (const lecturer of solution.lecturers) {
      for (const day of solution.days) {
        const dailyCount = solution.countAssignmentsForLecturerOnDay(lecturer.id, day.id);

        if (dailyCount > lecturer.maxPerDay) {
          violations.lecturer.push({
            lecturer: lecturer.id,
            day: day.id,
            count: dailyCount,
            max: lecturer.maxPerDay
          });
        }
      }
    }

    // Student group workload
    for (const group of solution.studentGroups) {
      for (const day of solution.days) {
        const dailyCount = solution.countAssignmentsForGroupOnDay(group.id, day.id);

        if (dailyCount > group.maxPerDay) {
          violations.student.push({
            group: group.id,
            day: day.id,
            count: dailyCount,
            max: group.maxPerDay
          });
        }
      }
    }

    return {
      satisfied: violations.lecturer.length === 0 &&
                violations.student.length === 0,
      violations: violations
    };
  }

  /**
   * Eq (11-12): Consecutive constraints
   */
  static checkConsecutive(solution) {
    const violations = {
      lecturer: [],
      student: []
    };

    // Check lecturer consecutive
    for (const lecturer of solution.lecturers) {
      for (const day of solution.days) {
        const maxConsecutive = lecturer.maxConsecutive;
        const assignments = solution.getAssignmentsForLecturerOnDay(lecturer.id, day.id);

        for (let i = 0; i <= assignments.length - maxConsecutive; i++) {
          let consecutive = 0;
          for (let j = 0; j < maxConsecutive; j++) {
            if (assignments[i + j]) consecutive++;
          }

          if (consecutive > maxConsecutive) {
            violations.lecturer.push({
              lecturer: lecturer.id,
              day: day.id,
              consecutive: consecutive,
              max: maxConsecutive
            });
          }
        }
      }
    }

    // Similar logic untuk student groups...

    return {
      satisfied: violations.lecturer.length === 0 &&
                violations.student.length === 0,
      violations: violations
    };
  }

  /**
   * Eq (13-21): Meeting patterns
   */
  static checkMeetingPatterns(solution) {
    const violations = [];

    // Eq (13): Same day - courses in O must be same day
    for (const [c1, c2] of solution.sameDayPairs) {
      const days1 = solution.getDaysForCourse(c1);
      const days2 = solution.getDaysForCourse(c2);

      if (!this.sameDay(days1, days2)) {
        violations.push({
          type: 'same_day',
          courses: [c1, c2],
          days1: days1,
          days2: days2
        });
      }
    }

    // Eq (14): Not same day - courses in O' must NOT be same day
    for (const [c1, c2] of solution.notSameDayPairs) {
      const days1 = solution.getDaysForCourse(c1);
      const days2 = solution.getDaysForCourse(c2);

      if (this.hasCommonDay(days1, days2)) {
        violations.push({
          type: 'not_same_day',
          courses: [c1, c2],
          commonDay: this.findCommonDay(days1, days2)
        });
      }
    }

    // Eq (15): Consecutive - courses in I must be consecutive
    for (const [c1, c2] of solution.consecutivePairs) {
      if (!this.areConsecutive(solution, c1, c2)) {
        violations.push({
          type: 'consecutive',
          courses: [c1, c2]
        });
      }
    }

    // Similar untuk other meeting patterns...

    return {
      satisfied: violations.length === 0,
      violations: violations
    };
  }

  /**
   * Eq (22-24): Time-based constraints
   */
  static checkTimeConstraints(solution) {
    const violations = [];

    // Eq (22): Prayer times / lunch breaks
    for (const assignment of solution.allAssignments) {
      if (solution.isPrayerTime(assignment.timeslot)) {
        violations.push({
          type: 'prayer_time',
          assignment: assignment
        });
      }
    }

    // Eq (23): Theory courses in morning only
    for (const assignment of solution.allAssignments) {
      const course = solution.courses.find(c => c.id === assignment.courseId);
      if (course.type === 'theory' && solution.isEvening(assignment.timeslot)) {
        violations.push({
          type: 'theory_evening',
          course: course.id,
          timeslot: assignment.timeslot
        });
      }
    }

    // Eq (24): Practical courses in evening only
    for (const assignment of solution.allAssignments) {
      const course = solution.courses.find(c => c.id === assignment.courseId);
      if (course.type === 'practical' && solution.isMorning(assignment.timeslot)) {
        violations.push({
          type: 'practical_morning',
          course: course.id,
          timeslot: assignment.timeslot
        });
      }
    }

    return {
      satisfied: violations.length === 0,
      violations: violations
    };
  }
}
```

#### 2. Preference-Based SA Objective Function

```javascript
/**
 * Preference-Based SA untuk UCTP
 * Berdasarkan Zaulir et al. (2022)
 */

class PreferenceBasedSA {
  constructor(config) {
    this.preferences = config.preferences || new Map(); // course -> (timeslot, room) -> preference
    this.saConfig = config.sa || {};
  }

  /**
   * Calculate fitness based on lecturer preferences
   * Preference scale: 1 (least) to 5 (most)
   */
  calculatePreferenceFitness(solution) {
    let totalPreference = 0;
    let penalty = 0;

    // Hard constraints (heavy penalty)
    const hardViolations = UCTPConstraints.checkAllHard(solution);
    penalty += hardViolations.count * 10000;

    // Soft constraints based on preferences
    for (const assignment of solution.allAssignments) {
      const key = `${assignment.courseId}_${assignment.timeslot}_${assignment.roomId}`;
      const pref = this.getPreference(assignment.courseId, assignment.timeslot, assignment.roomId);

      // Add to total (higher = better)
      totalPreference += pref;
    }

    // Maximize preference, minimize penalty
    return {
      score: totalPreference - penalty,
      totalPreference: totalPreference,
      penalty: penalty,
      maxPossible: solution.allAssignments.length * 5 // All preference 5
    };
  }

  /**
   * Get preference untuk assignment
   */
  getPreference(courseId, timeslot, room) {
    const key = `${courseId}_${timeslot}_${room}`;

    if (this.preferences.has(key)) {
      return this.preferences.get(key);
    }

    // Default: neutral preference
    return 3;
  }

  /**
   * Preference-aware neighbor generation
   */
  generatePreferenceAwareNeighbor(solution) {
    const neighbor = solution.clone();

    // Find assignments dengan low preference
    const lowPrefAssignments = this.findLowPreferenceAssignments(solution);

    if (lowPrefAssignments.length > 0) {
      // Try to improve one low-preference assignment
      const toImprove = lowPrefAssignments[0];
      const betterOptions = this.findBetterOptions(toImprove);

      if (betterOptions.length > 0) {
        // Reassign ke better option
        neighbor.reassign(toImprove, betterOptions[0]);
        return neighbor;
      }
    }

    // No improvement possible, random move
    return this.generateRandomNeighbor(solution);
  }

  /**
   * Find assignments dengan low preference (< 4)
   */
  findLowPreferenceAssignments(solution) {
    const lowPref = [];

    for (const assignment of solution.allAssignments) {
      const pref = this.getPreference(
        assignment.courseId,
        assignment.timeslot,
        assignment.roomId
      );

      if (pref < 4) {
        lowPref.push({
          assignment: assignment,
          preference: pref
        });
      }
    }

    // Sort by preference (lowest first)
    return lowPref.sort((a, b) => a.preference - b.preference);
  }

  /**
   * Find better options untuk assignment
   */
  findBetterOptions(assignment) {
    const currentPref = this.getPreference(
      assignment.courseId,
      assignment.timeslot,
      assignment.roomId
    );

    const better = [];

    // Try all combinations
    for (const timeslot of this.timeslots) {
      for (const room of this.rooms) {
        const newPref = this.getPreference(
          assignment.courseId,
          timeslot,
          room
        );

        if (newPref > currentPref) {
          better.push({
            timeslot: timeslot,
            room: room,
            preference: newPref
          });
        }
      }
    }

    return better.sort((a, b) => b.preference - a.preference);
  }

  /**
   * SA dengan preference-based objective
   */
  optimizeWithPreferences(instance) {
    let current = this.generateInitialSolution(instance);
    let best = current.clone();
    let T = this.saConfig.T0 || 1000;

    while (T > this.saConfig.Tf) {
      for (let i = 0; i < this.saConfig.iterationsPerTemp; i++) {
        // Generate preference-aware neighbor
        const neighbor = this.generatePreferenceAwareNeighbor(current);

        // Calculate fitness
        const currentFitness = this.calculatePreferenceFitness(current);
        const neighborFitness = this.calculatePreferenceFitness(neighbor);
        const delta = neighborFitness.score - currentFitness.score;

        // SA acceptance
        if (delta > 0 || Math.random() < Math.exp(delta / T)) {
          current = neighbor;

          // Update best
          if (currentFitness.score > this.calculatePreferenceFitness(best).score) {
            best = current.clone();
          }
        }
      }

      T *= this.saConfig.alpha || 0.995;
    }

    return best;
  }
}
```

---

## Kekurangan dan Keterbatasan Paper

### 1. Solver Dependency

- Menggunakan AIMMS + CPLEX (commercial)
- Tidak open-source
- Expensive untuk many institutions

### 2. Computational Time

- 1,340 seconds (~22 minutes) untuk 1,098 lectures
- Bisa lebih lama untuk larger instances
- Tidak scalable untuk real-time needs

### 3. Static Preferences

- Preferences di-input sebelum optimization
- Tidak dynamic atau adaptive
- Manual process untuk collect preferences

### 4. Single Objective

- Hanya maximize lecturer preferences
- Tidak mempertimbangkan student preferences
- Tidak multi-objective optimization

### 5. Dataset Terbatas

- Hanya 4 schools dari 1 university
- Tidak ada benchmark comparison
- Generalisability perlu validasi

---

## Arah Penelitian Lanjutan

### Research Gaps

#### 1. SA untuk Preference-Based UCTP

**Gap:**
Paper menggunakan MILP, bukan SA.

**Research direction:**
- SA untuk maximize lecturer preferences
- Compare SA vs MILP performance
- Hybrid approaches

#### 2. Dynamic Preference Handling

**Gap:**
Static preferences dalam model.

**Research direction:**
- SA dengan dynamic preference updates
- Real-time preference incorporation
- Learning-based preference prediction

#### 3. Multi-Objective Optimization

**Gap:**
Hanya lecturer preferences.

**Research direction:**
- Lecturer + Student preferences
- Preferences vs Resource utilization
- Pareto optimization dengan SA

#### 4. Open-Source Implementation

**Gap:**
Commercial solver dependency.

**Research direction:**
- SA dengan open-source tools
- Comparison CPLEX vs SA
- Cost-benefit analysis

---

## Kesimpulan

### Summary Temuan

1. **General mathematical model** dengan 24 constraints
2. **Survey-based requirements** - comprehensive list
3. **MILP approach** - CPLEX solver, 22 minutes runtime
4. **91.8% assignments** ke most preferred slots
5. **Real-world validation** - Malaysian university data

### Rekomendasi untuk Proyek

1. **Implement comprehensive constraints** - 24 constraints sebagai reference
2. **Preference-based objective** - Lecturer preferences optimization
3. **SA alternative ke MILP** - More accessible, open-source
4. **Meeting pattern constraints** - Consecutive, same day, etc.
5. **Time-based constraints** - Theory in morning, practical in evening

### Research Questions untuk Thesis

1. Dapatkah SA mengungguli MILP untuk preference-based UCTP?
2. Bagaimana mengoptimasi trade-off antara lecturer dan student preferences?
3. Apakah adaptive preference handling dapat meningkatkan solution acceptance?
4. Bagaimana scaling SA performance untuk instances similar ke paper (1,000+ lectures)?

---

## Referensi

- Zaulir, Z.M., Aziz, N.L.A., Aizam, N.H.H. (2022). "A General Mathematical Model for University Courses Timetabling: Implementation to a Public University in Malaysia." *Malaysian Journal of Fundamental and Applied Sciences*, 18, 82-94.
- Daskalaki, et al. "0-1 integer programming formulation."
- Lawrie. "Earliest IP untuk timetabling."
- Aizam, N.H.H., Caccetta, L. (2015). "Previous UCTP model."

---

*Analisis ini ditulis untuk mendukung penelitian tesis tentang University Course Timetabling Problem menggunakan Simulated Annealing.*
