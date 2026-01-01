/**
 * Move operator: Change both time slot AND room of a random class
 *
 * UPDATED: Temperature-dependent combination selection
 * - High temp (>10000): Any valid combination (exploration)
 * - Medium temp (1000-10000): Prefer different days
 * - Low temp (<1000): Prefer nearby slots and similar rooms (exploitation)
 */

import type { MoveGenerator } from '../../../src/index.js';
import type { TimetableState } from '../types/index.js';
import { getValidTimeSlotAndRoomCombinationsWithPriority, calculateEndTime } from '../utils/index.js';

export class ChangeTimeSlotAndRoom implements MoveGenerator<TimetableState> {
  name = 'Change Time Slot and Room';

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

    // Get ALL valid (time slot, room) combinations
    const { preferred, acceptable, all } = getValidTimeSlotAndRoomCombinationsWithPriority(
      state,
      entry
    );

    const allCombinations = [...preferred, ...acceptable];
    
    if (allCombinations.length === 0 && all.length === 0) {
      return state; // No valid combinations available
    }

    let selectedCombo;

    // Temperature-dependent combination selection
    if (temperature > 10000) {
      // HIGH TEMPERATURE: Exploration - any valid combination
      const pool = allCombinations.length > 0 ? allCombinations : all;
      selectedCombo = pool[Math.floor(Math.random() * pool.length)]!;
    } else if (temperature > 1000) {
      // MEDIUM TEMPERATURE: Prefer different days for diversity
      const differentDayCombos = allCombinations.filter(
        c => c.timeSlot.day !== entry.timeSlot.day
      );
      if (differentDayCombos.length > 0 && Math.random() < 0.7) {
        selectedCombo = differentDayCombos[Math.floor(Math.random() * differentDayCombos.length)]!;
      } else {
        const pool = allCombinations.length > 0 ? allCombinations : all;
        selectedCombo = pool[Math.floor(Math.random() * pool.length)]!;
      }
    } else {
      // LOW TEMPERATURE: Prefer nearby time slots on same day
      const sameDayCombos = allCombinations.filter(
        c => c.timeSlot.day === entry.timeSlot.day
      );
      const nearbyCombos = sameDayCombos.filter(
        c => Math.abs(c.timeSlot.period - entry.timeSlot.period) <= 2
      );

      if (nearbyCombos.length > 0 && Math.random() < 0.7) {
        selectedCombo = nearbyCombos[Math.floor(Math.random() * nearbyCombos.length)]!;
      } else if (sameDayCombos.length > 0 && Math.random() < 0.5) {
        selectedCombo = sameDayCombos[Math.floor(Math.random() * sameDayCombos.length)]!;
      } else if (preferred.length > 0) {
        selectedCombo = preferred[Math.floor(Math.random() * preferred.length)]!;
      } else {
        const pool = allCombinations.length > 0 ? allCombinations : all;
        selectedCombo = pool[Math.floor(Math.random() * pool.length)]!;
      }
    }

    // Calculate prayer time adjustment
    const calc = calculateEndTime(selectedCombo.timeSlot.startTime, entry.sks, selectedCombo.timeSlot.day);

    // Update BOTH time slot AND room
    entry.timeSlot = {
      period: selectedCombo.timeSlot.period,
      day: selectedCombo.timeSlot.day,
      startTime: selectedCombo.timeSlot.startTime,
      endTime: selectedCombo.timeSlot.endTime,
    };
    entry.room = selectedCombo.room;
    entry.prayerTimeAdded = calc.prayerTimeAdded;

    // Update overflow status
    const isLabRoom = selectedCombo.roomType.toLowerCase().includes('lab');
    entry.isOverflowToLab = !entry.needsLab && isLabRoom;

    return state;
  }
}
