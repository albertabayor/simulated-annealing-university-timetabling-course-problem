#!/usr/bin/env bun
import * as fs from 'fs';
import * as path from 'path';
import * as readline from 'readline';

interface TimeSlot {
  period: number;
  day: string;
  startTime: string;
  endTime: string;
}

interface ClassSchedule {
  classId: string;
  className: string;
  class: string;
  prodi: string;
  lecturers: string[];
  room: string;
  timeSlot: TimeSlot;
  sks: number;
  needsLab: boolean;
  participants: number;
  classType: string;
  prayerTimeAdded: number;
  isOverflowToLab: boolean;
}

interface TimetableResult {
  fitness: number;
  hardViolations: number;
  softViolations: number;
  iterations: number;
  schedule: ClassSchedule[];
}

const DAYS = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'];
const DAY_NAMES = {
  'Monday': 'Senin',
  'Tuesday': 'Selasa',
  'Wednesday': 'Rabu',
  'Thursday': 'Kamis',
  'Friday': 'Jumat',
  'Saturday': 'Sabtu'
};

class TimetableViewer {
  private data: TimetableResult;
  private filteredSchedule: ClassSchedule[];

  constructor(filePath: string) {
    const content = fs.readFileSync(filePath, 'utf-8');
    this.data = JSON.parse(content);
    this.data.schedule = this.data.schedule.map(item => this.sanitizeScheduleItem(item));
    this.filteredSchedule = this.data.schedule;
  }

  private padCenter(text: string, width: number): string {
    const padding = Math.max(0, width - text.length);
    const leftPad = Math.floor(padding / 2);
    const rightPad = padding - leftPad;
    return ' '.repeat(leftPad) + text + ' '.repeat(rightPad);
  }

  private padLeft(text: string, width: number): string {
    return text.padStart(width);
  }

  private padRight(text: string, width: number): string {
    return text.padEnd(width);
  }

  private truncate(text: string, maxWidth: number): string {
    if (text.length <= maxWidth) return text;
    return text.substring(0, maxWidth - 3) + '...';
  }

  private printBox(content: string[]): void {
    const maxLength = Math.max(...content.map(line => line.length));
    const border = '═'.repeat(maxLength + 4);

    console.log('╔' + border + '╗');
    for (const line of content) {
      console.log('║ ' + this.padRight(line, maxLength) + ' ║');
    }
    console.log('╚' + border + '╝');
  }

  private printHeader(title: string): void {
    const width = Math.min(title.length + 10, 100);
    const border = '═'.repeat(width);
    const centeredTitle = this.padCenter(title, width);

    console.log('\n' + '╔' + border + '╗');
    console.log('║' + centeredTitle + '║');
    console.log('╚' + border + '╝\n');
  }

  private printSummary(): void {
    const summary = [
      `Fitness: ${this.data.fitness.toFixed(2)}`,
      `Hard Violations: ${this.data.hardViolations}`,
      `Soft Violations: ${this.data.softViolations}`,
      `Iterations: ${this.data.iterations}`,
      `Total Classes: ${this.filteredSchedule.length}/${this.data.schedule.length}`
    ];

    this.printBox(summary);
    console.log();
  }

  private getClassesByDay(): Map<string, ClassSchedule[]> {
    const byDay = new Map<string, ClassSchedule[]>();
    DAYS.forEach(day => byDay.set(day, []));

    for (const item of this.filteredSchedule) {
      const day = item.timeSlot.day;
      if (byDay.has(day)) {
        byDay.get(day)!.push(item);
      }
    }

    for (const day of byDay.keys()) {
      byDay.set(day, byDay.get(day)!.sort((a, b) => 
        a.timeSlot.startTime.localeCompare(b.timeSlot.startTime)
      ));
    }

    return byDay;
  }

  private getUniqueRooms(): string[] {
    const rooms = new Set(this.filteredSchedule.map(item => item.room));
    return Array.from(rooms).sort();
  }

