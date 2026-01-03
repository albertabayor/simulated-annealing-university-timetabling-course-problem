# Paper Analysis: A Simulated Annealing Algorithm for the Faculty-Level University Course Timetabling Problem

## Metadata

| Field | Value |
|-------|-------|
| **Title** | A Simulated Annealing Algorithm for the Faculty-Level University Course Timetabling Problem |
| **Turkish Title** | Fakülte seviyesinde üniversite ders çizelgeleme problemi için bir tavlama benzetimi algoritması |
| **Authors** | Hatice Erdoğan Akbulut, Feristah Ozçelik, Tuğba Saraç |
| **Institutions** | Antalya Bilim University (Turkey), Eskisehir Osmangazi University (Turkey) |
| **Journal** | Pamukkale University Journal of Engineering Sciences |
| **Volume/Issue** | Vol. 30, No. 1 |
| **Date** | 2024 |
| **Pages** | 17-30 |
| **DOI** | 10.5505/pajes.2023.00483 |
| **Type** | Research Article |
| **Corresponding Author** | hatice.erdogan@antalya.edu.tr |

---

## Executive Summary

This paper presents a **novel approach** to faculty-level university course timetabling with **three unique constraints** that have never been combined before: (1) classrooms shared between faculties, (2) double major programs, and (3) minor programs. The authors propose a **Goal Programming (GP)** mathematical model and a **Simulated Annealing (SA)** algorithm for solving large-scale instances. A case study on a private university's engineering faculty shows **83% improvement** over the existing manual schedule.

**Overall Rating: 8.5/10**

---

## Key Novel Contributions

| Contribution | Description |
|--------------|-------------|
| **First study** to consider shared classrooms + double major + minor constraints together |
| **Goal Programming model** with 7 goals for handling soft constraints |
| **83% improvement** achieved on real-world problem |
| **Two-session course handling** (1 day vs 2 days assignment) |
| **Lunch break constraints** (12:00-14:00 gap requirements) |

---

## Problem Definition

### Context

- **Engineering faculty** with 5 departments
- **Private university** in Turkey
- **Shared classrooms** with other faculties
- **Double major programs** between departments
- **Minor programs** for students
- **Curriculum-based** timetabling

### Course Structure

| Characteristic | Description |
|----------------|-------------|
| **Weekly hours** | 1-4 hours per week |
| **1-2 hour courses** | Assigned in one session (one day) |
| **3 hour courses** | One session OR two sessions (instructor preference) |
| **4 hour courses** | Two sessions on two different days |
| **Years 1-2** | Only compulsory courses |
| **Years 3-4** | Compulsory + elective courses |
| **Common courses** | Divided into sections for multiple student groups |

### Time Structure

| Parameter | Value |
|-----------|-------|
| **Days** | Monday-Friday (5 days) |
| **Daily periods** | 11 periods (9:00-20:00) |
| **Weekly periods** | 55 periods total |
| **Lunch break** | 12:00-14:00 (periods 4-5) |
| **Classroom availability** | 9:00-20:00 (based on inter-faculty sharing) |

---

## Constraints

### Hard Constraints (H1-H8, H11-H17)

| Code | Description |
|------|-------------|
| **H1** | All courses assigned required weekly hours |
| **H2** | No student group has >1 compulsory course at same period |
| **H3** | No student group has >1 elective course at same period |
| **H4** | No instructor assigned to >1 course at same period |
| **H6** | No classroom assigned to >1 course at same period **[Shared with other faculties]** |
| **H7** | No course assigned to unavailable classroom periods |
| **H8** | Multi-hour sessions assigned consecutively |
| **H11** | One-session courses assigned to one day |
| **H12** | Two-session courses assigned to two different days |
| **H14** | Instructor availability respected |
| **H15** | Classroom capacity ≥ students enrolled |
| **H16** | Courses assigned to appropriate classroom type |
| **H17** | Year 3-4 compulsory courses don't conflict with electives |

**Note:** H6 (shared classrooms) is rarely discussed in literature but critical here.

### Soft Constraints (S1, S4, S6, S18, S19)

| Code | Description | Goal Target |
|------|-------------|-------------|
| **S1** | Avoid courses during lunch break (12:00-14:00) | Max 1 hour overlap |
| **S4** | Avoid two different courses consecutive during lunch | Max 1 course overlap |
| **S6** | Compulsory courses of consecutive groups don't overlap | Max 1 overlapping course |
| **S18** | Daily hours ≤ 8 for Years 1-2 | Target: 8 hours |
| **S19** | Daily hours ≤ 8 for Years 3-4 | Target: 8 hours |

### Novel Constraints: Double Major & Minor

