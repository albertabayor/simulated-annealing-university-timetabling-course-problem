# Visualisasi dan Diagram Alur

## 1. Overview Arsitektur Sistem

### 1.1 High-Level Architecture

```mermaid
graph TB
    subgraph "Input Layer"
        A[Excel Data] --> B[Data Loader]
        B --> C[Domain Types]
    end
    
    subgraph "Initial Solution"
        C --> D[Greedy Algorithm]
        D --> E[Initial State]
    end
    
    subgraph "Optimization Core"
        E --> F[Simulated Annealing]
        G[Constraints] --> F
        H[Move Generators] --> F
        I[Configuration] --> F
    end
    
    subgraph "Output Layer"
        F --> J[Optimal Solution]
        J --> K[Statistics]
        J --> L[Violation Reports]
        J --> M[Schedule Export]
    end
    
    style F fill:#e1f5fe
    style J fill:#c8e6c9
```

### 1.2 Component Interaction

```mermaid
sequenceDiagram
    participant Main as Main Application
    participant DL as Data Loader
    participant IS as Initial Solution
    participant SA as Simulated Annealing
    participant C as Constraints
    participant MG as Move Generators
    participant OUT as Output

    Main->>DL: Load Excel data
    DL-->>Main: TimetableInput
    
    Main->>IS: Generate initial solution
    IS-->>Main: Initial TimetableState
    
    Main->>SA: Create solver
    SA->>C: Load constraints
    SA->>MG: Load move generators
    
    Main->>SA: Run optimization
    loop Optimization Loop
        SA->>MG: Generate neighbor
        MG-->>SA: New state
        SA->>C: Evaluate constraints
        C-->>SA: Fitness score
        SA->>SA: Accept/reject decision
    end
    
    SA-->>Main: Final solution
    Main->>OUT: Export results
```

## 2. Algoritma Simulated Annealing

### 2.1 Two-Phase Optimization Flow

```mermaid
flowchart TD
    A[Start] --> B[Initialize State]
    B --> C[Calculate Initial Fitness]
    C --> D{Phase 1: Hard Constraints}
    
    D --> E[Generate Neighbor]
    E --> F[Evaluate Hard Violations]
    F --> G{Hard Violations Reduced?}
    
    G -->|Yes| H[Accept Move]
    G -->|No| I{Accept Probability}
    
    I -->|Accept| H
    I -->|Reject| J[Keep Current State]
    
    H --> K[Update Best State]
    J --> L{Temperature Check}
    K --> L
    
    L -->|T > Min/60%| M[Cooling: T = T * α]
    L -->|T ≤ Min/60%| N{Phase 2: Soft Constraints}
    
    M --> E
    N --> O[Generate Neighbor]
    O --> P[Evaluate All Constraints]
    P --> Q{Hard Violations = 0?}
    
    Q -->|No| R[Reject Move]
    Q -->|Yes| S{Fitness Improved?}
    
    S -->|Yes| T[Accept Move]
    S -->|No| U{Accept Probability}
    
    U -->|Accept| T
    U -->|Reject| V[Keep Current State]
    
    T --> W[Update Best State]
    V --> X{Temperature Check}
    W --> X
    
    X -->|T > Min| Y[Cooling: T = T * α]
    X -->|T ≤ Min| Z[Return Solution]
    
    Y --> O
    R --> X
    
    style D fill:#ffcdd2
    style N fill:#c8e6c9
    style Z fill:#e1f5fe
```

### 2.2 Temperature Schedule Visualization

```mermaid
graph LR
    subgraph "Temperature Schedule"
        A[Initial Temp: 100000] --> B[Phase 1: Hard Constraints]
        B --> C[Temp: 10000]
        C --> D[Phase 2: Soft Constraints]
        D --> E[Temp: 1000]
        E --> F[Temp: 100]
        F --> G[Temp: 10]
        G --> H[Temp: 1]
        H --> I[Min Temp: 0.0000001]
    end
    
    subgraph "Reheating Events"
        J[Local Minimum] --> K[Reheat: ×1.5]
        K --> L[Continue Cooling]
        L --> M[Local Minimum]
        M --> N[Reheat: ×1.5]
        N --> O[Continue Cooling]
    end
    
    style B fill:#ffcdd2
    style D fill:#c8e6c9
    style K fill:#fff3e0
    style N fill:#fff3e0
```

## 3. Constraint System

### 3.1 Constraint Hierarchy

