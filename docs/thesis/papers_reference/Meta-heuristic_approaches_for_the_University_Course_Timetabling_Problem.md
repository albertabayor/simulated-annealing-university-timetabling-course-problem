# Analisis Paper: Meta-heuristic Approaches for the University Course Timetabling Problem

## Informasi Publikasi

- **Judul:** Meta-heuristic Approaches for the University Course Timetabling Problem
- **Penulis:** Sina Abdipoor*, Razali Yaakob, Say Leng Goh*, Salwani Abdullah
- **Affiliasi:**
  - Universiti Putra Malaysia (UPM), Malaysia
  - Universiti Malaysia Sabah, Malaysia
  - Universiti Kebangsaan Malaysia (UKM), Malaysia
- **Jurnal:** Intelligent Systems with Applications (Elsevier)
- **Volume/Issue:** Vol. 19, Article 200253
- **Tahun:** 2023
- **DOI:** 10.1016/j.iswa.2023.200253
- **URL:** https://www.sciencedirect.com/journal/intelligent-systems-with-applications
- **Status:** Published, Open Access (CC BY 4.0)
- **Tipe Paper:** Survey / Review Article

---

## Abstrak

Paper ini adalah **survey paper** yang menyajikan review komprehensif dan sistematis tentang pendekatan meta-heuristik untuk University Course Timetabling Problem (UCTP). Paper ini:

1. mereview, merangkum, dan mengkategorikan pendekatan meta-heuristik
2. memperkenalkan klasifikasi baru untuk hybrid meta-heuristik methods
3. menganalisis secara kritis manfaat dan keterbatasan metode-metode tersebut
4. mempresentasikan tantangan, gaps, dan possible future work

**Keywords:** Operational research, Combinatorial optimization, UCTP, Meta-heuristics, Hybrid meta-heuristics

---

## Kontribusi Utama Paper

Sebagai survey paper, kontribusi utamanya adalah:

1. **Thorough overview of UCTP** dan benchmark datasets
2. **Classification berdasarkan problem variant** (CB-CTP vs PE-CTP)
3. **Kategorisasi hybrid meta-heuristik** (collaborative vs integrative)
4. **Critical analysis** meta-heuristik dan hybrid approaches
5. **Identifikasi trends, strengths, dan limitations**
6. **Future research directions**

---

## Metodologi Survey

### Proses Filtering

Paper ini menggunakan systematic literature review dengan 4 tahap filtering:

```
Stage 0: 151 papers (initial search)
         ↓
Stage 1: 134 papers (remove duplicates)
         ↓
Stage 2: 108 papers (filter by problem type)
         ↓
Stage 3: 77 papers (filter by methodology)
         ↓
Stage 4: 45 papers (detailed analysis)
```

### Strategi Pencarian

| Aspect | Detail |
|--------|--------|
| **Keywords** | University Course Timetabling, Hybrid, Meta-heuristic |
| **Tahun** | 2015-2022 |
| **Databases** | Google Scholar, Elsevier, Springer, IEEE |
| **Final selection** | 45 papers |

### Distribusi Tahun Publikasi

Paper yang direview tersebar dari 2015-2022, menunjukkan UCTP masih **active research field**.

---

## University Course Timetabling Problem (UCTP)

### Definisi Formal

UCTP dapat didefinisikan secara formal sebagai:

**Given:**
- Set of events, E = {e₁, e₂, ..., e|E|}
- Set of time slots, T = {t₁, t₂, ..., t|T|} (biasanya 45: 9 slots/day × 5 days)
- Set of rooms, R = {r₁, r₂, ..., r|R|}
- Set of students, S = {s₁, s₂, ..., s|S|}
- Set of features, F = {f₁, f₂, ..., f|F|}
- Set of days, D = {d₁, d₂, ..., d|D|} (biasanya 5 hari)

**Find:**
Assignment (timetable) dari E events ke R rooms dan T time slots yang **minimizes constraint violations**

### Kompleksitas

- UCTP adalah masalah **NP-hard**
- Special case dari Graph Coloring Problem
- Ruang solusi: R^E cara alokasi
- Waktu komputasi meningkat secara eksponensial dengan ukuran masalah

---

## Variants UCTP

### 1. Curriculum-Based Course Timetabling (CB-CTP)

