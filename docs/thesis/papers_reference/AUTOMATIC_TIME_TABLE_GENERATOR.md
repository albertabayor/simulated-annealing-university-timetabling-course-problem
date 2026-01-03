# Paper Analysis: AUTOMATIC TIME TABLE GENERATOR

## Metadata

| Field | Value |
|-------|-------|
| **Title** | AUTOMATIC TIME TABLE GENERATOR |
| **Authors** | Mitali Algamwar, Vaishnavi Gogulwar, Jahnavi Hedau, Sanket Meshram |
| **Advisor** | Prof. Anand Donald |
| **Institution** | Rajiv Gandhi College of Engineering Research and Technology, Chandrapur, Maharashtra, India |
| **Journal** | International Journal of Creative Research Thoughts (IJCRT) |
| **Volume/Issue** | Volume 12, Issue 5 |
| **Date** | May 2024 |
| **ISSN** | 2320-2882 |
| **Paper ID** | IJCRT2405777 |

---

## Executive Summary

This paper presents a desktop-based automatic timetable generator using Python and Tkinter. The system provides a GUI for managing subjects, teachers, and generating timetables. Similar to the previous paper, it lacks implementation details of the actual scheduling algorithm and focuses primarily on the application interface.

**Overall Rating: 3/10**

---

## Problem Statement

The paper identifies the following challenges in manual timetable generation:

1. **Complex and error-prone** - Manual planning is difficult and mistakes are common
2. **Time-consuming** - Requires significant time and manpower
3. **Resource allocation issues** - Limited faculties teaching multiple subjects
4. **Collision avoidance** - Need to schedule faculty without overlapping timings
5. **Frequent updates** - Timetables need regeneration each semester
6. **Temporary schedules** - Difficulty creating schedules when faculty are on leave

---

## Proposed Solution

### Tech Stack

| Component | Technology |
|-----------|------------|
| **Language** | Python |
| **GUI Framework** | Tkinter |
| **IDE** | VS Code |
| **Database** | Not specified |

### Hardware Requirements

- Windows 7 or higher
- i3 processor or higher
- 8 GB RAM or higher
- 100 GB ROM or higher

### System Architecture

```
┌─────────────────────────────────────┐
│            LOGIN PAGE               │
└──────────────┬──────────────────────┘
               │
               ▼
┌─────────────────────────────────────┐
│            HOME PAGE                │
└──────┬────────────────────────┬─────┘
       │                        │
       ▼                        ▼
┌─────────────┐         ┌─────────────┐
│  DATABASE   │         │  FUNCTIONS  │
└─────────────┘         └──────┬──────┘
                               │
        ┌──────────────────────┼──────────────────────┐
        │                      │                      │
        ▼                      ▼                      ▼
┌──────────────┐     ┌──────────────┐     ┌──────────────┐
│ Add Subject  │     │ Add Teacher  │     │  Assign      │
│ Delete       │     │ Delete       │     │  Teacher     │
│              │     │              │     │              │
└──────────────┘     └──────────────┘     └──────┬───────┘
                                                   │
                                                   ▼
                                          ┌──────────────┐
                                          │  TIMETABLE   │
                                          │    PAGE      │
                                          └──────────────┘
```

### Key Features

1. **Login System** - User authentication
2. **Subject Management** - Add/Delete subjects
3. **Teacher Management** - Add/Delete teachers
4. **Teacher Assignment** - Assign teachers to subjects
5. **Timetable Generation** - Automatic schedule creation

---

## Methodology

### Inputs Required
- Branch details
- Semester information
- Subjects (including electives and core subjects)
- Lab details
- Total number of periods

### Mentioned Algorithms (Not Implemented)
The paper mentions algorithms that could be used:
- Genetic algorithms
- Heuristic algorithms
- Resource scheduling

**Note:** Similar to the previous paper, these are mentioned but not actually implemented or described in detail.

---

## Critical Analysis

### Strengths

| Aspect | Description |
|--------|-------------|
| **Simple approach** | Python + Tkinter is accessible and easy to understand |
| **Desktop application** | No server setup required, can run standalone |
| **Clear functionality** | Well-defined features (add/delete, assign) |
| **UI screenshots** | Shows actual application interface |
| **Identifies real pain points** | Faculty leave management, temporary schedules |

