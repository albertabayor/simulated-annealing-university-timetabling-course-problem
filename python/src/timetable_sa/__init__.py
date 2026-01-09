"""
timetable-sa: Simulated Annealing optimizer for constraint satisfaction problems.

This package provides a flexible, multi-phase simulated annealing implementation
suitable for complex optimization problems like timetabling.

Features:
- Multi-phase optimization (Phase 1: hard constraints, Phase 2: soft constraints)
- Tabu Search integration to prevent cycling
- Intensification (Phase 1.5) for stubborn violations
- Reheating mechanism to escape local minima
- Adaptive operator selection based on success rates
"""

from timetable_sa.core.simulated_annealing import SimulatedAnnealing
from timetable_sa.core.interfaces.config import SAConfig
from timetable_sa.core.interfaces.constraint import Constraint
from timetable_sa.core.interfaces.move_generator import MoveGenerator
from timetable_sa.core.types.solution import Solution, OperatorStats
from timetable_sa.core.types.violation import Violation

__version__ = "0.1.0"

__all__ = [
    "SimulatedAnnealing",
    "SAConfig",
    "Constraint",
    "MoveGenerator",
    "Solution",
    "OperatorStats",
    "Violation",
]
