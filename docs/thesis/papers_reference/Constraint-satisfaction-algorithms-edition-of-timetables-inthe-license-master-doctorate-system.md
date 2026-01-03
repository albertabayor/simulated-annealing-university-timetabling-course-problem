# Analisis Paper: Constraint Satisfaction Algorithms: Edition of Timetables in the License-Master-Doctorate System

## Informasi Publikasi

- **Judul:** Constraint Satisfaction Algorithms: Edition of Timetables in the License-Master-Doctorate System
- **Penulis:** Maurice Comlan, Corentin Allohoumbo
- **Affiliasi:**
  - Department of Business Computing, National School of Applied Economics and Management, University of Abomey-Calavi, Benin
  - Department of Computer Engineering and Telecommunications, Polytechnic School of Abomey-Calavi, Benin
- **Jurnal:** Computer Science and Information Technologies
- **Volume/Issue:** Vol. 4, No. 3
- **Halaman:** 217-225
- **Tahun:** November 2023
- **ISSN:** 2722-3221
- **DOI:** 10.11591/csit.v4i3.pp217-225
- **License:** CC BY-SA
- **Publisher:** IAES (Institute of Advanced Engineering and Science)

---

## Abstrak

Paper ini mempelajari algorithms untuk **Constraint Satisfaction Problem (CSP)** dan mengaplikasikannya ke masalah pembuatan jadwal di universitas. Algorithms yang dikaji:

1. **Genetic Algorithm (GA)**
2. **Simulated Annealing (SA)**
3. **Hill Climbing (HC)**
4. **Hybrid GA + SA (SAGA)**
5. **Hybrid GA + HC (HCGA)**

**Temuan utama:**
- Hybridization GA dengan metaheuristic memberikan execution time yang lebih baik
- Hybrid performs lebih baik ketika problem size meningkat
- SAGA converges lebih cepat dari HCGA dan GA

**Keywords:** Constraint satisfaction problem, Genetic algorithm, License-master-doctorate system, Scheduling, Simulated annealing

---

## Latar Belakang

### License-Master-Doctorate (LMD) System

LMD reform di sistem pendidikan menyebabkan universitas menghadapi kesulitan:
- Membuat course timetables yang sesuai untuk semua stakeholders
- Hard constraints sering dilanggar
- Manual scheduling memakan waktu berminggu-minggu

### University Course Timetabling Problem (UCTP)

**Definisi:**
Assigning course events, students, dan teachers ke time slot dan classroom dengan meminimalkan constraint violations.

**Karakteristik:**
- **NP-hard combinatorial problem**
- Banyak variables: teachers, students, constraints
- Setiap universitas memiliki variables dan constraints yang berbeda

**Tantangan:**
- Naive solution (teacher memilih sendiri) → collisions dalam student schedules
- Manual scheduling → memakan waktu lama
- Harus menghindari collisions sambil memenuhi kebutuhan semua pihak

---

## Constraint Satisfaction Problem (CSP)

### Definisi

CSP consists of:
- Variables yang mengambil nilai dari domain
- Constraints yang membatasi kombinasi values

**Two types of constraints:**
1. **Hard constraints** - Wajib dipenuhi untuk viable solution
2. **Soft constraints** - Optional, evaluate solution quality

### Constraint Programming

**Paradigm:** Muncul 1970s-1980s

**Components:**
1. **Modeling part** - CSP
2. **Resolution part** - Constraint propagation

**Algorithms:**
- Constraint propagation → reduce search space
- Systematic search → explore assignments
- Filtering → deduce impossible values
- Rollback mechanism → backtrack saat violation

### Constraint Propagation

```
Generate and Test (naive approach):
  - Enumerate all possibilities
  - Check violations
  - Impractical untuk medium-large problems

Filtering (better approach):
  - Deduce impossible values from constraints
  - Instantiate variables with single candidates
  - Recursively split and search
  - Represented as tree search with pruning
```

---

## Algorithms yang Dikaji

### 1. Genetic Algorithm (GA)

**Principles:**
- Optimization method berdasarkan genetics dan natural selection
- "Survival of the fittest" (Darwinian theory)

**Process:**
1. Initialize population
2. Evaluate fitness
3. Selection (fittest individuals lebih likely to mate)
4. Crossover (recombination)
5. Mutation (modification)
6. Repeat until stopping criterion

