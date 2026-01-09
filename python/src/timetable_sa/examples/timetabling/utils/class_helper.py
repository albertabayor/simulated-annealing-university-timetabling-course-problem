"""Class-related helper functions."""

from typing import List, Dict, Any
from timetable_sa.examples.timetabling.domain_types.domain import ClassRequirement


def get_lecturers_for_class(class_req: ClassRequirement) -> List[str]:
    """Get all lecturer codes for a class.
    
    Args:
        class_req: Class requirement
        
    Returns:
        List of lecturer codes (excluding None values)
    """
    lecturers = []
    
    if class_req.kode_dosen1:
        lecturers.append(class_req.kode_dosen1)
    if class_req.kode_dosen2:
        lecturers.append(class_req.kode_dosen2)
    if class_req.kode_dosen_prodi_lain1:
        lecturers.append(class_req.kode_dosen_prodi_lain1)
    if class_req.kode_dosen_prodi_lain2:
        lecturers.append(class_req.kode_dosen_prodi_lain2)
    
    return lecturers


def needs_lab(class_req: ClassRequirement) -> bool:
    """Check if a class needs a lab room.
    
    Args:
        class_req: Class requirement
        
    Returns:
        True if class needs lab
    """
    return class_req.should_on_the_lab.lower() == "yes"


def get_preferred_rooms(class_req: ClassRequirement) -> List[str]:
    """Get list of preferred rooms for a class.
    
    Args:
        class_req: Class requirement
        
    Returns:
        List of room codes
    """
    if not class_req.rooms:
        return []
    
    rooms = [r.strip() for r in class_req.rooms.split(",")]
    return [r for r in rooms if r]


def get_class_identifier(class_req: ClassRequirement) -> str:
    """Get unique identifier for a class.
    
    Args:
        class_req: Class requirement
        
    Returns:
        Unique identifier string
    """
    return f"{class_req.kode_matakuliah}-{class_req.kelas}"


def group_classes_by_prodi(classes: List[ClassRequirement]) -> Dict[str, List[ClassRequirement]]:
    """Group classes by study program.
    
    Args:
        classes: List of class requirements
        
    Returns:
        Dictionary mapping prodi to list of classes
    """
    grouped: Dict[str, List[ClassRequirement]] = {}
    
    for class_req in classes:
        if class_req.prodi not in grouped:
            grouped[class_req.prodi] = []
        grouped[class_req.prodi].append(class_req)
    
    return grouped


def group_classes_by_kelas(classes: List[ClassRequirement]) -> Dict[str, List[ClassRequirement]]:
    """Group classes by class section.
    
    Args:
        classes: List of class requirements
        
    Returns:
        Dictionary mapping kelas to list of classes
    """
    grouped: Dict[str, List[ClassRequirement]] = {}
    
    for class_req in classes:
        if class_req.kelas not in grouped:
            grouped[class_req.kelas] = []
        grouped[class_req.kelas].append(class_req)
    
    return grouped


def filter_classes_by_prodi(
    classes: List[ClassRequirement],
    prodi: str
) -> List[ClassRequirement]:
    """Filter classes by study program.
    
    Args:
        classes: List of class requirements
        prodi: Study program to filter by
        
    Returns:
        Filtered list of classes
    """
    return [c for c in classes if c.prodi == prodi]


def filter_classes_by_lecturer(
    classes: List[ClassRequirement],
    lecturer_code: str
) -> List[ClassRequirement]:
    """Filter classes by lecturer code.
    
    Args:
        classes: List of class requirements
        lecturer_code: Lecturer code to filter by
        
    Returns:
        Filtered list of classes taught by the lecturer
    """
    filtered = []
    
    for class_req in classes:
        lecturers = get_lecturers_for_class(class_req)
        if lecturer_code in lecturers:
            filtered.append(class_req)
    
    return filtered


def filter_classes_by_type(
    classes: List[ClassRequirement],
    class_type: str
) -> List[ClassRequirement]:
    """Filter classes by class type (pagi/sore).
    
    Args:
        classes: List of class requirements
        class_type: Class type to filter by ("pagi" or "sore")
        
    Returns:
        Filtered list of classes
    """
    return [c for c in classes if c.class_type == class_type]


def filter_lab_classes(classes: List[ClassRequirement]) -> List[ClassRequirement]:
    """Filter to only classes that need labs.
    
    Args:
        classes: List of class requirements
        
    Returns:
        List of classes requiring lab rooms
    """
    return [c for c in classes if needs_lab(c)]


def count_total_participants(classes: List[ClassRequirement]) -> int:
    """Count total participants across all classes.
    
    Args:
        classes: List of class requirements
        
    Returns:
        Total number of participants
    """
    return sum(c.peserta for c in classes)


def count_total_sks(classes: List[ClassRequirement]) -> int:
    """Count total SKS across all classes.
    
    Args:
        classes: List of class requirements
        
    Returns:
        Total number of SKS
    """
    return sum(c.sks for c in classes)


def get_unique_lecturers(classes: List[ClassRequirement]) -> List[str]:
    """Get list of unique lecturer codes across all classes.
    
    Args:
        classes: List of class requirements
        
    Returns:
        List of unique lecturer codes
    """
    unique = set()
    
    for class_req in classes:
        unique.update(get_lecturers_for_class(class_req))
    
    return sorted(list(unique))


def get_class_summary(class_req: ClassRequirement) -> Dict[str, Any]:
    """Get summary dictionary for a class.
    
    Args:
        class_req: Class requirement
        
    Returns:
        Dictionary with class summary
    """
    return {
        "identifier": get_class_identifier(class_req),
        "prodi": class_req.prodi,
        "kelas": class_req.kelas,
        "course_code": class_req.kode_matakuliah,
        "course_name": class_req.mata_kuliah,
        "sks": class_req.sks,
        "participants": class_req.peserta,
        "lecturers": get_lecturers_for_class(class_req),
        "needs_lab": needs_lab(class_req),
        "class_type": class_req.class_type,
        "preferred_rooms": get_preferred_rooms(class_req),
    }


def has_class_overlap(kelas1: str, kelas2: str) -> bool:
    """Check if two class values have overlapping class codes.
    
    Matches TypeScript's hasClassOverlap exactly:
    - Handles comma-separated values like "MR-3A,MR-5A"
    - Handles arrays of classes
    - Returns True if there's any class code overlap
    
    Examples:
        has_class_overlap("MR-3A", "MR-3A") => True
        has_class_overlap("MR-3A", "MR-3B") => False
        has_class_overlap("MR-3A,MR-5A", "MR-3B") => True
        has_class_overlap(["MR-3A", "MR-5A"], "MR-3B") => True
        has_class_overlap(["MR-3A", "MR-5A"], ["MR-7A", "MR-9A"]) => False
    """
    if isinstance(kelas1, str) and isinstance(kelas2, str):
        # Handle comma-separated strings like "MR-3A,MR-5A"
        classes1 = [c.strip() for c in kelas1.split(',')]
        classes2 = [c.strip() for c in kelas2.split(',')]
        
        for c1 in classes1:
            for c2 in classes2:
                if c1 == c2:
                    return True
        return False
    
    elif isinstance(kelas1, list) and isinstance(kelas2, list):
        # Handle arrays
        for c1 in kelas1:
            for c2 in kelas2:
                if c1 == c2:
                    return True
        return False
    
    else:
        # Fallback to simple comparison
        return str(kelas1) == str(kelas2)