**Karakteristik:**
- Course terdiri dari set of lectures
- Curriculum pre-defined
- Student enrollment TIDAK diketahui
- Conflicts muncul dari curriculum
- TIDAK melibatkan student sectioning

### 2. Post-Enrollment Course Timetabling (PE-CTP)

**Karakteristik:**
- Setiap course adalah single event
- Student enrollment DIKETAHUI sebelum timetabling
- Conflicts muncul dari student enrollment data
- MELIBATKAN student sectioning
- Lebih kompleks karena sectioning

| Aspect | CB-CTP | PE-CTP |
|--------|--------|--------|
| **Conflict source** | Curriculum | Student enrollment |
| **Enrollment** | Unknown | Known |
| **Student sectioning** | No | Yes |
| **Course structure** | Multiple lectures | Single event |
| **Complexity** | Lower | Higher |

---

## Constraints UCTP

### Hard Constraints (HC) - Wajib Dipenuhi

| ID | Constraint | Deskripsi |
|----|------------|-----------|
| **HC1** | Student conflicts | Tidak ada student yang punya >1 course di waktu yang sama |
| **HC2** | Room features | Room harus memenuhi features yang dibutuhkan course |
| **HC3** | Room capacity | Jumlah student ≤ kapasitas room |
| **HC4** | Room conflicts | Tidak ada >1 course per slot per room |
| **HC5** | Availability | Course hanya bisa di-assigned ke preset time slots |
| **HC6** | Ordering | Course harus terjadwal sesuai urutan yang benar |
| **HC7** | All lectures scheduled | Semua lectures harus terjadwal |
| **HC8** | Curriculum conflicts | Lectures dari curriculum/teacher yang sama di periode berbeda |
| **HC9** | Teacher availability | Teacher tidak available → tidak bisa jadwal |

### Soft Constraints (SC) - Dipinalti

| ID | Constraint | Deskripsi |
|----|------------|-----------|
| **SC1** | Single course per day | Student tidak boleh hanya punya 1 course per hari |
| **SC2** | Consecutive courses | Student tidak boleh punya >2 course berurutan |
| **SC3** | Last slot | Student tidak boleh ada course di slot terakhir hari |
| **SC4** | Room capacity (soft) | Student ≤ kapasitas room (soft di ITC2007-Track3) |
| **SC5** | Spread days | Lectures course harus tersebar di minimum hari tertentu |
| **SC6** | Adjacent lectures | Lectures curriculum harus adjacent (consecutive periods) |
| **SC7** | Same room | Semua lectures course harus di room yang sama |

---

## Benchmark Datasets

### International Timetabling Competition (ITC)

PATAT conference mengadakan ITC setiap 2 tahun untuk standarisasi UCTP.

#### ITC Datasets Comparison

| Dataset | # Instances | Events | Rooms | Features | Students |
|---------|-------------|--------|-------|----------|----------|
| **ITC2002** | 20 | 350-440 | 10-11 | 5-10 | 200-350 |
| **ITC2007-Track2** (PE-CTP) | 24 | 100-600 | 10-20 | 10-30 | 300-1000 |
| **ITC2007-Track3** (CB-CTP) | 21 | 30-131 courses | 5-20 | - | 13-150 curricula |
| **ITC2019** | 30 | 36-2839 courses | 18-768 | - | 417-8813 classes |

#### ITC Winners

| Competition | Rank 1 | Rank 2 | Rank 3 |
|-------------|--------|--------|--------|
| **ITC2002** | SA (Meta-heuristic) | TS (Meta-heuristic) | GD (Meta-heuristic) |
| **ITC2007-Track2** | LS-based (Hybrid) | TS-based (Hybrid) | LS-based (Hybrid) |
| **ITC2007-Track3** | GD-based (Hybrid) | TS-based (Hybrid) | TS-based (Meta) |
| **ITC2019** | MIP (Mathematical) | MIP (Mathematical) | SA-based (Meta) |

**Insight:**
- Meta-heuristik dan hybrid methods mendominasi winners
- Mathematical approaches mulai competitive di ITC2019

### Other Benchmark Datasets

#### Socha Dataset
- 11 instances (5 small, 5 medium, 1 large)
- Developed by Ben Paechter
- Time limits: 90s (small), 900s (medium), 9000s (large)

#### Hard Dataset
- 60 instances (20 each size)
- Created by Lewis & Paechter (2007)
- Fokus pada hard constraints dan feasible solutions

---

## Meta-Heuristik untuk UCTP

