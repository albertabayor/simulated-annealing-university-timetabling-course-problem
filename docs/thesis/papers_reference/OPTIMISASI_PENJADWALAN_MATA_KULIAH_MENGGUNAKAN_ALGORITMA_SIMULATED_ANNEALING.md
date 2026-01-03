# Paper Analysis: OPTIMISASI_PENJADWALAN_MATA_KULIAH_MENGGUNAKAN_ALGORITMA_SIMULATED_ANNEALING

## Metadata

| Field | Value |
|-------|-------|
| **Title** | Optimisasi Penjadwalan Mata Kuliah Menggunakan Algoritma Simulated Annealing |
| **Authors** | Andre Yonathan Sukhoco, Ferdinand Lanvino, Ekabrata Yudhistyra, Budi Permana, Kurweni Ukar |
| **Institution** | STMIK LIKMI |
| **Journal** | Media Informatika |
| **Volume/Issue** | Vol. 23, No. 1 |
| **Date** | 2024 |
| **Pages** | 45-61 |
| **Email** | andre@likmi.ac.id |

---

## Executive Summary

This paper presents a university course scheduling system using Simulated Annealing (SA) algorithm implemented in Python/Jupyter Notebook. Similar to Paper 3, this provides actual implementation and experimental results. The paper is well-structured with detailed constraint definitions, algorithm implementation, and comprehensive experimental results across three scenarios.

**Overall Rating: 8/10**

---

## Problem Statement

The paper addresses the university course timetabling problem at **STMIK LIKMI** with the following challenges:

1. **Time pressure**: Limited time between registration and semester start
2. **Combinatorial complexity**: Many dimensions must be tested for optimal solution
3. **NP-hard problem**: Cannot be solved with conventional techniques in polynomial time
4. **Constraint variability**: Different institutions have different constraints

---

## Proposed Solution

### Method: Simulated Annealing (SA)

**Why SA?**
- Single solution-based meta-heuristic (local search)
- Easy to implement
- Produces high-quality solutions with reasonable computational power
- Proven superior to multi-start hill climbing and late acceptance hyper-heuristics (based on cited research)

### Key Features

1. **Two-stage approach:**
   - **Stage 1**: Class composition planning (plotting kelas)
   - **Stage 2**: SA-based scheduling

2. **Pre-processing**: Constraints H3 and H6 are satisfied before SA to reduce search space

3. **Restart mechanism**: SA restarts from initial temperature when stuck in local optima

---

## Constraints Specification

### Hard Constraints (H1-H8)

| Code | Constraint |
|------|------------|
| **H1** | Regular classes: slots 1-4 only, all days |
| **H2** | Employee classes: slots 5-6 only, NO Saturday |
| **H3** | Schedule count = SKS; 1 SKS = 50 min; max 2-3 SKS per session (100-150 min) |
| **H4** | Theory classes → theory rooms; Practice classes → practice rooms |
| **H5** | Certain practice courses → specific rooms (equipment requirements) |
| **H6** | Students ≤ room capacity (up to 150% tolerance) |
| **H7** | One room = one class per time slot |
| **H8** | One lecturer = one class per time slot |

### Soft Constraints (S1-S2)

| Code | Constraint |
|------|------------|
| **S1** | Students: max one class per time slot |
| **S2** | Lecturers: max four classes per day |

---

## Algorithm Implementation

### SA Components

1. **Slot Filtering Function**
   - Filters available time slots based on class specifications
   - Directly satisfies H1, H2, H4, H5
   - Eliminates need to evaluate these constraints

2. **Initial Solution Generator**
   - Creates initial solution using slot filtering

3. **Class Relocation Function**
   - Moves one class to another slot
   - Uses slot filtering for validity

4. **Solution Evaluation Function**
   - Evaluates violations of H7, H8, S1, S2
   - Fitness: lower violations = better (target: 0)

5. **Annealing Function (Main)**
   - Implements SA with geometric cooling
   - Restart mechanism when stuck

### SA Parameters

| Parameter | Value |
|-----------|-------|
| **Initial Temperature** | 1000 |
| **Cooling Factor (α)** | 0.99 |
| **Acceptance Criterion** | 0.8 |
| **Target Temperature** | 1 |
| **Target Fitness** | 0 |
| **Stuck Iteration Limit** | 50 |
| **Restart Limit** | 3 |
| **Trials per Scenario** | 10 |

### Pseudocode

```
1. Initialize: i := i_start, k := 0, c_k := c_0, L_k := L_0
2. Repeat
   For l = 0 to L_k do:
     a. Generate solution j from neighborhood S_i of current solution i
     b. If f(j) < f(i), then i := j
     c. Else, j becomes current solution with probability e^{(f(i)-f(j))/c_k}
   k := k + 1
   Calculate(L_k, c_k)
3. Until c_k ≈ 0
```

