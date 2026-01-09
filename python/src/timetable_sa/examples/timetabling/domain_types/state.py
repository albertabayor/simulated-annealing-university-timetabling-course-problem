"""State types for timetable optimization."""

from dataclasses import dataclass
from typing import Optional
from datetime import datetime

from timetable_sa.examples.timetabling.domain_types.domain import TimeSlot


@dataclass
class ScheduleEntry:
    """A single entry in the timetable schedule."""
    class_id: str  # Course code (kode_matakuliah)
    class_name: str  # Course name (mata_kuliah)
    kelas: str  # Class section
    prodi: str  # Study program
    lecturers: list[str]  # All lecturer codes
    room: str  # Assigned room code
    time_slot: TimeSlot  # Assigned time slot
    sks: int  # Credit hours
    needs_lab: bool  # Whether this class requires a lab
    participants: int  # Number of students
    class_type: str  # "pagi" or "sore"
    prayer_time_added: int = 0  # Minutes added for prayer time
    is_overflow_to_lab: bool = False  # Non-lab class using lab room

    def __repr__(self) -> str:
        return (f"ScheduleEntry({self.class_id} {self.kelas} @ {self.time_slot.day} "
                f"{self.time_slot.start_time} in {self.room})")


@dataclass
class TimetableState:
    """Complete timetable state for optimization."""
    schedule: list[ScheduleEntry]
    available_time_slots: list[TimeSlot]
    rooms: list
    lecturers: list

    def __repr__(self) -> str:
        return f"TimetableState({len(self.schedule)} entries, {len(self.available_time_slots)} slots)"

    def get_entry_by_class(self, class_id: str, kelas: str) -> Optional[ScheduleEntry]:
        """Get a schedule entry by class ID and section."""
        for entry in self.schedule:
            if entry.class_id == class_id and entry.kelas == kelas:
                return entry
        return None


@dataclass
class OptimizationResult:
    """Result of the optimization process."""
    state: TimetableState
    fitness: float
    hard_violations: int
    soft_violations: int
    iterations: int
    reheats: int
    final_temperature: float
    violations: list
    operator_stats: dict
    start_time: datetime
    end_time: datetime

    @property
    def duration_seconds(self) -> float:
        """Get optimization duration in seconds."""
        return (self.end_time - self.start_time).total_seconds()
