# Analisis Paper: Bibliometric Analysis of University Timetabling Using Publish and Perish

## Informasi Publikasi

- **Judul:** Bibliometric Analysis of University Timetabling Using Publish and Perish
- **Penulis:** Dyah Lintang Trenggonowati*, Lely Herlina, Evi Febianti, Muhammad Adha Ilhami, Yusraini Muharni, Bobby Kurniawan, Kulsum, Ade Irman
- **Affiliasi:** Industrial Engineering Department, Engineering Faculty, Universitas Sultan Ageng Tirtayasa, Indonesia
- **Conference:** Conference on Broad Exposure to Science and Technology 2021 (BEST 2021)
- **Proceedings:** Advances in Engineering Research, Volume 210
- **Publisher:** Atlantis Press
- **Tahun:** 2021 (dipublikasikan 2022)
- **DOI:** Tidak tersedia dalam teks
- **License:** CC BY-NC 4.0
- **Tipe Paper:** Bibliometric Analysis

---

## Abstrak

Paper ini menyajikan **bibliometric analysis** untuk University Course Timetabling Problem (UCTP). Menggunakan software **Publish and Perish** untuk pencarian data dan **VOSviewer** untuk analisis data.

**Temuan utama:**
- 62 artikel relevan dianalisis
- Trend penyelesaian UCTP menggunakan metaheuristic models
- **Genetic Algorithm (GA)** dan **Simulated Annealing (SA)** adalah trend saat ini
- Ada research gaps dalam improvement kedua metode tersebut

**Keywords:** Bibliometric Analysis, UCTP, VOSviewer, Genetic Algorithms, Simulated Annealing

---

## Latar Belakang

### University Course Timetabling Problem (UCTP)

**Definisi:**
Allocation of lecturers, students, and courses into rooms in a span of periods.

**Tantangan:**
- Dinamakan sebagai "main enemy" oleh universitas
- NP-hard problem
- Complexity dalam constructing university timetables
- Limited resources (time, rooms, lecturers)

**Parameter masalah:**
1. Limited time
2. Limited resources
3. Number of meetings
4. Limited number of constraints

### Jenis University Timetabling

| Tipe | Fokus |
|------|-------|
| **Course Scheduling** | Distribusi waktu, rooms, dan lecturers |
| **Exam Scheduling** | Waktu tertentu dalam limited rooms |

### Keterbatasan Riset

Menurut paper ini, literature review studies untuk UCTP **sulit ditemukan**. Ini menciptakan opportunities untuk:
- Melihat bagaimana research berlangsung
- Mengidentifikasi urgencies yang direkomendasikan untuk UCTP saat ini

---

## Metodologi Bibliometric Analysis

### Framework: Ilhami et al. (2019)

Paper ini menggunakan 5 langkah:

### Langkah 1: Defining Search Keyword

**Keywords yang digunakan:**
- "Course scheduling"
- "University timetable"

**Exclusion:**
- School course schedules
- Training programs

### Langkah 2: Initial Search Result

**Tools:** Publish and Perish Software v7.32.3373.7310

**Databases:** Google Scholar dan Scopus

| Keyword | Database | Results |
|---------|----------|---------|
| Course scheduling | Scopus | 200 |
| Course scheduling | Google Scholar | 998 |
| University timetable | Scopus | 200 |
| University timetable | Google Scholar | 999 |

**Catatan:**
- Publish or Perish limits Google Scholar ke 1000 articles
- Scopus limited ke 200 articles
- Google Scholar provides more articles

### Langkah 3: Refinement of Search Result

**Kriteria inklusi:**
1. Articles dari journals (bukan conference proceedings)
2. Citation value **di atas 4**
3. Abstract fits UCTP problem

**Hasil refinement:**

| Keyword | Google Scholar | Scopus |
|---------|----------------|--------|
| Course scheduling | 23 | 14 |
| University scheduling | 47 | 17 |

### Langkah 4: Compiling Initial Data Statistics

**Format:** CSV (comma-separated values)

**Tujuan:**
- Combine articles dari Scopus dan Google Scholar
- Complete metadata untuk mapping
- Ensure unique data

**Final result:** **62 unique articles**

### Langkah 5: Data Analysis

**Tool:** VOSviewer

**Analysis types:**
1. **Co-occurrence** - network visualization antar keywords
2. **Full counting** - menghitung articles sesuai appear

**Visualization outputs:**
1. Network visualization
2. Overlay visualization
3. Density visualization

