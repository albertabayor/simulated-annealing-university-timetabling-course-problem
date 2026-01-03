# Analisis Paper: Addressing Staffing Challenges Through Improved Planning

## Informasi Publikasi

- **Judul:** Addressing Staffing Challenges Through Improved Planning: Demand-Driven Course Schedule Planning and Instructor Assignment in Higher Education
- **Penulis:** Guisen Xue, O. Felix Offodile, Rouzbeh Razavi, Dong-Heon Kwak, Jose Benitez*
- **Affiliasi:** Department of Information Systems and Business Analytics, Ambassador Crawford College of Business and Entrepreneurship, Kent State University, Kent, USA
- **Jurnal:** Decision Support Systems (Elsevier)
- **Volume/Issue:** Vol. 187
- **Article Number:** 114345
- **Tahun:** 2024
- **DOI:** 10.1016/j.dss.2024.114345
- **License:** CC BY-NC 4.0
- **URL:** https://www.sciencedirect.com/journal/decision-support-systems

---

## Abstrak

Paper ini mempresentasikan **Decision Support System (DSS)** baru untuk menyelesaikan University Course Timetabling Problem (UCTP). Solusi ini **decomposes NP-complete UCTP menjadi dua sub-problems**:

1. **Course Schedule Planning** - Menentukan jumlah optimal sections untuk setiap course
2. **Instructor Assignment** - Menugaskan instructors ke course sections

**Metode:** Mixed Integer Linear Programming (MILP) model yang mengintegrasikan academic year course schedule planning dan instructor assignment.

**Hasil:**
- **14% reduction** dalam jumlah course sections
- **$130,000 annual savings**
- **81% reduction** dalam new courses assigned ke instructors
- **29% reduction** dalam distinct course sections assigned

**Keywords:** Academic scheduling, MILP, Decision support system, Integrated optimization

---

## Latar Belakang

### Universitas Menghadapi Tantangan Finansial

Dalam dekade terakhir:
- **Decline in enrollment** dan underfunding
- **Covid-19 pandemic** memperburuk situasi
- **Staff costs** = bagian terbesar dari university expenditures

**Data:**
- 4-year public institutions: **26%** expenses untuk instruction (NCES 2019-20)
- Stanford University: **64%** expenditures untuk salaries and benefits (fiscal 2022-23)

### Gap antara Literatur dan Praktik

**Problem:**
- Literature fokus pada sophisticated methods untuk timetabling
- Academic practice prioritizes user-friendly tools
- **Persistent gap** antara UCT literature dan practical application

**ITC 2019 Limitations:**
- Optimize assignment of times, rooms, dan students ke courses
- **Tidak mempertimbangkan:** Course schedule planning (jumlah sections per course)
- **Tidak mempertimbangkan:** Instructor assignment problem

---

## Process-Based Decision Support System Framework

### Decomposition dari UCTP

Paper ini memperkenalkan **process-based DSS** yang meng-decompose UCTP menjadi lebih manageable sub-models:

```
┌─────────────────────────────────────────────────────────┐
│                  UNIVERSITY COURSE                       │
│                  TIMETABLING PROBLEM                     │
│                    (NP-Complete)                         │
└─────────────────────────────────────────────────────────┘
                          │
                          ▼
┌─────────────────────────────────────────────────────────┐
│                   DECOMPOSITION INTO                      │
│                     SUB-MODELS                           │
└─────────────────────────────────────────────────────────┘
                          │
          ┌───────────────┼───────────────┐
          ▼               ▼               ▼
┌──────────────┐ ┌──────────────┐ ┌──────────────┐
│   COURSE     │ │  INSTRUCTOR  │ │  TIMESLOT &  │
│  SCHEDULE    │ │  ASSIGNMENT  │ │  CLASSROOM   │
│  PLANNING    │ │   (CSPIA)    │ │  ASSIGNMENT  │
└──────────────┘ └──────────────┘ └──────────────┘
```

### Tahap dalam DSS

#### Tahap 1: Course Demand Forecasting

**Inputs:**
- Current student enrollment
- Historical course registration data

**Methods:**
- Data mining
- Predictive modeling

