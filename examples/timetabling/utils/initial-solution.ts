/**
 * Generate initial timetable solution using greedy algorithm
 */

import type { TimetableState, ScheduleEntry, TimetableInput, TimeSlot } from '../types/index.js';
import { TIME_SLOTS_PAGI, TIME_SLOTS_SORE, initializeTimeSlots } from './timeslot-generator.js';

export function generateInitialSolution(data: TimetableInput): TimetableState {
  const { rooms, lecturers, classes } = data;

  // Initialize default time slots
  initializeTimeSlots();

  const schedule: ScheduleEntry[] = [];
  const availableTimeSlots: TimeSlot[] = [...TIME_SLOTS_PAGI, ...TIME_SLOTS_SORE];

  console.log(`\nGenerating initial solution for ${classes.length} classes...`);

  let successCount = 0;
  let failCount = 0;

  for (const classReq of classes) {
    // Extract lecturer codes
    const lecturerCodes: string[] = [];
    if (classReq.Kode_Dosen1) lecturerCodes.push(classReq.Kode_Dosen1);
    if (classReq.Kode_Dosen2) lecturerCodes.push(classReq.Kode_Dosen2);
    if (classReq.Kode_Dosen_Prodi_Lain1) lecturerCodes.push(classReq.Kode_Dosen_Prodi_Lain1);
    if (classReq.Kode_Dosen_Prodi_Lain2) lecturerCodes.push(classReq.Kode_Dosen_Prodi_Lain2);

    if (lecturerCodes.length === 0) {
      console.warn(`  ⚠️  Skipping ${classReq.Kode_Matakuliah}: No lecturers`);
      failCount++;
      continue;
    }

    // Get class properties
    const participants = classReq.Peserta || 30;
    const needsLab = classReq.should_on_the_lab?.toLowerCase() === 'yes';
    const classType = classReq.Class_Type?.toLowerCase() || 'pagi';
    const prodi = classReq.Prodi || 'Unknown';
    const sks = classReq.SKS || 3;

    // Filter time slots
    let slots = classType === 'sore' ? [...TIME_SLOTS_SORE] : [...TIME_SLOTS_PAGI];

    // Filter Saturday for non-Magister Manajemen
    const isMM = prodi.toLowerCase().includes('magister manajemen');
    if (!isMM) {
      slots = slots.filter(s => s.day !== 'Saturday');
    }

    // Try to find a valid slot and room
    let placed = false;

    for (const slot of slots) {
      // Find suitable room
      const suitableRooms = rooms.filter(room => {
        // Check capacity
        if (room.Capacity < participants) return false;

        // Check if lab requirement matches
        if (needsLab && !room.Type.toLowerCase().includes('lab')) return false;

        return true;
      });

      if (suitableRooms.length === 0) continue;

      // Pick first suitable room
      const room = suitableRooms[0];

      // Create schedule entry
      const entry: ScheduleEntry = {
        classId: classReq.Kode_Matakuliah,
        className: classReq.Mata_Kuliah || 'Unknown',
        class: classReq.Kelas || 'A',
        prodi: prodi,
        lecturers: lecturerCodes,
        room: room.Code,
        timeSlot: { ...slot },
        sks: sks,
        needsLab: needsLab,
        participants: participants,
        classType: classType,
        prayerTimeAdded: 0,
        isOverflowToLab: false,
      };

      schedule.push(entry);
      placed = true;
      successCount++;
      break;
    }

    if (!placed) {
      console.warn(`  ⚠️  Could not place ${classReq.Kode_Matakuliah}: ${classReq.Mata_Kuliah}`);
      failCount++;
    }
  }

  console.log(`\n✅ Initial solution generated:`);
  console.log(`   Successfully placed: ${successCount}/${classes.length}`);
  console.log(`   Failed to place: ${failCount}/${classes.length}\n`);

  return {
    schedule,
    availableTimeSlots,
    rooms,
    lecturers,
  };
}
