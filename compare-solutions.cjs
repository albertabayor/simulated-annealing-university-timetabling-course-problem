/**
 * Script to compare initial solution and final result with comprehensive effectiveness metrics
 */

const fs = require('fs');
const path = require('path');

const PRAYER_TIMES = {
  DZUHUR: { start: 704, end: 750, duration: 50 }, // 11:40-12:30 (in minutes)
  ASHAR: { start: 900, end: 930, duration: 30 },  // 15:00-15:30
  MAGHRIB: { start: 1080, end: 1110, duration: 30 } // 18:00-18:30
};

const LAB_ROOMS = [
  "CM-206", "CM-207", "CM-LabVirtual", "CM-Lab3",
  "G5-Lab1", "G5-Lab2", "G5-LabAudioVisual"
];

const DAYS = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'];

function parseArgs() {
  const args = process.argv.slice(2);
  const config = {
    initialFile: 'initial-solution.json',
    finalFile: 'timetable-result.json',
    maxDisplayClasses: 10,
    exportCSV: false,
    exportJSON: false,
    roomCapacities: null
  };

  for (let i = 0; i < args.length; i++) {
    const arg = args[i];
    switch (arg) {
      case '--show-all':
      case '-a':
        config.maxDisplayClasses = Infinity;
        break;
      case '--limit':
      case '-l':
        const limit = parseInt(args[++i], 10);
        if (isNaN(limit) || limit < 0) throw new Error(`Invalid limit value: ${args[i]}`);
        config.maxDisplayClasses = limit === 0 ? Infinity : limit;
        break;
      case '--initial':
      case '-i':
        config.initialFile = args[++i];
        break;
      case '--final':
      case '-f':
        config.finalFile = args[++i];
        break;
      case '--export-csv':
        config.exportCSV = true;
        break;
      case '--export-json':
        config.exportJSON = true;
        break;
      case '--help':
      case '-h':
        console.log(`
Usage: node compare-solutions.cjs [OPTIONS]

Options:
  -a, --show-all          Display all class changes (no limit)
  -l, --limit N           Limit display to N classes (default: 10)
  -i, --initial FILE      Initial solution file (default: initial-solution.json)
  -f, --final FILE        Final solution file (default: timetable-result.json)
  --export-csv            Export results to CSV file
  --export-json           Export results to JSON file
  -h, --help              Show this help message

Examples:
  node compare-solutions.cjs
  node compare-solutions.cjs --show-all
  node compare-solutions.cjs --limit 50 --export-csv
  node compare-solutions.cjs -i custom-initial.json -f custom-final.json
        `);
        process.exit(0);
      default:
        throw new Error(`Unknown argument: ${arg}`);
    }
  }
  return config;
}

const CONFIG = parseArgs();

function readFileSafe(filepath) {
  if (!fs.existsSync(filepath)) throw new Error(`File not found: ${filepath}`);
  try {
    return JSON.parse(fs.readFileSync(filepath, 'utf-8'));
  } catch (err) {
    throw new Error(`Failed to parse ${filepath}: ${err.message}`);
  }
}

function validateSolution(solution, type) {
  if (!solution) throw new Error(`${type} solution is null or undefined`);
  if (type === 'final') {
    if (!Array.isArray(solution.schedule)) throw new Error('Final solution must have schedule array');
    if (typeof solution.fitness !== 'number') throw new Error('Final solution must have fitness value');
  }
}

function timeToMinutes(timeStr) {
  const [hours, minutes] = timeStr.split(':').map(Number);
  return hours * 60 + minutes;
}

function overlapsWithPrayerTime(startTime, endTime) {
  const start = timeToMinutes(startTime);
  const end = timeToMinutes(endTime);

  for (const [name, prayer] of Object.entries(PRAYER_TIMES)) {
    if (start < prayer.end && end > prayer.start) {
      return { name, overlap: Math.min(end, prayer.end) - Math.max(start, prayer.start) };
    }
  }
  return null;
}

function isFriday(timeSlot) {
  return timeSlot.day === 'Friday';
}

function getTimeOfDay(timeStr) {
  const hour = parseInt(timeStr.split(':')[0], 10);
  if (hour < 12) return 'morning';
  if (hour < 15) return 'afternoon';
  return 'evening';
}

function isLabRoom(room) {
  return LAB_ROOMS.includes(room);
}

function calculateRoomCapacityIssue(schedule, roomCapacities = {}) {
  let issues = 0;
  schedule.forEach(cls => {
    const roomCapacity = roomCapacities[cls.room] || 50;
    if (cls.participants > roomCapacity) issues++;
  });
  return issues;
}