**Challenges:**
- Economic changes
- Demographic shifts
- Student preferences
- Unexpected events (pandemics, disasters)

#### Tahap 2: Course Schedule Planning

**Objective:** Determine optimal number of sections untuk setiap course

**Inputs:**
- Number of students eligible untuk setiap course
- Proportion of qualified students registering
- Threshold untuk opening new section
- Maximum capacity per section
- Previous year schedule

**Output:** Number of sections untuk setiap course

#### Tahap 3: Instructor Assignment

**Objective:** Assign instructors ke course sections

**Inputs:**
- Number of full-time faculty
- Courses taught oleh setiap faculty (previous year)
- Qualifications untuk specific courses
- Annual teaching load
- Minimum required percentage of full-time faculty

**Output:** Course-section-instructor combinations

#### Tahap 4: Timeslot & Classroom Assignment

**Output dari CSPIA** → Input untuk timeslot dan classroom assignment

---

## Model: CSPIA (Course Schedule Planning and Instructor Assignment)

### Formulasi Model

#### Decision Variables

$$x_{ijst} = \begin{cases}
1, & \text{jika instructor } i \text{ mengajar course } j \text{ di section } s \text{ pada semester } t \\
0, & \text{otherwise}
\end{cases}$$

$$y_{jt} = \text{jumlah sections untuk course } j \text{ di semester } t$$

#### Objective Function

**Minimize:** Weighted sum dari new course preparations dan distinct courses

$$\min Z = \alpha \sum_{i,j,s,t} n_{ijst} x_{ijst} + \beta \sum_{i,t} d_{it}$$

Dimana:
- $n_{ijst}$ = 1 jika course $j$ adalah **new course** untuk instructor $i$
- $d_{it}$ = jumlah **distinct courses** untuk instructor $i$ di semester $t$
- $\alpha, \beta$ = weights (parameterized, adjustable)

#### Constraints

**Hard Constraints (Student Demand):**

1. **Demand satisfaction:**
   $$\sum_{i,s} x_{ijst} \geq D_{jt}$$

   Dimana $D_{jt}$ = forecasted demand untuk course $j$ di semester $t$

2. **Teaching load:**
   $$L_{min} \leq \sum_{j,s} x_{ijst} \leq L_{max}$$

3. **Qualifications:**
   $$x_{ijst} = 0 \text{ jika instructor } i \text{ tidak qualified untuk course } j$$

4. **Full-time faculty ratio:**
   $$\frac{\sum_{i \in FT} \sum_{j,s} x_{ijst}}{\sum_{i} \sum_{j,s} x_{ijst}} \geq R_{min}$$

### Instructor Preferences

**Preference indicators:**

1. **New course preparations** - Courses instructor belum pernah mengajar
2. **Distinct courses** - Jumlah unique courses per semester

**Benefits:**
- Reduced preparation time
- Improved teaching quality
- Higher job satisfaction
- Deeper content expertise

---

## Hasil Case Study

### Dataset

**Institution:** Large public university di United States

**Department:** Computer Information Systems, Business Management, dan Business Analytics

### Hasil Komparasi

| Metric | Actual Schedule | Proposed DSS | Improvement |
|--------|----------------|--------------|-------------|
| **Course sections** | 100% | 86% | **14% reduction** |
| **Annual cost savings** | - | - | **$130,000** |
| **New courses per instructor** | 100% | 19% | **81% reduction** |
| **Distinct courses per instructor** | 100% | 71% | **29% reduction** |

### Financial Impact

**14% reduction dalam course sections:**
- Fewer sections needed
- Better alignment dengan student demand
- Efficient resource utilization
- Significant cost savings

**$130,000 annual savings:**
- Reduced staffing costs
- Better instructor utilization
- Minimized need untuk adjunct instructors

---

## Implikasi untuk Proyek Ini

### Relevansi

Paper ini sangat relevan untuk proyek Anda karena:

1. **Comprehensive UCTP framework** - Decomposition approach yang practical
2. **MILP formulation** - Mathematical foundation yang rigorous
3. **Real-world validation** - Proven results di actual university
4. **Instructor preferences** - Aspect yang sering diabaikan dalam literature

### Rekomendasi untuk Proyek

#### 1. Learn dari Decomposition Approach

