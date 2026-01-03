# Analisis Paper: Optimizing University Course Timetabling for Metaverse Integration

## Informasi Publikasi

- **Judul:** Optimizing University Course Timetabling for Metaverse Integration: A Human-Centered Decision Model in Medical Education
- **Penulis:** Seckin Damar, Gulsah Hancerliogullari Koksalmis*
- **Affiliasi:**
  - Department of Industrial Engineering, Istanbul Technical University, Turkey
  - Department of Industrial Engineering and Management Systems, University of Central Florida, USA
- **Status:** Preprint (belum peer-reviewed)
- **Source:** SSRN (https://ssrn.com/abstract=5641811)
- **Jumlah Halaman:** 26
- **Domain:** University Course Timetabling dengan Metaverse Integration

---

## Abstrak

Paper ini menyajikan **novel framework** untuk University Course Timetabling Problem (UCTTP) di medical schools yang mengintegrasikan **metaverse dan regular courses**.

**Komponen Utama:**
1. **Binary Integer Linear Programming (BILP)** model dengan metaverse courses
2. **Weighted assignment** berdasarkan behavioral intentions professors
3. **Weights dari AHP** berdasarkan constructs dari SEM
4. **GRAPE algorithm** (Greedy Reassignment and Assignment for Professor Equity)
5. **Simulated Annealing** dengan Taguchi DoE parameter tuning

**Hasil:**
- **45 synthetic problem instances** diuji
- **GRAPE:** Efisien dalam computation time
- **SA:** Lebih tinggi solution quality untuk large datasets

**Keywords:** University course timetabling, Educational technology integration, Metaverse in medical education, Integer linear programming, Analytic hierarchy process, Simulated annealing

---

## Latar Belakang

### University Course Timetabling Problem (UCTTP)

**Definisi:**
Assigning students, instructors, dan courses ke timeslots dan classrooms dengan memenuhi constraints.

**Karakteristik:**
- **NP-complete problem**
- Resource allocation challenge
- Kombinatorial complexity

### Metaverse dalam Medical Education

**Definisi:**
Integrasi VR, AR, dan immersive technologies dalam shared virtual environments.

**Aplikasi:**
- Virtual hospitals dan operating rooms
- Patient interactions simulations
- 3D anatomical visualizations
- Surgical training dengan AR
- Team-based training scenarios

**Manfaat:**
- Flexible dan safe learning space
- Active participation
- Student-centered approaches
- Personalized learning experiences
- Constructivist pedagogical principles

### Studi Empiris Metaverse dalam Medical Education

| Peneliti | Temuan |
|----------|--------|
| **Mergen et al. (2025)** | VR-based simulations improved self-efficacy untuk skin cancer screenings |
| **Bowen et al. (2021)** | VR enhanced emotional engagement, empathy, awareness |
| **Campos et al. (2020)** | Simulation-based education enhanced critical thinking, decision-making, collaboration |

### Tantangan Integrasi Metaverse

**Hardware challenges:**
- Internet bandwidth limitations
- Device access (smartphones, computers)
- AR/VR hardware availability
- Platform selection dan integration

**Cognitive challenges:**
- Cognitive overload
- Educational process challenges
- Isolation dan lack of social interaction
- Motion sickness

**Regulatory challenges:**
- Anonymity guidelines
- Intellectual property protection

---

## Problem Definition

### Model Components

1. **Timeslots:** 9 intervals per day (8:00 AM - 5:45 PM), Monday-Friday
2. **Course types:**
   - **Regular courses:** Traditional face-to-face di physical classrooms
   - **Metaverse courses:** VR/AR/simulation-based platforms

3. **Professor assignment:**
   - Field competencies untuk regular courses
   - **Technological aptitude + behavioral intention** untuk metaverse courses
   - **SEM-based weights** untuk metaverse course assignment priority

### Formula Tujuan

**Objective:** Assign metaverse courses ke professors dengan highest intention levels

$$w(i,p) = \text{weight dari AHP berdasarkan SEM constructs}$$

Dimana $w(i,p)$ adalah weight untuk profesor $p$ pada metaverse course/intention factors.

---

## Literature Review

### Bibliometric Analysis

**Search strategy:**
- Database: Scopus
- Keywords: timetable*, schedule*, course scheduling, metaheuristic*, universit*, college*
- **Results:** 236 records

**VOSviewer co-occurrence analysis findings:**
- **Simulated Annealing (SA)** adalah **most common metaheuristic** untuk course scheduling

### Klasifikasi Metaheuristics

#### 1. Classical Metaheuristics

| Peneliti | Metode | Kontribusi |
|----------|--------|-----------|
| **Sylejmani et al. (2023)** | Two-stage SA | Feasibility → Soft constraint optimization |
| **Bellio et al. (2016)** | Feature-guided SA | Parameter selection guided oleh problem features |
| **Junn et al. (2017)** | SA vs Big Flood | Comparative analysis |
| **Hossain et al. (2019)** | Extended PSO | Selective search + coercive trade-off |
| **Mahlous & Mahlous (2023)** | Modified GA | Student preferences integration |
| **Laguardia & Flores (2022)** | Tabu Search | Greedy initialization |
| **Al-Betar & Khader (2012)** | Harmony Search | Competitive vs established metaheuristics |

#### 2. Hybrid Metaheuristics

| Peneliti | Hybrid | Komponen |
|----------|--------|----------|
| **Vianna et al. (2020)** | VNS + TS | Systematic neighborhood + memory-based LS |
| **Wong et al. (2022)** | TS + GA | TS di initialization phase |
| **Thepphakorn & Pongcharoen (2020)** | Self-Adaptive CS | Dynamic parameter adjustment |
| **Badoni et al. (2023)** | GA + ILS | Global exploration + local refinement |
| **Song et al. (2021)** | Competition-Driven Multi-neighborhood LS | Operator competition |
| **Bolaji et al. (2014)** | ABC + Hill Climbing | Increased exploitation |
| **Abdullah et al. (2012)** | EM + Great Deluge | EM dynamics + adaptive acceptance |
| **De Causmaecker et al. (2009)** | Decomposed hybrid | Pillar-based preprocessing + TS |

#### 3. Adaptive dan Hyper-Heuristics

| Peneliti | Metode | Fitur |
|----------|--------|--------|
| **Tarawneh & Ayob (2013)** | Adaptive SA | Dynamic neighborhood selection |
| **Alhuniti et al. (2020)** | Intelligent mutation GA | Statistically likely mutations |
| **Prakasa et al. (2024)** | SA with reheating | Temperature revival untuk diversity |
| **Kiefer et al. (2017)** | ALNS | Adaptive Large Neighborhood Search |

---

## Methodologi

### Framework Overview

```
┌─────────────────────────────────────────────────────────┐
│              MULTI-STAGE METHODOLOGY                      │
└─────────────────────────────────────────────────────────┘
                          │
          ┌───────────────┼───────────────┐
          ▼               ▼               ▼
    ┌──────────┐   ┌──────────┐   ┌──────────┐
    │    SEM   │ → │   AHP    │ → │  BILP    │
    │ (Factors)│   │(Weights) │   │ (Model)  │
    └──────────┘   └──────────┘   └──────────┘
                                             │
                              ┌────────────┼────────────┐
                              ▼            ▼            ▼
                         ┌─────────┐  ┌─────────┐  ┌─────────┐
                         │ GRAPE   │  │    SA   │  │ Taguchi │
                         │ (Fast)  │  │(Quality)│  │  (DoE)  │
                         └─────────┘  └─────────┘  └─────────┘
```

### Tahap 1: Structural Equation Modeling (SEM)

**Tujuan:** Identifikasi key factors yang mempengaruhi professors' intentions to use metaverse technologies.

**Berdasarkan:** Damar & Koksalmis (2023)

**Input:** Latent constructs dan observed measures

**Output:** Key factors/factors untuk AHP criteria

### Tahap 2: Analytic Hierarchy Process (AHP)

**Tujuan:** Derive professor weights berdasarkan SEM factors

**Process:**
1. Pairwise comparisons antar factors
2. Construct reciprocal matrix A = [a_ij]
3. Solve eigenvalue problem
4. Derive priority weights

**Output:** Weights w(i,p) untuk setiap professor

### Tahap 3: Binary Integer Linear Programming (BILP)

**Decision variables:**
- x(i,j,k,t) = 1 jika course i di room j pada timeslot k pada day t
- Binary assignment variables

**Objective function:**

$$\min \sum_{i,j,k,t} w(i,p) \cdot x(i,j,k,t) \cdot \text{isMetaverse}(i)$$

**Constraints:**
- Hard constraints (no conflicts)
- Metaverse-specific constraints
- Professor capacity constraints

### Tahap 4: GRAPE Algorithm

**Greedy Reassignment and Assignment for Professor Equity**

**Purpose:** Rapidly generate initial solutions

**Process:**
1. Greedy initial assignment
2. Reassignment untuk equity
3. Fast computation time

### Tahap 5: Simulated Annealing

**Purpose:** Improve solution quality dari GRAPE initial solution

**Taguchi DoE tuning:**
- Optimize SA parameters
- Determine optimal configurations

---

## Implikasi untuk Proyek Ini

### Relevansi

Paper ini sangat relevan karena:

1. **SA confirmed sebagai most common metaheuristic** untuk course scheduling
2. **Hybrid approach (GRAPE + SA)** menunjukkan promise
3. **Parameter tuning dengan Taguchi DoE** - systematic methodology
4. **Synthetic instances validation** - 45 problem instances
5. **Human-centered weights** - behavioral intention integration

### Rekomendasi untuk Proyek

#### 1. Validasi SA sebagai Primary Metaheuristic

Berdasarkan bibliometric analysis:
> **"Simulated Annealing (SA) is the most common metaheuristic technique used for course scheduling problems"**

Ini mengkonfirmasi pilihan SA untuk proyek Anda.

#### 2. Implementasi Hybrid SA (GRAPE-style)

```javascript
/**
 * Hybrid SA dengan Greedy Initialization
 * Berdasarkan GRAPE + SA approach dari Damar & Koksalmis (2024)
 */

class HybridGrapeSA {
  constructor(config) {
    this.grapeConfig = config.grape || {};
    this.saConfig = config.sa || {};
  }

  /**
   * GRAPE: Greedy Reassignment for Professor Equity
   * Fast initial solution generation
   */
  grape(initialInstance) {
    const solution = this.createEmptySolution(initialInstance);

    // Phase 1: Greedy assignment
    for (const course of initialInstance.courses) {
      // Find best available slot based on constraints
      const assignment = this.findBestGreedyAssignment(course, solution);
      solution.assign(assignment);
    }

    // Phase 2: Reassignment untuk equity
    solution = this.reassignForEquity(solution);

    return solution;
  }

  /**
   * Find best greedy assignment
   */
  findBestGreedyAssignment(course, solution) {
    const availableSlots = this.getAvailableSlots(course, solution);

    // Sort by preference (minimize conflicts)
    const sorted = availableSlots.sort((a, b) => {
      const conflictsA = this.countConflicts(course, a);
      const conflictsB = this.countConflicts(course, b);
      return conflictsA - conflictsB;
    });

    return sorted[0]; // Best slot
  }

  /**
   * Reassignment untuk professor equity
   */
  reassignForEquity(solution) {
    // Calculate load distribution
    const loads = this.calculateProfessorLoads(solution);

    // Find overloaded dan underloaded professors
    const overloaded = this.getOverloadedProfessors(loads);
    const underloaded = this.getUnderloadedProfessors(loads);

    // Rebalance assignments
    for (const over of overloaded) {
      const reassign = this.findReassignment(over, underloaded, solution);
      if (reassign) {
        solution.reassign(reassign);
      }
    }

    return solution;
  }

  /**
   * SA improvement dari GRAPE solution
   */
  improveWithSA(grapeSolution, instance) {
    const sa = new SimulatedAnnealing({
      ...this.saConfig,
      initialState: grapeSolution
    });

    return sa.optimize();
  }

  /**
   * Solve hybrid GRAPE + SA
   */
  solve(instance) {
    console.log('Phase 1: GRAPE initial solution...');
    const grapeSolution = this.grape(instance);

    console.log('GRAPE penalty:', this.evaluate(grapeSolution));

    console.log('Phase 2: SA improvement...');
    const saSolution = this.improveWithSA(grapeSolution, instance);

    console.log('SA penalty:', this.evaluate(saSolution));

    return saSolution;
  }
}
```

#### 2. Taguchi Design of Experiments untuk SA Parameter Tuning

Paper ini menggunakan Taguchi DoE untuk mengoptimalkan SA parameters.

```javascript
/**
 * Taguchi DoE untuk SA Parameter Optimization
 * Berdasarkan Damar & Koksalmis (2024)
 */

class TaguchiSAOptimizer {
  constructor() {
    // Factors dan levels
    this.factors = {
      T0: [500, 1000, 2000],      // Initial temperature
      alpha: [0.95, 0.99, 0.995],  // Cooling rate
      iterations: [100, 500, 1000], // Iterations per temperature
      neighborhoodSize: [5, 10, 20] // Neighborhood size
    };

    // Taguchi orthogonal array L9 (3^4 = 81 combinations → 9 experiments)
    this.experiments = this.generateTaguchiL9();
  }

  /**
   * Generate Taguchi L9 orthogonal array
   */
  generateTaguchiL9() {
    return [
      { T0: 500, alpha: 0.95, iterations: 100, neighborhoodSize: 5 },
      { T0: 500, alpha: 0.99, iterations: 500, neighborhoodSize: 10 },
      { T0: 500, alpha: 0.995, iterations: 1000, neighborhoodSize: 20 },
      { T0: 1000, alpha: 0.95, iterations: 500, neighborhoodSize: 20 },
      { T0: 1000, alpha: 0.99, iterations: 1000, neighborhoodSize: 5 },
      { T0: 1000, alpha: 0.995, iterations: 100, neighborhoodSize: 10 },
      { T0: 2000, alpha: 0.95, iterations: 1000, neighborhoodSize: 10 },
      { T0: 2000, alpha: 0.99, iterations: 100, neighborhoodSize: 20 },
      { T0: 2000, alpha: 0.995, iterations: 500, neighborhoodSize: 5 }
    ];
  }

  /**
   * Run Taguchi experiments
   */
  async runExperiments(instance) {
    const results = [];

    for (const exp of this.experiments) {
      console.log(`Running experiment:`, exp);

      const sa = new SimulatedAnnealing(exp);
      const solution = await sa.optimize(instance);
      const penalty = this.evaluate(solution);

      results.push({
        parameters: exp,
        penalty: penalty,
        time: solution.executionTime
      });
    }

    return this.analyzeResults(results);
  }

  /**
   * Analyze Taguchi results
   */
  analyzeResults(results) {
    // Calculate signal-to-noise ratio (S/N) untuk each factor
    const snRatios = this.calculateSNRatios(results);

    // Find optimal level untuk setiap factor
    const optimal = {};
    for (const [factor, levels] of Object.entries(snRatios)) {
      const bestLevel = levels.indexOf(Math.max(...levels));
      optimal[factor] = this.factors[factor][bestLevel];
    }

    console.log('Optimal parameters:', optimal);

    return {
      optimal,
      snRatios,
      allResults: results
    };
  }

  /**
   * Calculate Signal-to-Noise ratio (smaller-is-better)
   */
  calculateSNRatios(results) {
    const snRatios = {};

    for (const factor of Object.keys(this.factors)) {
      snRatios[factor] = [];

      for (let level = 0; level < this.factors[factor].length; level++) {
        // Get results untuk this level
        const levelResults = results.filter(r =>
          r.parameters[factor] === this.factors[factor][level]
        );

        // Calculate S/N ratio (smaller-is-better)
        const mean = levelResults.reduce((sum, r) => sum + r.penalty, 0) / levelResults.length;
        const variance = levelResults.reduce((sum, r) => sum + Math.pow(r.penalty - mean, 2), 0) / levelResults.length;

        // S/N = -10 * log10(mean^2 + variance)
        const sn = -10 * Math.log10(Math.pow(mean, 2) + variance);
        snRatios[factor][level] = sn;
      }
    }

    return snRatios;
  }
}
```

#### 3. Weight-Based Assignment untuk Professor Preferences

```javascript
/**
 * Weight-Based SA dengan Professor Preferences
 * Berdasarkan SEM-AHP weights dari paper
 */

class WeightedSA {
  constructor(config) {
    this.professorWeights = config.professorWeights || new Map();
    this.courseTypes = config.courseTypes || new Map(); // regular vs metaverse
  }

  /**
   * Calculate fitness dengan weights
   */
  calculateWeightedFitness(solution) {
    let penalty = 0;

    // Hard constraints
    penalty += this.hardConstraintPenalty(solution) * 1000;

    // Soft constraints dengan weights
    for (const [courseId, assignment] of solution.assignments) {
      const professorId = assignment.professor;
      const weight = this.professorWeights.get(professorId) || 1.0;

      // Metaverse courses should go to high-weight professors
      if (this.isMetaverseCourse(courseId)) {
        // Penalty jika low-weight professor teaches metaverse course
        const desiredWeight = 0.7; // Threshold
        if (weight < desiredWeight) {
          penalty += (desiredWeight - weight) * 100;
        }
      }
    }

    return penalty;
  }

  /**
   * Weighted neighbor generation
   */
  generateWeightedNeighbor(solution) {
    const neighbor = solution.clone();

    // Find metaverse course assigned ke low-weight professor
    const problematic = this.findProblematicMetaverseAssignments(solution);

    if (problematic.length > 0) {
      // Fix: reassign ke high-weight professor
      const toFix = problematic[0];
      const betterProfessors = this.findBetterProfessors(toFix.course, toFix.currentProfessor);

      if (betterProfessors.length > 0) {
        neighbor.reassign(toFix.course, betterProfessors[0]);
        return neighbor;
      }
    }

    // No problematic assignments, random move
    return this.generateRandomNeighbor(solution);
  }

  /**
   * Find metaverse courses assigned ke low-weight professors
   */
  findProblematicMetaverseAssignments(solution) {
    const problematic = [];

    for (const [courseId, assignment] of solution.assignments) {
      if (this.isMetaverseCourse(courseId)) {
        const weight = this.professorWeights.get(assignment.professor) || 0;

        if (weight < 0.5) { // Low weight threshold
          problematic.push({
            course: courseId,
            currentProfessor: assignment.professor,
            weight: weight
          });
        }
      }
    }

    // Sort by weight (lowest first)
    return problematic.sort((a, b) => a.weight - b.weight);
  }

  /**
   * Find professors dengan higher weight untuk course
   */
  findBetterProfessors(courseId, currentProfessor) {
    const better = [];
    const currentWeight = this.professorWeights.get(currentProfessor) || 0;

    for (const [profId, weight] of this.professorWeights) {
      if (weight > currentWeight) {
        // Check if professor can teach course
        if (this.isQualified(profId, courseId)) {
          better.push(profId);
        }
      }
    }

    return better;
  }
}
```

---

## Kekurangan dan Keterbatasan Paper

### 1. Preprint Status

- Belum melalui peer review
- Tidak ada independent validation
- Potential changes sebelum final publication

### 2. Synthetic Data

- 45 synthetic problem instances
- Tidak ada real-world validation
- Tidak ada benchmark comparison (ITC, Socha, dll)

### 3. Complexity

- Multi-stage framework (SEM → AHP → BILP → GRAPE → SA)
- Implementasi sangat complex
- Requires multiple tools/expertise

### 4. Metaverse-Specific

- Fokus pada medical education dengan metaverse
- Generalisability ke non-medical fields unknown
- Metaverse technology masih evolving

### 5. SEM dan AHP Dependencies

- Memerlukan SEM study terlebih dahulu
- AHP pairwise comparisons time-consuming
- Static weights (tidak dynamic)

---

## Arah Penelitian Lanjutan

### Research Gaps

#### 1. Taguchi DoE untuk SA Parameters

**Gap:**
Paper menggunakan Taguchi DoE tetapi detail tidak lengkap dalam teks.

**Research direction:**
- Implementasi lengkap Taguchi DoE untuk SA parameters
- Compare dengan other tuning methods (grid search, Bayesian optimization)
- Parameter sensitivity analysis

#### 2. Weight-Based SA untuk Human Preferences

**Gap:**
Paper integrates weights dari behavioral intention.

**Research direction:**
- Weight-based SA untuk traditional UCTP (tanpa metaverse)
- Different weight derivation methods
- Dynamic weight updates during search

#### 3. GRAPE + SA Hybrid

**Gap:**
GRAPE generates fast initial solutions, SA improves quality.

**Research direction:**
- Compare GRAPE+SA vs pure SA
- Compare GRAPE+SA vs other hybrid approaches
- Analysis of when GRAPE initialization helps

#### 4. Scalability Analysis

**Gap:**
45 synthetic instances tetapi scalability analysis tidak detail.

**Research direction:**
- Performance scaling dengan problem size
- Large instances (hundreds of courses/professors)
- Real-world institution scaling

---

## Kesimpulan

### Summary Temuan

1. **SA adalah most common metaheuristic** untuk course scheduling (bibliometric analysis)
2. **Hybrid GRAPE + SA effective** - Fast initial + Quality improvement
3. **Taguchi DoE untuk parameter tuning** - Systematic optimization approach
4. **Weight-based assignment** - Behavioral intention integration
5. **45 synthetic instances** - Comprehensive computational study

### Rekomendasi untuk Proyek

1. **Implement Taguchi DoE** untuk SA parameter optimization
2. **Consider hybrid approach** - Greedy initialization + SA improvement
3. **Weight-based fitness** untuk professor preferences
4. **Systematic parameter tuning** - Tidak ad-hoc
5. **Multiple instance sizes** - Small, medium, large untuk validation

### Research Questions untuk Thesis

1. Bagaimana Taguchi DoE performs untuk SA parameter optimization pada UCTP?
2. Dapatkah GRAPE-style greedy initialization improve SA performance?
3. Bagaimana weight-based assignment untuk professor preferences mempengaruhi solution quality?
4. Apakah hybrid GRAPE+SA mengungguli pure SA untuk berbagai instance sizes?

---

## Referensi

- Damar, S., Koksalmis, G.H. (2024). "Optimizing University Course Timetabling for Metaverse Integration: A Human-Centered Decision Model in Medical Education." *SSRN Preprint*. https://ssrn.com/abstract=5641811
- Damar, S., Koksalmis, G.H. (2023). "Structural Equation Model untuk metaverse technology adoption."
- Sylejmani, et al. (2023). "Two-stage SA framework."
- Kiefer, et al. (2017). "Adaptive Large Neighborhood Search."

---

*Analisis ini ditulis untuk mendukung penelitian tesis tentang University Course Timetabling Problem menggunakan Simulated Annealing.*
