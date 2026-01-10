"""Excel data loader for UISI timetabling data.

Loads data from data_uisi.xlsx which contains:
- ruangan (rooms) sheet
- dosen (lecturers) sheet
- kebutuhan_kelas (class requirements) sheet
"""

import pandas as pd
from dataclasses import dataclass

from timetable_sa.examples.timetabling.domain_types.domain import (
    Room,
    Lecturer,
    ClassRequirement,
)


@dataclass
class DataPaths:
    """Paths to data files."""
    rooms: str
    lecturers: str
    classes: str


def load_from_excel(
    excel_path: str,
    rooms_sheet: str = "ruangan",
    lecturers_sheet: str = "dosen",
    classes_sheet: str = "kebutuhan_kelas",
) -> tuple[list[Room], list[Lecturer], list[ClassRequirement]]:
    """Load timetabling data from Excel file.
    
    Args:
        excel_path: Path to Excel file
        rooms_sheet: Name of rooms sheet
        lecturers_sheet: Name of lecturers sheet
        classes_sheet: Name of classes sheet
    
    Returns:
        Tuple of (rooms, lecturers, classes)
    
    Examples:
        >>> rooms, lecturers, classes = load_from_excel("data_uisi.xlsx")
        >>> print(f"Loaded {len(rooms)} rooms, {len(lecturers)} lecturers, {len(classes)} classes")
        Loaded 34 rooms, 100 lecturers, 374 classes
    """
    # Load rooms
    rooms_df = pd.read_excel(excel_path, sheet_name=rooms_sheet)
    rooms = load_rooms(rooms_df)
    
    # Load lecturers
    lecturers_df = pd.read_excel(excel_path, sheet_name=lecturers_sheet)
    lecturers = load_lecturers(lecturers_df)
    
    # Load class requirements
    classes_df = pd.read_excel(excel_path, sheet_name=classes_sheet)
    class_requirements = load_class_requirements(classes_df)
    
    return rooms, lecturers, class_requirements


def load_rooms(df: pd.DataFrame) -> list[Room]:
    """Load rooms from DataFrame.
    
    Expected columns: Code, Name, Type, Capacity
    """
    rooms = []
    for _, row in df.iterrows():
        room = Room(
            code=str(row.get("Code", "")),
            name=str(row.get("Name", "")),
            type=str(row.get("Type", "")),
            capacity=int(row.get("Capacity", 0)),
        )
        rooms.append(room)
    return rooms


def load_lecturers(df: pd.DataFrame) -> list[Lecturer]:
    """Load lecturers from DataFrame.
    
    Expected columns: Prodi, Code, Name, Prefered_Time, Research_Day, 
                      Transit_Time, Max_Daily_Periods, Prefered_Room
    """
    lecturers = []
    for _, row in df.iterrows():
        # Handle NaN values
        preferred_time = row.get("Prefered_Time")
        if pd.isna(preferred_time):
            preferred_time = None
        
        research_day = row.get("Research_Day")
        if pd.isna(research_day):
            research_day = None
        
        preferred_room = row.get("Prefered_Room")
        if pd.isna(preferred_room):
            preferred_room = None
        
        lecturer = Lecturer(
            prodi=str(row.get("Prodi", "")),
            code=str(row.get("Code", "")),
            name=str(row.get("Name", "")),
            preferred_time=preferred_time,
            research_day=research_day,
            transit_time=int(row.get("Transit_Time", 0)),
            max_daily_periods=int(row.get("Max_Daily_Periods", 0)),
            preferred_room=preferred_room,
        )
        lecturers.append(lecturer)
    return lecturers