**Hardware:**
- Intel® Core™ i5-8265U CPU @ 1.60GHz 1.80 GHz
- 8.00 GB RAM
- 64-bit OS, x64-based processor

---

## Hasil dan Pembahasan

### Temuan Utama dari VOSviewer

#### 1. Keyword Dominance

Dari overlay visualization (Figure 2):

| Ranking | Keyword | Circle Size |
|---------|---------|-------------|
| 1 | Integer programming | Largest |
| 2 | University course timetabling | Large |
| 3 | Course timetabling | Large |

#### 2. Color Interpretation (Overlay Visualization)

- **Dark colors** = Previous events/trends
- **Light colors** = **Current trends**

**Current trend keywords (light colors):**
- **Genetic Algorithm (GA)**
- **Simulated Annealing (SA)**

#### 3. Metaheuristics Dominance

Paper menyimpulkan bahwa research trends UCTP lebih menggunakan:
- **Heuristic methods**
- **Metaheuristic methods**

Dibanding mathematical models.

### Analysis of Metaheuristics

#### Genetic Algorithm (GA)

**Characteristics:**
- Works on principles of genetics
- Effective untuk NP-hard problems
- More popular than SA

#### Simulated Annealing (SA)

**Characteristics:**
- Moves based on temperature increase
- Inspired dari steel annealing process
- Less popular than GA
- Still significant in current research

### Research Gaps

Paper mengidentifikasi gaps:

1. **Proposal improvement of solution methods**
   - Khususnya untuk GA dan SA
   - Opportunities untuk enhancement

2. **Mathematical models**
   - Can still be used as alternative
   - Especially untuk describe UCTP in detail

3. **Hybrid approaches**
   - Combine two metaheuristic models
   - Produce more efficient solutions
   - Example: change rules for generating parameters

---

## Constraints dalam UCTP

Paper ini mengidentifikasi constraints dari Thepphakorn dan Pongcharoen:

### Hard Constraints (14 identified)

Yang paling sering digunakan:
1. **Students can only have one lecture at a time**
2. **A lecturer can only deliver one lecture at a time**
3. **Lecturers' unavailability is considered**

### Soft Constraints (18 identified)

Yang paling sering digunakan:
1. **Room timetables should be as compact as possible**
2. **Lecturers can specify times when they prefer not to lecture**
3. **Some lectures should not take place late in the evening**
4. **Number of students having lunch at a given time should be controlled**
5. **Classes should have lectures either in the morning or in the afternoon**

---

## Implikasi untuk Proyek Ini

### Relevansi

Paper ini sangat relevan karena:

1. **Mengkonfirmasi SA adalah trend** - Validasi pilihan metaheuristik
2. **Identifikasi research gaps** dalam SA improvement
3. **Comprehensive constraints list** untuk modeling
4. **Bibliometric evidence** bahwa SA adalah active research area

### Rekomendasi untuk Proyek

#### 1. Validasi Pilihan SA

Berdasarkan bibliometric analysis:
- SA adalah **current trend** (light color in VOSviewer)
- SA dan GA adalah dominant metaheuristics untuk UCTP
- Ada **research gap** dalam SA improvement

#### 2. Fokus pada Research Gaps

**Gap yang diidentifikasi:**
> "Proposal improvement of solution method especially in genetic algorithm and simulated annealing"

**Arah pengembangan:**
- Hybrid SA dengan metaheuristics lain
- Improved parameter control untuk SA
- Adaptive mechanisms dalam SA

#### 3. Implementasi SA dengan Enhancement