### Klasifikasi Meta-Heuristik

```
Meta-Heuristics
├── Single-Solution Based
│   ├── Simulated Annealing (SA)
│   ├── Tabu Search (TS)
│   ├── Variable Neighborhood Search (VNS)
│   └── Iterated Local Search (ILS)
│
├── Population-Based
│   ├── Genetic Algorithms (GA)
│   ├── Evolutionary Algorithms (EA)
│   ├── Particle Swarm Optimization (PSO)
│   ├── Ant Colony Optimization (ACO)
│   ├── Artificial Bee Colony (ABC)
│   └── Differential Evolution (DE)
│
└── Hyper-Heuristics
    └── Selection Heuristics
```

### Popularitas Meta-Heuristik (2015-2022)

Berdasarkan paper yang direview:

1. **Evolutionary Algorithms (EA)** - Paling sering digunakan
2. **Swarm Intelligence (SI)** - Sangat populer
3. **Hybrid Methods** - Meningkat popularity
4. **Single-solution based** - Masih relevan

---

## Hybrid Meta-Heuristics

### Klasifikasi Baru (Kontribusi Paper Ini)

Paper ini memperkenalkan klasifikasi hybrid meta-heuristik menjadi 2 kategori:

#### 1. Collaborative Hybrid

**Definisi:** Dua atau lebih algoritma bekerja secara **parallel** dan **berkomunikasi** untuk menukar informasi.

**Karakteristik:**
- Multiple algorithms run simultaneously
- Information exchange between algorithms
- Setiap algorithm menjaga identitasnya
- Contoh: GA + SA berjalan parallel dan bertukar solusi terbaik

**Arsitektur:**
```
┌─────────────┐     exchange     ┌─────────────┐
│  Algorithm  │ ←───────────→  │  Algorithm  │
│     (SA)    │                 │     (GA)    │
└─────────────┘                 └─────────────┘
      ↓                               ↓
┌─────────────┐     exchange     ┌─────────────┐
│  Algorithm  │ ←───────────→  │  Algorithm  │
│     (TS)    │                 │    (PSO)    │
└─────────────┘                 └─────────────┘
```

#### 2. Integrative Hybrid

**Definisi:** Satu algoritma **diintegrasikan** ke dalam algoritma lain, membentuk algoritma baru.

**Karakteristik:**
- Komponen dari satu algorithm embedded ke algorithm lain
- Menghasilkan single unified algorithm
- Contoh: SA dengan neighborhood structure dari TS

**Arsitektur:**
```
Main Algorithm (e.g., GA)
    │
    ├── Crossover (GA component)
    ├── Mutation (GA component)
    ├── Local Search ← TS component (embedded)
    │   ├── Tabu list
    │   └── Neighborhood search
    └── Selection (GA component)
```

### Perbandingan Collaborative vs Integrative

| Aspect | Collaborative | Integrative |
|--------|---------------|-------------|
| **Struktur** | Parallel, independent | Sequential/embedded |
| **Komunikasi** | Information exchange | Direct integration |
| **Kompleksitas** | Higher (multiple algorithms) | Moderate (single algorithm) |
| **Diversity** | Higher (multiple search patterns) | Lower (single search pattern) |
| **Contoh** | GA+SA parallel | GA with TS local search |

---

## Analisis Kritis Meta-Heuristik

### Simulated Annealing (SA)

**Strengths:**
- Excellent exploitation capability
- Asymptotic convergence (teoretis menuju optimal)
- Simple implementation
- Effective escape dari local optimum

**Limitations:**
- Parameter-sensitive (cooling schedule)
- Slow convergence
- Lack of memory (hanya mempertahankan current solution)
- Single-solution based (kurang diversity)

**Best for:**
- Fine-tuning solutions
- Problems dengan banyak local optima
- Implementasi sederhana yang needed

### Tabu Search (TS)

**Strengths:**
- Memory-based (tabu list)
- Excellent exploitation
- Flexible neighborhood structures
- Good intensification

**Limitations:**
- Parameter-sensitive (tabu tenure, list size)
- Can get stuck di cycles
- Diversification bisa lemah
- Memory intensive

**Best for:**
- Problems dengan complex neighborhood
- Intensification-focused search
- Medium-sized instances

### Genetic Algorithms (GA)

**Strengths:**
- Population-based (high diversity)
- Excellent exploration
- Parallelizable
- Flexible representation

