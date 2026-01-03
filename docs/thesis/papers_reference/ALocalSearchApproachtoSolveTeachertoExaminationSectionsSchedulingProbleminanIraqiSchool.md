# Analisis Paper: A Local Search Approach to Solve Teacher to Examination Sections Scheduling Problem in an Iraqi School

## Informasi Publikasi

- **Judul:** A Local Search Approach to Solve Teacher to Examination Sections Scheduling Problem in an Iraqi School
- **Penulis:** Dalia Sami Jasim
- **Email:** daliasami99@gmail.com
- **Affiliasi:** Tidak disebutkan (Iraqi school context)
- **Tipe Paper:** Research Article / Case Study
- **Tahun:** Tidak disebutkan (dari konteks dan referensi, kemungkinan 2023-2024)
- **Domain:** Examination Timetabling (Proctor Assignment Problem)
- **Status:** Published journal article

---

## Abstrak

Paper ini mempresentasikan pendekatan **local search menggunakan Simulated Annealing** untuk menyelesaikan masalah **Proctor Assignment Problem (PAPt)** - assigning teachers to examination sections.

**Problem:**
- 43 examination sections vs 50 teachers
- 10 days of examination
- Assign teacher untuk setiap section per day
- Generate list of (teacher-section) dan list of teachers free of duty

**Constraints:**
- Hard: No teacher twice per day, no same teacher in same section for all 10 days
- Soft: Each teacher free of duty at least one day

**Results:**
- Successfully generates required timetable
- Execution time: **within 2 seconds**

**Keywords:** Timetable scheduling, simulated annealing, local search

---

## Latar Belakang

### Konteks: Iraqi Schools

**Situasi saat ini:**
- Increasing number of students vs fixed number of teachers
- Manual scheduling: 2-3 hours per day preparation
- Time-consuming dan inaccurate scheduling

**Examination schedule:**
- Twice per year
- Mid-year: 10 days
- End-year: 10 days

**Problems:**
- Increasing examination sections
- Need to assign teacher ke setiap section
- Staff preparation takes significant time

### Proctor Assignment Problem (PAPt)

**Definisi:**
Type of assignment problem where university assigns teaching assistants sebagai proctors dalam final exams.

**Karakteristik:**
- **NP-hard problem**
- Multidimensional assignment problem
- Part of Academic Scheduling Problems

**Academic Scheduling Categories:**
1. **Course timetabling** - Regular class scheduling
2. **Exam timetabling** - Examination scheduling

### Examination Timetable vs Course Timetable

| Aspect | Course Timetable | Exam Timetable |
|--------|------------------|----------------|
| **Concurrent events** | Not allowed | Allowed |
| **Duration** | Entire semester | Short period (10 days) |
| **Assignment** | Students, teachers, rooms | Exams, timeslots, rooms, invigilators |

---

## Literature Review

### Metaheuristics untuk Timetabling

| Peneliti | Metode | Kontribusi |
|----------|--------|-----------|
| **Martí et al.** | Scatter Search | Mixed-integer programming formulation |
| **Awad & Chinneck** | Hybrid GA | Initial assignment problem |
| **Koide** | MIP + Spreadsheet | Prototype system untuk proctor assignment |
| **Zhang et al.** | SA dengan new neighborhood | Series of swaps antar time slots |
| **Seyyedabbasi et al.** | HBA + SCSO | Hybrid metaheuristics |
| **Abdullah et al.** | Dual-sequence SA + RR | Round Robin untuk neighborhood selection |
| **Romaguera et al.** | Enhanced GA | Heuristic mutation untuk infeasible genes |
| **Jafari & Salmasi** | SA untuk Nurse Scheduling | Accurate solutions dalam reasonable time |

### Key Findings

1. **SA effective** untuk nurse scheduling dan timetabling
2. **Neighborhood structure** critical untuk SA performance
3. **Hybrid approaches** superior untuk NP-hard problems
4. **Dual-sequence SA** dengan Round Robin competitive