```javascript
/**
 * Enhanced Simulated Annealing untuk UCTP
 * Berdasarkan research gaps dari Trenggonowati et al. (2021)
 */

class EnhancedSA {
  constructor(config) {
    // Standard SA parameters
    this.T0 = config.T0 || 1000;
    this.Tf = config.Tf || 0.01;
    this.alpha = config.alpha || 0.995;

    // Enhancement 1: Adaptive cooling (research gap)
    this.adaptiveCooling = config.adaptiveCooling || true;
    this.coolingHistory = [];

    // Enhancement 2: Hybrid with GA concepts (research gap)
    this.useCrossover = config.useCrossover || false;
    this.crossoverProbability = config.crossoverProbability || 0.1;

    // Enhancement 3: Multiple neighborhood structures
    this.neighborhoods = ['single', 'swap', 'kempe'];
    this.neighborhoodWeights = [0.5, 0.3, 0.2];
  }

  /**
   * Enhanced SA dengan adaptive mechanisms
   */
  solve(instance) {
    // Generate feasible initial solution
    let current = this.generateFeasibleSolution(instance);
    let best = current.clone();
    let T = this.T0;

    while (T > this.Tf) {
      for (let i = 0; i < this.iterationsPerTemp; i++) {
        // Select neighborhood (adaptive)
        const neighborhood = this.selectNeighborhood();
        const neighbor = neighborhood.generate(current);

        // Hybrid: GA crossover (occasionally)
        if (this.useCrossover && Math.random() < this.crossoverProbability) {
          const crossoverPartner = this.selectCrossoverPartner();
          const crossoverChild = this.crossover(current, crossoverPartner);
          if (crossoverChild.penalty < neighbor.penalty) {
            neighbor = crossoverChild;
          }
        }

        // SA acceptance dengan adaptive threshold
        const delta = neighbor.penalty - current.penalty;
        const adaptiveThreshold = this.getAdaptiveThreshold(T);

        if (delta < 0 || Math.random() < Math.exp(-delta / adaptiveThreshold)) {
          current = neighbor;

          if (current.penalty < best.penalty) {
            best = current.clone();
          }
        }

        // Update neighborhood weights
        this.updateNeighborhoodWeights(neighborhood, delta < 0);
      }

      // Adaptive cooling (enhancement)
      T = this.adaptiveCooling ? this.getAdaptiveTemperature(T) : T * this.alpha;
    }

    return best;
  }

  /**
   * Adaptive temperature calculation
   * Research gap: improvement dalam cooling schedule
   */
  getAdaptiveTemperature(currentT) {
    // Track improvement history
    this.coolingHistory.push({
      T: currentT,
      improvement: this.recentImprovement()
    });

    // If improvement detected, slow cooling
    if (this.recentImprovement() > threshold) {
      return currentT * (this.alpha + 0.001); // Slower cooling
    }

    return currentT * this.alpha; // Standard cooling
  }

  /**
   * GA crossover integration
   * Research gap: hybrid approaches
   */
  crossover(parent1, parent2) {
    // Uniform crossover untuk UCTP
    const child = parent1.clone();

    for (let i = 0; i < child.events.length; i++) {
      if (Math.random() < 0.5) {
        child.events[i] = parent2.events[i].clone();
      }
    }

    return child;
  }

  /**
   * Adaptive neighborhood selection
   */
  selectNeighborhood() {
    // Roulette wheel selection based on weights
    const r = Math.random();
    let cumsum = 0;

    for (let i = 0; i < this.neighborhoods.length; i++) {
      cumsum += this.neighborhoodWeights[i];
      if (r <= cumsum) {
        return this.neighborhoods[i];
      }
    }

    return this.neighborhoods[this.neighborhoods.length - 1];
  }

  /**
   * Update neighborhood weights based on success
   */
  updateNeighborhoodWeights(neighborhood, success) {
    const idx = this.neighborhoods.indexOf(neighborhood);

    if (success) {
      // Increase weight for successful neighborhood
      this.neighborhoodWeights[idx] *= 1.1;
    } else {
      // Decrease weight for unsuccessful neighborhood
      this.neighborhoodWeights[idx] *= 0.9;
    }

    // Normalize
    const sum = this.neighborhoodWeights.reduce((a, b) => a + b, 0);
    this.neighborhoodWeights = this.neighborhoodWeights.map(w => w / sum);
  }

  /**
   * Generate feasible initial solution
   * Menggunakan constraints yang diidentifikasi dalam paper
   */
  generateFeasibleSolution(instance) {
    const solution = this.createEmptySolution(instance);

    // Sort events by difficulty (most constrained first)
    const sortedEvents = this.sortEventsByDifficulty(instance.events);

    for (const event of sortedEvents) {
      // Find assignment yang satisfies hard constraints:
      // HC1: Student only has one lecture at a time
      // HC2: Lecturer only delivers one lecture at a time
      // HC3: Lecturer unavailability considered

      const assignment = this.findFeasibleAssignment(event, solution, instance);
      if (assignment) {
        solution.assignments[event.id] = assignment;
      }
    }

    return solution;
  }

  /**
   * Sort events by difficulty
   * Priority: events dengan lebih banyak constraints
   */
  sortEventsByDifficulty(events) {
    return [...events].sort((a, b) => {
      const difficultyA = this.calculateEventDifficulty(a);
      const difficultyB = this.calculateEventDifficulty(b);
      return difficultyB - difficultyA; // Descending
    });
  }

  calculateEventDifficulty(event) {
    let difficulty = 0;

    // Student count contributes to difficulty
    difficulty += event.students.length * 10;

    // Lecturer availability constraints
    if (event.lecturer.unavailableSlots) {
      difficulty += (45 - event.lecturer.availableSlots.length) * 5;
    }

    // Room requirements
    difficulty += event.requiredFeatures.length * 5;

    return difficulty;
  }

  /**
   * Find feasible assignment yang satisfies all hard constraints
   */
  findFeasibleAssignment(event, solution, instance) {
    for (let slot = 1; slot <= 45; slot++) {
      // Check lecturer availability (HC3)
      if (event.lecturer.unavailableSlots &&
          event.lecturer.unavailableSlots.includes(slot)) {
        continue;
      }

      for (const room of instance.rooms) {
        // Check room capacity and features
        if (room.capacity < event.students.length) continue;
        if (!this.roomHasFeatures(room, event.requiredFeatures)) continue;

        // Check HC1: Student conflicts
        if (this.hasStudentConflict(event, slot, solution)) continue;

        // Check HC2: Lecturer conflicts
        if (this.hasLecturerConflict(event.lecturer, slot, solution)) continue;

        // Check room availability
        if (this.hasRoomConflict(slot, room, solution)) continue;

        return { slot, room };
      }
    }

    return null; // No feasible assignment found
  }

  /**
   * Penalty calculation untuk soft constraints
   */
  calculatePenalty(solution, instance) {
    let penalty = 0;

    // SC1: Room timetables compact
    penalty += this.calculateCompactnessPenalty(solution);

    // SC2: Lecturer preferences
    penalty += this.calculateLecturerPreferencePenalty(solution);

    // SC3: No late evening lectures
    penalty += this.calculateLateEveningPenalty(solution);

    // SC4: Control lunch time students
    penalty += this.calculateLunchTimePenalty(solution);

    // SC5: Morning or afternoon consistency
    penalty += this.calculateConsistencyPenalty(solution);

    return penalty;
  }

  /**
   * SC1: Room timetables should be as compact as possible
   */
  calculateCompactnessPenalty(solution) {
    let penalty = 0;

    for (const room of solution.rooms) {
      const assignments = solution.getAssignmentsByRoom(room);
      const slots = assignments.map(a => a.slot).sort((a, b) => a - b);

      // Penalty untuk gaps dalam schedule
      for (let i = 1; i < slots.length; i++) {
        const gap = slots[i] - slots[i - 1];
        if (gap > 1) {
          penalty += gap - 1; // Penalty per gap
        }
      }
    }

    return penalty;
  }

  /**
   * SC2: Lecturer preferences
   */
  calculateLecturerPreferencePenalty(solution) {
    let penalty = 0;

    for (const [lecturerId, preferences] of solution.lecturerPreferences) {
      const assignments = solution.getAssignmentsByLecturer(lecturerId);

      for (const assignment of assignments) {
        if (assignments.preferredNotToLecture.includes(assignment.slot)) {
          penalty += 1;
        }
      }
    }

    return penalty;
  }

  /**
   * SC3: No late evening lectures
   */
  calculateLateEveningPenalty(solution) {
    let penalty = 0;
    const eveningSlots = [41, 42, 43, 44, 45]; // Last period of day

    for (const assignment of solution.assignments) {
      if (eveningSlots.includes(assignment.slot)) {
        penalty += 1;
      }
    }

    return penalty;
  }

  /**
   * SC4: Control lunch time students
   */
  calculateLunchTimePenalty(solution) {
    let penalty = 0;
    const lunchSlots = [20, 21, 22]; // Assuming lunch around midday

    // Count students at lunch
    const studentsAtLunch = new Set();
    for (const assignment of solution.assignments) {
      if (lunchSlots.includes(assignment.slot)) {
        assignment.event.students.forEach(s => studentsAtLunch.add(s));
      }
    }

    // Penalty jika terlalu banyak atau terlalu sedikit
    const targetStudents = 100; // Configurable
    if (studentsAtLunch.size > targetStudents * 1.2) {
      penalty += (studentsAtLunch.size - targetStudents * 1.2);
    }

    return penalty;
  }

  /**
   * SC5: Morning or afternoon consistency
   */
  calculateConsistencyPenalty(solution) {
    let penalty = 0;

    for (const [courseId, assignments] of solution.getCourseAssignments()) {
      const morningSlots = assignments.filter(a => a.slot <= 22).length;
      const afternoonSlots = assignments.filter(a => a.slot > 22).length;

      // Penalty jika mixed (should be either morning OR afternoon)
      if (morningSlots > 0 && afternoonSlots > 0) {
        penalty += Math.min(morningSlots, afternoonSlots);
      }
    }

    return penalty;
  }
}
```

