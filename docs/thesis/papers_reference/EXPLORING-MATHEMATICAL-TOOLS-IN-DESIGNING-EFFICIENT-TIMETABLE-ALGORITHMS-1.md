# Analisis Paper: Exploring Mathematical Tools in Designing Efficient Timetable Algorithms

## Informasi Publikasi

- **Judul:** Exploring Mathematical Tools in Designing Efficient Timetable Algorithms
- **Penulis:** Poonam Kumari, Dr. Vineeta Basotia, Dr. Harmendra Kumar Mandia
- **Affiliasi:** Shri JJT University, Rajasthan, India
- **Jurnal:** Anveshana's International Journal of Research in Engineering and Applied Sciences (AIJREAS)
- **Volume/Issue:** Vol. 9, Issue 08
- **Bulan/Tahun:** August 2024
- **ISSN:** 2455-6300 (Online)
- **Email:** anveshanaindia@gmail.com
- **Website:** www.anveshanaindia.com
- **Halaman:** 30-37
- **Tipe Paper:** Review / Case Study

---

## Abstrak

Paper ini mengeksplorasi **mathematical tools** untuk merancang efficient timetable algorithms. Fokus pada:

1. Mathematical models dan algorithms untuk faculty course assignment
2. Integer programming sebagai tools untuk academic course assignments
3. Fuzzy preferences-based method untuk faculty course scheduling
4. Optimization resource timetables untuk faculty course schedules

**Keywords:** Mathematical models, algorithms, timetables, educational institutions

---

## Latar Belakang

### University Course Timetabling Problem (UCTP)

**Definisi:**
Assignment of specified events (lessons, exams) into time slots or classes.

**Karakteristik:**
- **NP-hard problem**
- No deterministic polynomial time algorithm known
- Traditional computer-based methods fall short
- Knowledge-based atau OR-based methodologies: slow dan rigid

### Jenis Timetabling di Universitas

| Tipe | Deskripsi |
|------|-----------|
| **Course Planning** | Hanya satu group course dan satu course per timeslot |
| **Exam Planning** | Multiple events dapat scheduled concurrently |

### Perbedaan Utama

**Course Planning:**
- Hanya satu group course per timeslot
- Hanya satu course total per timeslot

**Exam Planning:**
- Multiple events dapat scheduled concurrently
- Common periods dan classes dapat digunakan bersama

---

## Literature Review

### Algethami & Laesanklang (2021)

**Fokus:** Multi-objective mixed-integer programming model untuk preregistration UCTP dengan faculty-related constraints

**Objective:**
- Maximize faculty members' happiness
- Follow university standards
- Minimize unscheduled activities
- Minimize student learning days

**Validation:** 8 various real-world scenarios

### AbdoulRjoub (2020)

**Fokus:** Automated school scheduling menggunakan improved Hill Climbing algorithms

**Hasil:**
- Initial solution improved by **72%** dalam 5 seconds
- **50%** improvement dalam second iteration
- Optimal solution setelah 15 iterations

### Anderson Goes (2019)

**Fokus:** School timetabling dengan operational research methodology

**Methods:**
- Non Linear Binary Integer Programming (NLBIP)
- Local Search (LS)
- Iterated Local Search (ILS)

**Hasil:**
- ILS: 3.5-7.7% lower dispersion than best solution
- ILS: 15-338 times quicker computational time

### Mohd Rahman (2018)

**Fokus:** Evaluation of optimization algorithms untuk course scheduling

**Classification:**
1. Hard Constraints vs Soft Constraints
2. Optimization Methods

**Finding:** Meta-heuristics adalah most frequently used method

---

## Mathematical Tools yang Dibahas

### 1. Linear Programming (LP)

**Application:** Faculty course assignment activities

**Formulation:**
Activities untuk faculty course assignment dilakukan sebagai linear programmers.

**Use case:** Creating mathematical models atau algorithms untuk solve faculty course assignment problem.

### 2. Integer Programming (IP)

**Application:** Academic course assignments

**Status:** One of the newest tools untuk dealing dengan academic course assignment problems.

**Advantage:** Can handle discrete decisions (assign atau tidak assign).

### 3. Fuzzy Preferences-Based Method

**Application:** Faculty course scheduling difficulties

**Approach:** Method based pada fuzzy preferences untuk handle faculty-related constraints.

