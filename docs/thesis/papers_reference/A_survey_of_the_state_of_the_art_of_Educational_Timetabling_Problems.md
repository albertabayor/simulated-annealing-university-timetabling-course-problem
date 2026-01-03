# Analisis Paper: A Survey of the State of the Art of Educational Timetabling Problems

## Informasi Publikasi

- **Judul:** A Survey of the State of the Art of Educational Timetabling Problems
- **Penulis:** Jade Diane Fernandes Targino Filgueira, Hugo Valadares Siqueira, Attilio Converti, Thiago Antonini Alves, Carmelo José Albanez Bastos Filho
- **Affiliasi:**
  - Paraná Federal University of Technology, Brazil
  - University of Genoa, Italy
  - Polytechnic Pernambuco University, Brazil
- **Publikasi:** IEEE Conference Paper
- **Tahun:** 2024
- **DOI:** Tidak tersedia dalam teks (conference proceeding)
- **Metodologi:** PRISMA (Preferred Reporting Items for Systematic Reviews and Meta-Analysis)
- **Tipe Paper:** Survey / Systematic Literature Review

---

## Abstrak

Paper ini menyajikan **comprehensive literature review** pada bidang Educational Timetabling Problems (ETP). Menggunakan protocol PRISMA, paper ini menganalisis 26 artikel dari 55 hasil pencarian awal (publikasi 2014-2022).

**Temuan utama:**
1. Meta-heuristic adalah pendekatan paling populer
2. Meta-heuristics jarang diimplementasikan secara terpisah (isolated)
3. Sebagian besar penulis memulai dengan feasible initial solutions
4. Ada mekanisme yang terintegrasi untuk generate initial solutions

**Keywords:** Educational Timetabling Problems, optimization, solution techniques

---

## Metodologi Survey

### PRISMA Protocol

Paper ini menggunakan **PRISMA** protocol untuk systematic literature review:

```
Initial Search (IEEE Xplore, ACM, ScienceDirect)
         ↓
      55 results
         ↓
    Screening (title + abstract)
         ↓
      43 results (12 excluded)
         ↓
    Eligibility assessment
         ↓
      26 papers included (17 excluded)
```

### Kriteria Eksklusi

**12 articles di screening stage:**
- Tidak termasuk variant ETP

**17 articles di eligibility stage:**
- 7 systematic review papers
- 7 problem formulation studies
- 1 case study
- 1 algorithm selection strategy study
- 1 application development paper

**Common exclusion:** Tidak mempelajari optimization strategy

### Distribusi Geografis

| Country | Publications |
|---------|--------------|
| **Brazil** | 7 (terbanyak) |
| United Kingdom | 3 |
| Indonesia | 2 |
| China | 2 |
| Portugal | 2 |
| Mexico | 2 |
| Malaysia | 2 |
| Tunisia | 2 |
| Australia | 1 |
| Greece | 1 |
| Egypt | 1 |
| Thailand | 1 |

### Distribusi Tahun

| Tahun | Publications |
|-------|--------------|
| 2014 | 5 |
| 2015 | 5 |
| 2016 | 3 |
| 2017 | 4 |
| 2018 | 2 |
| 2019 | 1 |
| 2020 | 3 |
| 2021 | 2 |
| 2022 | 1 |

**Observasi:** Terdapat **declining trend** dalam jumlah publikasi sejak 2017.

---

## Educational Timetabling Problems (ETP)

### Definisi

ETP consists of assigning meetings or exams between teachers and students, considering:
- **Hard constraints** - wajib dipenuhi untuk feasible timetable
- **Soft constraints** - tidak mandatory, minimum violation = optimal

### Klasifikasi

```
Educational Timetabling (ETP)
├── University Timetabling
│   ├── University Course Timetabling Problem (UCTP)
│   └── University Examination Timetabling Problem (UETP)
└── School Timetabling
    └── High School Timetabling Problem (HSTP)
```

**Kompleksitas:** NP-hard
- Waktu komputasi meningkat secara eksponensial dengan ukuran masalah
- Manual scheduling masih digunakan oleh sebagian besar universitas