  private formatCard(item: ClassSchedule, maxWidth: number = 40): string[] {
    const lines: string[] = [];
    
    lines.push(`┌${'─'.repeat(maxWidth)}┐`);
    
    const title = this.truncate(item.className, maxWidth - 2);
    lines.push(`│ ${this.padCenter(title, maxWidth - 4)} │`);
    lines.push(`├${'─'.repeat(maxWidth)}┤`);
    
    lines.push(`│ ID: ${this.truncate(item.classId, maxWidth - 7)} │`);
    
    const classInfo = `Class: ${item.class}`;
    lines.push(`│ ${this.truncate(classInfo, maxWidth - 2)} │`);
    
    const timeInfo = `${item.timeSlot.startTime} - ${item.timeSlot.endTime}`;
    lines.push(`│ ${this.padLeft('Time:', 10)} ${this.truncate(timeInfo, maxWidth - 13)} │`);
    
    const lecturers = item.lecturers.join(', ');
    const lecturerInfo = `Dosen: ${this.truncate(lecturers, maxWidth - 8)}`;
    lines.push(`│ ${this.truncate(lecturerInfo, maxWidth - 2)} │`);
    
    lines.push(`└${'─'.repeat(maxWidth)}┘`);
    
    return lines;
  }

  private sanitizeString(str: string): string {
    return str.replace(/\r\n/g, ' ').replace(/\n/g, ' ').replace(/\r/g, ' ').trim();
  }

  private sanitizeScheduleItem(item: ClassSchedule): ClassSchedule {
    return {
      ...item,
      classId: this.sanitizeString(item.classId),
      className: this.sanitizeString(item.className),
      class: this.sanitizeString(item.class),
      prodi: this.sanitizeString(item.prodi),
      room: this.sanitizeString(item.room),
      lecturers: item.lecturers.map(l => this.sanitizeString(l))
    };
  }

  private displayDayView(): void {
    const byDay = this.getClassesByDay();

    for (const day of DAYS) {
      const classes = byDay.get(day) || [];
      if (classes.length === 0) continue;

      this.printHeader(`${DAY_NAMES[day as keyof typeof DAY_NAMES]} (${day})`);

      const timeGroups = new Map<string, ClassSchedule[]>();
      for (const item of classes) {
        const timeKey = `${item.timeSlot.startTime}-${item.timeSlot.endTime}`;
        if (!timeGroups.has(timeKey)) {
          timeGroups.set(timeKey, []);
        }
        timeGroups.get(timeKey)!.push(item);
      }

      const sortedTimes = Array.from(timeGroups.keys()).sort();

      for (const time of sortedTimes) {
        const timeClasses = timeGroups.get(time)!;
        
        const [startTime, endTime] = time.split('-');
        const boxWidth = 80;
        console.log(`\n${'='.repeat(boxWidth)}`);
        console.log(`⏰ ${startTime} - ${endTime}`);
        console.log(`${'='.repeat(boxWidth)}`);

        timeClasses.forEach((item, idx) => {
          const boxWidth = 80;
          const roomDisplay = item.room.substring(0, 18);
          const roomLine = `─ Room: ${roomDisplay}─`;
          const topBorder = `┌${roomLine}${'─'.repeat(boxWidth - roomLine.length - 2)}┐`;
          
          console.log(`\n${topBorder}`);
          
          const padding = '│ ';
          const valueMaxLen = boxWidth - 20;
          
          console.log(`${padding}Mata Kuliah  : ${this.truncate(item.className, valueMaxLen)}`);
          console.log(`${padding}ID           : ${this.truncate(item.classId, valueMaxLen)}`);
          console.log(`${padding}Class        : ${this.truncate(item.class, valueMaxLen)}`);
          console.log(`${padding}Program Studi : ${this.truncate(item.prodi, valueMaxLen)}`);
          console.log(`${padding}Dosen         : ${this.truncate(item.lecturers.join(', '), valueMaxLen)}`);
          console.log(`${padding}SKS          : ${item.sks}`);
          console.log(`${padding}Peserta      : ${item.participants}`);
          console.log(`${padding}Type         : ${item.classType}`);
          console.log(`${padding}Lab          : ${item.needsLab ? 'Ya' : 'Tidak'}`);
          console.log(`${padding}Prayer Time   : ${item.prayerTimeAdded} min`);
          console.log(`${padding}Overflow Lab  : ${item.isOverflowToLab ? 'Ya' : 'Tidak'}`);
          
          console.log(`└${'─'.repeat(boxWidth - 2)}┘`);
        });
      }

      console.log('\n');
    }
  }