#### 4. Constraints Modeling untuk UCTP

```javascript
/**
 * UCTP Constraints
 * Berdasarkan Thepphakorn and Pongcharoen (dikutip dalam paper)
 */

class UCTPConstraints {
  /**
   * Hard Constraints - wajib dipenuhi untuk feasible solution
   */

  /**
   * HC1: Students can only have one lecture at a time
   */
  static checkStudentConflicts(event, slot, solution) {
    for (const student of event.students) {
      const existingAssignment = solution.findAssignmentByStudentAndSlot(student, slot);
      if (existingAssignment) {
        return true; // Conflict found
      }
    }
    return false; // No conflict
  }

  /**
   * HC2: A lecturer can only deliver one lecture at a time
   */
  static checkLecturerConflicts(lecturer, slot, solution) {
    const existingAssignment = solution.findAssignmentByLecturerAndSlot(lecturer, slot);
    return existingAssignment !== null;
  }

  /**
   * HC3: Lecturer unavailability is considered
   */
  static checkLecturerAvailability(lecturer, slot) {
    if (!lecturer.unavailableSlots) return true; // No restrictions
    return !lecturer.unavailableSlots.includes(slot);
  }

  /**
   * Additional hard constraints
   */

  /**
   * HC4: Room capacity must be sufficient
   */
  static checkRoomCapacity(room, event) {
    return room.capacity >= event.students.length;
  }

  /**
   * HC5: Room must have required features
   */
  static checkRoomFeatures(room, requiredFeatures) {
    return requiredFeatures.every(feature => room.features.includes(feature));
  }

  /**
   * HC6: No room can have two events at the same time
   */
  static checkRoomConflicts(room, slot, solution) {
    const existingAssignment = solution.findAssignmentByRoomAndSlot(room, slot);
    return existingAssignment !== null;
  }

  /**
   * Soft Constraints - dipinalti untuk quality assessment
   */

  /**
   * SC1: Room timetables should be as compact as possible
   * Minimize gaps dalam room schedules
   */
  static calculateCompactnessPenalty(solution) {
    let penalty = 0;

    for (const room of solution.rooms) {
      const assignments = solution.getAssignmentsByRoom(room)
        .sort((a, b) => a.slot - b.slot);

      for (let i = 1; i < assignments.length; i++) {
        const gap = assignments[i].slot - assignments[i - 1].slot - 1;
        penalty += gap > 0 ? gap : 0;
      }
    }

    return penalty;
  }

  /**
   * SC2: Lecturers can specify times when they prefer not to lecture
   */
  static calculateLecturerPreferencePenalty(solution) {
    let penalty = 0;

    for (const assignment of solution.assignments) {
      const lecturer = assignment.event.lecturer;
      if (lecturer.preferredNotToLecture &&
          lecturer.preferredNotToLecture.includes(assignment.slot)) {
        penalty += 1;
      }
    }

    return penalty;
  }

  /**
   * SC3: Some lectures should not take place late in the evening
   */
  static calculateLateEveningPenalty(solution) {
    let penalty = 0;
    const lateSlots = [41, 42, 43, 44, 45]; // Last period

    for (const assignment of solution.assignments) {
      if (lateSlots.includes(assignment.slot)) {
        penalty += 1;
      }
    }

    return penalty;
  }

  /**
   * SC4: Number of students having lunch should be controlled
   */
  static calculateLunchTimePenalty(solution) {
    let penalty = 0;
    const lunchSlots = [20, 21, 22];
    const studentsAtLunch = new Set();

    for (const assignment of solution.assignments) {
      if (lunchSlots.includes(assignment.slot)) {
        assignment.event.students.forEach(s => studentsAtLunch.add(s));
      }
    }

    // Penalty untuk imbalance
    const targetRatio = 0.3; // 30% students at lunch
    const totalStudents = solution.getTotalStudents();
    const actualRatio = studentsAtLunch.size / totalStudents;

    penalty += Math.abs(actualRatio - targetRatio) * 100;

    return penalty;
  }

  /**
   * SC5: Classes should have lectures either in morning or afternoon
   */
  static calculateConsistencyPenalty(solution) {
    let penalty = 0;

    for (const [courseId, assignments] of solution.getCourseAssignments()) {
      const hasMorning = assignments.some(a => a.slot <= 22);
      const hasAfternoon = assignments.some(a => a.slot > 22);

      // Penalty jika mixed morning dan afternoon
      if (hasMorning && hasAfternoon) {
        penalty += 1;
      }
    }

    return penalty;
  }
}
```