**Characteristics:**
- Population-based
- Domain-independent search
- Can find global optimum dalam complex search spaces
- Leverage historical information

### 2. Simulated Annealing (SA)

**Principles:**
- Local search algorithm sejak 1980s
- Terinspirasi dari annealing process dalam materials
- Monte Carlo method

**Process:**
1. Initial solution (random atau dari algorithm lain)
2. Temperature control parameter
3. Neighbor function generates new solution
4. Accept based on fitness improvement OR temperature
5. Cool down temperature

**Characteristics:**
- Single-solution, trajectory-based
- Can escape local optima
- Accepts worse solutions dengan probability

**Cooling Schedule:**

$$T = T_0 \times e^{-\mu \times k}$$

Dimana:
- $T$ = current temperature
- $T_0$ = initial temperature
- $\mu$ = constant (negative → temperature decreases)
- $k$ = number of iterations

### 3. Hill Climbing (HC)

**Principles:**
- Heuristic search technique
- Generate-and-test algorithm

**Process:**
1. Generate potential solution
2. Evaluate if satisfies criteria
3. If yes, stop; else repeat

**Variations:**
- **Steepest ascent HC:** Examines all moves, selects greatest improvement
- **First-choice HC:** Random move, accept if improves
- **Simulated annealing:** Probabilistic variation

**Limitations:**
- Gets stuck di local maxima
- Limited exploration of search space
- Often combined dengan other techniques

### 4. Hybrid Algorithms

#### Motivasi

**GA strengths:**
- Explores extensive search spaces
- Finds reasonable solutions

**GA weaknesses:**
- Falls short achieving optimal solution dalam reasonable time
- Can get stuck di local optimum

**SA strengths:**
- Focuses pada single solution improvement
- Can escape local optima

**SA weaknesses:**
- Doesn't explore search space comprehensively
- May miss valuable solution areas

**Synergy:** GA identifies high-performance regions → Local search (SA/HC) pinpoints optimal solution

#### Hybrid GA + SA (SAGA)

**Approach:**
1. Use SA to improve each individual in starting population
2. Run to certain stopping point
3. Send improved individuals to GA

#### Hybrid GA + HC (HCGA)

**Approach:**
1. Use HC to improve each individual in starting population
2. Run to certain stopping point
3. Send improved individuals to GA

---

## Fitness Function

### Formula

$$fitness = \frac{1}{1 + P_{clash}}$$

Dimana $P_{clash}$ = number of clashes (hard constraint violations)

### Interpretation

| Fitness Score | Meaning |
|---------------|---------|
| **1** | Perfect solution (no violations) |
| **< 1** | Violates one or more constraints |
| **Lower** = More violations |

### Clash Definition

Dalam konteks UCTP, **clash** = hard constraint violation

**Hard constraints untuk UCTP:**
1. Lessons hanya di available (unoccupied) rooms
2. Setiap teacher hanya instruct satu course pada satu waktu
3. Classrooms harus cukup spacious untuk student group
4. Students tidak bisa menghadiri dua classes secara simultan

---

## Neighbor Function untuk SA

### Matrix Modeling

Time intervals dimodelled sebagai 2D matrix:
- **X-axis:** Days (Monday - Saturday)
- **Y-axis:** Hours (7 AM - 7 PM)

### Neighbor Algorithm

```
1. Evaluate collision menggunakan fitness function
2. Untuk setiap colliding pair (i, j):
   a. Try move ke another cell
   b. Consider current position
   c. Possible moves: left, right, up, down
3. Choose best movement
4. Check bahwa temperature telah decreased
```

**Visualization:**
```
     Mon  Tue  Wed  Thu  Fri  Sat
7am   [ ]  [ ]  [ ]  [ ]  [ ]  [ ]
8am   [A]  [ ]  [B]  [ ]  [ ]  [ ]
...
7pm   [ ]  [ ]  [ ]  [ ]  [ ]  [ ]

If A and B collide (same student/teacher),
try moving one to adjacent empty cell
```

---

## Metodologi Eksperimen

### Hardware

- OS: Debian 10, 64-bit
- Processor: AMD Ryzen 7 Pro 3700 CPU @ 3.6 GHz × 8
- RAM: 64 GB

### Dataset