| Constraint | Description | Target |
|------------|-------------|--------|
| **Double Major** | No overlapping compulsory courses for same student group in different departments | Max 1 overlap |
| **Minor Program** | No overlapping minor courses with compulsory courses | Max 1 overlap |

**Why novel?**
- First study to handle both double major AND minor together
- Double major: Most courses of first-year groups are common
- Minor: Fewer courses, more flexible scheduling allowed

---

## Mathematical Model: Goal Programming

### Index Sets

```
C  = {i, p}      : Course indices
I  = {j}         : Instructor indices
DE = {m, m'}     : Department indices
SG = {n, u}      : Student group indices
DA = {l}         : Day indices
P  = {k}         : Period indices
CR = {q, o}      : Classroom indices
S  = {w}         : Session indices
CT = {v}         : Classroom type indices
```

### Decision Variables

```
Xilkq = 1 if course i assigned to classroom q on day l at period k
Yiwlq = 1 if session w of course i assigned to classroom q on day l
```

### Deviation Variables (for soft constraints)

| Variable | Meaning |
|----------|---------|
| `d1+` / `d1-` | Positive/negative deviation from lunch break goal (multi-hour courses) |
| `d2+` / `d2-` | Positive/negative deviation from lunch break goal (two different courses) |
| `d3+` / `d3-` | Positive/negative deviation from consecutive groups overlap goal |
| `d4++` / `d4-` | Positive/negative deviation from daily hours goal (Years 1-2) |
| `d5++` / `d5-` | Positive/negative deviation from daily hours goal (Years 3-4) |
| `d6+` / `d6-` | Positive/negative deviation from double major overlap goal |
| `d7+` / `d7-` | Positive/negative deviation from minor overlap goal |

### Seven Goals (G1-G7)

| Goal | Description | Target (T) |
|------|-------------|------------|
| **G1** | Avoid multi-hour courses during lunch | T1 = 1 hour |
| **G2** | Avoid two courses consecutive during lunch | T2 = 1 course |
| **G3** | Minimize overlap of consecutive groups' compulsory courses | T3 = 1 course |
| **G4** | Daily hours ≤ 8 for Years 1-2 | T4 = 8 hours |
| **G5** | Daily hours ≤ 8 for Years 3-4 | T5 = 8 hours |
| **G6** | No conflicts for double major students | T6 = 1 overlap |
| **G7** | No conflicts for minor students | T7 = 1 overlap |

### Objective Function

```
min f = Σ [normalized deviations from each goal]

Goals normalized by dividing by upper bounds
All goals have equal weight
```

---

## Simulated Annealing Algorithm

### SA Components

1. **Solution Representation**
   - Matrix: rows = classrooms, columns = periods
   - Cell values: 0 (unavailable), 1 (available), CourseCode (assigned)

2. **Initial Solution Generation**
   ```
   1. Sort courses by students (descending)
   2. Sort classrooms by capacity (ascending)
   3. Assign courses to suitable slots
   4. Handle one-session vs two-session courses
   5. Check instructor and student group availability
   ```

3. **Neighborhood Structures**
   - **Simple move**: Move one course to different slot
   - **Swap**: Swap two courses' slots

4. **Cooling Schedule**
   ```
   T(tc+1) = α × T(tc)
   where α = cooling factor
   ```

5. **Termination Criteria**
   - Temperature ≤ final temperature
   - Total steps ≥ maximum steps
   - Objective function = 0 (ideal)

### SA Parameters

| Parameter | Value |
|-----------|-------|
| Initial Temperature (T₀) | Tuned experimentally |
| Cooling Factor (α) | Tuned experimentally |
| Final Temperature | Stopping threshold |
| Max Steps | Iteration limit |

---

## Experimental Results

### Test Problems

| Instance | Courses | Instructors | Classrooms | Student Groups | Departments |
|----------|---------|-------------|------------|----------------|-------------|
| **Small** | 30 | 10 | 3 | 5 | 2 |
| **Medium** | 50 | 15 | 5 | 10 | 3 |
| **Large** | 100 | 25 | 10 | 20 | 5 |

### Real Case Study: Engineering Faculty

| Data | Count |
|------|-------|
| Departments | 5 |
| Courses | Not specified (real data) |
| Instructors | Not specified |
| Classrooms | Shared with other faculties |
| Student Groups | Multiple year levels |

### Results Summary

| Method | Small | Medium | Large | Real Problem |
|--------|-------|--------|-------|--------------|
| **GP Model** | Feasible | Feasible | Timeout (>1 hour) | Timeout |
| **SA Algorithm** | Feasible | Feasible | Feasible | **83% improvement** |

### Key Findings

