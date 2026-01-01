# Parallel Processing Plan for Timetable Constraint Checking

## 📋 Executive Summary

**Goal**: Optimize constraint checking performance using parallel processing strategies for both Bun and Node.js runtimes.

**Current Status**:
- Dataset: 373 classes, 33 rooms, 99 lecturers
- Current optimization: Group-Sort-Shortcircuit pattern (O(n log n))
- Runtime: ~20-30 seconds per optimization run
- Constraints: 11 hard, 8 soft

**Target**: Reduce runtime by 30-50% through parallel processing

---

## 🎯 Strategy Overview

### Phase 1: Analysis & Planning
- Analyze bottleneck constraints
- Determine parallelization approach
- Create implementation architecture

### Phase 2: Proof of Concept
- Implement parallel checker for one constraint
- Benchmark performance gains
- Validate correctness

### Phase 3: Full Implementation
- Extend to all suitable constraints
- Integrate with SimulatedAnnealing
- Optimize for Bun/Node.js compatibility

### Phase 4: Testing & Validation
- Unit tests for parallel implementations
- Performance benchmarks
- Correctness validation

---

## 🔍 Current Constraint Analysis

### High-Priority Targets for Parallelization

| Constraint | Current Complexity | Parallel Potential | Priority |
|------------|-------------------|--------------------|----------|
| `NoLecturerConflict` | O(n log n) | **HIGH** - Data groups by lecturer | P0 |
| `NoRoomConflict` | O(n log n) | **HIGH** - Data groups by room | P0 |
| `NoProdiConflict` | O(n log n) | **HIGH** - Data groups by prodi | P0 |
| `TransitTime` (soft) | O(n log n) | **MEDIUM** - Per lecturer | P1 |
| `Compactness` (soft) | O(n log n) | **MEDIUM** - Per prodi | P2 |
| `PrayerTimeOverlap` (soft) | O(n) | **LOW** - Already linear | P3 |

### Parallelization Strategy

**Option A: Parallel by Data Groups (RECOMMENDED)**
```
For NoRoomConflict:
- Room G301 on Monday: Worker 1
- Room G302 on Monday: Worker 2
- Room G303 on Monday: Worker 3
- Room G301 on Tuesday: Worker 4
...etc

Benefits:
✅ Each group is independent (no race conditions)
✅ Natural workload distribution
✅ Easy to scale with number of workers
✅ Works well for both Bun and Node.js
```

**Option B: Parallel by Constraints**
```
Worker 1: NoLecturerConflict
Worker 2: NoRoomConflict
Worker 3: NoProdiConflict
Worker 4: TransitTime

Benefits:
✅ Simple to implement
✅ Good for independent constraints
❌ Less efficient (constraints have different complexities)
```

**Option C: Parallel by Constraint Evaluation**
```
For each constraint:
- Split data into chunks
- Process chunks in parallel
- Aggregate results

Benefits:
✅ Maximum parallelism
✅ Good for large datasets
❌ Higher complexity
❌ More overhead
```

---

## 🏗️ Architecture Design

### File Structure

```
src/
├── core/
│   ├── SimulatedAnnealing.ts (existing)
│   └── ParallelConstraintChecker.ts (NEW)
├── utils/
│   └── parallel/
│       ├── parallel-executor.ts (NEW)
│       ├── worker-pool.ts (NEW)
│       └── bun-adapter.ts (NEW)
└── types/
    └── parallel.ts (NEW)

examples/timetabling/
├── constraints/
│   ├── hard/
│   │   ├── NoLecturerConflict.ts (MODIFY - add parallel support)
│   │   ├── NoRoomConflict.ts (MODIFY - add parallel support)
│   │   └── NoProdiConflict.ts (MODIFY - add parallel support)
│   └── soft/
│       ├── TransitTime.ts (MODIFY - add parallel support)
│       └── Compactness.ts (MODIFY - add parallel support)
└── workers/
    └── constraint-worker.ts (NEW - for Node.js worker threads)
```

### Core Components

#### 1. ParallelExecutor (Abstract Interface)