Data dari Department of Computer and Telecommunications Engineering + two preparatory years of Polytechnic School of Abomey-Calavi.

| Parameter | Small | Medium | Large |
|-----------|-------|--------|-------|
| **Teachers** | 10 | 28 | 41 |
| **Rooms** | 2 | 8 | 8 |
| **Courses** | 16 | 66 | 119 |
| **Time slots** | 16 | 33 | 36 |
| **Student groups** | 2 | 4 | 7 |

### Hard Constraints (Digunakan)

1. Classes hanya di free rooms
2. Teacher hanya teach satu course pada satu waktu
3. Classrooms cukup large untuk student group
4. Student groups tidak bisa attend dua classes pada waktu yang sama

### Stopping Criteria

- Fitness score = 1 (perfect solution)
- Time limit = 1 hour
- Max generations = 200 (GA)

### Parameter Settings

#### GA Parameters

| Parameter | Small | Medium | Large |
|-----------|-------|--------|-------|
| **Population size** | 100 | 200 | 600 |
| **Mutation probability (Pm)** | 0.1 | 0.05 | 0.01 |
| **Crossover probability (Pc)** | 0.7 | 0.7 | 0.7 |
| **Selection size** | 1 | 3 | 5 |

#### SA dan HC Parameters

| Parameter | Value |
|-----------|-------|
| **T0** | 1 |
| **k** | 200 |
| **µ** | 0.005 |

---

## Hasil Eksperimen

### Execution Time (seconds)

| Size | GA | SAGA | HCGA |
|------|-----|------|------|
| **Small** | 11 | 11 | 6 |
| **Medium** | 131 | 168 | 175 |
| **Large** | 2209 | 1713 | 2642 |

**Key findings:**
- **SAGA** fastest untuk large instances
- **HCGA** fastest untuk small instances
- GA moderate tapi slower untuk large problems

### Number of Generations

| Size | GA | SAGA | HCGA |
|------|-----|------|------|
| **Small** | 5 | 5 | 3 |
| **Medium** | 15 | 20 | 21 |
| **Large** | 125 | 97 | 149 |

**Key findings:**
- **HCGA** fewest generations untuk small
- **SAGA** fewest generations untuk large
- Hybrid algorithms more efficient dalam generations

### Visualizations

#### Figure 2: Elapsed Time (Large Size)
- SAGA shows fastest convergence
- HCGA slower
- GA falls into local optimum (flat curve portions)

#### Figure 3: Collisions vs Generations (Large Size)
- Shows decrease in collisions over generations
- SAGA reaches zero collisions faster

#### Figure 4: Average Fitness vs Generations
- Shows improvement in fitness over generations
- GA exhibits stagnant behavior di later stages
- Confirms Thierens' findings

---

## Implikasi untuk Proyek Ini

### Relevansi

Paper ini sangat relevan karena:

1. **Direct comparison** GA, SA, HC, dan hybrids
2. **Empirical evidence** bahwa hybrid approaches bekerja lebih baik
3. **Specific UCTP context** (LMD system)
4. **Detailed parameter settings** untuk replication

### Rekomendasi untuk Proyek

#### 1. Pertimbangkan Hybrid Approach

Berdasarkan hasil:
- **SAGA** performs best untuk large instances
- Hybridization improves execution time
- Hybrid converges dengan fewer generations