```mermaid
graph TD
    A[Constraint System] --> B[Hard Constraints]
    A --> C[Soft Constraints]
    
    B --> D[No Room Conflict]
    B --> E[No Lecturer Conflict]
    B --> F[Room Capacity]
    B --> G[No Prodi Conflict]
    B --> H[Friday Prayer Time]
    B --> I[Max Daily Periods]
    B --> J[Class Type Time]
    B --> K[Saturday Restriction]
    B --> L[Exclusive Room]
    
    C --> M[Preferred Time]
    C --> N[Preferred Room]
    C --> O[Transit Time]
    C --> P[Compactness]
    C --> Q[Prayer Time Overlap]
    C --> R[Evening Class Priority]
    C --> S[Research Day]
    C --> T[Overflow Penalty]
    
    style B fill:#ffcdd2
    style C fill:#c8e6c9
```

### 3.2 Constraint Evaluation Flow

```mermaid
flowchart LR
    A[State Input] --> B[Hard Constraints]
    A --> C[Soft Constraints]
    
    B --> D[No Room Conflict Check]
    D --> E[No Lecturer Conflict Check]
    E --> F[Room Capacity Check]
    F --> G[Other Hard Checks]
    G --> H[Hard Penalty Calculation]
    
    C --> I[Preferred Time Check]
    I --> J[Preferred Room Check]
    J --> K[Transit Time Check]
    K --> L[Other Soft Checks]
    L --> M[Soft Penalty Calculation]
    
    H --> N[Fitness = Hard Penalty × Weight + Soft Penalty]
    M --> N
    
    N --> O[Final Fitness Score]
    
    style B fill:#ffcdd2
    style C fill:#c8e6c9
    style N fill:#e1f5fe
```

## 4. Move Generator System

### 4.1 Move Generator Categories

```mermaid
graph TD
    A[Move Generators] --> B[Targeted Operators]
    A --> C[General Operators]
    
    B --> D[Fix Friday Prayer Conflict]
    B --> E[Swap Friday with Non-Friday]
    B --> F[Fix Lecturer Conflict]
    B --> G[Fix Room Conflict]
    B --> H[Fix Max Daily Periods]
    B --> I[Fix Room Capacity]
    
    C --> J[Change Time Slot and Room]
    C --> K[Change Time Slot]
    C --> L[Change Room]
    C --> M[Swap Classes]
    
    style B fill:#fff3e0
    style C fill:#e8eaf6
```

### 4.2 Adaptive Operator Selection

```mermaid
flowchart TD
    A[Select Move Operator] --> B{Random Selection?}
    
    B -->|30%| C[Random Operator]
    B -->|70%| D[Weighted Selection]
    
    D --> E[Calculate Success Rates]
    E --> F[Apply Weights]
    F --> G[Weighted Random Choice]
    
    C --> H[Selected Operator]
    G --> H
    
    H --> I[Execute Move]
    I --> J[Update Statistics]
    J --> K[Next Iteration]
    
    style C fill:#c5e1a5
    style D fill:#ffecb3
```

## 5. Data Flow and State Management

### 5.1 State Evolution

```mermaid
stateDiagram-v2
    [*] --> Initial
    Initial --> Phase1: Start Optimization
    
    Phase1 --> Phase1: Generate Neighbor
    Phase1 --> Phase1: Evaluate Hard Constraints
    Phase1 --> Phase1: Accept/Reject
    
    Phase1 --> Phase2: Hard Violations = 0
    Phase1 --> Phase1: Still Hard Violations
    
    Phase2 --> Phase2: Generate Neighbor
    Phase2 --> Phase2: Evaluate All Constraints
    Phase2 --> Phase2: Accept/Reject
    
    Phase2 --> Final: Temperature < Min
    Phase2 --> Phase2: Temperature OK
    
    Final --> [*]: Complete
    
    note right of Phase1
        Focus on eliminating
        hard constraint violations
        60% of iterations
    end note
    
    note right of Phase2
        Optimize soft constraints
        while maintaining hard constraints
        40% of iterations
    end note
```

### 5.2 Data Transformation Pipeline

```mermaid
graph LR
    subgraph "Input Data"
        A[Excel File] --> B[Rooms Sheet]
        A --> C[Lecturers Sheet]
        A --> D[Classes Sheet]
    end
    
    subgraph "Data Processing"
        B --> E[Room Objects]
        C --> F[Lecturer Objects]
        D --> G[Class Requirements]
    end
    
    subgraph "Initial Solution"
        E --> H[Greedy Algorithm]
        F --> H
        G --> H
        H --> I[Initial Schedule]
    end
    
    subgraph "Optimization"
        I --> J[Simulated Annealing]
        J --> K[Optimized Schedule]
    end
    
    subgraph "Output"
        K --> L[JSON Export]
        K --> M[Statistics Report]
        K --> N[Violation Analysis]
    end
    
    style H fill:#e1f5fe
    style J fill:#c8e6c9
```

