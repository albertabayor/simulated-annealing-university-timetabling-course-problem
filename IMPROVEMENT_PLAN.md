---

## Current State Analysis

### Constraint Files (examples/timetabling/constraints/)

#### 🔴 O(N²) Constraints - Require Optimization

| Constraint | File | Problem | Conflict Criteria |
|------------|------|---------|-------------------|
| **NoProdiConflict** | hard/NoProdiConflict.ts:22-31 | Nested loop N² comparisons | Same prodi + overlapping class sections + same day + time overlap |
| **NoLecturerConflict** | hard/NoLecturerConflict.ts:17-26 | Nested loop N² comparisons | Same lecturer + same day + time overlap |
| **NoRoomConflict** | hard/NoRoomConflict.ts:17-26 | Nested loop N² comparisons | Same room + same day + time overlap |

All three use the same inefficient pattern:
```typescript
for (let i = 0; i < schedule.length; i++) {
  for (let j = i + 1; j < schedule.length; j++) {
    // Compare EVERY entry with EVERY other entry
  }
}
```

**Impact:** With N=1000 entries, that's 499,500 comparisons per constraint evaluation. In Simulated Annealing, this runs thousands of times.

---

#### ✅ Already Optimized - No Changes Needed

**O(N) Constraints:**
- RoomCapacity, MaxDailyPeriods, ExclusiveRoom, NoFridayPrayConflict, PreferredRoom, ClassTypeTime, FridayTimeRestriction, PrayerTimeStart, SaturdayRestriction
- These use single loops with O(1) map lookups

**O(N log N) Constraints - Using Correct Pattern:**
- **Compactness** (soft/Compactness.ts:22-42)
  - Groups by `${prodi}-${day}`
  - Sorts by start time
  - Compares consecutive entries
  - Uses short-circuiting

- **TransitTime** (soft/TransitTime.ts:25-69)
  - Groups by day
  - Sorts by start time
  - Filters by lecturer
  - Compares consecutive entries

**Other Soft Constraints:**
- PreferredTime, PreferredRoom, ResearchDay, EveningClassPriority, OverflowPenalty, PrayerTimeOverlap
- Already use O(N) or better patterns

---

## Optimization Strategy

### The Pattern: Grouping + Sorting + Short-circuiting

**Step 1: Group by key** - O(N)
- NoProdiConflict: `${prodi}_${day}`
- NoLecturerConflict: For each lecturer, group by day
- NoRoomConflict: `${room}_${day}`

**Step 2: Sort by time within groups** - O(K log K) where K = group size
- Sort by `timeToMinutes(entry.timeSlot.startTime)`

**Step 3: Compare with short-circuiting** - O(K²) but K is small
- Only compare entries within same group
- Break inner loop when next entry starts after current ends
- Overall complexity: O(N log N)

**Performance Improvement:**
- Before: O(N²) = 1000² = 1,000,000 operations
- After: O(N log N) ≈ 1000 × 10 = 10,000 operations
- **100x faster!**

---

## Implementation Plan

### Phase 1: Create Helper Utilities

Create shared utility functions in `examples/timetabling/utils/`:

1. **`constraint-helpers.ts`**
   - `groupScheduleByKey(schedule, keyFn)` - Groups entries
   - `sortEntriesByTime(entries)` - Sorts by start time
   - `detectOverlaps(entries, conflictCheckFn)` - Detects conflicts with short-circuit

### Phase 2: Optimize Each Constraint

**Priority Order:**

1. **NoRoomConflict** (easiest, single resource type)
   - Group by `${room}_${day}`
   - Sort by time
   - Check overlaps within groups

2. **NoLecturerConflict** (medium, multiple lecturers per class)
   - Group by day first
   - For each lecturer, filter their classes
   - Sort and check overlaps

3. **NoProdiConflict** (most complex, class overlap check needed)
   - Group by `${prodi}_${day}`
   - Sort by time
   - Check class overlap AND time overlap

### Phase 3: Update All Three Methods

Each constraint needs updates to:
- `evaluate(state)` - Calculate violation count efficiently
- `describe(state)` - Return first violation description
- `getViolations(state)` - Return all violations

### Phase 4: Testing & Validation

- Verify same violations are detected as before
- Measure performance improvement
- Ensure correctness with edge cases

---

## Code Template

```typescript
evaluate(state: TimetableState): number {
  const { schedule } = state;
  let violationCount = 0;

  // 1. Group by resource and day (O(N))
  const grouped = new Map<string, ScheduleEntry[]>();
  for (const entry of schedule) {
    const key = `${entry.resource}_${entry.timeSlot.day}`;
    if (!grouped.has(key)) grouped.set(key, []);
    grouped.get(key)!.push(entry);
  }

  // 2. Check conflicts within each group
  for (const entries of grouped.values()) {
    // Sort by start time (O(K log K))
    entries.sort((a, b) =>
      timeToMinutes(a.timeSlot.startTime) - timeToMinutes(b.timeSlot.startTime)
    );

    // Check for overlaps with short-circuit (O(K²))
    for (let i = 0; i < entries.length; i++) {
      for (let j = i + 1; j < entries.length; j++) {
        const entry1 = entries[i];
        const entry2 = entries[j];

        // Check conflict conditions
        if (this.hasConflict(entry1, entry2)) {
          violationCount++;
        } else if (this.getEndTimeInMinutes(entry1) <= 
                   timeToMinutes(entry2.timeSlot.startTime)) {
          // Short-circuit: no more overlaps possible
          break;
        }
      }
    }
  }

  return violationCount === 0 ? 1 : 1 / (1 + violationCount);
}
```

---

## Expected Impact

### Performance Improvements

| Schedule Size | Before (O(N²)) | After (O(N log N)) | Speedup |
|--------------|----------------|-------------------|---------|
| 100 entries | 4,950 ops | ~664 ops | 7.5x |
| 500 entries | 124,750 ops | ~4,483 ops | 28x |
| 1,000 entries | 499,500 ops | ~9,966 ops | 50x |
| 5,000 entries | 12,497,500 ops | ~64,938 ops | 192x |

### SA Algorithm Impact

- **More iterations per second** → Better solution quality
- **Faster convergence** → Reduced runtime
- **Scalable to larger datasets** → Support for bigger institutions

---

## Success Criteria

- [ ] All three constraints optimized to O(N log N)
- [ ] All existing tests pass
- [ ] Performance benchmarks show >10x improvement for N≥500
- [ ] No regression in violation detection accuracy
- [ ] Code follows existing patterns (like Compactness/TransitTime)
- [ ] Documentation updated with complexity analysis