function checkRoomTypeMatch(schedule) {
  let mismatched = 0;
  schedule.forEach(cls => {
    const needsLab = cls.needsLab;
    const isLab = isLabRoom(cls.room);
    if (needsLab && !isLab) mismatched++;
    else if (!needsLab && isLab) mismatched++;
  });
  return mismatched;
}

function findConflicts(schedule) {
  const roomConflicts = [];
  const lecturerConflicts = [];

  for (let i = 0; i < schedule.length; i++) {
    for (let j = i + 1; j < schedule.length; j++) {
      const a = schedule[i];
      const b = schedule[j];

      const sameTime = a.timeSlot.day === b.timeSlot.day &&
                       a.timeSlot.startTime === b.timeSlot.startTime;

      if (sameTime) {
        if (a.room === b.room) {
          roomConflicts.push({ a, b });
        }
        if (a.lecturers.some(l => b.lecturers.includes(l))) {
          lecturerConflicts.push({ a, b });
        }
      }
    }
  }

  return { roomConflicts, lecturerConflicts };
}

function calculateDailyDistribution(schedule) {
  const distribution = {};
  schedule.forEach(cls => {
    const day = cls.timeSlot.day;
    distribution[day] = (distribution[day] || 0) + 1;
  });
  return distribution;
}

function calculateTimeOfDayDistribution(schedule) {
  const distribution = { morning: 0, afternoon: 0, evening: 0 };
  schedule.forEach(cls => {
    const timeOfDay = getTimeOfDay(cls.timeSlot.startTime);
    distribution[timeOfDay]++;
  });
  return distribution;
}

function calculateLecturerWorkload(schedule) {
  const workload = {};
  schedule.forEach(cls => {
    cls.lecturers.forEach(lecturer => {
      if (!workload[lecturer]) {
        workload[lecturer] = { total: 0, daily: {} };
      }
      workload[lecturer].total += cls.sks;
      const day = cls.timeSlot.day;
      workload[lecturer].daily[day] = (workload[lecturer].daily[day] || 0) + cls.sks;
    });
  });
  return workload;
}

function calculatePrayerConflicts(schedule) {
  let conflicts = 0;
  schedule.forEach(cls => {
    const overlap = overlapsWithPrayerTime(cls.timeSlot.startTime, cls.timeSlot.endTime);
    if (overlap) conflicts++;
  });
  return conflicts;
}

function calculateFridayClasses(schedule) {
  return schedule.filter(cls => isFriday(cls.timeSlot)).length;
}

function compareTimeSlots(init, fin) {
  return init.timeSlot.day === fin.timeSlot.day &&
         init.timeSlot.startTime === fin.timeSlot.startTime;
}

function compareClasses(init, fin) {
  const timeChanged = !compareTimeSlots(init, fin);
  const roomChanged = init.room !== fin.room;
  return { timeChanged, roomChanged, changed: timeChanged || roomChanged };
}

function buildScheduleMap(schedule) {
  const map = new Map();
  schedule.forEach(cls => map.set(cls.classId, cls));
  return map;
}

function displayComparison(init, fin, comparison) {
  console.log(`   ✓ ${init.classId}:`);
  if (comparison.timeChanged) {
    console.log(`      Time: ${init.timeSlot.day} ${init.timeSlot.startTime} → ${fin.timeSlot.day} ${fin.timeSlot.startTime}`);
  }
  if (comparison.roomChanged) {
    console.log(`      Room: ${init.room} → ${fin.room}`);
  }
}

function calculateConstraintImprovements(initial, final) {
  const improvements = {
    prayerConflicts: { initial: 0, final: 0, resolved: 0 },
    fridayClasses: { initial: 0, final: 0, resolved: 0 },
    roomConflicts: { initial: 0, final: 0, resolved: 0 },
    lecturerConflicts: { initial: 0, final: 0, resolved: 0 },
    roomTypeMismatches: { initial: 0, final: 0, resolved: 0 },
    capacityIssues: { initial: 0, final: 0, resolved: 0 }
  };

  const initialConflicts = findConflicts(initial);
  const finalConflicts = findConflicts(final);

  improvements.prayerConflicts.initial = calculatePrayerConflicts(initial);
  improvements.prayerConflicts.final = calculatePrayerConflicts(final);
  improvements.prayerConflicts.resolved = improvements.prayerConflicts.initial - improvements.prayerConflicts.final;

  improvements.fridayClasses.initial = calculateFridayClasses(initial);
  improvements.fridayClasses.final = calculateFridayClasses(final);

  improvements.roomConflicts.initial = initialConflicts.roomConflicts.length;
  improvements.roomConflicts.final = finalConflicts.roomConflicts.length;
  improvements.roomConflicts.resolved = improvements.roomConflicts.initial - improvements.roomConflicts.final;

  improvements.lecturerConflicts.initial = initialConflicts.lecturerConflicts.length;
  improvements.lecturerConflicts.final = finalConflicts.lecturerConflicts.length;
  improvements.lecturerConflicts.resolved = improvements.lecturerConflicts.initial - improvements.lecturerConflicts.final;

  improvements.roomTypeMismatches.initial = checkRoomTypeMatch(initial);
  improvements.roomTypeMismatches.final = checkRoomTypeMatch(final);
  improvements.roomTypeMismatches.resolved = improvements.roomTypeMismatches.initial - improvements.roomTypeMismatches.final;

  improvements.capacityIssues.initial = calculateRoomCapacityIssue(initial);
  improvements.capacityIssues.final = calculateRoomCapacityIssue(final);
  improvements.capacityIssues.resolved = improvements.capacityIssues.initial - improvements.capacityIssues.final;

  return improvements;
}