1. **Goal Programming (GP)**
   - Works for small and medium instances
   - Fails for large instances (timeout)
   - Provides lower bound for validation

2. **Simulated Annealing (SA)**
   - Solves all instance sizes
   - Fast convergence
   - 83% improvement over manual scheduling
   - Handles all novel constraints successfully

3. **Constraint Satisfaction**
   - Hard constraints: 100% satisfied
   - Soft constraints: Minimized deviations
   - Double major: Minimized overlaps
   - Minor: Minimized overlaps

---

## Critical Analysis

### Strengths

| Aspect | Description |
|--------|-------------|
| **Novelty** | First study combining shared classrooms + double major + minor |
| **Real-world impact** | 83% improvement on actual problem |
| **Mathematical rigor** | Complete goal programming model with 27 equations |
| **Comprehensive constraints** | 13 hard + 5 soft constraints |
| **Validation** | Both mathematical and computational validation |
| **Literature review** | 13 previous studies compared in Table 1 |
| **Practical relevance** | Addresses actual university needs |
| **Dual approach** | GP for small instances, SA for large |

### Weaknesses

| Issue | Description |
|-------|-------------|
| **Limited computational details** | SA parameters not fully specified |
| **No algorithm comparison** | Only SA tested (no GA, PSO, etc.) |
| **Scalability unclear** | Large instance = 100 courses (still moderate) |
| **No execution time** | Computational performance not reported |
| **Parameter tuning** | No sensitivity analysis for α, T₀ |
| **Single case study** | Only one engineering faculty tested |
| **Visualization missing** | No sample timetable output shown |

### Comparison with Previous SA Papers

| Aspect | Paper 3 (UNISSULA) | Paper 4 (STMIK) | Paper 6 (This) |
|--------|-------------------|-----------------|----------------|
| **Year** | 2016 | 2024 | 2024 |
| **Constraints** | 6 hard, 2 soft | 8 hard, 2 soft | 13 hard, 5 soft |
| **Novelty** | Standard SA | Restart mechanism | Double major + minor |
| **Mathematical model** | ✅ Complete | ❌ None | ✅ Goal Programming |
| **Real case study** | ✅ UNISSULA | ✅ STMIK LIKMI | ✅ Private university |
| **Improvement metric** | 84.87% allocation | 100% hard constraints | **83% improvement** |
| **Unique features** | Two-stage SA | Pre-processing, Restart | Shared classrooms, Double major, Minor |
| **Overall Rating** | 7.5/10 | 8/10 | 8.5/10 |

---

## Literature Review Summary (Table 1)

| Study | Constraints | Objectives | Methods |
|-------|-------------|------------|---------|
| MirHassani [7] | H1,H2,H5,H7,H8,H9,H19,H20,S2,S3,S14 | O2,O6 | IP |
| Ismayilova [8] | H1,H3,H5 | O4,O5 | MOP, AHP, ANP |
| Cura [9] | H1,H2,H3,H4,H20 | O3 | SA (vs GA, TS) |
| Al Tarawneh [10] | H1,H2,H3,H7,H8,H12,S1,S15,S16 | O2 | TS |
| Nguyen [11] | H1,H2,H3,H4,H6,H7,H9,H12,H13,H16,H18,S1,S3,S9,S11,S14,S15,S16,S17 | O2 | HM (HS, BA) |
| Demir [12] | H1,H2,H3,H4,H7,H8,H11,H12,H14,S4 | O3 | IP |
| Abdelhalim [13] | H1,H2,H10,H12,H14,H16,S1,S15,S16 | O1,O2 | GA |
| Borchani [14] | H1,H2,H3,H12,H14,S16 | O2 | VND |
| Ertane [15] | H2,H3,H4,H7,H18,S4,S5,S6,S7,S8,S18 | O2 | ILP |
| Ozkan [16] | H1,H2,H3,H9,H11,H12,H14,H15,H16,S4,S10,S14 | O2 | ILP, TS, SA |
| Thepphakorn [17] | H1,H2,H3,H7,H8,H11,H13,H16,S14 | O1,O2 | CS |
| Alnowaini [18] | H1,H2,H3,H12,S11,S12,S14,S15,S16,S17 | O6 | GA |
| Ariyazand [19] | H1,H2,H3,H4,H11,H12,S12,S14 | O3 | BTA, CS, ABC, FA, GA |
| **This study** | H1,H2,H3,H4,H6,H7,H8,H11,H12,H14,H15,H16,H17,S1,S4,S6,S18,S19 | O2,O7,O8 | GP, SA |