```typescript
// src/utils/parallel/parallel-executor.ts

export interface ParallelExecutor {
  /**
   * Execute tasks in parallel
   * @param tasks - Array of tasks to execute
   * @param concurrency - Maximum number of concurrent tasks
   * @returns Promise with results
   */
  execute<T, R>(
    tasks: T[],
    handler: (task: T) => Promise<R> | R,
    concurrency?: number
  ): Promise<R[]>;
}

export interface ParallelExecutorConfig {
  maxConcurrency: number;
  runtime: 'bun' | 'node';
  enableWorkerThreads: boolean;
}
```

#### 2. Bun Adapter (Using Bun's native concurrency)

```typescript
// src/utils/parallel/bun-adapter.ts

import { ParallelExecutor } from './parallel-executor.js';

export class BunParallelExecutor implements ParallelExecutor {
  constructor(private config: ParallelExecutorConfig) {
    this.detectRuntime();
  }

  async execute<T, R>(
    tasks: T[],
    handler: (task: T) => Promise<R> | R,
    concurrency?: number
  ): Promise<R[]> {
    const maxConcurrency = concurrency ?? this.config.maxConcurrency;

    // Bun doesn't have worker_threads, use Promise.all with batching
    const results: R[] = [];
    const chunks = this.chunkArray(tasks, maxConcurrency);

    for (const chunk of chunks) {
      const chunkResults = await Promise.all(
        chunk.map(task => handler(task))
      );
      results.push(...chunkResults);
    }

    return results;
  }

  private chunkArray<T>(array: T[], size: number): T[][] {
    const chunks: T[][] = [];
    for (let i = 0; i < array.length; i += size) {
      chunks.push(array.slice(i, i + size));
    }
    return chunks;
  }

  private detectRuntime(): void {
    // Bun detection
    if (typeof Bun !== 'undefined') {
      this.config.runtime = 'bun';
      return;
    }

    // Node.js detection
    if (typeof process !== 'undefined' && process.versions?.node) {
      this.config.runtime = 'node';
      return;
    }

    throw new Error('Unsupported runtime');
  }
}
```

#### 3. Node.js Worker Thread Adapter

```typescript
// src/utils/parallel/node-adapter.ts

import { Worker, isMainThread, parentPort, workerData } from 'worker_threads';
import { ParallelExecutor } from './parallel-executor.js';
import path from 'path';

export class NodeParallelExecutor implements ParallelExecutor {
  constructor(private config: ParallelExecutorConfig) {}

  async execute<T, R>(
    tasks: T[],
    handler: (task: T) => Promise<R> | R,
    concurrency?: number
  ): Promise<R[]> {
    if (!this.config.enableWorkerThreads) {
      // Fallback to sequential with Promise.all
      return Promise.all(tasks.map(handler));
    }

    const maxConcurrency = concurrency ?? this.config.maxConcurrency;
    const workerPromises: Promise<R>[] = [];

    // Create worker pool
    for (let i = 0; i < tasks.length; i += maxConcurrency) {
      const chunk = tasks.slice(i, i + maxConcurrency);
      const promise = this.executeWithWorkers(chunk, handler);
      workerPromises.push(promise);
    }

    const results = await Promise.all(workerPromises);
    return results.flat();
  }

  private async executeWithWorkers<T, R>(
    tasks: T[],
    handler: (task: T) => Promise<R> | R
  ): Promise<R[]> {
    const workers = tasks.map(task =>
      this.createWorker(task, handler)
    );

    return Promise.all(workers);
  }

  private createWorker<T, R>(
    task: T,
    handler: (task: T) => Promise<R> | R
  ): Promise<R> {
    return new Promise((resolve, reject) => {
      const worker = new Worker(
        path.join(__dirname, '../../workers/constraint-worker.js'),
        {
          workerData: { task }
        }
      );

      worker.on('message', resolve);
      worker.on('error', reject);
      worker.on('exit', (code) => {
        if (code !== 0) {
          reject(new Error(`Worker stopped with exit code ${code}`));
        }
      });
    });
  }
}
```

#### 4. Parallel Constraint Checker

