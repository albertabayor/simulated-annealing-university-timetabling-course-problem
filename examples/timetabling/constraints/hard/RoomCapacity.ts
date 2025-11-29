/**
 * HC3: Room capacity must accommodate all participants
 */

import type { Constraint } from 'timetable-sa';
import type { TimetableState } from '../../types/index.js';

export class RoomCapacity implements Constraint<TimetableState> {
  name = 'Room Capacity';
  type = 'hard' as const;

  evaluate(state: TimetableState): number {
    const { schedule, rooms } = state;
    const roomMap = new Map(rooms.map(r => [r.Code, r]));

    for (const entry of schedule) {
      const room = roomMap.get(entry.room);

      if (!room) {
        return 0; // Room not found - violation
      }

      if (room.Capacity < entry.participants) {
        return 0; // Room too small - violation
      }
    }

    return 1; // All rooms have sufficient capacity
  }

  describe(state: TimetableState): string | undefined {
    const { schedule, rooms } = state;
    const roomMap = new Map(rooms.map(r => [r.Code, r]));

    for (const entry of schedule) {
      const room = roomMap.get(entry.room);

      if (!room) {
        return `Room ${entry.room} not found for class ${entry.classId}`;
      }

      if (room.Capacity < entry.participants) {
        return `Room ${entry.room} capacity (${room.Capacity}) is less than participants (${entry.participants}) for class ${entry.classId}`;
      }
    }

    return undefined;
  }
}