**Legend:**
- **H**: Hard constraint
- **S**: Soft constraint
- **O**: Objective function
- **IP**: Integer Programming
- **MOP**: Multi-Objective Programming
- **AHP/ANP**: Analytic Hierarchy/Network Process
- **SA**: Simulated Annealing
- **GA**: Genetic Algorithm
- **TS**: Tabu Search
- **VND**: Variable Neighborhood Descent
- **ILP**: Integer Linear Programming
- **CS**: Cuckoo Search
- **ABC**: Artificial Bee Colony
- **GP**: Goal Programming
- **HM**: Hybrid Method
- **HS**: Harmony Search
- **BA**: Bee Algorithm
- **BTA**: Bat Algorithm
- **FA**: Firefly Algorithm

---

## Quality Assessment

| Criteria | Score (1-10) | Notes |
|----------|--------------|-------|
| **Originality** | 10/10 | First study with this constraint combination |
| **Technical Depth** | 9/10 | Complete GP model + SA implementation |
| **Scientific Rigor** | 8/10 | Real case study, but limited comparison |
| **Writing Quality** | 8/10 | Clear, well-structured |
| **Reproducibility** | 7/10 | GP model detailed, SA details sparse |
| **Practical Value** | 10/10 | 83% real-world improvement |
| **Overall** | **8.5/10** | Excellent practical contribution |

---

## Key Insights for Your Thesis

### What This Paper Offers

1. **Novel Constraint Modeling**
   - Shared classrooms between faculties (H6)
   - Double major programs
   - Minor programs
   - Lunch break constraints (S1, S4)

2. **Goal Programming Framework**
   - 7 goals with deviation variables
   - Normalized objective function
   - Equal weight for all goals
   - Can be adapted for other multi-objective problems

3. **Two-Phase Approach**
   - Phase 1: Goal Programming for small instances
   - Phase 2: Simulated Annealing for large instances
   - GP provides lower bound validation

4. **Validation Metrics**
   - Deviation from goal targets
   - Hard constraint satisfaction (100%)
   - Soft constraint minimization
   - Real-world improvement percentage

### Novel Contributions to Build Upon

1. **Double Major Constraint**
   ```
   Minimize overlap of compulsory courses for:
   - Same student group (n) in different departments (m, m')
   - Consecutive years (u = n + 1)
   ```

2. **Minor Program Constraint**
   ```
   Minimize overlap of:
   - Minor courses with compulsory courses
   - More flexible than double major (fewer courses)
   ```

3. **Shared Classrooms**
   ```
   Inter-faculty classroom availability matrix
   - Period-specific availability
   - Capacity constraints
   - Type matching
   ```

### Gaps to Address

1. **Algorithm comparison** - Test GA, PSO, hybrid approaches
2. **Larger datasets** - Test on 200+, 500+ courses
3. **Parameter sensitivity** - Analyze α, T₀ effects
4. **Execution time** - Report computational performance
5. **Multi-objective optimization** - Use Pareto fronts instead of weighted sum
6. **Dynamic constraints** - Handle real-time changes

---

## Conclusion

### What This Paper Is

- A **novel contribution** to faculty-level timetabling
- The **first study** combining shared classrooms, double major, and minor constraints
- A **practical solution** with 83% real-world improvement
- A **complete mathematical model** (Goal Programming)
- A **scalable approach** (GP for small, SA for large)

### What This Paper is NOT

- An algorithm comparison study (only SA tested)
- A comprehensive survey (focuses on one case)
- A theoretical paper (application-focused)

### Recommendation

**Highly recommended for thesis reference**, especially if:

- ✅ Your problem involves shared resources
- ✅ You need multi-objective optimization (Goal Programming)
- ✅ You're considering double major/minor programs
- ✅ You want a practical case study with measurable improvement

**Use this paper for:**
- Goal Programming model reference (equations 1-27)
- Double major/minor constraint modeling
- Shared classroom availability handling
- Two-phase approach (mathematical + metaheuristic)
- Validation metrics (deviation variables, improvement %)

**Areas to improve upon:**
- Add algorithm comparison (GA, PSO, hybrids)
- Test on larger datasets
- Report execution time
- Analyze parameter sensitivity
- Consider Pareto-based multi-objective optimization

---

## References from Paper

The paper cites 20 references covering:
1. Scheduling and timetabling definitions
2. University Course Timetabling Problem (UCTP) classifications
3. Faculty-level timetabling studies (13 papers compared)
4. Simulated Annealing applications
5. Goal Programming theory
6. Metaheuristic algorithms (GA, TS, CS, ABC, FA, BTA)
7. Constraint handling approaches

Key references for further reading:
- MirHassani [7]: IP model for faculty-level timetabling
- Cura [9]: SA vs GA vs TS comparison
- Ertane [15]: First double major constraint study
- Ismayilova [8]: Multi-objective 0-1 IP with AHP/ANP