```javascript
/**
 * Hybrid SA dengan Local Search
 * Berdasarkan findings dari Comlan & Allohoumbo (2023)
 */

class HybridSA {
  constructor(config) {
    // SA components
    this.sa = new SimulatedAnnealing(config.sa);

    // Local search untuk improvement
    this.localSearch = config.localSearch || new HillClimbing();
    this.useHybrid = config.useHybrid !== false; // Default true
  }

  /**
   * Hybrid SA dengan pre-processing
   * Similar ke SAGA approach dalam paper
   */
  solve(instance) {
    // Phase 1: Generate initial population
    const population = this.generateInitialPopulation(instance);

    // Phase 2: Pre-improvement dengan local search (SAGA-style)
    let improvedPopulation;
    if (this.useHybrid) {
      improvedPopulation = population.map(individual => {
        return this.localSearch.improve(individual, instance);
      });
    } else {
      improvedPopulation = population;
    }

    // Phase 3: Select best from improved population
    const bestInitial = this.selectBest(improvedPopulation);

    // Phase 4: SA search dari best improved individual
    const solution = this.sa.search(bestInitial, instance);

    return solution;
  }

  /**
   * Generate initial population
   */
  generateInitialPopulation(instance) {
    const population = [];
    const size = this.getPopulationSize(instance);

    for (let i = 0; i < size; i++) {
      const solution = this.generateRandomSolution(instance);
      population.push(solution);
    }

    return population;
  }

  /**
   * Hill climbing local search
   * Untuk pre-improvement seperti dalam paper
   */
  hillClimbingImprove(solution, instance, maxIterations = 100) {
    let current = solution.clone();
    let best = current.clone();

    for (let i = 0; i < maxIterations; i++) {
      // Generate neighbor
      const neighbor = this.generateNeighbor(current);

      // Accept if better (greedy)
      if (neighbor.penalty < current.penalty) {
        current = neighbor;

        if (current.penalty < best.penalty) {
          best = current.clone();
        }
      }

      // Early termination jika perfect
      if (best.penalty === 0) {
        break;
      }
    }

    return best;
  }

  /**
   * Generate neighbor untuk SA/HC
   * Based pada neighbor function dalam paper
   */
  generateNeighbor(solution) {
    const neighbor = solution.clone();

    // Pick random event
    const eventIdx = Math.floor(Math.random() * neighbor.events.length);

    // Matrix-style movement (left, right, up, down)
    const currentSlot = neighbor.events[eventIdx].slot;
    const currentDay = Math.floor((currentSlot - 1) / 12); // Assuming 12 slots/day
    const currentPeriod = (currentSlot - 1) % 12;

    // Possible moves
    const moves = [
      { day: currentDay, period: currentPeriod - 1 }, // left
      { day: currentDay, period: currentPeriod + 1 }, // right
      { day: currentDay - 1, period: currentPeriod }, // up (previous day)
      { day: currentDay + 1, period: currentPeriod }, // down (next day)
    ];

    // Select valid move
    const validMove = moves.find(move =>
      move.day >= 0 && move.day < 6 &&
      move.period >= 0 && move.period < 12
    );

    if (validMove) {
      neighbor.events[eventIdx].slot = validMove.day * 12 + validMove.period + 1;
    }

    return neighbor;
  }

  /**
   * Calculate fitness
   * Based pada formula dari paper
   */
  calculateFitness(solution) {
    const clashes = this.countClashes(solution);
    return 1 / (1 + clashes);
  }

  /**
   * Count hard constraint violations (clashes)
   */
  countClashes(solution) {
    let clashes = 0;

    // HC1: Teacher hanya satu course pada satu waktu
    clashes += this.countTeacherConflicts(solution);

    // HC2: Student groups tidak dua classes pada waktu yang sama
    clashes += this.countStudentConflicts(solution);

    // HC3: Room conflicts
    clashes += this.countRoomConflicts(solution);

    // HC4: Room capacity
    clashes += this.countCapacityViolations(solution);

    return clashes;
  }
}
```

#### 2. Parameter Recommendations

Berdasarkan paper, gunakan parameter berikut sebagai starting point:

| Parameter | Small | Medium | Large |
|-----------|-------|--------|-------|
| **Population** | 100 | 200 | 600 |
| **Mutation rate** | 0.1 | 0.05 | 0.01 |
| **Crossover rate** | 0.7 | 0.7 | 0.7 |

**SA Parameters:**
- T0 = 1
- k = 200 iterations
- µ = 0.005

#### 3. Adaptive Population Size

```javascript
/**
 * Adaptive population size berdasarkan problem size
 */
function getPopulationSize(numEvents) {
  if (numEvents <= 20) return 100;      // Small
  if (numEvents <= 70) return 200;      // Medium
  return 600;                            // Large
}

/**
 * Adaptive mutation rate
 */
function getMutationRate(numEvents) {
  if (numEvents <= 20) return 0.1;
  if (numEvents <= 70) return 0.05;
  return 0.01;
}
```

#### 4. Implementasi SAGA-style Hybrid