**Where:**
- `c_k`: temperature parameter
- `L_k`: number of transitions at iteration k
- `f(i)`: fitness function (violations count)

---

## Experimental Results

### Case Study: STMIK LIKMI (Semester Genap 2022/2023)

#### Scenario 1: Regular Classes Only

| Data | Count |
|------|-------|
| Students | 186 |
| Theory Classes | 24 |
| Practice Classes | 22 |
| **Total Classes** | **46** |

**Results (10 trials):**

| Metric | Value |
|--------|-------|
| **Avg Initial Fitness** | -493.4 |
| **Avg Final Fitness** | -16.2 |
| **Best Final Fitness** | -2 (Trial 9) |
| **Avg Iterations** | 1177 |
| **Avg Duration** | 65.86 seconds |
| **Success Rate** | 100% (all H1-H8 satisfied) |
| **Soft Constraint Violations** | Only S1 (16.2 avg) |

**Constraint Breakdown (Best Solution):**
- H1-H8: 0 violations ✅
- S1: -2 violations
- S2: 0 violations ✅

#### Scenario 2: Employee Classes Only

| Data | Count |
|------|-------|
| Students | 114 |
| Theory Classes | 25 |
| Practice Classes | 11 |
| **Total Classes** | **36** |

**Results (10 trials):**

| Metric | Value |
|--------|-------|
| **Avg Initial Fitness** | -322.8 |
| **Avg Final Fitness** | -46.5 |
| **Best Final Fitness** | -30 (Trial 7) |
| **Avg Iterations** | 976.3 |
| **Avg Duration** | 53.41 seconds |
| **Success Rate** | 100% (all H1-H8 satisfied) |
| **Soft Constraint Violations** | S1 and S2 |

**Constraint Breakdown (Best Solution):**
- H1-H8: 0 violations ✅ (except 0.2 H8 avg)
- S1: -0.2 violations (avg)
- S2: -46.3 violations (avg)

#### Scenario 3: Regular + Employee Classes (Combined)

| Data | Count |
|------|-------|
| Students | 280 |
| Theory Classes | 51 |
| Practice Classes | 47 |
| **Total Classes** | **98** |

**Results (10 trials):**

| Metric | Value |
|--------|-------|
| **Avg Initial Fitness** | -739.2 |
| **Avg Final Fitness** | -67.6 |
| **Best Final Fitness** | -40 (Trial 5) |
| **Avg Iterations** | 750.2 |
| **Avg Duration** | 48.34 seconds |
| **Success Rate** | 100% (all H1-H8 satisfied) |
| **Soft Constraint Violations** | Only S1 |

**Constraint Breakdown (Best Solution):**
- H1-H8: 0 violations ✅
- S1: -0.6 violations (avg)
- S2: -67 violations (avg)

---

## Critical Analysis

### Strengths

| Aspect | Description |
|--------|-------------|
| **Comprehensive constraint definition** | 8 hard + 2 soft constraints clearly specified |
| **Three test scenarios** | Regular, Employee, and Combined classes |
| **Detailed results** | 10 trials per scenario with full metrics |
| **Visual output** | Actual timetable schedules shown (Mon-Sat) |
| **Restart mechanism** | Novel addition to escape local optima |
| **Pre-processing optimization** | Filters slots to reduce search space |
| **Real-world case study** | STMIK LIKMI actual data |
| **Transparent reporting** | Shows all trials, not just best results |
| **Execution time reported** | Average duration per trial |
| **Recent publication** | 2024 - current state of the art |

### Weaknesses

| Issue | Description |
|-------|-------------|
| **Soft constraint violations remain** | S2 (lecturer daily limit) frequently violated |
| **No algorithm comparison** | Doesn't compare SA with GA, PSO, or other methods |
| **Limited problem size** | Max 98 classes (small-medium scale) |
| **Parameter tuning not explained** | Why T₀=1000, α=0.99? No sensitivity analysis |
| **Employee classes harder** | More soft constraint violations than regular |
| **No statistical analysis** | No variance, standard deviation, confidence intervals |
| **Implementation details sparse** | No code snippets or detailed pseudocode |
| **Fitness function simple** | Just counts violations (no weighted preferences) |

### Comparison with Paper 3 (UNISSULA)

