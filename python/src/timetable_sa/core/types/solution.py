"""
Solution type representing the result of the optimization.
"""

from typing import TypedDict, TypeVar, Generic

TState = TypeVar("TState")


class OperatorStatsEntry(TypedDict):
    """Statistics for a single move operator."""

    attempts: int
    improvements: int
    accepted: int
    success_rate: float


# OperatorStats is a dict mapping operator names to their statistics
OperatorStats = dict[str, OperatorStatsEntry]


class Solution(TypedDict, Generic[TState]):
    """
    Represents the solution found by the Simulated Annealing algorithm.

    Attributes:
        state: The best state found during optimization
        fitness: Final fitness score (lower is better)
        hard_violations: Number of hard constraint violations
        soft_violations: Number of soft constraint violations
        iterations: Total iterations performed
        reheats: Number of reheating events
        final_temperature: Temperature when optimization stopped
        violations: Detailed list of all constraint violations
        operator_stats: Statistics about move operators used
    """

    state: TState
    fitness: float
    hard_violations: int
    soft_violations: int
    iterations: int
    reheats: int
    final_temperature: float
    violations: list["Violation"]
    operator_stats: OperatorStats


# Import Violation for type hint
from timetable_sa.core.types.violation import Violation  # noqa: E402