  private displayCompactView(): void {
    const byDay = this.getClassesByDay();

    for (const day of DAYS) {
      const classes = byDay.get(day) || [];
      if (classes.length === 0) continue;

      this.printHeader(`${DAY_NAMES[day as keyof typeof DAY_NAMES]} (${day})`);

      const headers = ['Time', 'Room', 'Class ID', 'Class Name', 'Prodi', 'Class', 'SKS', 'Type', 'Part', 'Lab', 'Lecturers'];
      const widths = [13, 12, 10, 25, 20, 12, 4, 6, 4, 4, 20];
      const separator = '─';

      const headerLine = headers.map((h, i) => this.padCenter(h, widths[i])).join('│');
      console.log(headerLine);
      console.log(headers.map((_, i) => separator.repeat(widths[i])).join('─'));

      for (const item of classes) {
        const time = `${item.timeSlot.startTime}-${item.timeSlot.endTime}`;
        const lecturers = item.lecturers.join(', ').substring(0, 18);
        
        const row = [
          this.padCenter(time, widths[0]),
          this.padCenter(this.truncate(item.room, widths[1]), widths[1]),
          this.padCenter(this.truncate(item.classId, widths[2]), widths[2]),
          this.padCenter(this.truncate(item.className, widths[3] - 2), widths[3]),
          this.padCenter(this.truncate(item.prodi, widths[4] - 2), widths[4]),
          this.padCenter(this.truncate(item.class, widths[5] - 2), widths[5]),
          this.padCenter(item.sks.toString(), widths[6]),
          this.padCenter(item.classType, widths[7]),
          this.padCenter(item.participants.toString(), widths[8]),
          this.padCenter(item.needsLab ? 'Y' : 'N', widths[9]),
          this.padCenter(this.truncate(lecturers, widths[10] - 2), widths[10])
        ];

        console.log(row.join('│'));
      }

      console.log('\n');
    }
  }

  private searchByClassId(classId: string): ClassSchedule[] {
    const upperQuery = classId.toUpperCase();
    return this.data.schedule.filter(item => 
      item.classId.toUpperCase().includes(upperQuery)
    );
  }

  private filterByProdi(prodi: string): ClassSchedule[] {
    const upperQuery = prodi.toUpperCase();
    return this.data.schedule.filter(item => 
      item.prodi.toUpperCase().includes(upperQuery)
    );
  }

  private filterByClass(className: string): ClassSchedule[] {
    const upperQuery = className.toUpperCase();
    return this.data.schedule.filter(item => 
      item.class.toUpperCase().includes(upperQuery)
    );
  }

  private filterByLecturer(lecturer: string): ClassSchedule[] {
    const upperQuery = lecturer.toUpperCase();
    return this.data.schedule.filter(item => 
      item.lecturers.some(l => l.toUpperCase().includes(upperQuery))
    );
  }

  private filterByRoom(room: string): ClassSchedule[] {
    const upperQuery = room.toUpperCase();
    return this.data.schedule.filter(item => 
      item.room.toUpperCase().includes(upperQuery)
    );
  }

  private displaySearchResults(results: ClassSchedule[], query: string): void {
    if (results.length === 0) {
      this.printBox([`Tidak ditemukan hasil untuk: "${query}"`]);
      return;
    }

    this.printHeader(`Hasil Pencarian: "${query}" (${results.length} hasil)`);

    const headers = ['Day', 'Time', 'Room', 'Class ID', 'Class Name', 'Prodi', 'Class', 'SKS', 'Type', 'Part', 'Lab', 'Lecturers'];
    const widths = [10, 13, 12, 10, 25, 18, 12, 4, 6, 4, 4, 18];

    const headerLine = headers.map((h, i) => this.padCenter(h, widths[i])).join('│');
    console.log(headerLine);
    console.log(headers.map((_, i) => '─'.repeat(widths[i])).join('─'));

    for (const item of results) {
      const time = `${item.timeSlot.startTime}-${item.timeSlot.endTime}`;
      const lecturers = item.lecturers.join(', ').substring(0, 16);

      const row = [
        this.padCenter(this.truncate(item.timeSlot.day, widths[0]), widths[0]),
        this.padCenter(time, widths[1]),
        this.padCenter(this.truncate(item.room, widths[1]), widths[2]),
        this.padCenter(this.truncate(item.classId, widths[2]), widths[3]),
        this.padCenter(this.truncate(item.className, widths[3] - 2), widths[4]),
        this.padCenter(this.truncate(item.prodi, widths[4] - 2), widths[5]),
        this.padCenter(this.truncate(item.class, widths[5] - 2), widths[6]),
        this.padCenter(item.sks.toString(), widths[7]),
        this.padCenter(item.classType, widths[8]),
        this.padCenter(item.participants.toString(), widths[9]),
        this.padCenter(item.needsLab ? 'Y' : 'N', widths[10]),
        this.padCenter(this.truncate(lecturers, widths[10] - 2), widths[11])
      ];

      console.log(row.join('│'));
    }

    console.log('\n');
  }

