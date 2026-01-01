/**
 * Time calculation utilities - with caching for performance
 */

import { PRAYER_TIMES } from "./prayer-times.js";
import { TimeCache, EndTimeCache, PrayerOverlapCache } from "./cache.js";

/**
 * Convert time string (HH:MM) to minutes from midnight - CACHED
 */
export function timeToMinutes(time: string): number {
  return TimeCache.getMinutes(time);
}

/**
 * Convert minutes from midnight to time string (HH:MM) - CACHED
 */
export function minutesToTime(minutes: number): string {
  return TimeCache.getTimeString(minutes);
}

/**
 * Calculate prayer time overlap for a class session - CACHED
 */
export function getPrayerTimeOverlap(startTime: string, sks: number, day: string): number {
  // Check cache first
  const cached = PrayerOverlapCache.get(startTime, sks, day);
  if (cached !== undefined) {
    return cached;
  }

  // Calculate if not cached
  const startMinutes = TimeCache.getMinutes(startTime);
  const classMinutes = sks * 50;
  const endMinutes = startMinutes + classMinutes;

  let totalPrayerTime = 0;

  // DZUHUR (11:40-12:30): Only add if class significantly overlaps
  if (startMinutes < PRAYER_TIMES.DZUHUR.end && endMinutes > PRAYER_TIMES.DZUHUR.start) {
    if (endMinutes > PRAYER_TIMES.DZUHUR.end) {
      totalPrayerTime += PRAYER_TIMES.DZUHUR.duration;
    }
  }

  // ASHAR (15:00-15:30): Only add if class would span through it
  if (startMinutes < PRAYER_TIMES.ASHAR.end && endMinutes > PRAYER_TIMES.ASHAR.start) {
    if (endMinutes > PRAYER_TIMES.ASHAR.end) {
      totalPrayerTime += PRAYER_TIMES.ASHAR.duration;
    }
  }

  // MAGHRIB (18:00-18:30): Only add if class would span through it
  if (startMinutes < PRAYER_TIMES.MAGHRIB.end && endMinutes > PRAYER_TIMES.MAGHRIB.start) {
    if (endMinutes > PRAYER_TIMES.MAGHRIB.end) {
      totalPrayerTime += PRAYER_TIMES.MAGHRIB.duration;
    }
  }

  // Store in cache
  PrayerOverlapCache.set(startTime, sks, day, totalPrayerTime);

  return totalPrayerTime;
}

/**
 * Calculate end time for a class including prayer time - CACHED
 */
export function calculateEndTime(
  startTime: string,
  sks: number,
  day: string
): { endTime: string; prayerTimeAdded: number } {
  // Check cache first
  const cached = EndTimeCache.get(startTime, sks, day);
  if (cached !== undefined) {
    return cached;
  }

  // Calculate if not cached
  const startMinutes = TimeCache.getMinutes(startTime);
  const classMinutes = sks * 50;
  const prayerTimeAdded = getPrayerTimeOverlap(startTime, sks, day);
  const totalMinutes = classMinutes + prayerTimeAdded;
  const endMinutes = startMinutes + totalMinutes;

  const result = {
    endTime: TimeCache.getTimeString(endMinutes),
    prayerTimeAdded,
  };

  // Store in cache
  EndTimeCache.set(startTime, sks, day, result);

  return result;
}

/**
 * Check if start time is valid for Friday (cannot start at 11:00, 12:00, 13:00)
 */
export function isValidFridayStartTime(startTime: string): boolean {
  // Cannot start at exactly 11:00, 12:00, or 13:00
  // But 13:20, 13:30, etc are OK!
  const prohibited = ['11:00', '11:40', '12:00', '12:30', '13:00'];
  return !prohibited.includes(startTime);
}

/**
 * Check if a class would start during prayer time
 * Classes can start AT the prayer start time (e.g., 18:00) or after prayer end time (e.g., 18:30)
 * But they cannot start DURING prayer time (e.g., 18:15)
 */
export function isStartingDuringPrayerTime(startTime: string): boolean {
  const startMinutes = timeToMinutes(startTime);

  // Check DZUHUR (11:40-12:30): cannot start between 11:40 and 12:30 (exclusive)
  if (startMinutes > PRAYER_TIMES.DZUHUR.start && startMinutes < PRAYER_TIMES.DZUHUR.end) {
    return true;
  }

  // Check ASHAR (15:00-15:30): cannot start between 15:00 and 15:30 (exclusive)
  if (startMinutes > PRAYER_TIMES.ASHAR.start && startMinutes < PRAYER_TIMES.ASHAR.end) {
    return true;
  }

  // Check MAGHRIB (18:00-18:30): cannot start between 18:00 and 18:30 (exclusive)
  if (startMinutes > PRAYER_TIMES.MAGHRIB.start && startMinutes < PRAYER_TIMES.MAGHRIB.end) {
    return true;
  }

  return false;
}