```javascript
/**
 * SAGA-style implementation
 * SA dengan population-based pre-processing
 */

class SAGA {
  constructor(config) {
    this.populationSize = config.populationSize || 100;
    this.saConfig = config.sa || {};
    this.hcConfig = config.hc || {};
  }

  solve(instance) {
    // Step 1: Generate initial population
    const population = this.generatePopulation(instance, this.populationSize);

    // Step 2: Improve each individual dengan HC
    const improved = population.map(individual => {
      return this.hillClimbingImprove(individual, instance);
    });

    // Step 3: Select best
    const best = improved.reduce((best, current) =>
      current.penalty < best.penalty ? current : best
    );

    // Step 4: SA search dari best
    const sa = new SimulatedAnnealing(this.saConfig);
    const solution = sa.search(best, instance);

    return solution;
  }

  hillClimbingImprove(solution, instance) {
    const hc = new HillClimbing(this.hcConfig);
    return hc.improve(solution, instance);
  }
}
```

---

## Kekurangan dan Keterbatasan Paper

### 1. Dataset Terbatas

- Hanya 3 size instances (small, medium, large)
- Hanya dari one institution
- Tidak ada benchmark datasets (ITC, Socha, dll)

### 2. Sederhana dalam Constraints

- Hanya 4 hard constraints
- Tidak ada soft constraints yang explicit
- Tidak comprehensive UCTP formulation

### 3. Terbatas dalam Algorithm Variants

- Hanya satu variant untuk setiap algorithm
- Tidak ada comparison dengan other metaheuristics (VNS, TS, dll)
- Tidak ada hyper-heuristics atau matheuristics

### 4. Hardware-Specific

- Hasil mungkin spesifik untuk hardware yang digunakan
- Tidak ada normalization untuk comparison

### 5. Tidak Ada Statistical Analysis

- Hanya average dari 9 runs
- Tidak ada statistical significance tests
- Tidak ada variance/std deviation reporting

---

## Arah Penelitian Lanjutan

### Research Gaps

#### 1. Hybrid SA untuk UCTP

**Gap:**
Paper shows SAGA works well, tapi fokus GA+SA.

**Research direction:**
- Bagaimana SA standalone dengan adaptive mechanisms?
- Dapatkah SA dengan cooperative processes mengungguli SAGA?

#### 2. Multi-Objective Optimization

**Gap:**
Paper hanya focus hard constraints (feasibility).

**Research direction:**
- Soft constraints optimization
- Multi-objective UCTP (feasibility + quality + preferences)

#### 3. Benchmark Validation

**Gap:**
Hanya custom dataset, no standard benchmarks.

**Research direction:**
- Validate dengan ITC datasets
- Comparison dengan state-of-the-art

#### 4. Adaptive Parameter Control

**Gap:**
Parameters fixed untuk setiap problem size.

**Research direction:**
- Self-adaptive parameters
- Learning-based parameter tuning

---

## Kesimpulan

### Summary Temuan

1. **SAGA performs best** untuk large instances
2. **Hybrid approaches** outperform pure GA
3. **Local search pre-processing** improves efficiency
4. **SA effective** sebagai improvement mechanism
5. **Problem size affects** algorithm performance significantly

### Rekomendasi untuk Proyek

1. **Pertimbangkan hybrid approach** - SA dengan local search preprocessing
2. **Gunakan parameter guidelines** sebagai starting point
3. **Implement SAGA-style** pre-improvement
4. **Focus pada large instances** - di mana hybrid shows most benefit
5. **Validasi dengan benchmarks** - ITC datasets

### Research Questions untuk Thesis

1. Dapatkah SA dengan adaptive neighborhood selection mengungguli SAGA?
2. Bagaimana hybrid SA-VNS performs untuk UCTP?
3. Apakah cooperative SA (parallel) dapat mengungguli hybrid approaches?
4. Bagaimana mengintegrasikan soft constraints ke dalam SA framework?

---

## Referensi

- Comlan, M., Allohoumbo, C. (2023). "Constraint Satisfaction Algorithms: Edition of Timetables in the License-Master-Doctorate System." *Computer Science and Information Technologies*, 4(3), 217-225. https://doi.org/10.11591/csit.v4i3.pp217-225
- Abdullah, S., et al. (2019). "Various cooling schedules for solving examination timetabling problem."
- Thierens, D. "Stagnation behavior of genetic algorithms."

---

*Analisis ini ditulis untuk mendukung penelitian tesis tentang University Course Timetabling Problem menggunakan Simulated Annealing.*