Meskipun proyek Anda menggunakan SA (bukan MILP), decomposition principles tetap applicable:

```javascript
/**
 * Decomposition Approach untuk SA
 * Berdasarkan framework dari Xue et al. (2024)
 */

class DecomposedSA {
  constructor(config) {
    // SA configuration
    this.saConfig = config.sa || {};

    // Decomposition phases
    this.phases = [
      'coursePlanning',    // Determine optimal sections
      'instructorAssignment', // Assign instructors
      'timeslotAssignment', // Assign timeslots
      'classroomAssignment' // Assign rooms
    ];
  }

  /**
   * Phase 1: Course Schedule Planning
   * Determine optimal number of sections
   */
  courseSchedulePlanning(instance, demands) {
    // Use SA untuk optimize section quantities
    const solution = this.optimizeSectionQuantities(instance, demands);

    return {
      sections: solution.sections,
      objective: 'Minimize sections while meeting demand'
    };
  }

  /**
   * Phase 2: Instructor Assignment (CSPIA-like)
   * Assign instructors dengan preference optimization
   */
  instructorAssignment(instance, sections) {
    // SA dengan specific objective: minimize new + distinct courses
    const solution = this.optimizeInstructorAssignment(instance, sections);

    return {
      assignments: solution.assignments,
      newCourses: solution.newCourses,
      distinctCourses: solution.distinctCourses
    };
  }

  /**
   * Phase 3: Timeslot Assignment
   */
  timeslotAssignment(instance, assignments) {
    const solution = this.optimizeTimeslots(instance, assignments);

    return solution;
  }

  /**
   * Phase 4: Classroom Assignment
   */
  classroomAssignment(instance, scheduledCourses) {
    const solution = this.optimizeClassrooms(instance, scheduledCourses);

    return solution;
  }

  /**
   * Instructor Assignment SA dengan preference optimization
   */
  optimizeInstructorAssignment(instance, sections) {
    let current = this.generateInitialAssignment(instance, sections);

    // Custom fitness function incorporating preferences
    const fitness = (solution) => {
      // Hard constraints
      if (!this.satisfiesDemand(solution)) return Infinity;
      if (!this.satisfiesLoadConstraints(solution)) return Infinity;

      // Soft constraints (preferences)
      const newCourses = this.countNewCourses(solution);
      const distinctCourses = this.countDistinctCourses(solution);

      // Weighted objective (sesuai paper)
      return this.alpha * newCourses + this.beta * distinctCourses;
    };

    const sa = new SimulatedAnnealing({
      fitnessFunction: fitness,
      ...this.saConfig
    });

    return sa.search(current);
  }

  /**
   * Count new course preparations untuk instructor
   */
  countNewCourses(solution) {
    let count = 0;

    for (const [instructorId, courses] of solution.assignments) {
      const previousCourses = this.getPreviousCourses(instructorId);

      for (const course of courses) {
        if (!previousCourses.includes(course.id)) {
          count++;
        }
      }
    }

    return count;
  }

  /**
   * Count distinct courses per instructor per semester
   */
  countDistinctCourses(solution) {
    let total = 0;

    for (const [instructorId, semesterData] of solution.assignments) {
      for (const [semester, courses] of Object.entries(semesterData)) {
        const distinct = new Set(courses.map(c => c.courseId));
        total += distinct.size;
      }
    }

    return total;
  }
}
```

#### 2. Incorporate Instructor Preferences

Paper ini menunjukkan importance dari instructor preferences:

```javascript
/**
 * Instructor Preference System
 * Berdasarkan Xue et al. (2024)
 */

class InstructorPreference {
  constructor(instructor) {
    this.instructor = instructor;
    this.previousCourses = new Set();
    this.preferredCourses = new Set();
    this.avoidCourses = new Set();
  }

  /**
   * Calculate preference score untuk course
   */
  getPreferenceScore(courseId) {
    let score = 0;

    // Prefer courses previously taught (reduce new preparation)
    if (this.previousCourses.has(courseId)) {
      score += 10;
    }

    // Prefer explicitly preferred courses
    if (this.preferredCourses.has(courseId)) {
      score += 5;
    }

    // Avoid explicitly avoided courses
    if (this.avoidCourses.has(courseId)) {
      score -= 20;
    }

    return score;
  }

  /**
   * Calculate penalty untuk new course preparation
   */
  getNewCoursePenalty(courseId) {
    if (this.previousCourses.has(courseId)) {
      return 0; // No penalty, not new
    }
    return 1; // Penalty for new course
  }

  /**
   * Calculate penalty untuk distinct courses
   * (cognitive load dari multiple preparations)
   */
  getDistinctCoursePenalty(currentAssignments, newCourse) {
    const distinct = new Set([
      ...currentAssignments.map(a => a.courseId),
      newCourse
    ]);
    return distinct.size;
  }
}

/**
 * SA dengan Instructor Preferences
 */
class SAWithInstructorPreferences {
  constructor(config) {
    this.instructors = config.instructors.map(i => new InstructorPreference(i));
    this.alpha = config.alpha || 1.0; // Weight untuk new courses
    this.beta = config.beta || 0.5;   // Weight untuk distinct courses
  }

  /**
   * Calculate fitness incorporating instructor preferences
   */
  calculateFitness(solution) {
    let penalty = 0;

    // Hard constraint: student demand
    penalty += this.checkDemandViolation(solution) * 1000;

    // Hard constraint: teaching load
    penalty += this.checkLoadViolation(solution) * 1000;

    // Soft constraints: instructor preferences
    for (const [instructorId, courses] of solution.instructorAssignments) {
      const instructor = this.instructors.get(instructorId);

      // Count new courses
      const newCourses = courses.filter(c =>
        !instructor.previousCourses.has(c.courseId)
      ).length;

      // Count distinct courses
      const distinctCourses = new Set(courses.map(c => c.courseId)).size;

      // Weighted penalty
      penalty += this.alpha * newCourses;
      penalty += this.beta * distinctCourses;
    }

    return penalty;
  }

  /**
   * Generate neighbor yang respects instructor preferences
   */
  generatePreferenceAwareNeighbor(solution) {
    const neighbor = solution.clone();

    // Select random instructor
    const instructorId = this.selectRandomInstructor();
    const instructor = this.instructors.get(instructorId);

    // Get current assignments
    const currentCourses = solution.instructorAssignments.get(instructorId) || [];

    // Strategy 1: Swap dengan preferred course
    if (instructor.preferredCourses.size > 0) {
      const preferredCourse = this.getRandomPreferredCourse(instructor);
      // Implement swap logic
    }

    // Strategy 2: Replace new course dengan previous course
    const newCourses = currentCourses.filter(c =>
      !instructor.previousCourses.has(c.courseId)
    );

    if (newCourses.length > 0) {
      // Try to replace new course dengan previous course
    }

    return neighbor;
  }
}
```

#### 3. Demand-Driven Approach

```javascript
/**
 * Demand-Driven Course Planning
 * Berdasarkan Xue et al. (2024)
 */

class DemandDrivenPlanner {
  constructor(config) {
    this.demandForecaster = new DemandForecaster();
    this.thresholds = config.thresholds || {
      minEnrollment: 10,
      maxSectionSize: 40,
      newSectionThreshold: 35
    };
  }

  /**
   * Calculate optimal sections berdasarkan demand
   */
  calculateOptimalSections(courseId, demandData) {
    const forecast = this.demandForecaster.forecast(courseId, demandData);
    const optimalSections = [];

    // Calculate sections needed
    let remainingDemand = forecast;
    let sectionCount = 0;

    while (remainingDemand > 0) {
      sectionCount++;

      // First section: check minimum enrollment
      if (sectionCount === 1 && remainingDemand < this.thresholds.minEnrollment) {
        // Consider cancelling atau combining sections
        return { sections: 0, action: 'cancel' };
      }

      // Determine section size
      const sectionSize = Math.min(
        remainingDemand,
        this.thresholds.maxSectionSize
      );

      optimalSections.push({
        sectionId: sectionCount,
        capacity: sectionSize,
        expectedEnrollment: Math.min(sectionSize, remainingDemand)
      });

      remainingDemand -= sectionSize;

      // Check apakah section baru justified
      if (remainingDemand > 0 && remainingDemand < this.thresholds.newSectionThreshold) {
        // Consider alternative strategies
        break;
      }
    }

    return {
      courseId,
      sections: optimalSections.length,
      sectionDetails: optimalSections,
      forecast: forecast
    };
  }

  /**
   * SA untuk optimize section quantities
   */
  optimizeSectionQuantities(instance, demands) {
    let current = this.generateInitialSections(instance, demands);

    const fitness = (solution) => {
      // Minimize total sections
      const totalSections = solution.getTotalSections();

      // Penalty untuk unmet demand
      const unmetDemand = solution.getUnmetDemand(demands);

      return totalSections * 100 + unmetDemand * 1000;
    };

    const sa = new SimulatedAnnealing({
      fitnessFunction: fitness,
      initialState: current
    });

    return sa.optimize();
  }
}
```