function analyzeChanges(initial, finalSchedule) {
  const finalMap = buildScheduleMap(finalSchedule);
  const changes = {
    total: 0,
    timeOnly: 0,
    roomOnly: 0,
    both: 0,
    missing: 0,
    details: []
  };

  initial.forEach(init => {
    const fin = finalMap.get(init.classId);
    if (!fin) {
      changes.missing++;
      return;
    }

    const comparison = compareClasses(init, fin);
    if (comparison.changed) {
      changes.total++;
      if (comparison.timeChanged && comparison.roomChanged) {
        changes.both++;
      } else if (comparison.timeChanged) {
        changes.timeOnly++;
      } else {
        changes.roomOnly++;
      }
      changes.details.push({ init, fin, comparison });
    }
  });

  return changes;
}

function displayMetrics(initial, final) {
  console.log('\n📊 METRICS COMPARISON:');
  console.log(`   Initial classes: ${initial.length}`);
  console.log(`   Final classes: ${final.schedule.length}`);
  console.log(`   Final fitness: ${final.fitness.toFixed(2)}`);
  console.log(`   Hard violations: ${final.hardViolations}`);
  console.log(`   Soft violations: ${final.softViolations}`);
  if (final.iterations) console.log(`   Iterations: ${final.iterations}`);
}

function displayConstraintImprovements(improvements) {
  console.log('\n🎯 CONSTRAINT IMPROVEMENTS:');
  console.log(`   Prayer Time Conflicts: ${improvements.prayerConflicts.initial} → ${improvements.prayerConflicts.final} (${improvements.prayerConflicts.resolved >= 0 ? '+' : ''}${improvements.prayerConflicts.resolved})`);
  console.log(`   Friday Classes: ${improvements.fridayClasses.initial} → ${improvements.fridayClasses.final}`);
  console.log(`   Room Conflicts: ${improvements.roomConflicts.initial} → ${improvements.roomConflicts.final} (${improvements.roomConflicts.resolved >= 0 ? '+' : ''}${improvements.roomConflicts.resolved})`);
  console.log(`   Lecturer Conflicts: ${improvements.lecturerConflicts.initial} → ${improvements.lecturerConflicts.final} (${improvements.lecturerConflicts.resolved >= 0 ? '+' : ''}${improvements.lecturerConflicts.resolved})`);
  console.log(`   Room Type Mismatches: ${improvements.roomTypeMismatches.initial} → ${improvements.roomTypeMismatches.final} (${improvements.roomTypeMismatches.resolved >= 0 ? '+' : ''}${improvements.roomTypeMismatches.resolved})`);
  console.log(`   Capacity Issues: ${improvements.capacityIssues.initial} → ${improvements.capacityIssues.final} (${improvements.capacityIssues.resolved >= 0 ? '+' : ''}${improvements.capacityIssues.resolved})`);
}

function displayTimeSlotQuality(initial, final) {
  console.log('\n⏰ TIME SLOT QUALITY:');

  const initialDist = calculateDailyDistribution(initial);
  const finalDist = calculateDailyDistribution(final.schedule);

  console.log('   Daily Distribution:');
  DAYS.forEach(day => {
    const initCount = initialDist[day] || 0;
    const finalCount = finalDist[day] || 0;
    const diff = finalCount - initCount;
    const arrow = diff > 0 ? '↑' : diff < 0 ? '↓' : '→';
    console.log(`     ${day.padEnd(10)}: ${initCount} → ${finalCount} ${arrow}${Math.abs(diff)}`);
  });

  const initialTimeDist = calculateTimeOfDayDistribution(initial);
  const finalTimeDist = calculateTimeOfDayDistribution(final.schedule);

  console.log('   Time of Day Distribution:');
  ['morning', 'afternoon', 'evening'].forEach(period => {
    const initCount = initialTimeDist[period] || 0;
    const finalCount = finalTimeDist[period] || 0;
    const diff = finalCount - initCount;
    const arrow = diff > 0 ? '↑' : diff < 0 ? '↓' : '→';
    console.log(`     ${period.padEnd(10)}: ${initCount} → ${finalCount} ${arrow}${Math.abs(diff)}`);
  });
}