### Tantangan Manual Scheduling

1. **Large amount of time invested**
2. **Less flexibility to sudden changes**
3. **Poor consideration of students' needs**

---

## Solution Techniques & Approaches

### Klasifikasi

Paper ini mengkategorikan solution techniques menjadi:

1. **Meta-heuristics** (20 papers - terbanyak)
2. **Exact optimization methods** (4 papers)
3. **Hyper-heuristics** (1 paper)
4. **Matheuristics** (1 paper)

### Meta-Heuristics (Paling Populer)

#### Per Family Meta-Heuristics

| Meta-Heuristic | Total | Reference |
|----------------|-------|-----------|
| **Variable Neighborhood Search** | 4 | [16],[17],[18],[24],[6] |
| **Iterated Local Search** | 4 | [24],[27],[1],[31] |
| **Tabu Search** | 4 | [27],[6],[29],[1] |
| **Simulated Annealing** | 4 | [27],[28],[1],[31] |
| **Genetic Algorithm** | 3 | [19],[22],[32] |
| **Hill Climbing** | 1 | [23] |
| **Cuckoo Search** | 1 | [30] |

#### Per Problem Type

| Problem | Meta-Heuristics Used |
|---------|---------------------|
| **UCTP** | VNS, ILS, TS, SA, GA, CS |
| **HSTP** | VNS, ILS, GA, TS, CSO |
| **UETP** | VNS, ILS, R&R, PSO |

### Detail Meta-Heuristics

#### 1. Variable Neighborhood Search (VNS)

**Papers:** [15], [16], [17], [18], [6]

**Inovasi:**
- Dorneles et al. [15]: Fix and Optimize + VND untuk CTTPCR
- Elloumi et al. [16]: Size reduction schemes untuk classroom assignment
- Fonseca & Santos [18]: Skewed VNS dengan relaxed acceptance rule

#### 2. Iterated Local Search (ILS)

**Papers:** [24], [27], [1], [31]

**Inovasi:**
- Saviniec et al. [24]: Hybrid ILS dengan MT dan TQ operators
- Saviniec et al. [27]: Central memory parallel model
- Song et al. [31]: Multiple neighborhoods based on SA

#### 3. Tabu Search (TS)

**Papers:** [27], [6], [29], [1]

**Inovasi:**
- Muklason et al. [6]: VNS hybridized dengan TS
- Chen et al. [29]: Controlled randomization dengan acceptance threshold

#### 4. Simulated Annealing (SA)

**Papers:** [27], [28], [1], [31]

**Inovasi:**
- Leite et al. [28]: Fast Simulated Annealing (FastSA)
  - Versi lebih efisien dari SA
  - Mengurangi jumlah fitness evaluations
- Song et al. [31]: Multiple neighborhoods dengan SA acceptance

#### 5. Genetic Algorithm (GA)

**Papers:** [19], [22], [32]

**Inovasi:**
- Alves et al. [19]: Sequential course scheduling
  - Solve satu course pada satu waktu
  - Urutan berdasarkan complexity
- Abdelhalim & Khayat [22]: Utilization crossover operator
  - Fokus pada classroom utilization rate
  - Reduce under/overutilized events
- Tung Ngo et al. [32]: Repair process
  - Applied ke initial solutions
  - Setelah recombination dan mutation

#### 6. Swarm Intelligence

**Particle Swarm Optimization (PSO)**
- Salem & Hassine [21]: Meeting Scheduling Problem
  - Velocity operator: V = c1(pbest - present) + c2(gbest - present)
  - Difference = meetings di satu particle yang tidak terjadi di waktu yang sama

**Cat Swarm Optimization (CSO)**
- Skoullis et al. [25]: Hybrid CSO
  - Main process: basic CSO
  - Local search refinement

**Artificial Bee Colony (ABC)**
- Fong et al. [17]: ABC hybridized dengan Imperialist Nelder-Mead Great Deluge
  - Improve global exploration
  - Enhance local exploration

#### 7. Lainnya