## 6. Time Slot and Room Management

### 6.1 Time Slot Structure

```mermaid
gantt
    title Weekly Time Slot Structure
    dateFormat HH:mm
    axisFormat %H:%M
    
    section Monday
    Period 1    :08:00, 90m
    Period 2    :09:30, 90m
    Period 3    :11:00, 90m
    Period 4    :13:00, 90m
    Period 5    :14:30, 90m
    Period 6    :16:00, 90m
    
    section Tuesday
    Period 1    :08:00, 90m
    Period 2    :09:30, 90m
    Period 3    :11:00, 90m
    Period 4    :13:00, 90m
    Period 5    :14:30, 90m
    Period 6    :16:00, 90m
    
    section Friday
    Period 1    :08:00, 90m
    Prayer Time  :11:00, 60m
    Period 3    :13:00, 90m
    Prayer Time  :15:00, 60m
    Period 5    :16:00, 90m
```

### 6.2 Room Assignment Logic

```mermaid
flowchart TD
    A[Class Requirement] --> B{Needs Lab?}
    
    B -->|Yes| C[Filter Lab Rooms]
    B -->|No| D[Filter Regular Rooms]
    
    C --> E[Check Capacity]
    D --> E
    
    E --> F{Capacity ≥ Participants?}
    F -->|No| G[Skip Room]
    F -->|Yes| H[Check Availability]
    
    H --> I{Room Available?}
    I -->|No| G
    I -->|Yes| J[Assign Room]
    
    G --> K{More Rooms?}
    J --> L[Room Assigned]
    
    K -->|Yes| E
    K -->|No| M[No Suitable Room]
    
    style C fill:#ffecb3
    style D fill:#e8eaf6
    style L fill:#c8e6c9
    style M fill:#ffcdd2
```

## 7. Performance and Optimization

### 7.1 Performance Bottlenecks

```mermaid
graph TD
    A[Performance Analysis] --> B[State Cloning]
    A --> C[Constraint Evaluation]
    A --> D[Move Generation]
    A --> E[Conflict Detection]
    
    B --> F[JSON.parse/stringify]
    B --> G[Custom Cloning]
    
    C --> H[O(n²) Room Conflicts]
    C --> I[O(n²) Lecturer Conflicts]
    C --> J[O(n) Other Constraints]
    
    D --> K[Random Selection]
    D --> L[Constraint-Aware Selection]
    
    E --> M[Nested Loops]
    E --> N[Hash-based Lookup]
    
    style F fill:#ffcdd2
    style G fill:#c8e6c9
    style H fill:#ffcdd2
    style I fill:#ffcdd2
    style M fill:#ffcdd2
    style N fill:#c8e6c9
```

### 7.2 Optimization Strategies

```mermaid
flowchart LR
    A[Optimization Techniques] --> B[State Management]
    A --> C[Constraint Evaluation]
    A --> D[Move Selection]
    A --> E[Data Structures]
    
    B --> F[Selective Cloning]
    B --> G[Immutable Updates]
    
    C --> H[Constraint Caching]
    C --> I[Incremental Evaluation]
    
    D --> J[Adaptive Selection]
    D --> K[Temperature-Aware Moves]
    
    E --> L[Hash Maps]
    E --> M[Indexed Data]
    
    style F fill:#e1f5fe
    style H fill:#e1f5fe
    style J fill:#e1f5fe
    style L fill:#e1f5fe
```

## 8. Error Handling and Recovery

### 8.1 Error Handling Flow

```mermaid
flowchart TD
    A[Operation Start] --> B{Error Occurred?}
    
    B -->|No| C[Continue Operation]
    B -->|Yes| D[Error Classification]
    
    D --> E{Critical Error?}
    D --> F{Recoverable Error?}
    D --> G{Warning?}
    
    E -->|Yes| H[Stop Optimization]
    F -->|Yes| I[Apply Recovery Strategy]
    G -->|Yes| J[Log Warning]
    
    I --> K{Recovery Successful?}
    K -->|Yes| C
    K -->|No| L[Fallback Strategy]
    
    L --> M{Fallback Successful?}
    M -->|Yes| C
    M -->|No| H
    
    J --> C
    C --> N{Operation Complete?}
    N -->|No| B
    N -->|Yes| O[Success]
    
    style H fill:#ffcdd2
    style I fill:#fff3e0
    style J fill:#fff9c4
    style O fill:#c8e6c9
```

