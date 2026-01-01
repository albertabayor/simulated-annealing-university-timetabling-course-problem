/**
 * HC5: No two classes from the same program can be scheduled at the same time
 * (for overlapping class sections like A, AB, B)
 * Optimized from O(N²) to O(N log N) using group-sort-shortcircuit pattern
 */

import type { Constraint } from 'timetable-sa';
import type { TimetableState, ScheduleEntry } from '../../types/index.js';
import {
  timeToMinutes,
  hasClassOverlap,
  groupScheduleByKey,
  sortEntriesByStartTime,
  getEndTimeInMinutes,
  startsAfterEnd,
} from '../../utils/index.js';

export class NoProdiConflict implements Constraint<TimetableState> {
  name = 'No Prodi Conflict';
  type = 'hard' as const;

  evaluate(state: TimetableState): number {
    const { schedule } = state;
    let violationCount = 0;

    // Step 1: Group by prodi + day - O(N)
    const grouped = groupScheduleByKey(schedule, (entry) =>
      `${entry.prodi}_${entry.timeSlot.day}`
    );

    // Step 2: Check conflicts within each group
    for (const entries of grouped.values()) {
      if (entries.length < 2) continue;

      // Sort by start time - O(K log K)
      sortEntriesByStartTime(entries);

      // Check for overlaps - O(K²) but K is small (same prodi + same day)
      for (let i = 0; i < entries.length; i++) {
        const entry1 = entries[i];
        const end1 = getEndTimeInMinutes(entry1);

        for (let j = i + 1; j < entries.length; j++) {
          const entry2 = entries[j];
          const start2 = timeToMinutes(entry2.timeSlot.startTime);

          // Short-circuit: if entry2 starts after entry1 ends, no more time overlaps
          if (startsAfterEnd(end1, start2)) {
            break;
          }

          // Check if class sections overlap (A with AB, AB with B, etc.)
          if (hasClassOverlap(entry1.class, entry2.class)) {
            violationCount++;
          }
        }
      }
    }

    if (violationCount === 0) return 1;
    return 1 / (1 + violationCount);
  }

  describe(state: TimetableState): string | undefined {
    const { schedule } = state;

    const grouped = groupScheduleByKey(schedule, (entry) =>
      `${entry.prodi}_${entry.timeSlot.day}`
    );

    for (const entries of grouped.values()) {
      if (entries.length < 2) continue;

      sortEntriesByStartTime(entries);

      for (let i = 0; i < entries.length; i++) {
        const entry1 = entries[i];
        const end1 = getEndTimeInMinutes(entry1);

        for (let j = i + 1; j < entries.length; j++) {
          const entry2 = entries[j];
          const start2 = timeToMinutes(entry2.timeSlot.startTime);

          if (startsAfterEnd(end1, start2)) {
            break;
          }

          if (hasClassOverlap(entry1.class, entry2.class)) {
            return `Prodi ${entry1.prodi} has overlapping classes ${entry1.classId} (${entry1.class}) and ${entry2.classId} (${entry2.class}) on ${entry1.timeSlot.day}`;
          }
        }
      }
    }

    return undefined;
  }

  getViolations(state: TimetableState): string[] {
    const { schedule } = state;
    const violations: string[] = [];

    const grouped = groupScheduleByKey(schedule, (entry) =>
      `${entry.prodi}_${entry.timeSlot.day}`
    );

    for (const entries of grouped.values()) {
      if (entries.length < 2) continue;

      sortEntriesByStartTime(entries);

      for (let i = 0; i < entries.length; i++) {
        const entry1 = entries[i];
        const end1 = getEndTimeInMinutes(entry1);

        for (let j = i + 1; j < entries.length; j++) {
          const entry2 = entries[j];
          const start2 = timeToMinutes(entry2.timeSlot.startTime);

          if (startsAfterEnd(end1, start2)) {
            break;
          }

          if (hasClassOverlap(entry1.class, entry2.class)) {
            violations.push(
              `Prodi ${entry1.prodi} has overlapping classes ${entry1.classId} (${entry1.class}, ${entry1.timeSlot.day} ${entry1.timeSlot.startTime}) and ${entry2.classId} (${entry2.class}, ${entry2.timeSlot.day} ${entry2.timeSlot.startTime})`
            );
          }
        }
      }
    }

    return violations;
  }
}
