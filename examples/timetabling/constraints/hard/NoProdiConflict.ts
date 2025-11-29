/**
 * HC5: No two classes from the same program can be scheduled at the same time
 * (for overlapping class sections like A, AB, B)
 */

import type { Constraint } from 'timetable-sa';
import type { TimetableState, ScheduleEntry } from '../../types/index.js';
import { timeToMinutes, calculateEndTime, hasClassOverlap } from '../../utils/index.js';

export class NoProdiConflict implements Constraint<TimetableState> {
  name = 'No Prodi Conflict';
  type = 'hard' as const;

  evaluate(state: TimetableState): number {
    const { schedule } = state;

    for (let i = 0; i < schedule.length; i++) {
      for (let j = i + 1; j < schedule.length; j++) {
        const entry1 = schedule[i];
        const entry2 = schedule[j];

        if (this.hasProdiConflict(entry1, entry2)) {
          return 0; // Violation found
        }
      }
    }

    return 1; // No violations
  }

  describe(state: TimetableState): string | undefined {
    const { schedule } = state;

    for (let i = 0; i < schedule.length; i++) {
      for (let j = i + 1; j < schedule.length; j++) {
        const entry1 = schedule[i];
        const entry2 = schedule[j];

        if (this.hasProdiConflict(entry1, entry2)) {
          return `Prodi ${entry1.prodi} has overlapping classes ${entry1.classId} (${entry1.class}) and ${entry2.classId} (${entry2.class}) on ${entry1.timeSlot.day}`;
        }
      }
    }

    return undefined;
  }

  private hasProdiConflict(entry1: ScheduleEntry, entry2: ScheduleEntry): boolean {
    // Must be same prodi
    if (entry1.prodi !== entry2.prodi) {
      return false;
    }

    // Must be same day
    if (entry1.timeSlot.day !== entry2.timeSlot.day) {
      return false;
    }

    // Check if class sections overlap (e.g., A overlaps with AB)
    if (!hasClassOverlap(entry1.class, entry2.class)) {
      return false;
    }

    // Check time overlap
    return this.isTimeOverlap(entry1, entry2);
  }

  private isTimeOverlap(entry1: ScheduleEntry, entry2: ScheduleEntry): boolean {
    const calc1 = calculateEndTime(entry1.timeSlot.startTime, entry1.sks, entry1.timeSlot.day);
    const calc2 = calculateEndTime(entry2.timeSlot.startTime, entry2.sks, entry2.timeSlot.day);

    const start1 = timeToMinutes(entry1.timeSlot.startTime);
    const end1 = timeToMinutes(calc1.endTime);
    const start2 = timeToMinutes(entry2.timeSlot.startTime);
    const end2 = timeToMinutes(calc2.endTime);

    return start1 < end2 && start2 < end1;
  }
}
