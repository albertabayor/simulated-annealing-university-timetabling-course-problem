// solve.js
// Minimal Simulated Annealing scheduler for XLSX (hard+soft constraints)
// Run: node solve.js "20180727 Uji Coba Timetable.xlsx"

const fs = require("fs");
const path = require("path");
const XLSX = require("xlsx");

// ====================== CONFIG ======================
const SLOT_MINUTES = 50; // 1 slot = 50 menit (ubah jika 60)
const DAY_LABELS = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]; // Sen–Sab
const START_TIME = "07:30"; // origin
const MAX_SLOTS = 14; // jumlah baris grid
const BIG_M = 1e9; // penalti keras
const STEPS = 120000; // iterasi SA
const COOL_ALPHA = 0.995; // cooling rate
const REPORT_EVERY = 2000;

// Heuristik baca kolom dari Excel (boleh kamu ubah sesuai sheet aslimu)
const SHEET_GUESS_ORDER = ["Courses", "Mata Kuliah", "Matakuliah", "Kuliah", "Sheet1"];
const HEADER_MAP_CANDIDATES = {
  courseId: ["courseId", "kode", "kode mk", "kode_mk", "id", "id mk", "id_mk"],
  name: ["name", "mata kuliah", "matakuliah", "nama mk", "judul", "mk"],
  class: ["class", "kelas", "rombel", "group", "kelompok"],
  lecturer: ["lecturer", "dosen", "pengajar", "nama dosen"],
  roomType: ["roomtype", "tipe ruang", "jenis ruang", "tipe", "lab/teori", "tipe_lab"],
  duration: ["duration", "durasi", "sks", "menit", "lama"],
  capacity: ["capacity", "kapasitas", "kuota", "size"],
  preferredDay: ["preferred day", "prefer day", "hari prefer", "prefer_hari"],
  preferredRoom: ["preferred room", "prefer room", "ruang prefer", "prefer_ruang"],
};

// Opsional: daftar ruang (kalau tidak ada di Excel, kita buat dummy)
const DEFAULT_ROOMS = [
  { id: 1, name: "R101", capacity: 40, type: "theory" },
  { id: 2, name: "R102", capacity: 40, type: "theory" },
  { id: 3, name: "Lab A", capacity: 30, type: "lab" },
  { id: 4, name: "Lab B", capacity: 30, type: "lab" },
];

// ====================== UTIL TIME ======================
function parseHHMM(s) {
  const [hh, mm] = s.split(":").map(Number);
  return hh * 60 + mm;
}
const ORIGIN_MIN = parseHHMM(START_TIME);

function toSlotOffset(hhmm) {
  // "08:20" -> (menit sejak ORIGIN) dibagi 50
  const mins = parseHHMM(hhmm) - ORIGIN_MIN;
  return Math.max(0, Math.round(mins / SLOT_MINUTES));
}
function slotToHHMM(slot) {
  // 1 -> "08:20"
  const mins = ORIGIN_MIN + slot * SLOT_MINUTES;
  const hh = String(Math.floor(mins / 60)).padStart(2, "0");
  const mm = String(mins % 60).padStart(2, "0");
  return `${hh}:${mm}`;
}

// ====================== XLSX PARSER ======================
function pickSheet(wb) {
  // Pilih sheet terbaik berdasar nama yang paling mirip
  const names = wb.SheetNames;
  for (const g of SHEET_GUESS_ORDER) {
    const hit = names.find((n) => n.toLowerCase().includes(g.toLowerCase()));
    if (hit) return hit;
  }
  return names[0];
}
function normalizeKey(k) {
  return String(k).trim().toLowerCase();
}
function findHeaderKey(obj, candidates) {
  const keys = Object.keys(obj).map((k) => normalizeKey(k));
  for (const cand of candidates) {
    const idx = keys.indexOf(cand.toLowerCase());
    if (idx !== -1) return Object.keys(obj)[idx];
  }
  return null;
}