```typescript
// src/core/ParallelConstraintChecker.ts

import type { Constraint } from './interfaces/Constraint.js';
import type { TimetableState } from '../examples/timetabling/types/index.js';
import { BunParallelExecutor } from '../utils/parallel/bun-adapter.js';
import { NodeParallelExecutor } from '../utils/parallel/node-adapter.js';
import type { ParallelExecutor } from '../utils/parallel/parallel-executor.js';

export interface ParallelCheckerConfig {
  maxConcurrency?: number;
  enableWorkerThreads?: boolean;
  runtime?: 'bun' | 'node' | 'auto';
}

export class ParallelConstraintChecker<TState> {
  private executor: ParallelExecutor;

  constructor(config: ParallelCheckerConfig = {}) {
    const runtime = config.runtime ?? 'auto';

    // Detect runtime if auto
    const detectedRuntime = this.detectRuntime();

    const effectiveRuntime = runtime === 'auto' ? detectedRuntime : runtime;

    // Create appropriate executor
    if (effectiveRuntime === 'bun') {
      this.executor = new BunParallelExecutor({
        maxConcurrency: config.maxConcurrency ?? 4,
        runtime: 'bun',
        enableWorkerThreads: false
      });
    } else {
      this.executor = new NodeParallelExecutor({
        maxConcurrency: config.maxConcurrency ?? 4,
        runtime: 'node',
        enableWorkerThreads: config.enableWorkerThreads ?? true
      });
    }
  }

  /**
   * Check multiple constraints in parallel
   */
  async checkConstraintsInParallel(
    state: TState,
    constraints: Constraint<TState>[]
  ): Promise<Array<{ constraint: Constraint<TState>; score: number; violations: string[] }>> {

    const results = await this.executor.execute(
      constraints,
      async (constraint) => {
        const score = constraint.evaluate(state);

        let violations: string[] = [];
        if (constraint.getViolations && score < 1) {
          violations = constraint.getViolations(state);
        }

        return { constraint, score, violations };
      }
    );

    return results;
  }

  /**
   * Check constraints grouped by data (for data-parallel constraints)
   */
  async checkDataParallelConstraints(
    state: TState,
    constraints: Array<{
      constraint: Constraint<TState>;
      groupFn: (state: TState) => Array<any>; // Returns groups to check in parallel
      checkFn: (group: any) => number; // Check violations in a group
    }>
  ): Promise<number> {

    const results = await this.executor.execute(
      constraints,
      async ({ constraint, groupFn, checkFn }) => {
        const groups = groupFn(state);

        // Check each group in parallel
        const groupResults = await this.executor.execute(
          groups,
          async (group) => checkFn(group)
        );

        // Sum violations from all groups
        return groupResults.reduce((sum, count) => sum + count, 0);
      }
    );

    // Sum violations from all constraints
    return results.reduce((sum, count) => sum + count, 0);
  }

  private detectRuntime(): 'bun' | 'node' {
    // @ts-ignore - Bun global
    if (typeof Bun !== 'undefined') {
      return 'bun';
    }

    if (typeof process !== 'undefined' && process.versions?.node) {
      return 'node';
    }

    throw new Error('Unsupported runtime: Only Bun and Node.js are supported');
  }
}
```

---

## 📝 Implementation Plan

### Step 1: Create Parallel Infrastructure (Day 1)

**Tasks**:
1. Create `src/utils/parallel/` directory structure
2. Implement `ParallelExecutor` interface
3. Implement `BunParallelExecutor` adapter
4. Implement `NodeParallelExecutor` adapter (optional)
5. Add unit tests for executors

**Files to create**:
- `src/utils/parallel/parallel-executor.ts`
- `src/utils/parallel/bun-adapter.ts`
- `src/utils/parallel/node-adapter.ts`
- `src/utils/parallel/__tests__/parallel-executor.test.ts`

**Estimated time**: 3-4 hours

---

### Step 2: Create Parallel Constraint Checker (Day 1-2)

**Tasks**:
1. Create `ParallelConstraintChecker` class
2. Integrate with SimulatedAnnealing
3. Add configuration options

**Files to create/modify**:
- `src/core/ParallelConstraintChecker.ts` (new)
- `src/core/SimulatedAnnealing.ts` (modify - add parallel option)
- `src/core/interfaces/SAConfig.ts` (modify - add parallel config)