### Weaknesses

#### 1. **Even Less Technical Depth Than Previous Paper**
- No algorithm explanation at all
- No pseudocode
- No mathematical formulation
- No discussion of how conflicts are resolved

#### 2. **Very Generic Architecture**
- Architecture diagram is extremely basic
- Shows only CRUD operations
- No insight into the actual timetable generation logic

#### 3. **No Algorithm Implementation**
Despite mentioning:
> "we are going to use algorithms like genetic, heuristic, resource scheduling"

There is absolutely no description of:
- How these algorithms work
- Which one was actually used
- How constraints are encoded
- How optimization is performed

#### 4. **No Results or Evaluation**
- No performance metrics
- No comparison with manual scheduling
- No conflict resolution examples
- Result section only shows UI screenshots

#### 5. **Literature Review Issues**
- Very brief (only 3 papers summarized)
- Summaries are generic
- No critical analysis of existing approaches

#### 6. **Future Scope Contradiction**
The Future Scope section suggests:
> "Incorporating advanced scheduling algorithms... Algorithms such as genetic algorithms, simulated annealing, or constraint programming can be explored"

This implies these algorithms were NOT used in the current implementation, contradicting the claim in the Literature Review.

---

## Quality Assessment

| Criteria | Score (1-10) | Notes |
|----------|--------------|-------|
| **Originality** | 2/10 | Basic CRUD application |
| **Technical Depth** | 1/10 | Almost zero algorithmic content |
| **Scientific Rigor** | 1/10 | No experiments, no validation |
| **Writing Quality** | 4/10 | Clear but very basic |
| **Reproducibility** | 1/10 | Cannot reproduce |
| **Practical Value** | 4/10 | Simple desktop app concept |
| **Overall** | **3/10** | Very weak as research paper |

---

## Comparison with Previous Paper

| Aspect | Paper 1 (React) | Paper 2 (Tkinter) |
|--------|-----------------|-------------------|
| **Tech Stack** | Modern web (React/Firebase) | Traditional desktop (Python/Tkinter) |
| **Architecture** | Client-Server | Standalone desktop |
| **Algorithm Discussion** | Theoretical survey of 6 methods | Brief mention of 3 methods |
| **Technical Depth** | Low (but better) | Very low |
| **UI Evidence** | 1 figure | 5 screenshots |
| **Overall Rating** | 3.5/10 | 3/10 |

**Both papers suffer from the same fundamental issue:** Neither actually describes how the timetable generation algorithm works.

---

## Conclusion

### What This Paper Actually Is

- A **basic desktop application project report**
- A **CRUD system** for managing timetable data
- A **tutorial-level** Python/Tkinter project

### What This Paper is NOT

- An algorithmic contribution
- A research paper with scientific rigor
- A reproducible study

### Value for Your Thesis

**Use this paper for:**
- ✅ Comparison of desktop vs web approaches
- ✅ Simple feature list for a timetable system
- ✅ Basic UI flow reference (Login → Home → Functions → Result)
- ✅ Hardware/software requirements consideration

**Do NOT use this paper for:**
- ❌ Algorithm implementation (none provided)
- ❌ Optimization techniques (only mentioned, not implemented)
- ❌ Performance benchmarks (none provided)
- ❌ Scalability considerations

### Recommendation

This paper is even weaker than the previous one. It's essentially a student project report with minimal technical depth. Use it only as a reference for basic system features and UI flow.

---

## Bibliography

1. Mhaise, G. D., et al. "AUTOMATIC TIME TABLE GENERATOR." IRJMETS, 2023.
2. Puttaswamy, A., et al. "A STUDY ON AUTOMATIC TIMETABLE GENERATOR." IJIRG, 2018.
3. Gadekar, S., et al. "AUTOMATIC TIME TABLE GENERATOR SYSTEM." IJARIIE, 2022.
4. Sugunamukia, K. R., & Anoop, M. A. "A SMART TIME TABLE GENERATOR." IJRPR, 2021.
5. Varsha, S., et al. "DESIGN AND IMPLEMENTATION OF TIME TABLE GENERATOR." JETIR, 2022.