function displayRoomUtilization(initial, final) {
  console.log('\n🏫 ROOM UTILIZATION:');

  const initialRooms = {};
  const finalRooms = {};

  initial.forEach(cls => {
    initialRooms[cls.room] = (initialRooms[cls.room] || 0) + 1;
  });
  final.schedule.forEach(cls => {
    finalRooms[cls.room] = (finalRooms[cls.room] || 0) + 1;
  });

  const allRooms = new Set([...Object.keys(initialRooms), ...Object.keys(finalRooms)]);
  const roomUsage = [];

  allRooms.forEach(room => {
    const initUsage = initialRooms[room] || 0;
    const finalUsage = finalRooms[room] || 0;
    const diff = finalUsage - initUsage;
    if (Math.abs(diff) > 0) {
      roomUsage.push({ room, initUsage, finalUsage, diff });
    }
  });

  roomUsage.sort((a, b) => Math.abs(b.diff) - Math.abs(a.diff));

  console.log('   Most Changed Rooms (top 10):');
  roomUsage.slice(0, 10).forEach(({ room, initUsage, finalUsage, diff }) => {
    const arrow = diff > 0 ? '↑' : '↓';
    console.log(`     ${room.padEnd(15)}: ${initUsage} → ${finalUsage} ${arrow}${Math.abs(diff)}`);
  });

  const initialLabUsage = initial.filter(cls => isLabRoom(cls.room)).length;
  const finalLabUsage = final.schedule.filter(cls => isLabRoom(cls.room)).length;
  console.log(`   Lab Usage: ${initialLabUsage} → ${finalLabUsage}`);
}

function displayLecturerWorkload(initial, final) {
  console.log('\n👨‍🏫 LECTURER WORKLOAD:');

  const initialWorkload = calculateLecturerWorkload(initial);
  const finalWorkload = calculateLecturerWorkload(final.schedule);

  const allLecturers = new Set([...Object.keys(initialWorkload), ...Object.keys(finalWorkload)]);
  const workloadChanges = [];

  allLecturers.forEach(lecturer => {
    const init = initialWorkload[lecturer]?.total || 0;
    const fin = finalWorkload[lecturer]?.total || 0;
    if (init !== fin) {
      workloadChanges.push({ lecturer, init, fin, diff: fin - init });
    }
  });

  workloadChanges.sort((a, b) => Math.abs(b.diff) - Math.abs(a.diff));

  console.log('   Most Changed Workloads (top 10):');
  workloadChanges.slice(0, 10).forEach(({ lecturer, init, fin, diff }) => {
    const arrow = diff > 0 ? '↑' : '↓';
    console.log(`     ${lecturer.padEnd(5)}: ${init} → ${fin} SKS ${arrow}${Math.abs(diff)}`);
  });

  const totalInit = Object.values(initialWorkload).reduce((sum, w) => sum + w.total, 0);
  const totalFinal = Object.values(finalWorkload).reduce((sum, w) => sum + w.total, 0);
  console.log(`   Total Workload: ${totalInit} → ${totalFinal} SKS`);
}

function displayChanges(changes, totalClasses) {
  const displayLimit = CONFIG.maxDisplayClasses;
  const showAll = displayLimit === Infinity;
  console.log('\n🔍 COMPARING CLASSES:');

  changes.details.slice(0, displayLimit).forEach(({ init, fin, comparison }) => {
    displayComparison(init, fin, comparison);
  });

  if (!showAll && changes.details.length > displayLimit) {
    console.log(`   ... (${changes.details.length - displayLimit} more changes hidden)`);
  }

  console.log(`\n📈 CHANGE BREAKDOWN:`);
  console.log(`   Total changed: ${changes.total}/${totalClasses} (${(changes.total/totalClasses*100).toFixed(1)}%)`);
  console.log(`   - Time only: ${changes.timeOnly}`);
  console.log(`   - Room only: ${changes.roomOnly}`);
  console.log(`   - Both: ${changes.both}`);

  if (changes.missing > 0) {
    console.log(`   ⚠️  Missing in final: ${changes.missing}`);
  }

  const unchanged = totalClasses - changes.total - changes.missing;
  console.log(`   Unchanged: ${unchanged}/${totalClasses} (${(unchanged/totalClasses*100).toFixed(1)}%)`);
}

