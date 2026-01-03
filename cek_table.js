#!/usr/bin/env bun

import fs from "fs";
import path from "path";
import { fileURLToPath } from "url";

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

const jsonPath = path.join(__dirname, "timetable-result.json");
const data = JSON.parse(fs.readFileSync(jsonPath, "utf-8"));

/**
 * Memfilter data kelas berdasarkan multiple criteria
 * @param {Object} data - Data jadwal
 * @param {Object} filters - Filter criteria {room, day, lecturer, class, prodi}
 * @returns {Array<Object>} Array kelas yang sesuai filter
 */
function filterClasses(data, filters) {
  return data.schedule.filter((classItem) => {
    if (filters.room && classItem.room.toLowerCase() !== filters.room.toLowerCase()) {
      return false;
    }
    if (filters.day && classItem.timeSlot.day.toLowerCase() !== filters.day.toLowerCase()) {
      return false;
    }
    if (filters.lecturer && !classItem.lecturers.some(l => l.toLowerCase().includes(filters.lecturer.toLowerCase()))) {
      return false;
    }
    if (filters.class && !classItem.class.toLowerCase().includes(filters.class.toLowerCase())) {
      return false;
    }
    if (filters.prodi && !classItem.prodi.toLowerCase().includes(filters.prodi.toLowerCase())) {
      return false;
    }
    return true;
  });
}

/**
 * Parse command line arguments
 * @returns {Object} Parsed filters
 */
function parseArguments() {
  const args = process.argv.slice(2);
  const filters = {};

  for (let i = 0; i < args.length; i++) {
    const arg = args[i];
    
    if (arg.startsWith("--room=") || arg.startsWith("-r=")) {
      filters.room = arg.split("=")[1];
    } else if (arg.startsWith("--day=") || arg.startsWith("-d=")) {
      filters.day = arg.split("=")[1];
    } else if (arg.startsWith("--lecturer=") || arg.startsWith("-l=")) {
      filters.lecturer = arg.split("=")[1];
    } else if (arg.startsWith("--class=") || arg.startsWith("-c=")) {
      filters.class = arg.split("=")[1];
    } else if (arg.startsWith("--prodi=") || arg.startsWith("-p=")) {
      filters.prodi = arg.split("=")[1];
    } else if (!arg.startsWith("--") && !arg.startsWith("-")) {
      if (!filters.room && !filters.day && !filters.lecturer && !filters.class && !filters.prodi) {
        filters.room = arg;
      }
    }
  }

  return filters;
}

/**
 * Menampilkan pesan help
 */
function showHelp() {
  console.log("\n📋 Penggunaan: bun cek_table.js [OPTIONS]\n");
  console.log("Opsi tersedia:");
  console.log("  -r, --room=<room>      Filter berdasarkan Ruangan");
  console.log("  -d, --day=<day>        Filter berdasarkan Hari (Monday, Tuesday, etc)");
  console.log("  -l, --lecturer=<dosen>  Filter berdasarkan Nama Dosen");
  console.log("  -c, --class=<class>    Filter berdasarkan Class");
  console.log("  -p, --prodi=<prodi>    Filter berdasarkan Program Studi\n");
  console.log("Contoh penggunaan:");
  console.log('  bun cek_table.js --room="CM-201"');
  console.log('  bun cek_table.js --day="Monday"');
  console.log('  bun cek_table.js --lecturer="EMH"');
  console.log('  bun cek_table.js --class="IF-1A"');
  console.log('  bun cek_table.js --prodi="INFORMATIKA"');
  console.log('  bun cek_table.js --room="CM-201" --day="Monday"');
  console.log('  bun cek_table.js -r="CM-201" -d="Monday" -l="TQB"');
  console.log('  bun cek_table.js --room="CM-207" --prodi="INFORMATIKA"\n');
}

/**
 * Generate filter description text
 * @param {Object} filters - Filter criteria
 * @returns {string} Description text
 */
function getFilterDescription(filters) {
  const parts = [];
  if (filters.room) parts.push(`Room: ${filters.room}`);
  if (filters.day) parts.push(`Day: ${filters.day}`);
  if (filters.lecturer) parts.push(`Dosen: ${filters.lecturer}`);
  if (filters.class) parts.push(`Class: ${filters.class}`);
  if (filters.prodi) parts.push(`Prodi: ${filters.prodi}`);
  return parts.join(", ");
}

// Ambil argument dari command line
const filters = parseArguments();

// Check jika tidak ada filter atau minta help
if (process.argv.includes("--help") || process.argv.includes("-h")) {
  showHelp();
  process.exit(0);
}

if (Object.keys(filters).length === 0) {
  console.log("\n⚠️  Tidak ada filter yang diberikan\n");
  showHelp();
  process.exit(1);
}

// Filter data
const filteredData = filterClasses(data, filters);

// Tampilkan hasil
if (filteredData.length === 0) {
  const filterDesc = getFilterDescription(filters);
  console.log(`\n⚠️  Tidak ada data untuk: ${filterDesc}\n`);
} else {
  const filterDesc = getFilterDescription(filters);
  console.log(`\n✅ Ditemukan ${filteredData.length} kelas untuk: ${filterDesc}\n`);
  console.log("=".repeat(100));

  // Sort berdasarkan hari
  const dayOrder = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"];
  filteredData.sort((a, b) => {
    const dayDiff = dayOrder.indexOf(a.timeSlot.day) - dayOrder.indexOf(b.timeSlot.day);
    if (dayDiff !== 0) return dayDiff;
    
    // Jika hari sama, sort berdasarkan waktu mulai
    const timeA = a.timeSlot.startTime.split(":").map(Number);
    const timeB = b.timeSlot.startTime.split(":").map(Number);
    return (timeA[0] * 60 + timeA[1]) - (timeB[0] * 60 + timeB[1]);
  });

  // Group by day
  const groupedByDay = {};
  filteredData.forEach((classItem) => {
    const day = classItem.timeSlot.day;
    if (!groupedByDay[day]) {
      groupedByDay[day] = [];
    }
    groupedByDay[day].push(classItem);
  });

  // Tampilkan hasil per hari
  for (const day of dayOrder) {
    if (!groupedByDay[day]) continue;
    
    const dayClasses = groupedByDay[day];
    console.log(`\n📅 ${day}`);
    console.log("-".repeat(100));

    dayClasses.forEach((classItem, index) => {
      console.log(`\n  📚 ${index + 1}. ${classItem.className}`);
      console.log(`     Class ID     : ${classItem.classId}`);
      console.log(`     Class        : ${classItem.class}`);
      console.log(`     Program      : ${classItem.prodi}`);
      console.log(`     Lecturers    : ${classItem.lecturers.join(", ")}`);
      console.log(`     Room         : ${classItem.room}`);
      console.log(`     Waktu        : ${classItem.timeSlot.startTime} - ${classItem.timeSlot.endTime}`);
      console.log(`     Peserta      : ${classItem.participants} | SKS: ${classItem.sks} | Type: ${classItem.classType}`);
      console.log(`     Lab          : ${classItem.needsLab ? "Ya" : "Tidak"} | Prayer: ${classItem.prayerTimeAdded} min | Overflow: ${classItem.isOverflowToLab ? "Ya" : "Tidak"}`);
    });
  }

  console.log("\n" + "=".repeat(100));
  console.log(`\nTotal: ${filteredData.length} kelas\n`);
}
