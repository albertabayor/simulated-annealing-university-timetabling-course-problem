/**
 * Shared helper utilities for constraint evaluation optimization
 * Uses grouping + sorting + short-circuiting pattern for O(N log N) complexity
 */

import type { ScheduleEntry } from '../types/index.js';
import { timeToMinutes, calculateEndTime } from './time.js';

/**
 * Group schedule entries by a key function
 * O(N) complexity
 */
export function groupScheduleByKey<T extends ScheduleEntry>(
  schedule: T[],
  keyFn: (entry: T) => string
): Map<string, T[]> {
  const grouped = new Map<string, T[]>();

  for (const entry of schedule) {
    const key = keyFn(entry);
    if (!grouped.has(key)) {
      grouped.set(key, []);
    }
    grouped.get(key)!.push(entry);
  }

  return grouped;
}

/**
 * Sort entries by start time in place
 * O(K log K) complexity where K is array length
 */
export function sortEntriesByStartTime<T extends ScheduleEntry>(entries: T[]): T[] {
  return entries.sort((a, b) =>
    timeToMinutes(a.timeSlot.startTime) - timeToMinutes(b.timeSlot.startTime)
  );
}

/**
 * Get end time in minutes for an entry (cached via calculateEndTime)
 */
export function getEndTimeInMinutes(entry: ScheduleEntry): number {
  const calc = calculateEndTime(entry.timeSlot.startTime, entry.sks, entry.timeSlot.day);
  return timeToMinutes(calc.endTime);
}

/**
 * Check if two time ranges overlap
 * Returns true if [start1, end1) overlaps with [start2, end2)
 */
export function hasTimeOverlap(
  start1: number,
  end1: number,
  start2: number,
  end2: number
): boolean {
  return start1 < end2 && start2 < end1;
}

/**
 * Check if entry2 starts after entry1 ends (no overlap possible)
 * Used for short-circuiting in sorted arrays
 */
export function startsAfterEnd(entry1End: number, entry2Start: number): boolean {
  return entry1End <= entry2Start;
}