**Limitations:**
- Premature convergence
- Parameter-sensitive (crossover, mutation rates)
- Slower convergence
- Complex implementation

**Best for:**
- Large-scale problems
- Exploration-focused search
- Problems dengan complex fitness landscapes

### Variable Neighborhood Search (VNS)

**Strengths:**
- Multiple neighborhood structures
- Balance exploration/exploitation
- Simple concept
- Effective escape dari local optima

**Limitations:**
- Neighborhood design critical
- Can be slow (many neighborhoods)
- Parameter-sensitive
- Not as widely adopted

**Best for:**
- Problems dengan diverse neighborhood structures
- Medium-sized instances

### Swarm Intelligence (PSO, ACO, ABC)

**Strengths:**
- Population-based exploration
- Inspired by nature (proven concepts)
- Good for continuous and discrete
- Emergent behavior

**Limitations:**
- Complex parameter tuning
- Premature convergence possible
- Problem-specific adaptation needed
- Computational overhead

**Best for:**
- Problems dengan landscape structures
- Dynamic environments
- Multi-objective problems

---

## Tren dan Kesenjangan Penelitian

### Tren Utama (2015-2022)

1. **Hybrid approaches mendominasi**
   - Kombinasi meta-heuristik dengan local search
   - Collaborative dan integrative hybrids

2. **Multi-objective optimization meningkat**
   - Bukan hanya minimize penalty
   - Energy efficiency, fairness, robustness

3. **Real-world applications fokus**
   - Tidak hanya benchmark
   - Institution-specific constraints

4. **Hyper-heuristics emerging**
   - Learning to select heuristics
   - Domain-independent approaches

### Research Gaps

1. **General applicability**
   - Kebanyakan approaches instance-specific
   - Kurang general-purpose solvers

2. **Theoretical analysis**
   - Kurang convergence proofs
   - Complexity analysis tidak lengkap

3. **Parameter tuning**
   - Parameter selection masih ad-hoc
   - Kurang systematic tuning methods

4. **Large-scale instances**
   - Kebanyakan papers fokus medium-sized
   - Scalability issues unexplored

5. **ITC2019 understudied**
   - Baru 30 instances, sedikit papers
   - High complexity (student sectioning)

6. **Hyper-heuristics kurang diadaptasi**
   - Potensi besar tapi kurang eksplorasi

---

## Implikasi untuk Proyek Ini

### Relevansi Tinggi

Paper ini sangat relevan untuk proyek Anda karena:

1. **Comprehensive overview** dari semua meta-heuristik untuk UCTP
2. **Klasifikasi hybrid** yang bisa diaplikasikan
3. **Identifikasi gaps** untuk research directions
4. **Benchmark comparison** untuk validasi

### Rekomendasi untuk Proyek

#### 1. Pilih Meta-Heuristik yang Tepat

Berdasarkan analisis paper:

| Requirement | Recommended Meta-Heuristic |
|-------------|---------------------------|
| **Simple implementation** | Simulated Annealing |
| **Exploration-focused** | Genetic Algorithm |
| **Fast convergence** | Tabu Search + Local Search |
| **Large-scale** | Hybrid GA + Local Search |
| **Balance exploration/exploitation** | SA with Adaptive Moves |

#### 2. Pertimbangkan Hybrid Approach

**Rekomendasi: Integrative Hybrid**

```
Simulated Annealing with Adaptive Components:

SA Algorithm
├── Move Generation (Adaptive)
│   ├── Single-event move (exploitation)
│   ├── Swap move (exploration)
│   └── Kempe chain (complex move)
│
├── Cooling Schedule (Adaptive)
│   ├── Geometric cooling
│   └── Reheat mechanism
│
└── Local Search (Integrative Component)
    ├── Hill climbing
    └── Tabu list (prevent cycling)
```

#### 3. Implementasi Hybrid SA untuk UCTP

