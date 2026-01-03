# Paper Analysis: Metode Simulated Annealing untuk Optimasi Penjadwalan Perkuliahan Perguruan Tinggi

## Metadata

| Field | Value |
|-------|-------|
| **Title** | Metode Simulated Annealing untuk Optimasi Penjadwalan Perkuliahan Perguruan Tinggi |
| **Authors** | Wiktasari, Jatmiko Endro Suseno |
| **Institution** | Universitas Islam Sultan Agung (UNISSULA) Semarang, Universitas Diponegoro |
| **Journal** | Jurnal Sistem Informasi Bisnis (JSINBIS) |
| **Volume** | Vol 6, No. 2 |
| **Date** | 2016 |
| **Pages** | 133-143 |
| **DOI** | 10.21456/vol6iss2pp133-143 |

---

## Executive Summary

This paper presents a university course scheduling system using Simulated Annealing (SA) algorithm. Unlike the previous two papers, this paper provides **actual mathematical formulation**, **detailed algorithm implementation**, and **quantitative experimental results**. This is a proper research paper with scientific rigor.

**Overall Rating: 7.5/10**

---

## Problem Statement

The paper addresses the **TACS (Teacher Assignment Course Scheduling)** problem:

1. **Two-stage scheduling problem:**
   - Stage 1: Assign lecturers to courses they can teach
   - Stage 2: Assign lecturer-course pairs to available time slots and rooms

2. **Constraints involved:**
   - Lecturer expertise in subject matter
   - Maximum workload per lecturer
   - Room availability
   - Time slot availability
   - Avoiding lecturer conflicts

---

## Proposed Solution

### Method: Simulated Annealing (SA)

**Why SA?**
- SA is a heuristic method for combinatorial optimization
- Can escape local optima through probabilistic acceptance of worse solutions
- Suitable for complex constraint satisfaction problems

### Data Variables (5 variables)

| Variable | Description |
|----------|-------------|
| **Dosen (Lecturers)** | Set of all lecturers (I) |
| **Mata Kuliah (Courses)** | Set of all courses (J) |
| **Hari (Days)** | Set of available days (L) |
| **Waktu Periode (Time Slots)** | Set of time slots (M) |
| **Ruang (Rooms)** | Available classrooms |

---

## Mathematical Formulation

### 1. Sets and Parameters

```
I  : Himpunan semua dosen (Set of all lecturers)
J  : Himpunan semua mata kuliah (Set of all courses)
H  : Himpunan semua mahasiswa (Set of all students)
L  : Himpunan semua hari (Set of all days)
M  : Himpunan semua slot waktu (Set of time slots)
Ji : Himpunan mata kuliah yang diajar dosen i (Courses taught by lecturer i)
```

**Parameters:**
- `Ni`: Maximum workload for lecturer i
- `C`: Number of available rooms per time period
- `Hj`: Time slots required for course j
- `PCij`: Preference value for lecturer i teaching course j
- `PTilm`: Preference value for lecturer i teaching on day l, time slot m
- `LTj`: Minimum lecturers for course j
- `UTj`: Maximum lecturers for course j

### 2. Decision Variables

```
Xijlm = 1 if lecturer i teaches course j on day l at time slot m; else 0
Yijl = 1 if lecturer i teaches course j on day l; else 0
Uijlm = 1 if lecturer i teaches course j on day l starting at time slot m; else 0
Pij = 1 if lecturer i teaches course j; else 0
Li = Number of courses taught by lecturer i
Vi = Number of courses taught by lecturer i each day
```

### 3. Objective Functions

**Objective Function 1 (Lecturer-Course Assignment):**

```
Max ∑∑ PCij × Pij
   i∈I j∈J
```

Maximize total preference value for lecturer-course assignments.

**Objective Function 2 (Time Slot Assignment):**

```
Max ∑∑∑∑ PTilm × Xijlm
   i∈I j∈J l∈L m∈M
```

Maximize total preference for lecturer-course-time slot assignments.

### 4. Constraints