---

## Arah Penelitian Lanjutan

### Research Gaps dari Bibliometric Analysis

#### 1. SA Improvement Methods

**Gap:**
> "There are still research gaps, especially regarding the proposal improvement of solution method especially in genetic algorithm and simulated annealing"

**Research Questions:**
- Bagaimana meningkatkan cooling schedule SA?
- Dapatkah SA ditingkatkan dengan adaptive mechanisms?
- Bagaimana menggabungkan SA dengan metaheuristics lain?

#### 2. Hybrid Approaches

**Opportunity:**
> "We may combine the two metaheuristic models to produce a more efficient solution"

**Research Directions:**
- SA + GA hybrid
- SA + VNS hybrid
- SA + Tabu Search hybrid

#### 3. Mathematical Modeling

**Observation:**
> "Mathematical models can still be used as alternative, especially to describe the university timetabling problems in detail"

**Research Directions:**
- Integer programming formulation untuk UCTP
- Hybrid mathematical-metaheuristic approaches
- Constraint programming integration

#### 4. Post-Pandemic Considerations

**Note dari paper:**
> "The new world situations such as pandemics and lecture modes also provide opportunities that might influence the direction of research in UCTP"

**Research Directions:**
- Online/hybrid scheduling constraints
- Social distancing dalam room assignments
- Flexible timetabling untuk changing conditions