function parseExcel(filePath) {
  const wb = XLSX.readFile(filePath);
  const sheetName = pickSheet(wb);
  const raw = XLSX.utils.sheet_to_json(wb.Sheets[sheetName], { defval: "" });

  if (!raw.length) throw new Error("Sheet kosong / tidak ada data.");

  // Map header dinamis
  const sample = raw[0];
  const headerMap = {};
  for (const [std, cands] of Object.entries(HEADER_MAP_CANDIDATES)) {
    headerMap[std] = findHeaderKey(sample, cands);
  }

  // Bentuk courses
  let nextCourseId = 1;
  const courses = raw
    .map((r) => {
      const name = (headerMap.name ? r[headerMap.name] : r["name"] || r["mk"] || "").toString().trim();
      if (!name) return null;

      const courseId = headerMap.courseId && r[headerMap.courseId] ? r[headerMap.courseId].toString().trim() : String(nextCourseId++);
      const lecturer = headerMap.lecturer && r[headerMap.lecturer] ? String(r[headerMap.lecturer]).trim() : "TBA";
      const group = headerMap.class && r[headerMap.class] ? String(r[headerMap.class]).trim() : "GEN-1";
      const roomType = headerMap.roomType && r[headerMap.roomType] ? (("" + r[headerMap.roomType]).toLowerCase().includes("lab") ? "lab" : "theory") : "theory";
      const capacity = headerMap.capacity && Number(r[headerMap.capacity]) ? Number(r[headerMap.capacity]) : 30;

      // Durasi: dari kolom durasi/menit/sks → konversi ke slots
      let durationSlots = 2; // default 2x50=100 menit
      if (headerMap.duration) {
        const v = String(r[headerMap.duration]).toLowerCase().trim();
        const num = Number(v.replace(/[^0-9.]/g, ""));
        if (!isNaN(num) && num > 0) {
          if (v.includes("sks")) durationSlots = Math.max(1, Math.round((num * 50 * 2) / SLOT_MINUTES)); // 1 SKS tatap muka ~ 100 menit?
          else if (v.includes(":")) {
            // "01:40" format
            const m = v.split(":").map(Number);
            if (m.length === 2) durationSlots = Math.max(1, Math.round((m[0] * 60 + m[1]) / SLOT_MINUTES));
          } else if (num > 10) {
            // menit
            durationSlots = Math.max(1, Math.round(num / SLOT_MINUTES));
          } else {
            // asumsikan num = jumlah slot
            durationSlots = Math.max(1, Math.round(num));
          }
        }
      }

      const preferredDay = headerMap.preferredDay && r[headerMap.preferredDay] ? String(r[headerMap.preferredDay]).trim() : null;
      const preferredRoom = headerMap.preferredRoom && r[headerMap.preferredRoom] ? String(r[headerMap.preferredRoom]).trim() : null;

      return {
        id: courseId,
        name,
        group,
        lecturer,
        roomType,
        capacity,
        durationSlots,
        preferredDay,
        preferredRoom,
      };
    })
    .filter(Boolean);

  // Rooms (kalau sheetRooms ada, kamu bisa perluas; untuk test pakai default)
  const rooms = DEFAULT_ROOMS.map((r, i) => ({ id: i + 1, ...r }));

  return { courses, rooms };
}

// ====================== MODEL & ENERGY ======================
// Representasi sebuah penempatan:
/// { cid, day, start, roomId }
function seedSolution(inst) {
  const { courses, rooms } = inst;
  const rnd = (a, b) => a + Math.floor(Math.random() * (b - a + 1));
  const dayIdx = (d) => {
    if (!d) return rnd(0, DAY_LABELS.length - 1);
    const i = DAY_LABELS.findIndex((x) => x.toLowerCase().startsWith(d.toLowerCase().slice(0, 3)));
    return i >= 0 ? i : rnd(0, DAY_LABELS.length - 1);
  };

  const A = courses.map((c) => {
    const r = rooms.filter((rm) => rm.type === c.roomType && rm.capacity >= c.capacity);
    const room = r.length ? r[rnd(0, r.length - 1)] : rooms[rnd(0, rooms.length - 1)];
    const d = dayIdx(c.preferredDay);
    const maxStart = Math.max(0, MAX_SLOTS - c.durationSlots);
    const start = rnd(0, maxStart);
    return { cid: c.id, day: d, start, roomId: room.id };
  });

  return A;
}

function energy(inst, A) {
  const { courses, rooms } = inst;
  const Cmap = new Map(courses.map((c) => [c.id, c]));

  let hard = 0,
    soft = 0;

  // Index untuk cek bentrok: per day/slot
  // lecturer/day/slot, group/day/slot, room/day/slot occupancy
  const occLec = new Map(); // key `${lec}|${day}|${slot}` -> count
  const occGrp = new Map();
  const occRoom = new Map();

  function count(map, key) {
    map.set(key, (map.get(key) || 0) + 1);
  }

  for (const asg of A) {
    const c = Cmap.get(asg.cid);
    // out-of-bound
    if (asg.start < 0 || asg.start + c.durationSlots > MAX_SLOTS) hard++;

    // room type & capacity
    const room = rooms.find((r) => r.id === asg.roomId);
    if (!room) {
      hard++;
      continue;
    }
    if (room.type !== c.roomType) hard++;
    if (room.capacity < c.capacity) hard++;

    // fill occupancy
    for (let s = asg.start; s < asg.start + c.durationSlots; s++) {
      const k1 = `${c.lecturer}|${asg.day}|${s}`;
      const k2 = `${c.group}|${asg.day}|${s}`;
      const k3 = `${asg.roomId}|${asg.day}|${s}`;
      count(occLec, k1);
      count(occGrp, k2);
      count(occRoom, k3);
    }

    // soft: prefer day
    if (c.preferredDay != null) {
      const pd = DAY_LABELS[asg.day].toLowerCase();
      const want = c.preferredDay.toLowerCase().slice(0, 3);
      if (!pd.startsWith(want)) soft += 20; // tidak sesuai prefer
    }
  }

  // Bentrok = count > 1
  for (const v of occLec.values()) if (v > 1) hard += v - 1;
  for (const v of occGrp.values()) if (v > 1) hard += v - 1;
  for (const v of occRoom.values()) if (v > 1) hard += v - 1;

  // soft: gap per group & per lecturer (kasar)
  // kumpulkan slot aktif per (group, day) dan (lecturer, day)
  function collectGaps(keyMaker) {
    const map = new Map(); // key -> sorted slots
    for (const asg of A) {
      const c = Cmap.get(asg.cid);
      for (let s = asg.start; s < asg.start + c.durationSlots; s++) {
        const k = keyMaker(c, asg);
        const arr = map.get(k) || [];
        arr.push(s);
        map.set(k, arr);
      }
    }
    let g = 0;
    for (const arr of map.values()) {
      arr.sort((a, b) => a - b);
      for (let i = 1; i < arr.length; i++) {
        const gap = arr[i] - arr[i - 1] - 1;
        if (gap > 0) g += gap; // semakin besar gap, semakin jelek
      }
    }
    return g;
  }
  soft += collectGaps((c, asg) => `${c.group}|${asg.day}`) * 2; // gap mahasiswa
  soft += collectGaps((c, asg) => `${c.lecturer}|${asg.day}`) * 1; // gap dosen

  return BIG_M * hard + soft;
}

