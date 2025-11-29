/**
 * Move operator: Change room of a random class
 */

import type { MoveGenerator } from 'timetable-sa';
import type { TimetableState } from '../types/index.js';

export class ChangeRoom implements MoveGenerator<TimetableState> {
  name = 'Change Room';

  canApply(state: TimetableState): boolean {
    return state.schedule.length > 0 && state.rooms.length > 0;
  }

  generate(state: TimetableState, temperature: number): TimetableState {
    // Clone state
    const newState = JSON.parse(JSON.stringify(state)) as TimetableState;

    if (newState.schedule.length === 0 || newState.rooms.length === 0) {
      return newState;
    }

    // Pick random class
    const randomIndex = Math.floor(Math.random() * newState.schedule.length);
    const entry = newState.schedule[randomIndex];

    // Pick random room
    const newRoom = newState.rooms[Math.floor(Math.random() * newState.rooms.length)];

    // Update room
    entry.room = newRoom.Code;

    return newState;
  }
}
