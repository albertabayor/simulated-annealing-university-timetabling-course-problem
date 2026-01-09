"""Data loaders __init__.py"""

from timetable_sa.examples.timetabling.data.excel_loader import (
    load_from_excel,
    load_uisi_data,
    load_sample_data,
    load_rooms,
    load_lecturers,
    load_class_requirements,
)

__all__ = [
    "load_from_excel",
    "load_uisi_data",
    "load_sample_data",
    "load_rooms",
    "load_lecturers",
    "load_class_requirements",
]
