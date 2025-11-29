/**
 * HC1: No lecturer can teach two classes at the same time
 */

import type { Constraint } from 'timetable-sa';
import type { TimetableState, ScheduleEntry } from '../../types/index.js';
import { timeToMinutes, calculateEndTime } from '../../utils/index.js';

export class NoLecturerConflict implements Constraint<TimetableState> {
  name = 'No Lecturer Conflict';
  type = 'hard' as const;

  evaluate(state: TimetableState): number {
    const { schedule } = state;

    for (let i = 0; i < schedule.length; i++) {
      for (let j = i + 1; j < schedule.length; j++) {
        const entry1 = schedule[i];
        const entry2 = schedule[j];

        if (this.hasLecturerConflict(entry1, entry2)) {
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

        if (this.hasLecturerConflict(entry1, entry2)) {
          const conflictingLecturer = entry1.lecturers.find(l => entry2.lecturers.includes(l));
          return `Lecturer ${conflictingLecturer} has conflict between ${entry1.classId} and ${entry2.classId} on ${entry1.timeSlot.day}`;
        }
      }
    }

    return undefined;
  }

  private hasLecturerConflict(entry1: ScheduleEntry, entry2: ScheduleEntry): boolean {
    // Must be same day
    if (entry1.timeSlot.day !== entry2.timeSlot.day) {
      return false;
    }

    // Check time overlap
    if (!this.isTimeOverlap(entry1, entry2)) {
      return false;
    }

    // Check if any lecturer is teaching both classes
    for (const lecturer of entry1.lecturers) {
      if (entry2.lecturers.includes(lecturer)) {
        return true;
      }
    }

    return false;
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
