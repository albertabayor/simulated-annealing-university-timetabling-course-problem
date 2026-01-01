/**
 * Move operator: Change room of a random class
 *
 * UPDATED: Temperature-dependent room selection
 * - High temp (>10000): Any valid room (exploration)
 * - Low temp (<1000): Prefer similar capacity rooms (exploitation)
 */

import type { MoveGenerator } from '../../../src/index.js';
import type { TimetableState } from '../types/index.js';
import { isRoomAvailable, canUseExclusiveRoom } from '../utils/index.js';

export class ChangeRoom implements MoveGenerator<TimetableState> {
  name = 'Change Room';

  canApply(state: TimetableState): boolean {
    return state.schedule.length > 0 && state.rooms.length > 0;
  }

  generate(state: TimetableState, temperature: number): TimetableState {
    // SA engine already clones state, so we work directly on the passed state
    if (state.schedule.length === 0 || state.rooms.length === 0) {
      return state;
    }

    // Pick random class
    const randomIndex = Math.floor(Math.random() * state.schedule.length);
    const entry = state.schedule[randomIndex]!;

    // Find current room to get its capacity for comparison
    const currentRoom = state.rooms.find(r => r.Code === entry.room);
    const currentCapacity = currentRoom?.Capacity ?? entry.participants;

    // Filter available rooms (exclude current entry from schedule check)
    const otherSchedule = state.schedule.filter((_, idx) => idx !== randomIndex);

    const availableRooms = state.rooms.filter(room => {
      // Check capacity
      if (room.Capacity < entry.participants) return false;

      // Check exclusive room permissions
      if (!canUseExclusiveRoom(room.Code, entry.className, entry.prodi)) return false;

      // Check if room is available at this time
      if (!isRoomAvailable(otherSchedule, room.Code, entry.timeSlot, entry.sks)) return false;

      // Check lab requirement
      if (entry.needsLab && !room.Type.toLowerCase().includes('lab')) return false;

      return true;
    });

    // If no available rooms, return unchanged state
    if (availableRooms.length === 0) {
      return state;
    }

    let selectedRoom;

    // Temperature-dependent room selection
    if (temperature > 10000) {
      // HIGH TEMPERATURE: Exploration - pick any valid room
      selectedRoom = availableRooms[Math.floor(Math.random() * availableRooms.length)]!;
    } else if (temperature > 1000) {
      // MEDIUM TEMPERATURE: Balanced - slight preference for same type
      const sameTypeRooms = availableRooms.filter(
        r => r.Type === currentRoom?.Type
      );
      if (sameTypeRooms.length > 0 && Math.random() < 0.5) {
        selectedRoom = sameTypeRooms[Math.floor(Math.random() * sameTypeRooms.length)]!;
      } else {
        selectedRoom = availableRooms[Math.floor(Math.random() * availableRooms.length)]!;
      }
    } else {
      // LOW TEMPERATURE: Exploitation - prefer similar capacity rooms (minimize waste)
      const sortedByCapacity = [...availableRooms].sort((a, b) => 
        Math.abs(a.Capacity - entry.participants) - Math.abs(b.Capacity - entry.participants)
      );
      
      // Pick from top 3 best-fit rooms (or less if fewer available)
      const topRooms = sortedByCapacity.slice(0, Math.min(3, sortedByCapacity.length));
      if (Math.random() < 0.8) {
        selectedRoom = topRooms[Math.floor(Math.random() * topRooms.length)]!;
      } else {
        selectedRoom = availableRooms[Math.floor(Math.random() * availableRooms.length)]!;
      }
    }

    // Update room
    entry.room = selectedRoom.Code;

    return state;
  }
}