---

## Kekurangan dan Keterbatasan Paper

### 1. Computational Complexity

- MILP models dapat menjadi intractable untuk large instances
- Tidak ada discussion tentang solver time atau scalability limits

### 2. Static Model

- Model tidak robust terhadap dynamic changes
- Demand forecasting errors tidak secara explicit ditangani

### 3. Single Institution Case

- Hanya divalidasi di one university
- Generalisability ke different institutions uncertain

### 4. Limited Soft Constraints

- Fokus pada new dan distinct courses
- Tidak comprehensive soft constraint optimization

### 5. Instructor Preferences Simplified

- Hanya dua preference metrics
- Tidak include time slot atau room preferences

---

## Arah Penelitian Lanjutan

### Research Gaps

#### 1. SA for Integrated CSPIA

**Gap:**
Paper menggunakan MILP, tidak SA.

**Research direction:**
- Dapatkah SA menyelesaikan CSPIA secara lebih efisien?
- Bagaimana SA handles trade-off antara preferences?

#### 2. Dynamic Demand Handling

**Gap:**
Model menggunakan forecasted demand yang static.

**Research direction:**
- SA dengan adaptive demand handling
- Real-time re-optimization saat demand berubah

#### 3. Multi-Objective Optimization

**Gap:**
Paper fokus pada cost dan preferences.

**Research direction:**
- Multi-objective SA untuk UCTP
- Balance antara student satisfaction, instructor preferences, dan institutional costs

#### 4. Scalability untuk Large Institutions

**Gap:**
Case study di satu department level.

**Research direction:**
- Scaling SA untuk entire university
- Hierarchical decomposition untuk multi-department

---

## Kesimpulan

### Summary Temuan

1. **DSS decomposition** - UCTP dapat di-decompose menjadi manageable sub-models
2. **MILP effective** - Tapi bisa expensive untuk large problems
3. **Significant savings** - 14% reduction dalam sections, $130K savings
4. **Instructor preferences matter** - 81% reduction dalam new courses
5. **Practical validation** - Proven effectiveness di real university

### Rekomendasi untuk Proyek

1. **Adopt decomposition approach** - Phase 1 (sections), Phase 2 (instructors), etc.
2. **Incorporate instructor preferences** - New dan distinct course minimization
3. **Use demand-driven planning** - Section quantities berdasarkan forecasted demand
4. **Implement flexible weights** - Parameterized alpha dan beta
5. **Validate dengan real data** - Compare dengan actual schedules

### Research Questions untuk Thesis

1. Dapatkah SA menggantikan MILP untuk CSPIA dengan comparable results?
2. Bagaimana mengoptimalkan trade-off antara student demand dan instructor preferences?
3. Dapatkah SA dengan adaptive mechanisms handle dynamic demand changes?
4. Apakah decomposition approach beneficial untuk SA performance?

---

## Referensi

- Xue, G., Offodile, O.F., Razavi, R., Kwak, D.-H., Benitez, J. (2024). "Addressing Staffing Challenges Through Improved Planning: Demand-Driven Course Schedule Planning and Instructor Assignment in Higher Education." *Decision Support Systems*, 187, 114345. https://doi.org/10.1016/j.dss.2024.114345

---

*Analisis ini ditulis untuk mendukung penelitian tesis tentang University Course Timetabling Problem menggunakan Simulated Annealing.*