function displayWarnings(changes, totalClasses, final) {
  console.log('\n🔍 ANALYSIS:');

  if (changes.total === 0) {
    console.log('   ⚠️  WARNING: No changes detected! SA algorithm might not be working properly.');
  } else if (changes.total < totalClasses * 0.1) {
    console.log('   ⚠️  WARNING: Very few changes detected (< 10%). SA might need better parameters.');
  } else if (changes.total > totalClasses * 0.8) {
    console.log('   ℹ️  INFO: Most classes changed (> 80%). Initial solution may need improvement.');
  } else {
    console.log('   ✅ Good! SA algorithm made significant changes to the schedule.');
  }

  if (final.hardViolations > 0) {
    console.log(`   ⚠️  WARNING: ${final.hardViolations} hard violations remain!`);
  } else {
    console.log('   ✅ All hard constraints satisfied!');
  }

  if (final.softViolations === 0) {
    console.log('   ✅ Perfect! No soft violations!');
  }
}

function displayOverallEffectiveness(improvements, final, initial, changes) {
  console.log('\n📊 OVERALL EFFECTIVENESS:');

  const totalResolved = Object.values(improvements).reduce((sum, imp) => {
    return sum + Math.max(0, imp.resolved);
  }, 0);

  const changeRate = changes.total / initial.length;
  const effectiveness = totalResolved > 0 ? (totalResolved * 0.7) + (changeRate * 0.3) : 0;

  let rating = 'Poor';
  if (effectiveness > 0.8) rating = 'Excellent';
  else if (effectiveness > 0.6) rating = 'Good';
  else if (effectiveness > 0.4) rating = 'Fair';

  console.log(`   Total Issues Resolved: ${totalResolved}`);
  console.log(`   Change Rate: ${(changeRate * 100).toFixed(1)}%`);
  console.log(`   Algorithm Rating: ${rating} (${(effectiveness * 100).toFixed(1)}%)`);
}

function exportToCSV(data, filename) {
  const header = Object.keys(data[0]).join(',');
  const rows = data.map(row => Object.values(row).join(',')).join('\n');
  fs.writeFileSync(filename, header + '\n' + rows);
  console.log(`   📄 Exported to ${filename}`);
}

function exportToJSON(data, filename) {
  fs.writeFileSync(filename, JSON.stringify(data, null, 2));
  console.log(`   📄 Exported to ${filename}`);
}

function main() {
  console.log('='.repeat(70));
  console.log('  COMPREHENSIVE SOLUTION COMPARISON');
  console.log('='.repeat(70));

  try {
    const initial = readFileSafe(CONFIG.initialFile);
    const final = readFileSafe(CONFIG.finalFile);

    validateSolution(initial, 'initial');
    validateSolution(final, 'final');

    displayMetrics(initial, final);

    const changes = analyzeChanges(initial, final.schedule);
    displayChanges(changes, initial.length);

    const improvements = calculateConstraintImprovements(initial, final.schedule);
    displayConstraintImprovements(improvements);

    displayTimeSlotQuality(initial, final);
    displayRoomUtilization(initial, final);
    displayLecturerWorkload(initial, final);

    displayWarnings(changes, initial.length, final);
    displayOverallEffectiveness(improvements, final, initial, changes);

    if (CONFIG.exportCSV || CONFIG.exportJSON) {
      console.log('\n📤 EXPORTING RESULTS:');
      const exportData = {
        changes,
        improvements,
        finalFitness: final.fitness,
        finalViolations: { hard: final.hardViolations, soft: final.softViolations }
      };

      if (CONFIG.exportCSV) {
        const csvData = changes.details.map(({ init, fin, comparison }) => ({
          classId: init.classId,
          timeChanged: comparison.timeChanged,
          roomChanged: comparison.roomChanged,
          initialDay: init.timeSlot.day,
          initialTime: init.timeSlot.startTime,
          finalDay: fin.timeSlot.day,
          finalTime: fin.timeSlot.startTime,
          initialRoom: init.room,
          finalRoom: fin.room
        }));
        exportToCSV(csvData, 'comparison-results.csv');
      }

      if (CONFIG.exportJSON) {
        exportToJSON(exportData, 'comparison-results.json');
      }
    }

  } catch (err) {
    console.error(`\n❌ Error: ${err.message}`);
    process.exit(1);
  }

  console.log('\n' + '='.repeat(70));
}

main();