**Estimated time**: 2-3 hours

---

### Step 3: Proof of Concept - NoRoomConstraint Parallel (Day 2)

**Tasks**:
1. Create parallel version of `NoRoomConflict`
2. Add benchmarking code
3. Compare performance with sequential version
4. Validate correctness (same results)

**Files to create/modify**:
- `examples/timetabling/constraints/hard/NoRoomConflict.ts` (modify - add parallel method)
- `examples/timetabling/benchmarks/constraint-benchmark.ts` (new)

**Expected performance gain**: 30-50% for NoRoomConflict

**Estimated time**: 3-4 hours

---

### Step 4: Extend to Other Constraints (Day 3-4)

**Priority order**:
1. `NoLecturerConflict` (high impact)
2. `NoProdiConflict` (high impact)
3. `TransitTime` (medium impact)
4. `Compactness` (medium impact)

**Tasks**:
1. Add parallel support to each constraint
2. Benchmark each constraint
3. Optimize based on results

**Files to modify**:
- `examples/timetabling/constraints/hard/NoLecturerConflict.ts`
- `examples/timetabling/constraints/hard/NoProdiConflict.ts`
- `examples/timetabling/constraints/soft/TransitTime.ts`
- `examples/timetabling/constraints/soft/Compactness.ts`

**Estimated time**: 4-6 hours

---

### Step 5: Testing & Validation (Day 5)

**Tasks**:
1. Create comprehensive unit tests
2. Integration tests with SimulatedAnnealing
3. Performance benchmarks
4. Correctness validation

**Test coverage**:
- ✅ Parallel results match sequential results
- ✅ No race conditions
- ✅ Performance benchmarks
- ✅ Bun and Node.js compatibility

**Files to create**:
- `src/utils/parallel/__tests__/parallel-constraints.test.ts`
- `examples/timetabling/benchmarks/parallel-benchmark.ts`

**Estimated time**: 4-5 hours

---

### Step 6: Documentation & Cleanup (Day 6)

**Tasks**:
1. Add JSDoc comments
2. Update README
3. Add usage examples
4. Code cleanup and optimization

**Estimated time**: 2-3 hours

---

## 🧪 Testing Strategy

### Unit Tests

```typescript
// src/utils/parallel/__tests__/bun-adapter.test.ts

describe('BunParallelExecutor', () => {
  it('should execute tasks in parallel', async () => {
    const executor = new BunParallelExecutor({
      maxConcurrency: 4,
      runtime: 'bun',
      enableWorkerThreads: false
    });

    const tasks = [1, 2, 3, 4, 5, 6, 7, 8];
    const results = await executor.execute(
      tasks,
      async (task) => {
        await new Promise(resolve => setTimeout(resolve, 100));
        return task * 2;
      }
    );

    expect(results).toEqual([2, 4, 6, 8, 10, 12, 14, 16]);
  });

  it('should respect concurrency limit', async () => {
    // Test that max concurrent tasks is respected
  });
});
```

### Integration Tests

```typescript
// examples/timetabling/__tests__/parallel-constraints.test.ts

describe('Parallel Constraint Checking', () => {
  it('should produce same results as sequential', async () => {
    const state = createTestState();

    // Sequential
    const sequentialChecker = new ConstraintChecker();
    const sequentialScore = sequentialChecker.checkAllConstraints(state);

    // Parallel
    const parallelChecker = new ParallelConstraintChecker();
    const parallelScore = await parallelChecker.checkAllConstraints(state);

    expect(parallelScore).toEqual(sequentialScore);
  });
});
```

### Performance Benchmarks