### 8.2 Reheating Mechanism

```mermaid
stateDiagram-v2
    [*] --> NormalCooling
    NormalCooling --> NormalCooling: Accept Move
    NormalCooling --> NormalCooling: Reject Move
    
    NormalCooling --> StuckDetection: No Improvement for N iterations
    StuckDetection --> Reheating: Temperature < Threshold
    
    Reheating --> NormalCooling: Temperature Increased
    NormalCooling --> StuckDetection: Continue Monitoring
    
    StuckDetection --> MaxReheats: Reheat Count < Max
    MaxReheats --> [*]: Stop Optimization
    
    note right of StuckDetection
        Check if stuck in local minimum
        by monitoring improvement rate
    end note
    
    note right of Reheating
        Increase temperature to escape
        local minimum and continue search
    end note
```

## 9. Integration and Deployment

### 9.1 System Integration

```mermaid
graph TB
    subgraph "External Systems"
        A[Student Information System]
        B[Room Management System]
        C[Lecturer Management]
        D[Academic Calendar]
    end
    
    subgraph "Timetable-SA System"
        E[Data Import Module]
        F[Optimization Engine]
        G[Export Module]
        H[Web Interface]
    end
    
    subgraph "Output Systems"
        I[Student Portal]
        J[Lecturer Portal]
        K[Room Display]
        L[Administrative Dashboard]
    end
    
    A --> E
    B --> E
    C --> E
    D --> E
    
    E --> F
    F --> G
    G --> I
    G --> J
    G --> K
    G --> L
    
    H --> F
    H --> G
    
    style F fill:#e1f5fe
    style G fill:#c8e6c9
```

### 9.2 Deployment Architecture

```mermaid
graph LR
    subgraph "Development"
        A[Local Development]
        B[Unit Tests]
        C[Integration Tests]
    end
    
    subgraph "Staging"
        D[Staging Server]
        E[Performance Testing]
        F[User Acceptance Testing]
    end
    
    subgraph "Production"
        G[Production Server]
        H[Load Balancer]
        I[Database]
        J[Monitoring]
    end
    
    A --> D
    B --> D
    C --> D
    
    D --> G
    E --> G
    F --> G
    
    G --> H
    H --> I
    G --> J
    
    style A fill:#e8eaf6
    style D fill:#fff3e0
    style G fill:#c8e6c9
```

## 10. Monitoring and Analytics

### 10.1 Performance Metrics

```mermaid
graph TD
    A[Performance Monitoring] --> B[Optimization Metrics]
    A --> C[System Metrics]
    A --> D[User Metrics]
    
    B --> E[Convergence Rate]
    B --> F[Solution Quality]
    B --> G[Iteration Count]
    B --> H[Reheating Events]
    
    C --> I[CPU Usage]
    C --> J[Memory Usage]
    C --> K[Execution Time]
    C --> L[Error Rate]
    
    D --> M[User Satisfaction]
    D --> N[Adoption Rate]
    D --> O[Feature Usage]
    D --> P[Feedback Score]
    
    style E fill:#e1f5fe
    style I fill:#e1f5fe
    style M fill:#e1f5fe
```

### 10.2 Analytics Dashboard

```mermaid
graph LR
    subgraph "Real-time Dashboard"
        A[Current Optimization Status]
        B[Performance Metrics]
        C[Error Alerts]
    end
    
    subgraph "Historical Analytics"
        D[Trend Analysis]
        E[Comparison Reports]
        F[Optimization History]
    end
    
    subgraph "Predictive Analytics"
        G[Performance Prediction]
        H[Resource Planning]
        I[Capacity Forecasting]
    end
    
    A --> D
    B --> E
    C --> F
    
    D --> G
    E --> H
    F --> I
    
    style A fill:#e8eaf6
    style D fill:#fff3e0
    style G fill:#c8e6c9
```

Visualisasi dan diagram ini memberikan pemahaman visual yang komprehensif tentang bagaimana Timetable-SA package bekerja, dari arsitektur tingkat tinggi hingga detail implementasi spesifik. Diagram-diagram ini membantu dalam memahami alur data, interaksi komponen, dan strategi optimasi yang digunakan dalam sistem.