| Constraint | Formula | Description |
|------------|---------|-------------|
| **Minimum courses** | `1 ≤ ∑Pij ≤ Ni` | Each lecturer teaches at least 1 course |
| **Course lecturer limits** | `LTj ≤ ∑Pij ≤ UTj` | Min/max lecturers per course |
| **Time slot requirement** | `∑Xijlm = Yijl × Hj` | Course requires specific time slots |
| **No lecturer conflict** | `∑Xijlm ≤ 1` | One course per lecturer per time slot |
| **Room capacity** | `∑∑Xijlm ≤ C` | No more courses than rooms |
| **Single lecturer** | `∑∑Yijl = 1` | One lecturer per course |
| **Expertise** | `Xijlm = 0 if j∉Ji` | Lecturer can only teach qualified courses |
| **Daily workload** | `∑Yijl ≤ Vi` | Limit courses per day per lecturer |

---

## Algorithm Implementation

### Simulated Annealing Parameters

| Parameter | Symbol | Description |
|-----------|--------|-------------|
| Initial Temperature | T₀ | Search space size (|I| × |J|) |
| Cooling Factor | α | Multiplier per iteration (α < 1) |
| Final Temperature | Tn | Stopping condition |
| Cooling Schedule | Geometric: Ti+1 = α × Ti |

### SA Algorithm Steps

1. **Initialize**: Select initial point X₀, compute objective function φ(X₀)
2. **Random Step**: Select random step s ∈ X
3. **Compute Change**: Calculate Δf ← f(s′) − f(s)
4. **Check Stopping**: If stopping condition met, exit
5. **Accept Better**: If Δf ≤ 0, accept: Xk+1 ← Xk + Δf
6. **Probabilistic Accept**: If Δf > 0, accept with probability exp(−βΔf)
   - Generate random ρ ∈ [0,1]
   - If exp(−βΔf) > ρ, accept; else reject

---

## Experimental Results

### Real Dataset (Case Study: UNISSULA)

| Parameter | Value |
|-----------|-------|
| **Study Program** | 3 programs |
| **Total Courses** | 152 |
| **Total Lecturers** | 52 |
| **Time Slots** | 10 per day |
| **Days** | Monday-Friday (5 days) |
| **Rooms** | 9 |
| **Total Slots** | 450 (10 × 5 × 9) |

### Results - Objective Function 1

| Metric | Result |
|--------|--------|
| **Courses with lecturer** | 152 / 152 (100%) |
| **Lecturers assigned** | 52 / 52 (100%) |
| **T₀** | [1, 152] |
| **α** | {0.1} |
| **Tn** | 0 |

### Results - Objective Function 2

| Metric | Result |
|--------|--------|
| **Courses plotted** | 129 / 152 (84.87%) |
| **Unplotted courses** | 23 (15.13%) |
| **Conflict-free courses** | 145 / 152 (95.39%) |
| **Conflicting courses** | 7 (4.61%) |
| **T₀** | [1, 152] |
| **α** | {0.19} |
| **Tn** | 30 |

### Multiple Dataset Experiments

The paper conducted experiments with 13 different dataset variations:

| Course:Lecturer Ratio | Avg. Allocation Rate |
|-----------------------|---------------------|
| 1:1 | ~70% |
| 2:1 | ~72.5% |
| 1:2 | ~80% |

### Validation Results

- **Average variance**: 77.791%
- **Standard deviation**: 3.931509

---

## Critical Analysis

### Strengths

| Aspect | Description |
|--------|-------------|
| **Mathematical rigor** | Complete formulation with sets, parameters, variables, objective functions, and constraints |
| **Real-world case study** | Tested on actual university data (UNISSULA) |
| **Two-stage approach** | Separates lecturer assignment from time slot allocation |
| **Detailed constraints** | Both hard and soft constraints clearly defined |
| **Quantitative results** | Specific percentages and metrics reported |
| **Parameter sensitivity** | Tested multiple cooling factor values (0.1 to 0.9) |
| **Reproducible** | Sufficient detail to replicate the study |
| **Proper academic standard** | Published in reputable journal (JSINBIS) |

### Weaknesses