**Ruin and Recreate (R&R)**
- Li et al. [20]: Stochastic Evolutionary Ruin and Recreate
  - Components dievaluasi dengan score
  - Components dengan score rendah dihapus

**Cuckoo Search (CS)**
- Thepphakorn & Pongcharoen [30]:
  - Static vs adaptive parameter setting
  - Lévy flights vs Gaussian random walk
  - Hybrid dengan local search

---

## Exact Optimization Methods

### Papers: 4 papers

#### Branch and Check
**Esmaeilbeigi et al. [33]:** Multiphase Course Timetabling Problem (MCTP)

**Procedure:**
1. Relax problem
2. Solve dengan solver
3. Check apakah feasible untuk non-relaxed problem
4. Jika tidak, tambahkan constraints untuk remove infeasible solution

---

## Hyper-Heuristics

### Papers: 1 paper

#### Soria-Alcaraz et al. [34]

**Approach:** ILS-based hyper-heuristic
- Combines multiple move operators
- Operators = low-level heuristics
- Selection mechanism:
  - Probability vector
  - Score berdasarkan performance

#### Soria-Alcaraz et al. [36]

**Approach:** Add and delete operations dalam ILS
- Construct solution dari existing feasible solution
- Events dihapus dan di-reinsert ke valid periods
- List untuk tracking add/delete operations

#### Ahmed Özcan & Kheiri [35]

**Comparison:** 15 hyperheuristics
- 5 selection methods × 3 acceptance methods
- Select dan combine 9 low-level heuristics
- Applied ke 18 HSTP instances

#### Muklason et al. [37]

**Fairness-based approach:**
- Phase 1: Construct initial feasible solutions
- Phase 2 & 3: Hyper-heuristic dengan reinforcement learning
- GD algorithm untuk heuristic selection

---

## Matheuristics

### Papers: 1 paper

#### Fonseca, Santos & Carrano [38]

**Hybrid:** VNS + Matheuristic
- VNS untuk main search
- Matheuristic untuk refinement
- Matheuristic:
  - Heuristic di macro level
  - Controls local search procedures
  - Local search = integer programming models
  - Subset of variables fixed
  - Remaining variables dimodifikasi oleh IP solver

---

## Initialization Strategies (Novel Kategorisasi)

Paper ini memperkenalkan **kategorisasi baru** untuk initialization strategies:

### 1. Unfeasible Initial Solutions

**Karakteristik:**
- Tidak atau hanya sebagian hard constraints yang dipertimbangkan
- Tidak ada guarantee viabilitas
- Perlu feasibility check sebelum termination

### 2. Feasible Initial Solutions

**Karakteristik:**
- Hard constraints dipenuhi
- Soft constraints diabaikan
- Mengurangi computational time
- Dapat compromise optimality

### 3. Good Quality Initial Solutions

**Karakteristik:**
- Kedua hard dan soft constraints dipertimbangkan
- Meningkatkan probability menuju better search regions
- Membantu convergence ke better solutions

### Mechanism untuk Generate Initial Solutions

| Mechanism | Count |
|-----------|-------|
| **Algorithm-integrated** | 23 |
| **Solver** | 3 |

### Summary Initialization Strategy

| Reference | Strategy | Mechanism |
|-----------|----------|-----------|
| [23], [33] | Unfeasible | Algorithm |
| [15], [16], [17], [18], [34], [35], [19], [20], [21], [22], [38], [36], [37], [24], [25], [26], [27], [28], [6], [29], [1], [30], [31], [32] | Feasible | Algorithm |
| - | High Quality | - |

**Observasi:**
- **Tidak ada author** yang menggunakan good quality initial solutions
- **Sebagian besar** (23/26) menggunakan feasible initial solutions dengan algorithm-integrated mechanism
- Hanya **2 authors** menggunakan unfeasible initial solutions
- **3 authors** menggunakan solver untuk generate initial solutions

---

## Perbandingan dengan Survey Lain

### Previous Surveys