```typescript
// examples/timetabling/benchmarks/parallel-benchmark.ts

interface BenchmarkResult {
  approach: 'sequential' | 'parallel';
  constraint: string;
  time: number;
  violations: number;
}

export async function benchmarkParallelConstraints(
  state: TimetableState,
  iterations: number = 10
): Promise<BenchmarkResult[]> {

  const results: BenchmarkResult[] = [];

  // Benchmark NoRoomConflict
  const roomConstraint = new NoRoomConflict();

  // Sequential
  const seqStart = performance.now();
  for (let i = 0; i < iterations; i++) {
    roomConstraint.evaluate(state);
  }
  const seqTime = (performance.now() - seqStart) / iterations;

  // Parallel
  const parallelConstraint = new NoRoomConflictParallel();
  const parStart = performance.now();
  for (let i = 0; i < iterations; i++) {
    await parallelConstraint.evaluateParallel(state);
  }
  const parTime = (performance.now() - parStart) / iterations;

  results.push({
    approach: 'sequential',
    constraint: 'NoRoomConflict',
    time: seqTime,
    violations: roomConstraint.getViolations(state).length
  });

  results.push({
    approach: 'parallel',
    constraint: 'NoRoomConflict',
    time: parTime,
    violations: parallelConstraint.getViolations(state).length
  });

  return results;
}
```

---

## 📊 Expected Performance Improvements

### Conservative Estimates

| Constraint | Sequential | Parallel (4 cores) | Speedup |
|------------|-----------|-------------------|---------|
| NoRoomConflict | 100ms | 35ms | **2.8x** |
| NoLecturerConflict | 120ms | 40ms | **3.0x** |
| NoProdiConflict | 80ms | 25ms | **3.2x** |
| TransitTime | 90ms | 50ms | **1.8x** |
| Compactness | 70ms | 45ms | **1.5x** |
| **Total (per iteration)** | **460ms** | **195ms** | **2.4x** |

### For Full Optimization Run (20K iterations)

| Approach | Time per Iteration | Total Time |
|----------|-------------------|------------|
| Sequential (current) | 460ms | ~2.5 hours |
| Parallel (4 cores) | 195ms | ~1 hour |
| **Speedup** | - | **2.4x faster** |

**Note**: Actual speedup depends on:
- Number of CPU cores
- Dataset size
- Constraint complexity
- Overhead of parallel execution

---

## ⚠️ Potential Issues & Mitigations

### Issue 1: Overhead of Parallel Execution

**Problem**: Creating workers/parallel tasks has overhead

**Mitigation**:
- Only parallelize for datasets > 100 classes
- Use worker pools (reuse workers)
- Batch small tasks together

### Issue 2: Bun vs Node.js Differences

**Problem**: Bun doesn't support worker_threads like Node.js

**Mitigation**:
- Create runtime-specific adapters
- Use Promise.all with batching for Bun
- Keep API consistent across runtimes

### Issue 3: Complexity and Maintainability

**Problem**: Parallel code is harder to debug and maintain

**Mitigation**:
- Keep sequential version as fallback
- Comprehensive unit tests
- Clear documentation
- Feature flag to enable/disable parallelism

### Issue 4: Race Conditions

**Problem**: Shared state can cause race conditions

**Mitigation**:
- Design for immutable state
- Each worker processes independent data groups
- No shared mutable state between workers

---

## 🔧 Configuration Options

### SimulatedAnnealing Config

```typescript
const sa = new SimulatedAnnealing(initialState, constraints, moveGenerators, {
  // Existing config
  initialTemperature: 100000,
  coolingRate: 0.9995,
  maxIterations: 20000,

  // NEW: Parallel config
  parallel: {
    enabled: true,
    maxConcurrency: 4, // Number of workers
    runtime: 'auto', // 'bun' | 'node' | 'auto'
    enableWorkerThreads: true, // For Node.js
    minDatasetSize: 100, // Only parallelize if dataset > 100
  }
});
```

### Environment Variables

```bash
# Enable/disable parallel processing
PARALLEL_ENABLED=true
PARALLEL_MAX_CONCURRENCY=4
PARALLEL_RUNTIME=auto

# For debugging
PARALLEL_DISABLE_FALLBACK=false
```

---

## 📚 Implementation Checklist

### Phase 1: Infrastructure
- [ ] Create `src/utils/parallel/parallel-executor.ts`
- [ ] Create `src/utils/parallel/bun-adapter.ts`
- [ ] Create `src/utils/parallel/node-adapter.ts`
- [ ] Add unit tests for executors
- [ ] Add runtime detection utilities