| Issue | Description |
|-------|-------------|
| **Allocation rate** | Only 84.87% of courses could be scheduled - 15.13% failed |
| **No comparison** | Doesn't compare SA with other algorithms (GA, tabu search, etc.) |
| **Limited scale** | 152 courses is relatively small for university scheduling |
| **No execution time** | Computational performance not reported |
| **Fixed parameters** | No discussion of parameter tuning methodology |
| **Conflict handling** | 4.61% still had conflicts (not fully conflict-free) |

### Comparison with Previous Papers

| Aspect | Paper 1 (React) | Paper 2 (Tkinter) | Paper 3 (SA) |
|--------|-----------------|-------------------|--------------|
| **Mathematical Formulation** | ❌ None | ❌ None | ✅ Complete |
| **Algorithm Details** | ❌ Theoretical only | ❌ Mentioned only | ✅ Implemented |
| **Experimental Results** | ❌ None | ❌ None | ✅ Quantitative |
| **Real Dataset** | ❌ Not mentioned | ❌ Not mentioned | ✅ UNISSULA data |
| **Comparison Study** | ❌ None | ❌ None | ❌ None |
| **Overall Rating** | 3.5/10 | 3/10 | 7.5/10 |

---

## Quality Assessment

| Criteria | Score (1-10) | Notes |
|----------|--------------|-------|
| **Originality** | 7/10 | SA is standard, but two-stage approach is interesting |
| **Technical Depth** | 9/10 | Excellent mathematical formulation |
| **Scientific Rigor** | 8/10 | Real experiments, but no baseline comparison |
| **Writing Quality** | 8/10 | Clear and structured (Indonesian) |
| **Reproducibility** | 8/10 | Most details provided |
| **Practical Value** | 7/10 | Good results but allocation rate could be better |
| **Overall** | **7.5/10** | Solid research paper |

---

## Key Insights for Your Thesis

### What This Paper Offers

1. **Complete Mathematical Model**
   - Can use the constraint formulation (equations 2.5 - 2.19)
   - Two-stage objective functions are well-defined

2. **SA Parameter Guidance**
   - Initial temperature: range [1, n] where n is problem size
   - Cooling factor: 0.1 to 0.9 (optimal varies by dataset)
   - Geometric cooling schedule works well

3. **Validation Metrics**
   - Allocation rate: % of courses successfully scheduled
   - Conflict rate: % of courses with scheduling conflicts
   - Variance and standard deviation across runs

4. **Practical Considerations**
   - Hard constraints: must be satisfied
   - Soft constraints: lecturer preferences
   - Two-phase optimization: assignment first, then scheduling

### Gaps to Address

1. **No algorithm comparison** - You could compare SA with GA, PSO, etc.
2. **Moderate success rate** - 84.87% leaves room for improvement
3. **No performance metrics** - Execution time, memory usage not reported
4. **Limited scalability** - Not tested on larger datasets

---

## Conclusion

### What This Paper Is

- A **proper research paper** with mathematical rigor
- An **actual implementation** of Simulated Annealing
- A **case study** with real university data
- A **reference** for timetabling formulation

### What This Paper is NOT

- A system implementation paper (focus is on algorithm, not UI)
- A comparison study (no other algorithms benchmarked)
- A scalability study (limited to 152 courses)

### Recommendation

**This is the best paper so far** among the three analyzed. Use this paper as:

- ✅ **Primary reference** for mathematical formulation
- ✅ **Algorithm reference** for Simulated Annealing implementation
- ✅ **Validation metrics** reference for your experiments
- ✅ **Constraint modeling** reference for your problem

**Areas to improve upon:**
- Compare SA with other metaheuristics
- Test on larger datasets
- Report computational performance
- Improve allocation rate beyond 84.87%

---

## References from Paper

1. Chambers, 1998 - University timetabling definition
2. Basir et al., 2013 - Hard/soft constraints
3. Daskalaki et al., 2004 - Objective function formulation
4. Kalivas, 1995 - SA formulation requirements
5. Chibante, 2010 - SA flowchart and algorithm
6. Gunawan et al., 2012 - Mathematical modeling notation