| Survey | Focus | Scope |
|--------|-------|-------|
| **Babaei et al. [8]** | UCTP | No limitation |
| **Yang et al. [9]** | UCTP | Practical case, satisfaction factors |
| **Abdipoor et al. [2]** | UCTP | Meta-heuristic approaches |
| **Johnes [10]** | Education topics | Operational Research techniques |
| **Drake et al. [11]** | General | Selection hyper-heuristics |
| **Tan et al. [12]** | HSTP | Optimization methodologies |
| **Ceschia et al. [13]** | ETP | Problem formulations, benchmarks, state-of-the-art |

### Diferensiasi Paper Ini

1. **Fokus pada optimization strategies** (bukan problem formulation)
2. **Novel categorization** untuk initialization strategies
3. **Analysis** feasibility of initial solutions
4. **Chronological organization** dari solution techniques

---

## Implikasi untuk Proyek Ini

### Relevansi

Survey ini sangat relevan untuk proyek Anda karena:

1. **Systematic review** dengan PRISMA protocol (rigorous methodology)
2. **Current state** (2014-2022, dengan paper 2024)
3. **Initialization strategy analysis** - penting untuk SA implementation
4. **Meta-heuristics dominance** terkonfirmasi

### Rekomendasi untuk Proyek

#### 1. Pilih Initialization Strategy yang Tepat

Berdasarkan findings:

| Strategy | Recommended | Reason |
|----------|-------------|--------|
| **Unfeasible** | Tidak | Menambah complexity |
| **Feasible (Algorithm)** | YA | Paling populer, balance |
| **Good Quality** | Ideal | Tidak ada yang implement (gap!) |

#### 2. Implementasi Feasible Initial Solution Generator