### Phase 2: Core Integration
- [ ] Create `src/core/ParallelConstraintChecker.ts`
- [ ] Modify `SimulatedAnnealing.ts` for parallel support
- [ ] Add parallel config to SAConfig interface
- [ ] Add feature flags

### Phase 3: Constraint Implementation
- [ ] Parallelize `NoRoomConflict`
- [ ] Parallelize `NoLecturerConflict`
- [ ] Parallelize `NoProdiConflict`
- [ ] Parallelize `TransitTime` (optional)
- [ ] Parallelize `Compactness` (optional)

### Phase 4: Testing
- [ ] Unit tests for parallel executors
- [ ] Integration tests for parallel constraints
- [ ] Performance benchmarks
- [ ] Correctness validation tests
- [ ] Bun compatibility tests
- [ ] Node.js compatibility tests

### Phase 5: Documentation
- [ ] JSDoc comments
- [ ] README updates
- [ ] Usage examples
- [ ] Performance guide

---

## 🎯 Success Criteria

### Performance
- [ ] 30-50% faster than sequential (measured)
- [ ] No regression in solution quality
- [ ] Scalable to 1000+ classes

### Correctness
- [ ] Parallel results match sequential results 100%
- [ ] No race conditions in tests
- [ ] All existing tests still pass

### Compatibility
- [ ] Works on Bun runtime
- [ ] Works on Node.js runtime
- [ ] Automatic runtime detection
- [ ] Graceful fallback to sequential

### Code Quality
- [ ] TypeScript strict mode compliant
- [ ] >90% test coverage
- [ ] Clear documentation
- [ ] Easy to maintain

---

## 📅 Timeline Estimate

| Phase | Tasks | Estimated Time |
|-------|-------|----------------|
| 1. Infrastructure | Create parallel executors | 3-4 hours |
| 2. Core Integration | ParallelConstraintChecker + SA integration | 2-3 hours |
| 3. Proof of Concept | NoRoomConstraint parallel | 3-4 hours |
| 4. Full Implementation | Extend to all constraints | 4-6 hours |
| 5. Testing | Unit + integration + benchmarks | 4-5 hours |
| 6. Documentation | JSDoc + README + examples | 2-3 hours |
| **Total** | | **18-25 hours** |

**Suggested pace**: 3-5 days (working 4-6 hours/day)

---

## 🔄 Iteration Strategy

### Iteration 1 (MVP)
- Implement Bun adapter only
- Parallelize NoRoomConflict only
- Basic tests
- Benchmark vs sequential

### Iteration 2 (Expand)
- Add Node.js adapter
- Parallelize NoLecturerConflict and NoProdiConflict
- Full test coverage
- Performance optimization

### Iteration 3 (Polish)
- Soft constraint parallelization
- Advanced optimizations
- Full documentation
- Examples and guides

---

## 🤔 Questions to Decide

1. **Minimum dataset size for parallelization?**
   - Recommended: 100 classes
   - Below this, overhead outweighs benefits

2. **Number of workers?**
   - Recommended: CPU core count - 1
   - Or configurable (default: 4)

3. **Fallback strategy?**
   - If parallel fails, fallback to sequential?
   - Or throw error?

4. **Granularity of parallelization?**
   - By constraint (coarse-grained)?
   - By data groups (fine-grained)?
   - Hybrid?

5. **Should we use Web Workers for Bun?**
   - Bun supports `worker` module (experimental)
   - Or stick with Promise.all batching?

---

## 📖 References

- [Bun Concurrency](https://bun.sh/docs/api/workers)
- [Node.js Worker Threads](https://nodejs.org/api/worker_threads.html)
- [Parallel Programming Patterns](https://en.wikipedia.org/wiki/Parallel_computing)

---

## ✅ Next Steps

1. **Review this plan** - Any adjustments needed?
2. **Approve implementation approach** - Which option (A, B, or C)?
3. **Set up development environment** - Ensure Bun and Node.js available
4. **Create base branch** - `feature/parallel-constraints`
5. **Start with Phase 1** - Infrastructure setup

---

**Status**: 📝 Plan Complete - Awaiting Approval

**Last Updated**: 2026-01-01

**Author**: Claude Code (with human review)