---

## Problem Description

### Dataset: Babylon Province School

**Scale:**
- **43 examination sections**
- **50 teachers**
- **10 examination days**

**Output requirements:**
1. List of (teacher-section) assignments
2. List of teachers free of duty per day

### Constraints

#### Hard Constraints (Wajib)

1. **No duplicate teacher per day**
   - Teacher name must NOT appear twice in a single day

2. **No same teacher untuk same section**
   - Exact teacher name must NOT appear in same section for all 10 days

#### Soft Constraints

1. **Minimum one day off**
   - Every teacher must be free of duty for at least one day

**Objective function:**

$$\min \sum (\text{repetition of exact teacher for all ten days}) \leq 9$$

---

## Metodologi

### Simulated Annealing Parameters

Based on Abdullah & Burke (2006):

| Parameter | Value |
|-----------|-------|
| **Initial temperature (T0)** | 5000 |
| **Final temperature (Tf)** | 0.05 |
| **Iterations (NumOfIte)** | 10,000,000 |
| **Cooling formula** | $a = (\log(T) - \log(0.05)) / \text{NumOfIte}$ |

### SA Pseudocode

```
ALGORITMA Simulated Annealing untuk Teacher-Section Assignment:

INPUT: Sections (43), Teachers (50), Days (10)
OUTPUT: Assignment matrix

1. Generate initial solution (satisfy hard constraints)
2. Set T = T0 = 5000
3. Set Tf = 0.05
4. Set NumOfIte = 10,000,000

5. WHILE T > Tf:
   a. Generate neighbor:
      - Find teacher appearing 10 times (no day off)
      - Find teacher appearing < 9 times
      - Exchange their assignments
      - Check hard constraints

   b. Calculate Δ = f(neighbor) - f(current)

   c. IF Δ < 0 OR random() < e^(-Δ/T):
        current = neighbor

   d. T = T - a (decrease temperature)

6. RETURN current solution
```

### Solution Structure

**Matrix representation:**
```
        Day 0  Day 1  Day 2  ...  Day 9
Sec 0: [  5  ][  12 ][  47 ] ... [  23 ]
Sec 1: [  15 ][  3  ][  31 ] ... [  8  ]
...
Sec 42:[  49 ][  21 ][  7  ] ... [  35 ]

Values: Teacher IDs (0-49)
```

**Conversion:**
- Integer values → Teacher names via lookup file
- Matrix → Text file ready untuk use

---

## Neighborhood Structure

### Key Innovation

**Problem-specific neighborhood:**
Exchange values that make solution **far from feasible** dengan values that make solution **near to optimality**

### Algorithm

```
GENERATE NEIGHBOR:

1. Identify problem:
   - Find teacher T1 appearing 10 times (no day off)
   - This violates soft constraint

2. Find solution:
   - Find teacher T2 appearing < 9 times (has day off)
   - Can substitute T1 with T2

3. Exchange:
   - Replace some T1 assignments dengan T2

4. Validate:
   - Check hard constraints not violated
   - If violated, find alternative T2

5. Return new solution
```

### Heuristic Behavior

- **Targeted exchange** - Only swap problematic assignments
- **Constraint-aware** - Validates hard constraints after swap
- **Soft-constraint focused** - Specifically addresses day-off requirement

---

## Fitness Function

### Objective

Minimize number of teachers assigned to examination sections untuk 10 times (no day off).

### Calculation

```
f(solution) = Σ (teachers with 10 assignments)

Ideal: f(solution) = 0
Every teacher has ≤ 9 assignments (at least 1 day off)
```

### Penalty Structure

| Teacher assignments | Penalty |
|---------------------|---------|
| **10 times** | 1 (violates soft constraint) |
| **≤ 9 times** | 0 (satisfies soft constraint) |

---

## Hasil Eksperimen

### Implementation

**Platform:**
- Language: Java
- IDE: NetBeans IDE 8.2
- Algorithm: Simulated Annealing