---

## Kekurangan dan Keterbatasan Paper

### 1. Sample Size Terbatas

- Hanya 62 articles
- Dari 2 databases saja (Google Scholar, Scopus)
- Tidak mencakup semua databases (IEEE Xplore, Springer, dll)

### 2. Keyword Limitations

- Hanya 2 keywords: "course scheduling" dan "university timetable"
- Paper mengakui: "keyword 'course timetabling' and 'university timetabling' often represented by several keywords and could lead to miss calculation"

### 3. Citation Threshold

- Minimum 4 citations
- Dapat exclude recent papers yang relevan tapi belum cited

### 4. Time Range Terbatas

- Analisis 2017-2021
- Tidak memasukkan historical papers yang penting

### 5. Tidak Ada Detailed Analysis

- Tidak ada in-depth analysis dari individual papers
- Hanya keyword-level analysis

---

## Kesimpulan

### Summary Temuan

1. **SA adalah current trend** - Dikonfirmasi oleh bibliometric analysis
2. **GA lebih populer** dari SA, tapi SA tetap significant
3. **62 articles** dianalisis dari 2017-2021
4. **Metaheuristics dominate** mathematical methods
5. **Research gaps exist** dalam SA improvement

### Rekomendasi untuk Proyek

1. **Validasi pilihan SA** - SA memang current trend
2. **Fokus pada SA improvements** - Ada research gap yang jelas
3. **Pertimbangkan hybrid approaches** - SA + GA, SA + VNS, dll
4. **Gunakan constraints yang diidentifikasi** - 14 HC, 18 SC
5. **Consider post-pandemic factors** - Hybrid learning constraints

### Research Questions untuk Thesis

1. Bagaimana mengimprove Simulated Annealing untuk UCTP?
2. Dapatkah hybrid SA-GA mengungguli pure SA atau GA?
3. Bagaimana mengintegrasikan post-pandemic constraints ke UCTP?
4. Apakah adaptive SA dapat mengungguli standard SA?

---

## Referensi

- Trenggonowati, D.L., et al. (2021). "Bibliometric Analysis of University Timetabling Using Publish and Perish." *Conference on Broad Exposure to Science and Technology (BEST 2021)*. Advances in Engineering Research, Volume 210.
- Thepphakorn, T., Pongcharoen, P. (2020). Expert Systems with Applications.
- Ilhami, M.A., et al. (2019). IOP Conference Series.

---

*Analisis ini ditulis untuk mendukung penelitian tesis tentang University Course Timetabling Problem menggunakan Simulated Annealing.*