// Mutasi tetangga
function mutate(inst, A) {
  const { courses, rooms } = inst;
  const Cmap = new Map(inst.courses.map((c) => [c.id, c]));
  const B = A.slice();
  const i = Math.floor(Math.random() * B.length);
  const asg = { ...B[i] };
  const c = Cmap.get(asg.cid);
  const moveType = Math.random();

  if (moveType < 0.34) {
    // pindah hari
    asg.day = Math.floor(Math.random() * DAY_LABELS.length);
  } else if (moveType < 0.68) {
    // pindah start (snap)
    const maxStart = Math.max(0, MAX_SLOTS - c.durationSlots);
    asg.start = Math.floor(Math.random() * (maxStart + 1));
  } else {
    // tukar ruang
    const candidates = rooms.filter((r) => r.type === c.roomType && r.capacity >= c.capacity);
    const r = candidates.length ? candidates[Math.floor(Math.random() * candidates.length)] : rooms[Math.floor(Math.random() * rooms.length)];
    asg.roomId = r.id;
  }

  B[i] = asg;
  return B;
}

async function anneal(inst, seed) {
  let A = seed;
  let E = energy(inst, A);
  let bestA = A,
    bestE = E;

  let T = 1.0;
  for (let k = 1; k <= STEPS; k++) {
    const B = mutate(inst, A);
    const dE = energy(inst, B) - E;
    if (dE <= 0 || Math.random() < Math.exp(-dE / T)) {
      A = B;
      E = E + dE;
      if (E < bestE) {
        bestE = E;
        bestA = A;
      }
    }
    if (k % 500 === 0) T *= COOL_ALPHA;
    if (k % REPORT_EVERY === 0) {
      console.log(`[${k}/${STEPS}] T=${T.toFixed(4)}  E=${E.toFixed(0)}  best=${bestE.toFixed(0)}`);
    }
  }
  return { bestA, bestE };
}

// ====================== MAIN ======================
(async () => {
  try {
    const file = process.argv[2];
    if (!file) {
      console.error('Usage: node solve.js "file.xlsx"');
      process.exit(1);
    }
    const inst = parseExcel(file);
    console.log(`Loaded: ${inst.courses.length} courses, ${inst.rooms.length} rooms`);

    const seed = seedSolution(inst);
    const { bestA, bestE } = await anneal(inst, seed);
    console.log("Best energy:", bestE);

    // Export
    const outDir = path.join(process.cwd(), "out");
    if (!fs.existsSync(outDir)) fs.mkdirSync(outDir);

    // Join detail course
    const Cmap = new Map(inst.courses.map((c) => [c.id, c]));
    const Rmap = new Map(inst.rooms.map((r) => [r.id, r]));
    const rows = bestA.map((a) => {
      const c = Cmap.get(a.cid),
        r = Rmap.get(a.roomId);
      return {
        courseId: c.id,
        name: c.name,
        class: c.group,
        lecturer: c.lecturer,
        room: r ? r.name : a.roomId,
        day: DAY_LABELS[a.day],
        startSlot: a.start,
        endSlot: a.start + c.durationSlots,
        startTime: slotToHHMM(a.start),
        endTime: slotToHHMM(a.start + c.durationSlots),
        durationSlots: c.durationSlots,
        roomType: c.roomType,
        capacityNeed: c.capacity,
      };
    });

    fs.writeFileSync(path.join(outDir, "schedule.json"), JSON.stringify(rows, null, 2));
    // CSV
    const header = Object.keys(rows[0] || {});
    const csv = [header.join(",")].concat(rows.map((r) => header.map((h) => String(r[h]).replace(/,/g, " ")).join(","))).join("\n");
    fs.writeFileSync(path.join(outDir, "schedule.csv"), csv);

    console.log("Written: out/schedule.json & out/schedule.csv");
    console.log("Note: Perkuat kualitas dengan menyesuaikan header & rooms dari Excel aslimu (lihat CONFIG di atas).");
  } catch (e) {
    console.error(e);
    process.exit(1);
  }
})();