| Aspect | Paper 3 (UNISSULA) | Paper 4 (STMIK LIKMI) |
|--------|-------------------|----------------------|
| **Year** | 2016 | 2024 |
| **Mathematical Formulation** | ✅ Complete | ❌ None |
| **Algorithm Details** | ✅ Detailed | ✅ Detailed |
| **Test Scenarios** | 1 real + 13 synthetic | 3 real scenarios |
| **Constraints** | 6 hard, 2 soft | 8 hard, 2 soft |
| **Hard Constraint Success** | 84.87% | 100% |
| **Soft Constraint Success** | Not clearly reported | Partial (S1 ok, S2 struggles) |
| **Results Tables** | Detailed parameters | Per-trial breakdown |
| **Visual Output** | Screenshots | Full timetables (Mon-Sat) |
| **Execution Time** | ❌ Not reported | ✅ Reported (35-95s) |
| **Restart Mechanism** | ❌ No | ✅ Yes |
| **Overall Rating** | 7.5/10 | 8/10 |

---

## Quality Assessment

| Criteria | Score (1-10) | Notes |
|----------|--------------|-------|
| **Originality** | 7/10 | SA is standard, but restart mechanism is nice |
| **Technical Depth** | 8/10 | Good implementation details |
| **Scientific Rigor** | 8/10 | 10 trials per scenario, transparent reporting |
| **Writing Quality** | 8/10 | Clear structure, both Indonesian and English |
| **Reproducibility** | 7/10 | Good details, but no code provided |
| **Practical Value** | 9/10 | 100% hard constraint satisfaction |
| **Overall** | **8/10** | Excellent practical implementation paper |

---

## Key Insights for Your Thesis

### What This Paper Offers

1. **Practical SA Implementation**
   - Restart mechanism for escaping local optima
   - Pre-processing with slot filtering
   - Geometric cooling schedule (α = 0.99)

2. **Comprehensive Constraint Model**
   - 8 hard constraints (must satisfy)
   - 2 soft constraints (prefer to satisfy)
   - Clear separation of regular vs employee classes

3. **Validation Metrics**
   - Fitness function: count of constraint violations
   - Target: 0 (no violations)
   - Execution time: 35-95 seconds

4. **Three Testing Scenarios**
   - Regular only (easiest)
   - Employee only (hardest for soft constraints)
   - Combined (moderate difficulty)

### Novel Contributions

1. **Restart Mechanism**
   - When stuck for 50 iterations, restart from T₀
   - Up to 3 restarts allowed
   - Helps escape local optima

2. **Slot Filtering Pre-processing**
   - Reduces search space by eliminating invalid slots upfront
   - Satisfies H1, H2, H4, H5 directly
   - More efficient than blind search

3. **100% Hard Constraint Satisfaction**
   - All hard constraints (H1-H8) satisfied in final solutions
   - Better than Paper 3's 84.87%

### Gaps to Address

1. **No algorithm comparison** - Add GA, PSO, or hybrid approaches
2. **Soft constraint optimization** - S2 (lecturer daily limit) needs work
3. **Parameter sensitivity** - Test different T₀, α values
4. **Larger datasets** - Test on 200+, 500+ classes
5. **Weighted fitness** - Different weights for different constraints

---

## Conclusion

### What This Paper Is

- A **practical implementation** of SA for timetabling
- A **case study** with real university data
- A **detailed experimental study** with multiple scenarios
- A **reference** for constraint modeling and SA tuning

### What This Paper is NOT

- A theoretical paper (no mathematical proofs)
- A comparison study (no other algorithms)
- A scalability study (limited to ~100 classes)

### Recommendation

**This is the best practical paper so far.** Use this paper as:

- ✅ **Primary reference** for SA implementation details
- ✅ **Constraint modeling** reference (H1-H8, S1-S2)
- ✅ **Validation approach** reference (fitness, trials, metrics)
- ✅ **Pre-processing** reference (slot filtering)
- ✅ **Restart mechanism** reference for escaping local optima

**Areas to improve upon:**
- Compare with other metaheuristics
- Improve soft constraint satisfaction (especially S2)
- Test on larger datasets
- Add parameter sensitivity analysis
- Implement weighted fitness function

---

## References from Paper

1. Single solution-based meta-heuristic efficiency
2. Greedy + SA on Carter dataset (vs multi-start hill climbing, hyper-heuristics)
3. SA vs GA vs SA-GA hybrid on KTH dataset
4. Optimization definition (finding minimum/maximum of function)
5. Timetabling as NP-hard problem
6. Constraint definitions (event, timeslot, resource, hard/soft, people, conflict)
7. Metaheuristic approaches review
8. SA theory (Kirkpatrick, Gelatt, Vecchi - 1980s)
9. Local search (Monte Carlo) algorithm
10. Metropolis algorithm (1953)
11. Geometric cooling approach
