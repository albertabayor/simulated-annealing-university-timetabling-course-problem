"""
Constraint interface for defining optimization constraints.

Constraints can be either:
- **Hard constraints**: Must be satisfied (violations are heavily penalized)
- **Soft constraints**: Preferred but not required (violations are lightly penalized)
"""

from abc import ABC, abstractmethod
from typing import TypeVar, Literal, Generic

TState = TypeVar("TState")


class Constraint(ABC, Generic[TState]):
    """
    Abstract base class for constraints in the optimization problem.

    Attributes:
        name: Unique name for this constraint (used in logging and violation reports)
        type: 'hard' or 'soft' - determines how violations are penalized
        weight: Weight for soft constraints (ignored for hard constraints)

    Example:
        ```python
        class NoRoomConflict(Constraint[TimetableState]):
            name = "No Room Conflict"
            type: Literal['hard', 'soft'] = 'hard'

            def evaluate(self, state: TimetableState) -> float:
                # Check for conflicts...
                return 1.0 if no_conflicts else 0.0
        ```
    """

    name: str
    type: Literal["hard", "soft"]
    weight: float = 10.0

    @abstractmethod
    def evaluate(self, state: TState) -> float:
        """
        Evaluate the constraint for the given state.

        Args:
            state: Current state to evaluate

        Returns:
            Score between 0 and 1 (inclusive):
            - 1.0 = fully satisfied (no violation)
            - 0.0 = completely violated
            - 0.5 = partially satisfied (for soft constraints)

        Note:
            - Hard constraints typically return 0 (violated) or 1 (satisfied)
            - Soft constraints can return intermediate values
        """
        pass

    def describe(self, state: TState) -> str | None:
        """
        Provide human-readable description of violations.

        Args:
            state: Current state

        Returns:
            Description of violations, or None if satisfied
        """
        return None

    def get_violations(self, state: TState) -> list[str]:
        """
        Get detailed list of all violations for this constraint.

        Args:
            state: Current state

        Returns:
            List of violation descriptions, or empty list if satisfied
        """
        return []