**Use case:** Mengoptimasi resource timetables dan producing course schedules untuk faculty members.

---

## University Timetabling Regulations

### Hard Constraints (Wajib)

1. **No teacher conflicts:** Setiap teacher hanya satu class per timeslot
2. **All classes scheduled:** Semua classes harus mengikuti plan
3. **Room concordance:** Semua planned rooms harus concordance dengan guidance
4. **Teaching load limits:** Teacher's teaching load tidak boleh exceed established limit
5. **Course hours completion:** Total hours untuk course harus established

**Scheduling conflicts terjadi jika:**
- Two atau lebih classes untuk same teacher di same time
- Two atau lebih classrooms assigned ke same course dan group di same time
- Two atau lebih teachers assigned ke same group untuk independent courses di same time

### Soft Constraints (Preferensi)

1. **Teacher time preferences** dihormati sebisa mungkin
2. **Subject preferences:** Setiap faculty dapat name favorite subject area

---

## Genetic Algorithms untuk UCTP

### Prinsip Dasar

GA berdasarkan ideas of genetics dan natural selection:
- Healthiest population members chosen
- Mix dengan population lain (crossover)
- Mutate into new forms (mutation)
- Establish new groups

### Penerapan pada Timetabling

```
GA untuk UCTP:
├── Population of solutions
├── Fitness evaluation (constraint satisfaction)
├── Selection (fittest chosen)
├── Crossover (mix solutions)
├── Mutation (random changes)
└── New generation
```

### Karakteristik UCTP

- Memerlukan instructors dan students bekerja sama
- Arrange scheduling multiple classes dalam limited time
- Adhere berbagai regulations
- Complexity meningkat dengan school size

---

## Memetic Algorithm untuk UCTP

### Konsep

Memetic Algorithm = **Genetic Algorithm + Local Search**

Kombinasi global search (GA) dan local optimization (LS) untuk:
- Better convergence
- Escape local optima
- Balance exploration dan exploitation

### Keunggulan

- GA provides global exploration
- LS provides local exploitation
- Hybrid approach lebih effective dari masing-masing secara terpisah

---

## Case Study: XYZ Institution

### Dataset

- **8 tenured faculty members**
- **4 new faculty members**
- **Total:** 12 faculty members
- **Courses:** 20 courses untuk di-assign

### Administrator Preferences

**Preference levels:** 1 (highest) sampai 4 (lowest)

**Contoh interpretation:**
- Course 3 → 3rd option untuk faculty
- Course 6 → 4th choice
- Course 13 → 1st choice untuk F' faculty
- Blank → course tidak akan assigned ke faculty tersebut

### Implementation Details

**Hardware:**
- Intel(R) Core(TM) i3-7100 CPU @ 2.50GHz
- 32GB Hard Disk
- 4GB RAM
- Windows 7, 32-bit

**Software:**
- Matrix Laboratory 8.6 (MATLAB)
- LINGO software untuk optimization

**Methods:**
1. Mixed Integer Linear Programming (MILP)
2. Enhanced Simulated Annealing (ESA)
3. SA + GA hybrid

### Mathematical Formulation

#### Variables

$x_{ij}$ = assignment dari course $i$ ke faculty $j$

$x_r$ = new variables untuk computational simplicity
- Contoh: $x_1$ = 1st course ke 2nd faculty
- Contoh: $x_{45}$ = 9th course ke 6th faculty

#### Objective Functions

$f_k$ = faculty preference levels untuk courses yang di-assign

**Goal:** Minimize total preference violations

### Hasil Komputasi

#### Table 3: Courses Assigned to Faculty

Setiap faculty mendapat course assignments sesuai dengan preference levels.

**Interpretasi:**
- $x_{14}$ = 3rd course ke 1st faculty, ideal value = 1
- Semua courses assigned dengan similar fashion

#### Table 4: Objective Function Values (menggunakan Linear Membership Function)

| Objective | $f_1$ | $f_2$ | $f_3$ | ... | $f_{15}$ |
|-----------|-------|-------|-------|-----|---------|
| **Values** | 1 | 1 | 2 | ... | 2 |

**O, M, P values:** Not clearly explained dalam paper

---

## Methodology

### Two-Phase Approach

Paper ini menggunakan **two-phase technique**:

**Rationale:**
- Memberikan algorithms bigger search field di first phase
- Meet hard constraints sambil ignoring soft constraints
- Solve timetabling issues secara structured

#### Phase 1: Hard Constraint Satisfaction

- Focus pada meeting mandatory constraints
- Ignore soft constraints temporarily
- Generate feasible solutions

#### Phase 2: Soft Constraint Optimization

- Optimize soft constraints
- Improve solution quality
- Incorporate preferences

### Metaheuristic-Based Solutions

Paper ini mengusulkan metaheuristic-based solutions:

1. **Evolutionary Algorithms** (termasuk GA)
2. **Simulated Annealing**
3. **Tabu Search**
4. **Ant Colony Optimization**
5. **Honey Bee Algorithms**

**Universal algorithmic framework** yang dapat dimodifikasi untuk:
- Timetabling challenges
- Combinatorial optimization issues
- Various problem domains

---

## Implikasi untuk Proyek Ini

### Relevansi

Paper ini relevan untuk proyek Anda karena:

1. **Comprehensive overview** dari mathematical tools untuk timetabling
2. **Two-phase approach** yang dapat diadaptasi untuk SA
3. **Metaheuristics comparison** termasuk SA
4. **Real case study** dengan faculty preferences

### Rekomendasi untuk Proyek

#### 1. Two-Phase SA Implementation

```javascript
/**
 * Two-Phase Simulated Annealing
 * Berdasarkan framework dari Kumari et al. (2024)
 */

class TwoPhaseSA {
  constructor(config) {
    // Phase 1: Hard constraint satisfaction
    this.phase1Config = config.phase1 || {
      T0: 1000,
      Tf: 0.1,
      alpha: 0.99,
      focus: 'hard'
    };

    // Phase 2: Soft constraint optimization
    this.phase2Config = config.phase2 || {
      T0: 100,
      Tf: 0.01,
      alpha: 0.995,
      focus: 'soft'
    };
  }

  /**
   * Phase 1: Hard Constraint Satisfaction
   * Focus: Feasible solution generation
   */
  phase1(instance) {
    const sa = new SimulatedAnnealing({
      ...this.phase1Config,
      fitnessFunction: (solution) => {
        // Heavy penalty untuk hard constraint violations
        return this.hardConstraintPenalty(solution);
      }
    });

    // Generate feasible solution
    const feasible = sa.optimize(instance);

    console.log('Phase 1 complete: Feasible solution found');
    return feasible;
  }

  /**
   * Phase 2: Soft Constraint Optimization
   * Focus: Quality improvement
   */
  phase2(feasibleSolution) {
    const sa = new SimulatedAnnealing({
      ...this.phase2Config,
      initialState: feasibleSolution,
      fitnessFunction: (solution) => {
        // Soft constraints (preferences)
        return this.softConstraintPenalty(solution);
      }
    });

    // Optimize soft constraints
    const optimized = sa.optimize();

    console.log('Phase 2 complete: Soft constraints optimized');
    return optimized;
  }

  /**
   * Hard constraint penalty
   */
  hardConstraintPenalty(solution) {
    let penalty = 0;

    // HC1: Teacher conflicts
    penalty += this.countTeacherConflicts(solution) * 1000;

    // HC2: Student conflicts
    penalty += this.countStudentConflicts(solution) * 1000;

    // HC3: Room conflicts
    penalty += this.countRoomConflicts(solution) * 1000;

    // HC4: Teaching load limits
    penalty += this.checkLoadViolations(solution) * 1000;

    return penalty;
  }

  /**
   * Soft constraint penalty
   */
  softConstraintPenalty(solution) {
    let penalty = 0;

    // SC1: Teacher time preferences
    penalty += this.calculateTimePreferenceViolation(solution);

    // SC2: Subject preferences
    penalty += this.calculateSubjectPreferenceViolation(solution);

    // SC3: Compactness
    penalty += this.calculateCompactnessPenalty(solution);

    return penalty;
  }

  /**
   * Solve UCTP menggunakan two-phase approach
   */
  solve(instance) {
    console.log('Starting two-phase SA...');

    // Phase 1: Generate feasible solution
    const feasible = this.phase1(instance);

    if (feasible.penalty > 0) {
      console.warn('Phase 1 failed to find feasible solution');
      return feasible;
    }

    // Phase 2: Optimize soft constraints
    const optimized = this.phase2(feasible);

    return optimized;
  }
}
```