def load_class_requirements(df: pd.DataFrame) -> list[ClassRequirement]:
    """Load class requirements from DataFrame.
    
    Expected columns: Prodi, Kelas, Kode_Matakuliah, Mata_Kuliah, SKS, Jenis,
                      Peserta, Kode_Dosen1, Kode_Dosen2, Kode_Dosen_Prodi_Lain1,
                      Kode_Dosen_Prodi_Lain2, Class_Type, should_on_the_lab, rooms
    """
    classes = []
    for _, row in df.iterrows():
        # Handle NaN values
        kode_dosen2 = row.get("Kode_Dosen2")
        if pd.isna(kode_dosen2):
            kode_dosen2 = None
        
        kode_dosen_prodi_lain1 = row.get("Kode_Dosen_Prodi_Lain1")
        if pd.isna(kode_dosen_prodi_lain1):
            kode_dosen_prodi_lain1 = None
        
        kode_dosen_prodi_lain2 = row.get("Kode_Dosen_Prodi_Lain2")
        if pd.isna(kode_dosen_prodi_lain2):
            kode_dosen_prodi_lain2 = None

        # Handle NaN/empty class_type: default to "pagi"
        raw_class_type = row.get("Class_Type", "")
        if pd.isna(raw_class_type) or not raw_class_type or str(raw_class_type).lower() == "nan":
            class_type = "pagi"
        else:
            class_type = str(raw_class_type)

        class_req = ClassRequirement(
            prodi=str(row.get("Prodi", "")),
            kelas=str(row.get("Kelas", "")),
            kode_matakuliah=str(row.get("Kode_Matakuliah", "")),
            mata_kuliah=str(row.get("Mata_Kuliah", "")),
            sks=int(row.get("SKS", 0)),
            jenis=str(row.get("Jenis", "")),
            peserta=int(row.get("Peserta", 0)),
            kode_dosen1=str(row.get("Kode_Dosen1", "")),
            kode_dosen2=kode_dosen2,
            kode_dosen_prodi_lain1=kode_dosen_prodi_lain1,
            kode_dosen_prodi_lain2=kode_dosen_prodi_lain2,
            class_type=class_type,
            should_on_the_lab=str(row.get("should_on_the_lab", "")),
            rooms=str(row.get("rooms", "")),
        )
        classes.append(class_req)
    return classes


def load_uisi_data(
    excel_path: str = "/home/emmanuelabayor/projects/timetable-sa/data_uisi.xlsx",
) -> tuple[list[Room], list[Lecturer], list[ClassRequirement]]:
    """Load UISI timetabling data from default location.
    
    Args:
        excel_path: Path to data_uisi.xlsx
    
    Returns:
        Tuple of (rooms, lecturers, classes)
    """
    return load_from_excel(excel_path)


def load_sample_data() -> tuple[list[Room], list[Lecturer], list[ClassRequirement]]:
    """Load sample data for testing/demo purposes.
    
    Returns:
        Tuple of sample rooms, lecturers, and classes
    """
    # Sample rooms
    rooms = [
        Room(code="B2-R1", name="Kampus B B2 Ruang 1", type="theory", capacity=30),
        Room(code="B2-R2", name="Kampus B B2 Ruang 2", type="theory", capacity=30),
        Room(code="B3-R1", name="Kampus B B3 Ruang 1", type="theory", capacity=35),
        Room(code="CM-101", name="CM Building Room 101", type="theory", capacity=40),
        Room(code="LAB-1", name="Computer Lab 1", type="lab", capacity=25),
        Room(code="LAB-2", name="Computer Lab 2", type="lab", capacity=25),
    ]
    
    # Sample lecturers
    lecturers = [
        Lecturer(
            prodi="Magister Management",
            code="RPA",
            name="Dr. Rr. Rooswanti",
            preferred_time="18.30 - 21.00 Thursday",
            research_day=None,
            transit_time=0,
            max_daily_periods=9,
            preferred_room=None,
        ),
        Lecturer(
            prodi="Magister Management",
            code="GTK",
            name="Dr. Ir. Gatot",
            preferred_time="18.30 - 21.00 Friday",
            research_day=None,
            transit_time=0,
            max_daily_periods=9,
            preferred_room=None,
        ),
        Lecturer(
            prodi="Magister Management",
            code="ALF",
            name="Prof. Alf",
            preferred_time=None,
            research_day="Wednesday",
            transit_time=15,
            max_daily_periods=6,
            preferred_room="B2-R1",
        ),
    ]
    
    # Sample class requirements
    classes = [
        ClassRequirement(
            prodi="Magister Management",
            kelas="MM-1A",
            kode_matakuliah="MM23EB03",
            mata_kuliah="Economic for Business",
            sks=3,
            jenis="wajib",
            peserta=15,
            kode_dosen1="BAT",
            kode_dosen2=None,
            kode_dosen_prodi_lain1="WAH",
            kode_dosen_prodi_lain2=None,
            class_type="sore",
            should_on_the_lab="no",
            rooms="B2-R1, B3-R1, B3-R2, CM-101, CM-102",
        ),
        ClassRequirement(
            prodi="Magister Management",
            kelas="MM-1A",
            kode_matakuliah="MM23SM03",
            mata_kuliah="Strategic Marketing Management",
            sks=3,
            jenis="wajib",
            peserta=15,
            kode_dosen1="ALF",
            kode_dosen2=None,
            kode_dosen_prodi_lain1=None,
            kode_dosen_prodi_lain2=None,
            class_type="pagi",
            should_on_the_lab="no",
            rooms="B2-R1, B3-R1",
        ),
    ]
    
    return rooms, lecturers, classes