```javascript
/**
 * Feasible Initial Solution Generator
 * Berdasarkan findings dari Filgueira et al. (2024)
 * - 23/26 papers menggunakan feasible initial solutions
 * - Algorithm-integrated mechanism
 */

class FeasibleInitialSolutionGenerator {
  constructor(instance) {
    this.instance = instance;
    this.events = instance.events;
    this.rooms = instance.rooms;
    this.timeslots = 45; // 9 slots/day × 5 days
  }

  /**
   * Generate feasible initial solution
   * Hard constraints satisfied, soft constraints ignored
   */
  generate() {
    const solution = this.createEmptySolution();

    // Sort events by difficulty (degree of constraints)
    const sortedEvents = this.sortByDifficulty();

    // Assign events sequentially with backtracking
    for (const event of sortedEvents) {
      const assignment = this.findFeasibleAssignment(event, solution);

      if (assignment) {
        solution.assignments[event.id] = assignment;
      } else {
        // Backtrack or repair
        this.repair(event, solution);
      }
    }

    return solution;
  }

  /**
   * Sort events by difficulty (Most Constrained First)
   */
  sortByDifficulty() {
    return [...this.events].sort((a, b) => {
      // Prioritize events dengan:
      // 1. Lebih banyak enrolled students
      // 2. Lebih banyak room requirements
      // 3. Lebih sedikit available timeslots

      const difficultyA = this.calculateDifficulty(a);
      const difficultyB = this.calculateDifficulty(b);

      return difficultyB - difficultyA; // Descending
    });
  }

  calculateDifficulty(event) {
    let difficulty = 0;

    // Student count weight
    difficulty += event.students.length * 10;

    // Room requirements weight
    difficulty += event.requiredFeatures.length * 5;

    // Timeslot availability (inverse)
    const availableSlots = this.countAvailableSlots(event);
    difficulty += (45 - availableSlots) * 2;

    return difficulty;
  }

  /**
   * Find feasible assignment for single event
   * Satisfies hard constraints:
   * - HC1: No student conflicts
   * - HC2: Room features satisfied
   * - HC3: Room capacity sufficient
   * - HC4: No room conflicts
   * - HC5: Timeslot availability
   */
  findFeasibleAssignment(event, solution) {
    // Try all timeslots (prioritize available ones)
    for (let slot = 1; slot <= this.timeslots; slot++) {
      // Check HC5: timeslot availability
      if (!this.isTimeslotAvailable(event, slot)) {
        continue;
      }

      // Try all suitable rooms
      const suitableRooms = this.getSuitableRooms(event);
      for (const room of suitableRooms) {
        // Check hard constraints
        if (this.satisfiesHardConstraints(event, slot, room, solution)) {
          return { slot, room };
        }
      }
    }

    return null; // No feasible assignment found
  }

  /**
   * Check all hard constraints
   */
  satisfiesHardConstraints(event, slot, room, solution) {
    // HC1: Student conflicts
    if (this.hasStudentConflict(event, slot, solution)) {
      return false;
    }

    // HC2: Room features
    if (!this.roomHasFeatures(room, event.requiredFeatures)) {
      return false;
    }

    // HC3: Room capacity
    if (room.capacity < event.students.length) {
      return false;
    }

    // HC4: Room conflicts
    if (this.hasRoomConflict(slot, room, solution)) {
      return false;
    }

    return true;
  }

  /**
   * Get suitable rooms for event
   * Filter by capacity and features
   */
  getSuitableRooms(event) {
    return this.rooms.filter(room =>
      room.capacity >= event.students.length &&
      this.roomHasFeatures(room, event.requiredFeatures)
    );
  }

  /**
   * Check if room has required features
   */
  roomHasFeatures(room, requiredFeatures) {
    return requiredFeatures.every(feature =>
      room.features.includes(feature)
    );
  }

  /**
   * Check student conflicts (HC1)
   */
  hasStudentConflict(event, slot, solution) {
    for (const student of event.students) {
      // Check if student has another event at this slot
      const existingEvent = this.findEventByStudentAndSlot(student, slot, solution);
      if (existingEvent) {
        return true;
      }
    }
    return false;
  }

  /**
   * Check room conflicts (HC4)
   */
  hasRoomConflict(slot, room, solution) {
    // Find if any event already assigned to this slot+room
    return Object.values(solution.assignments).some(
      assignment => assignment.slot === slot && assignment.room.id === room.id
    );
  }

  /**
   * Check timeslot availability (HC5)
   */
  isTimeslotAvailable(event, slot) {
    if (!event.availableSlots) {
      return true; // No restriction
    }
    return event.availableSlots.includes(slot);
  }

  /**
   * Repair mechanism for infeasible events
   */
  repair(event, solution) {
    // Strategy 1: Swap with existing event
    // Strategy 2: Move conflicting events
    // Strategy 3: Relax and retry

    // Implementation varies by preference
  }

  /**
   * Create empty solution structure
   */
  createEmptySolution() {
    return {
      assignments: {}, // event_id -> {slot, room}
      events: this.events,
      rooms: this.rooms,
      penalty: this.calculatePenalty // Will be high initially (soft constraints violated)
    };
  }
}
```

#### 3. Konfirmasi Meta-Heuristic Dominance

Survey mengkonfirmasi:
- **20/26 papers** menggunakan meta-heuristics
- **VNS, ILS, TS, SA** adalah paling populer
- **SA digunakan dalam 4 papers**

#### 4. Hybrid Approaches adalah Trend

Key insight:
- Meta-heuristics **jarang digunakan secara isolated**
- Hybrid dengan auxiliary heuristics adalah common practice