  private showAvailableFilters(): void {
    const filters = [
      'Program Studi: ' + Array.from(new Set(this.data.schedule.map(s => s.prodi))).sort().join(', '),
      'Class: ' + Array.from(new Set(this.data.schedule.map(s => s.class))).sort().slice(0, 10).join(', ') + '...',
      'Rooms: ' + Array.from(new Set(this.data.schedule.map(s => s.room))).sort().slice(0, 10).join(', ') + '...',
    ];

    this.printBox(filters);
  }

  private showMainMenu(): void {
    console.clear();
    this.printHeader('📊 JADWAL KULIAH - TIMETABLE VIEWER');
    this.printSummary();

    console.log('Menu Utama:');
    console.log('1. Tampilkan semua jadwal (Tabel Lengkap)');
    console.log('2. Tampilkan semua jadwal (Tampilan Ringkas)');
    console.log('3. Cari berdasarkan Class ID');
    console.log('4. Filter berdasarkan Program Studi');
    console.log('5. Filter berdasarkan Class');
    console.log('6. Filter berdasarkan Lecturer');
    console.log('7. Filter berdasarkan Room');
    console.log('8. Lihat opsi filter tersedia');
    console.log('9. Reset filter');
    console.log('0. Keluar');
    console.log();
  }

  private askQuestion(prompt: string): Promise<string> {
    const rl = readline.createInterface({
      input: process.stdin,
      output: process.stdout
    });

    return new Promise(resolve => {
      rl.question(prompt, answer => {
        rl.close();
        resolve(answer);
      });
    });
  }

  private async waitForEnter(): Promise<void> {
    await this.askQuestion('\nTekan Enter untuk melanjutkan...');
  }

  public async run(): Promise<void> {
    while (true) {
      this.showMainMenu();
      const choice = await this.askQuestion('Pilih menu (0-9): ');

      console.clear();

      switch (choice.trim()) {
        case '1':
          this.printHeader('JADWAL KULIAH - TAMPILAN LENGKAP');
          this.displayDayView();
          await this.waitForEnter();
          break;

        case '2':
          this.printHeader('JADWAL KULIAH - TAMPILAN RINGKAS');
          this.displayCompactView();
          await this.waitForEnter();
          break;

        case '3':
          const classId = await this.askQuestion('Masukkan Class ID: ');
          const classResults = this.searchByClassId(classId);
          this.displaySearchResults(classResults, classId);
          await this.waitForEnter();
          break;

        case '4':
          const prodi = await this.askQuestion('Masukkan Program Studi: ');
          const prodiResults = this.filterByProdi(prodi);
          this.displaySearchResults(prodiResults, `Program Studi: ${prodi}`);
          await this.waitForEnter();
          break;

        case '5':
          const className = await this.askQuestion('Masukkan Class: ');
          const classResults2 = this.filterByClass(className);
          this.displaySearchResults(classResults2, `Class: ${className}`);
          await this.waitForEnter();
          break;

        case '6':
          const lecturer = await this.askQuestion('Masukkan Nama Lecturer: ');
          const lecturerResults = this.filterByLecturer(lecturer);
          this.displaySearchResults(lecturerResults, `Lecturer: ${lecturer}`);
          await this.waitForEnter();
          break;

        case '7':
          const room = await this.askQuestion('Masukkan Room: ');
          const roomResults = this.filterByRoom(room);
          this.displaySearchResults(roomResults, `Room: ${room}`);
          await this.waitForEnter();
          break;

        case '8':
          this.showAvailableFilters();
          await this.waitForEnter();
          break;

        case '9':
          this.filteredSchedule = this.data.schedule;
          this.printBox(['Filter berhasil direset!']);
          await this.waitForEnter();
          break;

        case '0':
          console.log('Terima kasih! 👋');
          process.exit(0);

        default:
          this.printBox(['Pilihan tidak valid! Silakan coba lagi.']);
          await this.waitForEnter();
          break;
      }
    }
  }
}

if (process.argv.length < 3) {
  console.log('Usage: node display-timetable.ts <path-to-timetable-result.json>');
  process.exit(1);
}

const filePath = process.argv[2];
if (!fs.existsSync(filePath)) {
  console.log(`Error: File "${filePath}" tidak ditemukan!`);
  process.exit(1);
}

const viewer = new TimetableViewer(filePath);
viewer.run().catch(error => {
  console.error('Error:', error);
  process.exit(1);
});