```javascript
/**
 * Hybrid Simulated Annealing dengan Integrative Components
 * Berdasarkan rekomendasi dari Abdipoor et al. (2023)
 */

class HybridSA {
  constructor(config) {
    this.T0 = config.T0 || 1000;
    this.Tf = config.Tf || 0.01;
    this.alpha = config.alpha || 0.995;
    this.reheatThreshold = config.reheatThreshold || 100;

    // Integrative component: Tabu list
    this.tabuList = new TabuList({
      maxSize: config.tabuSize || 100
    });

    // Adaptive move selection
    this.moveSelector = new AdaptiveMoveSelector({
      moves: ['single', 'swap', 'kempe'],
      initialProbabilities: [0.5, 0.3, 0.2]
    });
  }

  solve(instance) {
    // Generate initial feasible solution
    let current = this.generateInitialSolution(instance);
    let best = current.clone();
    let T = this.T0;
    let noImprovement = 0;

    while (T > this.Tf) {
      for (let i = 0; i < this.iterationsPerTemp; i++) {
        // Adaptive move generation
        const moveType = this.moveSelector.selectMove();
        const neighbor = this.generateMove(current, moveType);

        // Check tabu status (integrative component)
        if (this.tabuList.isTabu(neighbor)) {
          // Aspiration criterion: terima jika lebih baik
          if (neighbor.penalty < current.penalty) {
            current = neighbor;
          }
        } else {
          // SA acceptance criterion
          const delta = neighbor.penalty - current.penalty;
          if (delta < 0 || Math.random() < Math.exp(-delta / T)) {
            current = neighbor;

            // Update move selection probability
            if (delta < 0) {
              this.moveSelector.update(moveType, true);
            }
          }
        }

        // Update best
        if (current.penalty < best.penalty) {
          best = current.clone();
          noImprovement = 0;
        } else {
          noImprovement++;
        }
      }

      // Reheat mechanism (integrative component)
      if (noImprovement > this.reheatThreshold) {
        T = this.T0; // Reheat to initial temperature
        noImprovement = 0;
      } else {
        T *= this.alpha; // Geometric cooling
      }
    }

    return best;
  }

  generateMove(solution, moveType) {
    switch (moveType) {
      case 'single':
        return this.singleEventMove(solution);
      case 'swap':
        return this.swapMove(solution);
      case 'kempe':
        return this.kempeChainMove(solution);
      default:
        throw new Error(`Unknown move type: ${moveType}`);
    }
  }

  singleEventMove(solution) {
    // Move single event to different slot/room
    const neighbor = solution.clone();
    const eventIdx = Math.floor(Math.random() * neighbor.events.length);

    neighbor.events[eventIdx] = {
      ...neighbor.events[eventIdx],
      slot: Math.floor(Math.random() * 45) + 1,
      room: Math.floor(Math.random() * solution.rooms.length)
    };

    return neighbor;
  }

  swapMove(solution) {
    // Swap two events
    const neighbor = solution.clone();
    const idx1 = Math.floor(Math.random() * neighbor.events.length);
    const idx2 = Math.floor(Math.random() * neighbor.events.length);

    const tempSlot = neighbor.events[idx1].slot;
    const tempRoom = neighbor.events[idx1].room;

    neighbor.events[idx1].slot = neighbor.events[idx2].slot;
    neighbor.events[idx1].room = neighbor.events[idx2].room;

    neighbor.events[idx2].slot = tempSlot;
    neighbor.events[idx2].room = tempRoom;

    return neighbor;
  }

  kempeChainMove(solution) {
    // Kempe chain interchange (more complex)
    // Implementasi sesuai literatur UCTP
    // ...
    return solution; // placeholder
  }
}

/**
 * Adaptive Move Selector
 * Mempelajari move type mana yang paling efektif
 */
class AdaptiveMoveSelector {
  constructor(config) {
    this.moves = config.moves;
    this.probabilities = config.initialProbabilities;
    this.successCounts = this.moves.map(() => 0);
    this.totalAttempts = this.moves.map(() => 0);
  }

  selectMove() {
    // Roulette wheel selection
    const r = Math.random();
    let cumsum = 0;

    for (let i = 0; i < this.moves.length; i++) {
      cumsum += this.probabilities[i];
      if (r <= cumsum) {
        this.totalAttempts[i]++;
        return this.moves[i];
      }
    }

    return this.moves[this.moves.length - 1];
  }

  update(moveType, success) {
    const idx = this.moves.indexOf(moveType);

    if (success) {
      this.successCounts[idx]++;
    }

    // Update probabilities based on success rate
    const totalSuccess = this.successCounts.reduce((a, b) => a + b, 0);
    const totalAttempts = this.totalAttempts.reduce((a, b) => a + b, 0);

    if (totalAttempts > 0) {
      this.probabilities = this.moves.map((_, i) => {
        const successRate = this.totalAttempts[i] > 0
          ? this.successCounts[i] / this.totalAttempts[i]
          : 0;
        return successRate;
      });

      // Normalize
      const sum = this.probabilities.reduce((a, b) => a + b, 0);
      this.probabilities = this.probabilities.map(p => p / sum);
    }
  }
}

/**
 * Tabu List untuk integrative component
 */
class TabuList {
  constructor(config) {
    this.maxSize = config.maxSize || 100;
    this.list = [];
  }

  isTabu(solution) {
    return this.list.some(s => this.equals(s, solution));
  }

  add(solution) {
    this.list.push(solution);

    if (this.list.length > this.maxSize) {
      this.list.shift(); // Remove oldest
    }
  }

  equals(s1, s2) {
    // Implementasi equality check untuk solutions
    // Bisa menggunakan hash atau direct comparison
    return JSON.stringify(s1.events) === JSON.stringify(s2.events);
  }
}
```