#### 2. Faculty Preference Modeling

```javascript
/**
 * Faculty Preference System
 * Berdasarkan case study dari Kumari et al. (2024)
 */

class FacultyPreferenceModel {
  constructor() {
    // Preference levels: 1 (highest) to 4 (lowest)
    this.preferenceLevels = {
      P1: 1, // First choice
      P2: 2, // Second choice
      P3: 3, // Third choice
      P4: 4, // Fourth choice
      NONE: null // Not assigned
    };
  }

  /**
   * Calculate preference score untuk assignment
   */
  calculatePreferenceScore(facultyId, courseId) {
    const preference = this.getPreference(facultyId, courseId);

    if (preference === null) {
      return 1000; // High penalty jika tidak preferred
    }

    // Lower preference level = higher penalty
    return preference * 10;
  }

  /**
   * Get preference level untuk faculty-course pair
   */
  getPreference(facultyId, courseId) {
    // Check preference table
    return this.preferenceTable[facultyId]?.[courseId] || null;
  }

  /**
   * Calculate total preference violation untuk solution
   */
  calculateTotalPreferenceViolation(solution) {
    let totalPenalty = 0;

    for (const [facultyId, assignments] of solution.facultyAssignments) {
      for (const course of assignments) {
        totalPenalty += this.calculatePreferenceScore(facultyId, course.id);
      }
    }

    return totalPenalty;
  }

  /**
   * Linear membership function (seperti dalam paper)
   */
  linearMembershipFunction(value, min, max) {
    if (value <= min) return 1;
    if (value >= max) return 0;
    return (max - value) / (max - min);
  }
}
```

#### 3. Hybrid SA-GA (Memetic Algorithm)

```javascript
/**
 * Memetic Algorithm: SA + GA Hybrid
 * Berdasarkan konsep dari Kumari et al. (2024)
 */

class MemeticAlgorithm {
  constructor(config) {
    this.gaConfig = config.ga || {};
    this.saConfig = config.sa || {};
    this.lsConfig = config.ls || {}; // Local Search
  }

  /**
   * Memetic algorithm: GA + SA + LS
   */
  solve(instance) {
    // Phase 1: GA untuk global exploration
    const ga = new GeneticAlgorithm(this.gaConfig);
    let population = ga.initializePopulation(instance);

    // Evolve population
    for (let generation = 0; generation < ga.maxGenerations; generation++) {
      population = ga.evolve(population);

      // Apply SA ke setiap individual (local improvement)
      population = population.map(individual => {
        return this.localSearchSA(individual, instance);
      });
    }

    // Select best
    const best = this.selectBest(population);

    return best;
  }

  /**
   * Local search menggunakan SA
   */
  localSearchSA(individual, instance) {
    const sa = new SimulatedAnnealing({
      ...this.saConfig,
      initialState: individual,
      iterations: 100 // Short SA untuk local search
    });

    return sa.optimize();
  }

  /**
   * Memetic SA dengan periodic local search
   */
  memeticSA(instance) {
    let current = this.generateInitialSolution(instance);
    let best = current.clone();
    let T = this.saConfig.T0 || 1000;

    while (T > this.saConfig.Tf) {
      // Standard SA move
      const neighbor = this.generateNeighbor(current);
      const delta = this.evaluate(neighbor) - this.evaluate(current);

      if (delta < 0 || Math.random() < Math.exp(-delta / T)) {
        current = neighbor;

        // Periodic local search enhancement
        if (this.shouldApplyLocalSearch()) {
          current = this.localSearch(current);
        }

        if (this.evaluate(current) < this.evaluate(best)) {
          best = current.clone();
        }
      }

      T *= this.saConfig.alpha;
    }

    return best;
  }

  /**
   * Local search (hill climbing style)
   */
  localSearch(solution) {
    let current = solution.clone();
    let improved = true;

    while (improved) {
      improved = false;

      // Try all neighboring moves
      const neighbors = this.generateAllNeighbors(current);
      const bestNeighbor = this.findBest(neighbors);

      if (this.evaluate(bestNeighbor) < this.evaluate(current)) {
        current = bestNeighbor;
        improved = true;
      }
    }

    return current;
  }
}
```

