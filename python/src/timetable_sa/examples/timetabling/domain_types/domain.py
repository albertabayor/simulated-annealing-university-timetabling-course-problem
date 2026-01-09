"""
Domain types for university course timetabling.

Based on data from data_uisi.xlsx with:
- 34 rooms
- 100 lecturers  
- 374 class requirements
"""

from dataclasses import dataclass
from typing import Optional


@dataclass
class Room:
    """Room/classroom definition - matches 'ruangan' sheet"""
    code: str
    name: str
    type: str  # "theory", "lab", etc.
    capacity: int

    def __repr__(self) -> str:
        return f"Room({self.code}, {self.name}, {self.type}, cap={self.capacity})"


@dataclass
class Lecturer:
    """Lecturer definition - matches 'dosen' sheet"""
    prodi: str
    code: str
    name: str
    preferred_time: Optional[str]  # e.g., "18.30 - 21.00 Thursday"
    research_day: Optional[str]  # Reserved day for research
    transit_time: int  # Minutes needed between classes
    max_daily_periods: int  # Maximum teaching hours per day
    preferred_room: Optional[str]

    def __repr__(self) -> str:
        return f"Lecturer({self.code}, {self.name})"


@dataclass
class TimeSlot:
    """Time slot definition"""
    day: str  # "Monday", "Tuesday", etc.
    start_time: str  # "08:00", "09:30", etc.
    end_time: str  # "10:00", "11:30", etc.
    period: int  # Period number for ordering

    def __repr__(self) -> str:
        return f"TimeSlot({self.day} {self.start_time}-{self.end_time}, period={self.period})"

    def to_minutes(self) -> int:
        """Convert start time to minutes from midnight."""
        hours, minutes = map(int, self.start_time.split(':'))
        return hours * 60 + minutes


@dataclass
class ClassRequirement:
    """Class requirement - matches 'kebutuhan_kelas' sheet"""
    prodi: str
    kelas: str  # Class section (e.g., "MM-1A")
    kode_matakuliah: str  # Course code
    mata_kuliah: str  # Course name
    sks: int  # Credit hours
    jenis: str  # "wajib" (required), "pilihan" (elective)
    peserta: int  # Number of participants
    kode_dosen1: str  # Primary lecturer code
    kode_dosen2: Optional[str]  # Secondary lecturer (optional)
    kode_dosen_prodi_lain1: Optional[str]  # External lecturer 1 (optional)
    kode_dosen_prodi_lain2: Optional[str]  # External lecturer 2 (optional)
    class_type: str  # "pagi" (morning) or "sore" (evening)
    should_on_the_lab: str  # "yes" or "no"
    rooms: str  # Comma-separated list of preferred rooms

    def __repr__(self) -> str:
        return f"ClassRequirement({self.kode_matakuliah}, {self.mata_kuliah}, {self.kelas})"

    def get_lecturers(self) -> list[str]:
        """Get all lecturer codes for this class.
        
        Filters out 'nan' values to match TypeScript behavior:
        TypeScript: if (classReq.Kode_Dosen1) lecturerCodes.push(...)
        """
        lecturers = []
        
        if self.kode_dosen1 and self.kode_dosen1 != 'nan':
            lecturers.append(self.kode_dosen1)
        if self.kode_dosen2 and self.kode_dosen2 != 'nan':
            lecturers.append(self.kode_dosen2)
        if self.kode_dosen_prodi_lain1 and self.kode_dosen_prodi_lain1 != 'nan':
            lecturers.append(self.kode_dosen_prodi_lain1)
        if self.kode_dosen_prodi_lain2 and self.kode_dosen_prodi_lain2 != 'nan':
            lecturers.append(self.kode_dosen_prodi_lain2)
        
        return lecturers

    def needs_lab(self) -> bool:
        """Check if this class requires a lab room."""
        return self.should_on_the_lab.lower() == "yes"
