"""Room type constants and definitions."""

from typing import Dict, List


ROOM_TYPE_THEORY = "theory"
ROOM_TYPE_LAB = "lab"
ROOM_TYPE_COMPUTER_LAB = "computer_lab"
ROOM_TYPE_MEETING = "meeting"
ROOM_TYPE_LECTURE = "lecture"


ROOM_CAPACITY_TIERS = {
    "small": {"max": 30, "label": "Small (≤30)"},
    "medium": {"max": 50, "label": "Medium (31-50)"},
    "large": {"max": 100, "label": "Large (51-100)"},
    "auditorium": {"max": float("inf"), "label": "Auditorium (>100)"},
}


ROOM_TYPE_CONFIG: Dict[str, Dict] = {
    ROOM_TYPE_THEORY: {
        "can_host_lab": False,
        "can_host_lecture": True,
        "default_equipment": ["whiteboard", "projector"],
        "min_period_duration": 50,
    },
    ROOM_TYPE_LAB: {
        "can_host_lab": True,
        "can_host_lecture": True,
        "default_equipment": ["computers", "whiteboard", "projector"],
        "min_period_duration": 50,
    },
    ROOM_TYPE_COMPUTER_LAB: {
        "can_host_lab": True,
        "can_host_lecture": False,
        "default_equipment": ["computers", "whiteboard"],
        "min_period_duration": 50,
    },
    ROOM_TYPE_MEETING: {
        "can_host_lab": False,
        "can_host_lecture": False,
        "default_equipment": ["whiteboard"],
        "min_period_duration": 50,
    },
    ROOM_TYPE_LECTURE: {
        "can_host_lab": False,
        "can_host_lecture": True,
        "default_equipment": ["whiteboard", "projector", "microphone"],
        "min_period_duration": 50,
    },
}


def get_room_capacity_tier(capacity: int) -> str:
    """Get the capacity tier for a room.
    
    Args:
        capacity: Room capacity
        
    Returns:
        Tier name: "small", "medium", "large", or "auditorium"
    """
    if capacity <= 30:
        return "small"
    elif capacity <= 50:
        return "medium"
    elif capacity <= 100:
        return "large"
    else:
        return "auditorium"


def get_room_type_config(room_type: str) -> Dict:
    """Get configuration for a room type.
    
    Args:
        room_type: Type of room
        
    Returns:
        Configuration dictionary with room type settings
    """
    return ROOM_TYPE_CONFIG.get(room_type, ROOM_TYPE_CONFIG[ROOM_TYPE_THEORY])


def get_available_room_types() -> List[str]:
    """Get list of all available room types.
    
    Returns:
        List of room type strings
    """
    return list(ROOM_TYPE_CONFIG.keys())


def is_valid_room_type(room_type: str) -> bool:
    """Check if a room type is valid.
    
    Args:
        room_type: Room type to validate
        
    Returns:
        True if room type is valid
    """
    return room_type in ROOM_TYPE_CONFIG
