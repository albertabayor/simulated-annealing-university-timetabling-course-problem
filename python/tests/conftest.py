"""Test fixtures and utilities for constraint tests."""

import pytest
from timetable_sa.examples.timetabling.domain_types.domain import (
    Room, Lecturer, TimeSlot, ClassRequirement
)
from timetable_sa.examples.timetabling.domain_types.state import TimetableState, ScheduleEntry


@pytest.fixture
def sample_rooms():
    """Create sample rooms for testing."""
    return [
        Room(code="R101", name="Room 101", type="theory", capacity=30),
        Room(code="R102", name="Room 102", type="theory", capacity=40),
        Room(code="LAB1", name="Lab 1", type="lab", capacity=25),
        Room(code="AUD", name="Auditorium", type="theory", capacity=100),
    ]


@pytest.fixture
def sample_lecturers():
    """Create sample lecturers for testing."""
    return [
        Lecturer(
            prodi="Informatika",
            code="LEC1",
            name="Dr. Smith",
            preferred_time=None,
            research_day=None,
            transit_time=10,
            max_daily_periods=6,
            preferred_room=None
        ),
        Lecturer(
            prodi="Informatika",
            code="LEC2",
            name="Prof. Johnson",
            preferred_time="08:00 - 10:00 Monday",
            research_day="Friday",
            transit_time=15,
            max_daily_periods=5,
            preferred_room="R101"
        ),
        Lecturer(
            prodi="Management",
            code="LEC3",
            name="Dr. Brown",
            preferred_time=None,
            research_day=None,
            transit_time=0,
            max_daily_periods=8,
            preferred_room=None
        ),
    ]


@pytest.fixture
def sample_time_slots():
    """Create sample time slots for testing."""
    slots = []
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    
    for day in days:
        for period in range(1, 7):
            start_minutes = (7 * 60) + ((period - 1) * 60)
            end_minutes = start_minutes + 50
            slots.append(TimeSlot(
                day=day,
                start_time=f"{start_minutes // 60:02d}:{start_minutes % 60:02d}",
                end_time=f"{end_minutes // 60:02d}:{end_minutes % 60:02d}",
                period=period
            ))
    
    return slots


@pytest.fixture
def sample_class_requirements():
    """Create sample class requirements for testing."""
    return [
        ClassRequirement(
            prodi="Informatika",
            kelas="IF-1A",
            kode_matakuliah="CS101",
            mata_kuliah="Introduction to Programming",
            sks=3,
            jenis="wajib",
            peserta=30,
            kode_dosen1="LEC1",
            kode_dosen2=None,
            kode_dosen_prodi_lain1=None,
            kode_dosen_prodi_lain2=None,
            class_type="pagi",
            should_on_the_lab="no",
            rooms="R101, R102"
        ),
        ClassRequirement(
            prodi="Informatika",
            kelas="IF-1B",
            kode_matakuliah="CS102",
            mata_kuliah="Data Structures",
            sks=4,
            jenis="wajib",
            peserta=25,
            kode_dosen1="LEC1",
            kode_dosen2="LEC2",
            kode_dosen_prodi_lain1=None,
            kode_dosen_prodi_lain2=None,
            class_type="pagi",
            should_on_the_lab="yes",
            rooms="LAB1"
        ),
        ClassRequirement(
            prodi="Management",
            kelas="MG-1A",
            kode_matakuliah="MG101",
            mata_kuliah="Management Principles",
            sks=2,
            jenis="wajib",
            peserta=35,
            kode_dosen1="LEC3",
            kode_dosen2=None,
            kode_dosen_prodi_lain1=None,
            kode_dosen_prodi_lain2=None,
            class_type="sore",
            should_on_the_lab="no",
            rooms="R102, AUD"
        ),
    ]