#### 4. Validasi dengan Benchmark

Gunakan benchmark yang disarankan paper ini:

| Benchmark | Use case |
|-----------|----------|
| **ITC2007-Track3** | CB-CTP validation |
| **ITC2007-Track2** | PE-CTP validation |
| **Socha** | Quick testing |
| **Hard** | Feasibility testing |

---

## Future Research Directions

Untuk thesis Anda, berikut adalah directions yang menjanjikan:

### 1. Hyper-Heuristics untuk UCTP

**Research Question:** Can we learn to select the best heuristic for each state of the search?

**Approach:**
- Machine learning untuk move selection
- Adaptive heuristic selection
- Domain-independent framework

### 2. Multi-Objective UCTP

**Research Question:** How to balance multiple competing objectives?

**Objectives:**
- Minimize penalty
- Maximize room utilization
- Minimize energy consumption
- Maximize fairness

**Approach:** Pareto optimization with SA

### 3. Large-Scale UCTP

**Research Question:** How to scale meta-heuristics to thousands of events?

**Approach:**
- Decomposition methods
- Parallel computing
- Hierarchical optimization

### 4. Dynamic UCTP

**Research Question:** How to handle changes after initial timetabling?

**Scenarios:**
- Room unavailability
- Enrollment changes
- Teacher availability changes

**Approach:** Reactive SA with quick repair

### 5. Parameter-Free SA

**Research Question:** Can we eliminate parameter tuning?

**Approach:**
- Adaptive cooling schedules
- Self-adjusting parameters
- Learning-based parameter selection

---

## Kesimpulan

### Summary

Paper ini adalah survey yang sangat comprehensive untuk meta-heuristik UCTP:

1. **Systematic review** dari 45 papers (2015-2022)
2. **Novel classification** untuk hybrid meta-heuristics
3. **Critical analysis** strengths dan limitations
4. **Identification** trends dan research gaps

### Takeaways untuk Proyek Anda

1. **SA adalah solid choice** - simple, effective, proven
2. **Hybrid approaches** menunjukkan promise tinggi
3. **Adaptive mechanisms** dapat meningkatkan performa
4. **Benchmark validation** penting untuk comparison
5. **Parameter tuning** adalah challenge utama

### Research Questions untuk Thesis

Berdasarkan gaps yang diidentifikasi:

1. Bagaimana mengoptimalkan parameter SA secara otomatis?
2. Apakah hybrid SA dengan adaptive moves dapat mengungguli approaches lain?
3. Bagaimana scaling SA untuk large-scale instances?
4. Dapatkah hyper-heuristic approach diterapkan untuk UCTP?

---

## Referensi

- Abdipoor, S., Yaakob, R., Goh, S.L., Abdullah, S. (2023). "Meta-heuristic Approaches for the University Course Timetabling Problem." *Intelligent Systems with Applications*, 19, 200253. https://doi.org/10.1016/j.iswa.2023.200253
- Lewis, R., & Thompson, J. (2015). "Analysing the Effects of Solution Space Connectivity and Hardness on the Graph Colouring Problem." *Evolutionary Computation*.
- Di Gaspero, L., & Schaerf, A. (2006). "Neighborhood Portfolio Approach for Local Search Applied to Timetabling Problems." *Journal of Mathematical Modelling and Algorithms*.

---

*Analisis ini ditulis untuk mendukung penelitian tesis tentang University Course Timetabling Problem menggunakan Simulated Annealing.*
