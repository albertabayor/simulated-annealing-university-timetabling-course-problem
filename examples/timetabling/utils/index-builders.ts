/**
 * Index builders for O(1) conflict lookups
 * Pre-builds lookup structures to avoid O(N) searches during move generation
 */

import type { ScheduleEntry } from '../types/index.js';
import { timeToMinutes } from './time.js';

export interface TimeRange {
  start: number;  // minutes from midnight
  end: number;    // minutes from midnight
  entry: ScheduleEntry;
}

export type DayIndex = Map<string, TimeRange[]>;  // day -> sorted list of time ranges

/**
 * Build lecturer-day index for O(1) conflict lookups
 * Key: "lecturerCode_day" -> sorted array of time ranges
 */
export function buildLecturerDayIndex(schedule: ScheduleEntry[]): Map<string, TimeRange[]> {
  const index = new Map<string, TimeRange[]>();
  
  for (const entry of schedule) {
    const start = timeToMinutes(entry.timeSlot.startTime);
    const end = timeToMinutes(entry.timeSlot.endTime);
    const timeRange: TimeRange = { start, end, entry };
    
    for (const lecturer of entry.lecturers) {
      const key = `${lecturer}_${entry.timeSlot.day}`;
      if (!index.has(key)) {
        index.set(key, []);
      }
      index.get(key)!.push(timeRange);
    }
  }
  
  // Sort each group by start time for efficient overlap checking
  for (const ranges of index.values()) {
    ranges.sort((a, b) => a.start - b.start);
  }
  
  return index;
}

/**
 * Build room-day index for O(1) conflict lookups
 * Key: "roomCode_day" -> sorted array of time ranges
 */
export function buildRoomDayIndex(schedule: ScheduleEntry[]): Map<string, TimeRange[]> {
  const index = new Map<string, TimeRange[]>();
  
  for (const entry of schedule) {
    const key = `${entry.room}_${entry.timeSlot.day}`;
    const start = timeToMinutes(entry.timeSlot.startTime);
    const end = timeToMinutes(entry.timeSlot.endTime);
    
    if (!index.has(key)) {
      index.set(key, []);
    }
    index.get(key)!.push({ start, end, entry });
  }
  
  // Sort each group by start time
  for (const ranges of index.values()) {
    ranges.sort((a, b) => a.start - b.start);
  }
  
  return index;
}

/**
 * Build prodi-day index for O(1) conflict lookups
 * Key: "prodi_day" -> sorted array of time ranges
 */
export function buildProdiDayIndex(schedule: ScheduleEntry[]): Map<string, TimeRange[]> {
  const index = new Map<string, TimeRange[]>();
  
  for (const entry of schedule) {
    const key = `${entry.prodi}_${entry.timeSlot.day}`;
    const start = timeToMinutes(entry.timeSlot.startTime);
    const end = timeToMinutes(entry.timeSlot.endTime);
    
    if (!index.has(key)) {
      index.set(key, []);
    }
    index.get(key)!.push({ start, end, entry });
  }
  
  // Sort each group by start time
  for (const ranges of index.values()) {
    ranges.sort((a, b) => a.start - b.start);
  }
  
  return index;
}

/**
 * Check if a time range would conflict with any entry in a sorted list
 * Uses binary search + linear scan for efficiency
 */
export function hasConflictInSortedRanges(
  ranges: TimeRange[] | undefined,
  newStart: number,
  newEnd: number,
  excludeClassId?: string
): boolean {
  if (!ranges || ranges.length === 0) return false;
  
  // Find first range that could possibly overlap (ends after our start)
  // Can use binary search for large lists, but linear is fine for typical sizes
  for (const range of ranges) {
    // Skip the class we're checking for (self)
    if (excludeClassId && range.entry.classId === excludeClassId) continue;
    
    // Short circuit: if range starts after our end, no more overlaps possible
    if (range.start >= newEnd) break;
    
    // Check overlap: range.start < newEnd && range.end > newStart
    if (range.end > newStart) {
      return true;  // Conflict found
    }
  }
  
  return false;
}

/**
 * Find all conflicting entries for a time range in sorted list
 */
export function findConflictsInSortedRanges(
  ranges: TimeRange[] | undefined,
  newStart: number,
  newEnd: number,
  excludeClassId?: string
): ScheduleEntry[] {
  if (!ranges || ranges.length === 0) return [];
  
  const conflicts: ScheduleEntry[] = [];
  
  for (const range of ranges) {
    if (excludeClassId && range.entry.classId === excludeClassId) continue;
    if (range.start >= newEnd) break;
    
    if (range.end > newStart) {
      conflicts.push(range.entry);
    }
  }
  
  return conflicts;
}

/**
 * Combined index container for all indexes
 * Build once, reuse for all checks
 */
export interface ScheduleIndexes {
  lecturerDay: Map<string, TimeRange[]>;
  roomDay: Map<string, TimeRange[]>;
  prodiDay: Map<string, TimeRange[]>;
}

/**
 * Build all indexes at once
 */
export function buildAllIndexes(schedule: ScheduleEntry[]): ScheduleIndexes {
  return {
    lecturerDay: buildLecturerDayIndex(schedule),
    roomDay: buildRoomDayIndex(schedule),
    prodiDay: buildProdiDayIndex(schedule),
  };
}