@pytest.fixture
def state_with_no_conflicts(sample_rooms, sample_time_slots, sample_lecturers):
    """Create a state with no conflicts."""
    slots = {f"{s.day}-{s.period}": s for s in sample_time_slots}
    
    schedule = [
        ScheduleEntry(
            class_id="CS101",
            class_name="Introduction to Programming",
            kelas="IF-1A",
            prodi="Informatika",
            lecturers=["LEC1"],
            room="R101",
            time_slot=slots["Monday-1"],
            sks=3,
            needs_lab=False,
            participants=30,
            class_type="pagi",
        ),
        ScheduleEntry(
            class_id="CS102",
            class_name="Data Structures",
            kelas="IF-1B",
            prodi="Informatika",
            lecturers=["LEC1", "LEC2"],
            room="LAB1",
            time_slot=slots["Monday-4"],
            sks=4,
            needs_lab=True,
            participants=25,
            class_type="pagi",
        ),
        ScheduleEntry(
            class_id="MG101",
            class_name="Management Principles",
            kelas="MG-1A",
            prodi="Management",
            lecturers=["LEC3"],
            room="R102",
            time_slot=slots["Tuesday-1"],
            sks=2,
            needs_lab=False,
            participants=35,
            class_type="sore",
        ),
    ]
    
    return TimetableState(
        schedule=schedule,
        available_time_slots=sample_time_slots,
        rooms=sample_rooms,
        lecturers=sample_lecturers,
    )


@pytest.fixture
def state_with_room_conflict(sample_rooms, sample_time_slots, sample_lecturers):
    """Create a state with a room conflict."""
    slots = {f"{s.day}-{s.period}": s for s in sample_time_slots}
    
    schedule = [
        ScheduleEntry(
            class_id="CS101",
            class_name="Introduction to Programming",
            kelas="IF-1A",
            prodi="Informatika",
            lecturers=["LEC1"],
            room="R101",
            time_slot=slots["Monday-1"],
            sks=3,
            needs_lab=False,
            participants=30,
            class_type="pagi",
        ),
        ScheduleEntry(
            class_id="MG101",
            class_name="Management Principles",
            kelas="MG-1A",
            prodi="Management",
            lecturers=["LEC3"],
            room="R101",  # Same room as CS101 - CONFLICT!
            time_slot=slots["Monday-1"],  # Same time - CONFLICT!
            sks=2,
            needs_lab=False,
            participants=35,
            class_type="sore",
        ),
    ]
    
    return TimetableState(
        schedule=schedule,
        available_time_slots=sample_time_slots,
        rooms=sample_rooms,
        lecturers=sample_lecturers,
    )


@pytest.fixture
def state_with_lecturer_conflict(sample_rooms, sample_time_slots, sample_lecturers):
    """Create a state with a lecturer conflict."""
    slots = {f"{s.day}-{s.period}": s for s in sample_time_slots}
    
    schedule = [
        ScheduleEntry(
            class_id="CS101",
            class_name="Introduction to Programming",
            kelas="IF-1A",
            prodi="Informatika",
            lecturers=["LEC1"],
            room="R101",
            time_slot=slots["Monday-1"],
            sks=3,
            needs_lab=False,
            participants=30,
            class_type="pagi",
        ),
        ScheduleEntry(
            class_id="CS102",
            class_name="Data Structures",
            kelas="IF-1B",
            prodi="Informatika",
            lecturers=["LEC1"],  # Same lecturer - CONFLICT!
            room="R102",
            time_slot=slots["Monday-1"],  # Same time - CONFLICT!
            sks=4,
            needs_lab=True,
            participants=25,
            class_type="pagi",
        ),
    ]
    
    return TimetableState(
        schedule=schedule,
        available_time_slots=sample_time_slots,
        rooms=sample_rooms,
        lecturers=sample_lecturers,
    )


@pytest.fixture
def state_with_capacity_violation(sample_rooms, sample_time_slots, sample_lecturers):
    """Create a state with room capacity violation."""
    slots = {f"{s.day}-{s.period}": s for s in sample_time_slots}
    
    schedule = [
        ScheduleEntry(
            class_id="CS101",
            class_name="Introduction to Programming",
            kelas="IF-1A",
            prodi="Informatika",
            lecturers=["LEC1"],
            room="R101",  # Capacity is 30
            time_slot=slots["Monday-1"],
            sks=3,
            needs_lab=False,
            participants=50,  # More than capacity - VIOLATION!
            class_type="pagi",
        ),
    ]
    
    return TimetableState(
        schedule=schedule,
        available_time_slots=sample_time_slots,
        rooms=sample_rooms,
        lecturers=sample_lecturers,
    )