### Performance

| Metric | Value |
|--------|-------|
| **Execution time** | Within 2 seconds untuk 10 days |
| **Solution quality** | Optimal (all teachers get day off) |
| **Iterations** | Up to 10,000,000 |
| **Convergence** | Successful |

### Visualization

**Figure 3:** Result of multiple executions vs iterations
- Shows convergence pattern
- Demonstrates escape dari local optimum

**Figure 4:** Resulted integer matrix
- Example output matrix
- 43 rows × 10 columns

**Figure 5:** Text file output (single day example)
- Section numbers
- Teacher names
- List of out-of-duty teachers

### User Satisfaction

> "Our result satisfies all the persons in charge and it is very practical"

**Benefits:**
1. **Fast** - 2 seconds vs 2-3 hours manual
2. **Accurate** - No human errors
3. **Flexible** - Different distribution every execution
4. **Practical** - Ready-to-use text file output

---

## Implikasi untuk Proyek Ini

### Relevansi

Paper ini sangat relevan karena:

1. **Direct SA application** untuk timetabling
2. **Specific neighborhood structure** design
3. **Real-world validation** dengan actual school data
4. **Fast execution** - 2 seconds untuk complete solution

### Rekomendasi untuk Proyek

#### 1. Neighborhood Structure Design

Paper ini menunjukkan importance dari problem-specific neighborhood:

```javascript
/**
 * Problem-Specific Neighborhood untuk UCTP
 * Berdasarkan Jasim (2024)
 */

class ProblemSpecificNeighborhood {
  constructor(problem) {
    this.problem = problem;
    this.violationAnalyzers = [
      new TeacherConflictAnalyzer(),
      new StudentConflictAnalyzer(),
      new RoomConflictAnalyzer()
    ];
  }

  /**
   * Generate targeted neighbor
   * Focus pada resolving specific violations
   */
  generateTargetedNeighbor(solution) {
    // Step 1: Analyze current solution untuk violations
    const violations = this.analyzeViolations(solution);

    if (violations.length === 0) {
      // No violations, generate random neighbor
      return this.generateRandomNeighbor(solution);
    }

    // Step 2: Select most critical violation
    const criticalViolation = this.selectMostCritical(violations);

    // Step 3: Generate neighbor yang addresses this violation
    return this.generateRepairingNeighbor(solution, criticalViolation);
  }

  /**
   * Analyze solution untuk constraint violations
   */
  analyzeViolations(solution) {
    const violations = [];

    for (const analyzer of this.violationAnalyzers) {
      const found = analyzer.find(solution);
      violations.push(...found);
    }

    return violations;
  }

  /**
   * Select most critical violation
   * Priority: Hard > Soft, Severity, Frequency
   */
  selectMostCritical(violations) {
    // Sort by priority
    const sorted = violations.sort((a, b) => {
      // Hard constraints first
      if (a.type === 'hard' && b.type === 'soft') return -1;
      if (a.type === 'soft' && b.type === 'hard') return 1;

      // Then by severity
      return b.severity - a.severity;
    });

    return sorted[0];
  }

  /**
   * Generate neighbor yang repairs specific violation
   */
  generateRepairingNeighbor(solution, violation) {
    const neighbor = solution.clone();

    switch (violation.type) {
      case 'teacher_conflict':
        return this.repairTeacherConflict(neighbor, violation);

      case 'student_conflict':
        return this.repairStudentConflict(neighbor, violation);

      case 'room_conflict':
        return this.repairRoomConflict(neighbor, violation);

      case 'no_day_off':
        return this.repairDayOff(neighbor, violation);

      default:
        return this.generateRandomNeighbor(solution);
    }
  }

  /**
   * Repair: Teacher has no day off (seperti dalam paper)
   */
  repairDayOff(solution, violation) {
    const teacherId = violation.teacherId;
    const assignments = solution.getAssignmentsForTeacher(teacherId);

    // Teacher appears every day (10 assignments)
    // Need to replace one assignment dengan teacher who has day off

    // Find teacher dengan < 9 assignments (has day off)
    const availableTeachers = this.findTeachersWithDayOff(solution);

    for (const replacementId of availableTeachers) {
      // Try replacing each assignment
      for (const assignment of assignments) {
        const neighbor = solution.clone();

        // Replace assignment
        neighbor.assignments[assignment.day][assignment.section] = replacementId;

        // Check hard constraints
        if (!this.hasHardConflicts(neighbor)) {
          return neighbor; // Valid neighbor found
        }
      }
    }

    // No valid replacement found
    return solution;
  }

  /**
   * Find teachers dengan day off (less than max assignments)
   */
  findTeachersWithDayOff(solution) {
    const maxAssignments = solution.days; // e.g., 10
    const teachers = [];

    for (const teacherId of solution.teacherIds) {
      const count = solution.countAssignmentsForTeacher(teacherId);

      if (count < maxAssignments) {
        teachers.push(teacherId);
      }
    }

    return teachers;
  }

  /**
   * Check hard constraints
   */
  hasHardConflicts(solution) {
    // HC1: No teacher twice per day
    for (const day of solution.days) {
      const teachers = new Set();
      for (const section of solution.sections) {
        const teacher = solution.assignments[day][section];
        if (teachers.has(teacher)) return true;
        teachers.add(teacher);
      }
    }

    // HC2: No same teacher in same section untuk all days
    for (const section of solution.sections) {
      const teachers = new Set();
      for (const day of solution.days) {
        const teacher = solution.assignments[day][section];
        teachers.add(teacher);
      }
      if (teachers.size === 1) return true; // Same teacher
    }

    return false;
  }
}

/**
 * Violation Analyzer untuk Teacher Conflicts
 */
class TeacherConflictAnalyzer {
  find(solution) {
    const violations = [];

    for (const day of solution.days) {
      const teacherMap = new Map(); // teacher -> list of sections

      for (const section of solution.sections) {
        const teacher = solution.assignments[day][section];

        if (!teacherMap.has(teacher)) {
          teacherMap.set(teacher, []);
        }

        teacherMap.get(teacher).push(section);
      }

      // Check conflicts
      for (const [teacher, sections] of teacherMap) {
        if (sections.length > 1) {
          violations.push({
            type: 'teacher_conflict',
            severity: sections.length,
            teacher: teacher,
            day: day,
            sections: sections
          });
        }
      }
    }

    return violations;
  }
}
```

#### 2. Fast SA dengan Smart Initialization

Paper ini menggunakan smart initialization yang satisfies hard constraints:

```javascript
/**
 * Smart Initial Solution Generator
 * Berdasarkan Jasim (2024)
 */

class SmartInitialSolution {
  constructor(problem) {
    this.sections = problem.sections;
    this.teachers = problem.teachers;
    this.days = problem.days;
  }

  /**
   * Generate initial solution satisfying hard constraints
   */
  generate() {
    const solution = this.createEmptySolution();

    for (const day of this.days) {
      for (const section of this.sections) {
        let assigned = false;

        // Try assign teacher
        while (!assigned) {
          const teacher = this.selectRandomTeacher();

          // Check hard constraints
          if (this.satisfiesHardConstraints(solution, teacher, day, section)) {
            solution.assign(teacher, day, section);
            assigned = true;
          }
        }
      }
    }

    return solution;
  }

  /**
   * Check if assignment satisfies hard constraints
   */
  satisfiesHardConstraints(solution, teacher, day, section) {
    // HC1: Teacher not already assigned di this day
    if (solution.isTeacherAssignedOnDay(teacher, day)) {
      return false;
    }

    // HC2: Teacher not already assigned di this section
    // (untuk all days - need to check)
    // Note: This is simplified - real implementation more complex

    return true;
  }

  /**
   * Optimized SA untuk timetabling
   */
  optimize(initialSolution) {
    let current = initialSolution;
    let T = 5000;
    const Tf = 0.05;
    const maxIterations = 10000000;
    const alpha = (Math.log(T) - Math.log(Tf)) / maxIterations;

    while (T > Tf) {
      // Generate targeted neighbor
      const neighbor = this.generateTargetedNeighbor(current);

      // Evaluate
      const delta = this.evaluate(neighbor) - this.evaluate(current);

      // Accept or reject
      if (delta < 0 || Math.random() < Math.exp(-delta / T)) {
        current = neighbor;
      }

      // Cool down
      T -= alpha;
    }

    return current;
  }

  /**
   * Generate targeted neighbor (problem-specific)
   */
  generateTargetedNeighbor(solution) {
    // Find teachers violating soft constraint (no day off)
    const overworked = this.findOverworkedTeachers(solution);

    if (overworked.length > 0) {
      // Try to fix overworked teacher
      return this.fixOverworkedTeacher(solution, overworked[0]);
    }

    // No violations, random move
    return this.generateRandomNeighbor(solution);
  }

  /**
   * Find teachers dengan no day off
   */
  findOverworkedTeachers(solution) {
    const overworked = [];
    const maxDays = this.days.length;

    for (const teacher of this.teachers) {
      const assignedDays = solution.getAssignedDaysForTeacher(teacher);

      if (assignedDays.length >= maxDays) {
        overworked.push(teacher);
      }
    }

    return overworked;
  }
}
```

#### 3. Output Conversion untuk Practical Use

```javascript
/**
 * Solution Converter untuk Practical Output
 * Berdasarkan text file output dari paper
 */

class SolutionConverter {
  constructor(teacherNames, sectionNames) {
    this.teacherNames = teacherNames; // Map ID -> Name
    this.sectionNames = sectionNames; // Map ID -> Name
  }

  /**
   * Convert integer matrix to text file
   */
  convertToTextFile(solutionMatrix) {
    const lines = [];

    for (let day = 0; day < solutionMatrix[0].length; day++) {
      lines.push(`=== DAY ${day + 1} ===`);
      lines.push('');
      lines.push('ASSIGNMENTS:');
      lines.push('Section | Teacher');

      const assignedTeachers = new Set();

      for (let section = 0; section < solutionMatrix.length; section++) {
        const teacherId = solutionMatrix[section][day];
        const teacherName = this.teacherNames[teacherId];
        const sectionName = this.sectionNames[section];

        lines.push(`${sectionName} | ${teacherName}`);
        assignedTeachers.add(teacherId);
      }

      lines.push('');
      lines.push('FREE DUTY TEACHERS:');

      for (const [id, name] of Object.entries(this.teacherNames)) {
        if (!assignedTeachers.has(parseInt(id))) {
          lines.push(name);
        }
      }

      lines.push('');
      lines.push(''.repeat(50));
    }

    return lines.join('\n');
  }

  /**
   * Generate summary statistics
   */
  generateStatistics(solutionMatrix) {
    const stats = {
      totalAssignments: 0,
      assignmentsPerTeacher: new Map(),
      dayOffsPerTeacher: new Map(),
      sectionAssignmentsPerDay: []
    };

    // Count assignments per teacher
    for (const teacherId of Object.keys(this.teacherNames)) {
      stats.assignmentsPerTeacher.set(teacherId, 0);
      stats.dayOffsPerTeacher.set(teacherId, 0);
    }

    for (let day = 0; day < solutionMatrix[0].length; day++) {
      const dayAssignments = [];

      for (let section = 0; section < solutionMatrix.length; section++) {
        const teacherId = solutionMatrix[section][day];
        dayAssignments.push(teacherId);
        stats.assignmentsPerTeacher.set(
          teacherId,
          stats.assignmentsPerTeacher.get(teacherId) + 1
        );
      }

      stats.sectionAssignmentsPerDay.push(dayAssignments);
    }

    // Calculate day offs
    const totalDays = solutionMatrix[0].length;
    for (const [teacherId, assignments] of stats.assignmentsPerTeacher) {
      const dayOffs = totalDays - assignments;
      stats.dayOffsPerTeacher.set(teacherId, dayOffs);
    }

    stats.totalAssignments = solutionMatrix.length * totalDays;

    return stats;
  }
}
```

