/**
 * Move operator: Change time slot of a random class
 *
 * UPDATED: Temperature-dependent slot selection
 * - High temp (>10000): Exploration - pick any random valid slot
 * - Medium temp (1000-10000): Balanced - prefer different days
 * - Low temp (<1000): Exploitation - prefer nearby time slots on same day
 */

import type { MoveGenerator } from '../../../src/index.js';

import type { TimetableState } from "../types/index.js";
import { getValidTimeSlotsWithPriority, calculateEndTime } from "../utils/index.js";

export class ChangeTimeSlot implements MoveGenerator<TimetableState> {
  name = "Change Time Slot";

  canApply(state: TimetableState): boolean {
    return state.schedule.length > 0;
  }

  generate(state: TimetableState, temperature: number): TimetableState {
    // SA engine already clones state, so we work directly on the passed state
    if (state.schedule.length === 0) {
      return state;
    }

    // Pick random class
    const randomIndex = Math.floor(Math.random() * state.schedule.length);
    const entry = state.schedule[randomIndex]!;

    // Get constraint-aware valid slots
    const { preferred, acceptable } = getValidTimeSlotsWithPriority(state, entry);
    
    // Combine all available slots
    const allSlots = [...preferred, ...acceptable];
    
    if (allSlots.length === 0) {
      return state; // No valid slots available
    }

    let selectedSlot;

    // Temperature-dependent slot selection
    if (temperature > 10000) {
      // HIGH TEMPERATURE: Exploration mode - pick any random valid slot
      // This allows big jumps across the solution space
      selectedSlot = allSlots[Math.floor(Math.random() * allSlots.length)]!;
    } else if (temperature > 1000) {
      // MEDIUM TEMPERATURE: Balanced - prefer different days for diversity
      const differentDaySlots = allSlots.filter(s => s.day !== entry.timeSlot.day);
      if (differentDaySlots.length > 0 && Math.random() < 0.7) {
        selectedSlot = differentDaySlots[Math.floor(Math.random() * differentDaySlots.length)]!;
      } else {
        selectedSlot = allSlots[Math.floor(Math.random() * allSlots.length)]!;
      }
    } else {
      // LOW TEMPERATURE: Exploitation mode - prefer nearby time slots
      // Look for slots on the same day or adjacent periods
      const sameDaySlots = allSlots.filter(s => s.day === entry.timeSlot.day);
      const nearbySlots = sameDaySlots.filter(s => 
        Math.abs(s.period - entry.timeSlot.period) <= 2
      );
      
      if (nearbySlots.length > 0 && Math.random() < 0.8) {
        selectedSlot = nearbySlots[Math.floor(Math.random() * nearbySlots.length)]!;
      } else if (sameDaySlots.length > 0 && Math.random() < 0.6) {
        selectedSlot = sameDaySlots[Math.floor(Math.random() * sameDaySlots.length)]!;
      } else {
        // Fallback to any valid slot with preference for preferred slots
        selectedSlot = preferred.length > 0 
          ? preferred[Math.floor(Math.random() * preferred.length)]!
          : allSlots[Math.floor(Math.random() * allSlots.length)]!;
      }
    }

    // Calculate prayer time adjustment
    const calc = calculateEndTime(selectedSlot.startTime, entry.sks, selectedSlot.day);

    // Update time slot
    entry.timeSlot = {
      period: selectedSlot.period,
      day: selectedSlot.day,
      startTime: selectedSlot.startTime,
      endTime: selectedSlot.endTime,
    };
    entry.prayerTimeAdded = calc.prayerTimeAdded;

    return state;
  }
}
