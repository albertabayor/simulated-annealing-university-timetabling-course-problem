/**
 * Move operator: Change time slot of a random class
 */

import type { MoveGenerator } from 'timetable-sa';
import type { TimetableState } from '../types/index.js';
import { TIME_SLOTS_PAGI, TIME_SLOTS_SORE } from '../utils/index.js';

export class ChangeTimeSlot implements MoveGenerator<TimetableState> {
  name = 'Change Time Slot';

  canApply(state: TimetableState): boolean {
    return state.schedule.length > 0 && state.availableTimeSlots.length > 0;
  }

  generate(state: TimetableState, temperature: number): TimetableState {
    // Clone state
    const newState = JSON.parse(JSON.stringify(state)) as TimetableState;

    if (newState.schedule.length === 0) {
      return newState;
    }

    // Pick random class
    const randomIndex = Math.floor(Math.random() * newState.schedule.length);
    const entry = newState.schedule[randomIndex];

    // Get available time slots based on class type
    let availableSlots = entry.classType === 'sore'
      ? TIME_SLOTS_SORE.filter(s => s.day !== 'Saturday' || entry.prodi.toLowerCase().includes('magister manajemen'))
      : TIME_SLOTS_PAGI.filter(s => s.day !== 'Saturday' || entry.prodi.toLowerCase().includes('magister manajemen'));

    if (availableSlots.length === 0) {
      return newState;
    }

    // Pick random time slot
    const newSlot = availableSlots[Math.floor(Math.random() * availableSlots.length)];

    // Update time slot
    entry.timeSlot = { ...newSlot };

    return newState;
  }
}
