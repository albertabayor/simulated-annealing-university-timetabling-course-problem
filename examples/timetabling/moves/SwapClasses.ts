/**
 * Move operator: Swap time slots and/or rooms between two classes
 *
 * UPDATED: Temperature-dependent swap behavior
 * - High temp (>10000): Prefer full swaps (both time+room) for exploration
 * - Low temp (<1000): Prefer targeted swaps (just time OR room) for exploitation
 */

import type { MoveGenerator } from '../../../src/index.js';
import type { TimetableState } from '../types/index.js';
import { calculateEndTime } from '../utils/index.js';

export class SwapClasses implements MoveGenerator<TimetableState> {
  name = 'Swap Classes';

  canApply(state: TimetableState): boolean {
    return state.schedule.length >= 2;
  }

  generate(state: TimetableState, temperature: number): TimetableState {
    // SA engine already clones state, so we work directly on the passed state
    if (state.schedule.length < 2) {
      return state;
    }

    // Pick two random classes
    const idx1 = Math.floor(Math.random() * state.schedule.length);
    let idx2 = Math.floor(Math.random() * state.schedule.length);

    while (idx2 === idx1) {
      idx2 = Math.floor(Math.random() * state.schedule.length);
    }

    const entry1 = state.schedule[idx1]!;
    const entry2 = state.schedule[idx2]!;

    // Temperature-dependent swap type selection
    let swapType: 'time' | 'room' | 'both';
    
    if (temperature > 10000) {
      // HIGH TEMPERATURE: Prefer full swaps for maximum exploration
      const rand = Math.random();
      if (rand < 0.5) {
        swapType = 'both';  // 50% full swap
      } else if (rand < 0.75) {
        swapType = 'time';  // 25% time only
      } else {
        swapType = 'room';  // 25% room only
      }
    } else if (temperature > 1000) {
      // MEDIUM TEMPERATURE: Balanced
      const rand = Math.random();
      if (rand < 0.33) {
        swapType = 'both';
      } else if (rand < 0.66) {
        swapType = 'time';
      } else {
        swapType = 'room';
      }
    } else {
      // LOW TEMPERATURE: Prefer targeted swaps for fine-tuning
      const rand = Math.random();
      if (rand < 0.2) {
        swapType = 'both';  // 20% full swap
      } else if (rand < 0.6) {
        swapType = 'time';  // 40% time only (more precise)
      } else {
        swapType = 'room';  // 40% room only (more precise)
      }
    }

    if (swapType === 'time' || swapType === 'both') {
      // Swap time slots
      const tempTimeSlot = { ...entry1.timeSlot };
      entry1.timeSlot = { ...entry2.timeSlot };
      entry2.timeSlot = tempTimeSlot;

      // Recalculate end times based on each class's SKS
      const calc1 = calculateEndTime(entry1.timeSlot.startTime, entry1.sks, entry1.timeSlot.day);
      const calc2 = calculateEndTime(entry2.timeSlot.startTime, entry2.sks, entry2.timeSlot.day);

      entry1.timeSlot.endTime = calc1.endTime;
      entry1.prayerTimeAdded = calc1.prayerTimeAdded;

      entry2.timeSlot.endTime = calc2.endTime;
      entry2.prayerTimeAdded = calc2.prayerTimeAdded;
    }

    if (swapType === 'room' || swapType === 'both') {
      // Swap rooms
      const tempRoom = entry1.room;
      entry1.room = entry2.room;
      entry2.room = tempRoom;
    }

    return state;
  }
}
