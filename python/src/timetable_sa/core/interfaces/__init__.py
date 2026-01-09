"""Interface definitions for constraints and move generators."""

from timetable_sa.core.interfaces.constraint import Constraint
from timetable_sa.core.interfaces.move_generator import MoveGenerator
from timetable_sa.core.interfaces.config import SAConfig

__all__ = ["Constraint", "MoveGenerator", "SAConfig"]