---

## Kekurangan dan Keterbatasan Paper

### 1. Limited Dataset

- Hanya satu school (43 sections, 50 teachers)
- Tidak ada generalization ke other schools
- Tidak ada benchmark comparisons

### 2. Simple Problem Instance

- Hanya 2 hard constraints
- Hanya 1 soft constraint
- Real-world UCTP biasanya jauh lebih complex

### 3. Parameter Values Tidak Dioptimasi

- Menggunakan parameters dari Abdullah & Burke (2006)
- Tidak ada sensitivity analysis
- 10 million iterations mungkin excessive

### 4. Kurang Detail dalam Implementasi

- Tidak ada pseudocode lengkap
- Cooling formula tidak jelas
- Neighborhood generation tidak detail

### 5. Tidak Ada Statistical Validation

- Hanya "satisfies all persons in charge"
- Tidak ada quantitative comparison
- Tidak ada variance analysis

---

## Arah Penelitian Lanjutan

### Research Gaps

#### 1. Extended Neighborhood Structures

**Gap:**
Hanya simple exchange strategy.

**Research direction:**
- Multiple neighborhood structures
- Adaptive neighborhood selection
- Complex moves (Kempe chains, swap multiple)

#### 2. Multi-Objective Optimization

**Gap:**
Hanya single objective (minimize teachers with no day off).

**Research direction:**
- Balance teacher preferences
- Minimize total assignments variance
- Maximize fairness

#### 3. Dynamic Constraints Handling

**Gap:**
Static constraints throughout search.

**Research direction:**
- Weighted constraints yang adapt
- Priority-based constraint handling
- Real-time constraint updates

#### 4. Scalability Analysis

**Gap:**
Hanya one instance size tested.

**Research direction:**
- Performance scaling dengan size
- Large instances (hundreds of sections/teachers)
- Distributed SA approaches

---

## Kesimpulan

### Summary Temuan

1. **SA effective** untuk teacher-section assignment (PAPt)
2. **Problem-specific neighborhood** critical untuk performance
3. **Fast execution** - 2 seconds untuk complete solution
4. **Smart initialization** satisfies hard constraints
5. **Real-world validation** - Practical use di Iraqi school

### Rekomendasi untuk Proyek

1. **Design problem-specific neighborhood** - Target constraint violations
2. **Smart initialization** - Start dengan feasible solution
3. **Fast SA implementation** - 2 seconds achievable
4. **Practical output** - Ready-to-use text format
5. **Test dengan real data** - Validate dengan actual institutions

### Research Questions untuk Thesis

1. Dapatkah problem-specific neighborhood SA mengungguli generic SA untuk UCTP?
2. Bagaimana mengoptimasi neighborhood selection strategy secara adaptive?
3. Apakah smart initialization menghasilkan better final solutions?
4. Bagaimana scaling SA performance untuk larger instances?

---

## Referensi

- Jasim, D.S. "A Local Search Approach to Solve Teacher to Examination Sections Scheduling Problem in an Iraqi School."
- Abdullah, S., Burke, E.K. (2006). "A Multi-start Very Large Neighbourhood Search Approach with Local Search Methods for Examination Timetabling." ICAPS 2006.
- Zhang, D., et al. (2010). "A Simulated Annealing with a New Neighborhood Structure Based Algorithm for High School Timetabling Problems." *European Journal of Operational Research*, 203, 550-558.

---

*Analisis ini ditulis untuk mendukung penelitian tesis tentang University Course Timetabling Problem menggunakan Simulated Annealing.*