---

## Kekurangan dan Keterbatasan Paper

### 1. Kurang Detail dalam Penjelasan

- Mathematical formulation tidak lengkap
- Objective functions tidak jelas definisinya
- Variabel $x_r$ tidak dijelaskan secara menyeluruh

### 2. Case Study Terbatas

- Hanya satu institution
- Dataset kecil (12 faculty, 20 courses)
- Tidak ada generalization ke larger instances

### 3. Hasil Tidak Komprehensif

- Tidak ada performance metrics yang jelas
- Tidak ada comparison dengan baseline
- Tidak ada statistical analysis

### 4. Review Section Singkat

- Literature review sangat ringkas
- Tidak ada critical analysis
- Tidak ada gap identification yang jelas

### 5. Metodologi Tidak Detail

- Tidak ada pseudocode atau algoritma detail
- Implementation specifics tidak jelas
- Parameter values tidak dijelaskan

---

## Arah Penelitian Lanjutan

### Research Gaps

#### 1. SA dengan Faculty Preferences

**Gap:**
Paper menyebutkan SA tetapi tidak implement secara detail untuk faculty preferences.

**Research direction:**
- SA dengan preference-based objective function
- Adaptive weights untuk faculty preferences
- Multi-objective SA untuk balance preferences

#### 2. Scalability untuk Large Institutions

**Gap:**
Case study hanya 12 faculty, 20 courses.

**Research direction:**
- SA untuk hundreds of faculty dan courses
- Hierarchical decomposition untuk large-scale UCTP
- Parallel SA untuk speedup

#### 3. Dynamic Preferences Handling

**Gap:**
Static preferences dalam model.

**Research direction:**
- SA dengan dynamic preference updates
- Real-time preference incorporation
- Negotiation mechanisms untuk conflicts

#### 4. Integration dengan Other Tools

**Gap:**
Paper fokus mathematical tools saja.

**Research direction:**
- SA + machine learning untuk demand forecasting
- SA + constraint programming untuk hybrid solving
- SA + user interfaces untuk interactive scheduling

---

## Kesimpulan

### Summary Temuan

1. **Mathematical tools overview** - LP, IP, fuzzy preferences untuk UCTP
2. **Two-phase approach** - Hard constraints dulu, soft constraints kemudian
3. **Metaheuristics dominance** - GA, SA, TS, ACO, honey bee algorithms
4. **Faculty preferences matter** - Perlu diintegrasikan ke objective function
5. **Case study validation** - XYZ institution dengan 12 faculty, 20 courses

### Rekomendasi untuk Proyek

1. **Implement two-phase SA** - Hard constraints → Soft constraints
2. **Incorporate faculty preferences** - Weighted objective function
3. **Consider memetic algorithm** - SA + GA + LS hybrid
4. **Validate dengan real data** - Faculty preferences dari actual institution
5. **Document clearly** - Provide comprehensive mathematical formulation

### Research Questions untuk Thesis

1. Bagaimana SA dengan two-phase approach performs untuk UCTP dengan faculty preferences?
2. Dapatkah memetic SA (SA+GA) mengungguli pure SA atau GA?
3. Bagaimana mengoptimasi trade-off antara faculty preferences dan institutional constraints?
4. Apakah two-phase approach menghasilkan better solutions dibanding single-phase?

---

## Referensi

- Kumari, P., Basotia, V., Mandia, H.K. (2024). "Exploring Mathematical Tools in Designing Efficient Timetable Algorithms." *Anveshana's International Journal of Research in Engineering and Applied Sciences*, 9(8), 30-37.
- Algethami, H., Laesanklang, W. (2021). "A Mathematical Model for Course Timetabling Problem With Faculty-Course Assignment Constraints." *IEEE Access*.
- AbdoulRjoub, A. (2020). "Courses Timetabling Based on Hill Climbing Algorithm." *International Journal of Electrical and Computer Engineering*, 10(6), 6558-6573.
- Goes, A. (2019). "Optimization in Timetabling in Schools Using a Mathematical Model, Local Search and Iterated Local Search." *Gestão & Produção*, 26.

---

*Analisis ini ditulis untuk mendukung penelitian tesis tentang University Course Timetabling Problem menggunakan Simulated Annealing.*