**Rekomendasi untuk SA Anda:**
```javascript
/**
 * Hybrid SA dengan berbagai auxiliary heuristics
 * Berdasarkan trend dari Filgueira et al. (2024)
 */

class HybridSA {
  constructor(config) {
    // SA components
    this.sa = new SimulatedAnnealing(config.sa);

    // Auxiliary heuristics
    this.localSearch = new HillClimbing();
    this.vns = new VariableNeighborhoodSearch();
    this.ts = new TabuList({ size: 100 });

    // Initialization
    this.initializer = new FeasibleInitialSolutionGenerator(config.instance);
  }

  solve() {
    // Phase 1: Generate feasible initial solution
    const initial = this.initializer.generate();

    // Phase 2: SA main loop dengan auxiliary components
    let current = initial;
    let best = current;
    let T = this.sa.T0;

    while (T > this.sa.Tf) {
      for (let i = 0; i < this.sa.iterationsPerTemp; i++) {
        // Generate neighbor (VNS-style neighborhood selection)
        const neighborhood = this.vns.selectNeighborhood();
        const neighbor = neighborhood.generate(current);

        // TS check
        if (this.ts.isTabu(neighbor)) {
          continue;
        }

        // SA acceptance
        const delta = neighbor.penalty - current.penalty;
        if (delta < 0 || Math.random() < Math.exp(-delta / T)) {
          current = neighbor;

          // Local search refinement
          if (delta < 0) {
            current = this.localSearch.improve(current);
          }

          // Update best
          if (current.penalty < best.penalty) {
            best = current;
          }
        }

        // Add to tabu if rejected
        if (delta >= 0) {
          this.ts.add(neighbor);
        }
      }

      T *= this.sa.alpha;
    }

    return best;
  }
}
```

---

## Arah Penelitian Lanjutan

### Research Gaps dari Survey

#### 1. Initialization Strategies

**Gap:**
- Tidak ada author yang menggunakan **good quality initial solutions**
- Semua feasible initial solutions mengabaikan soft constraints

**Research Question:**
Bagaimana menghasilkan good quality initial solutions yang mempertimbangkan soft constraints tanpa excessive computational cost?

**Approach:**
- Fast heuristics untuk soft constraint optimization
- Multi-objective initialization
- Machine learning untuk quality prediction

#### 2. Declining Publication Trend

**Observation:**
Publikasi menurun sejak 2017

**Possible explanations:**
- Field matang?
- Move ke other journals/conferences?
- Loss of interest?

**Research direction:**
Investigate apakah ada shift ke:
- Real-world applications
- Industry collaborations
- Other optimization domains

#### 3. Hyper-Heuristics Underrepresented

**Gap:**
- Hanya 1 paper dari 26
- Potensi besar tapi kurang eksplorasi

**Research direction:**
- Hyper-heuristics untuk ETP
- Learning-based heuristic selection
- Domain-independent approaches

#### 4. Exact Methods untuk Large-Scale

**Gap:**
- Hanya 4 papers menggunakan exact methods
- Scalability issues

**Research direction:**
- Hybrid exact-metaheuristic approaches
- Decomposition methods
- Parallel exact algorithms

---

## Kesimpulan

### Summary Temuan

1. **Meta-heuristics dominate** - 20/26 papers
2. **SA adalah pilihan populer** - 4 papers
3. **Hybrid approaches adalah norm** - meta-heuristics rarely isolated
4. **Feasible initialization adalah standard** - 23/26 papers
5. **Brazil leads production** - 7 papers
6. **Declining trend** sejak 2017

### Rekomendasi untuk Proyek

1. **Gunakan feasible initialization** dengan algorithm-integrated mechanism
2. **Implement hybrid SA** dengan auxiliary heuristics (VNS, TS, local search)
3. **Focus pada soft constraint optimization** setelah feasible solution tercapai
4. **Consider parallel approaches** untuk large-scale instances
5. **Validate dengan benchmark** (ITC datasets)

### Research Questions untuk Thesis

1. Bagaimana menghasilkan good quality initial solutions?
2. Apakah hybrid SA dengan VNS neighborhood dapat mengungguli pure SA?
3. Bagaimana scaling SA untuk large-scale ETP instances?
4. Dapatkah hyper-heuristic approach improve SA performance?

---

## Referensi

- Filgueira, J.D.F.T., et al. (2024). "A Survey of the State of the Art of Educational Timetabling Problems." *IEEE Conference Proceedings*.
- Abdipoor, S., et al. (2023). "Meta-heuristic Approaches for the University Course Timetabling Problem." *Intelligent Systems with Applications*, 19, 200253.
- Gotlieb, C.C. (1962). "The Construction of Class-Teacher Timetables." *IFIP Congress*.

---

*Analisis ini ditulis untuk mendukung penelitian tesis tentang University Course Timetabling Problem menggunakan Simulated Annealing.*
