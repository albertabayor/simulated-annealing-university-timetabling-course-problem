"""
MoveGenerator interface for generating neighboring states.

Move generators define how to explore the solution space. Common types include:
- Local moves: Modify a single element (e.g., change room, change time slot)
- Swap moves: Exchange properties between two elements
- Insert/Remove moves: Add or remove elements from the solution
"""

from abc import ABC, abstractmethod
from typing import TypeVar, Generic

TState = TypeVar("TState")


class MoveGenerator(ABC, Generic[TState]):
    """
    Abstract base class for move generators (neighborhood operators).

    Move generators create neighboring states by applying modifications
    to the current state during the optimization process.

    Attributes:
        name: Unique name for this move operator (used in logging and statistics)

    Example:
        ```python
        class ChangeTimeSlot(MoveGenerator[TimetableState]):
            name = "Change Time Slot"

            def can_apply(self, state: TimetableState) -> bool:
                return len(state.schedule) > 0

            def generate(self, state: TimetableState, temperature: float) -> TimetableState:
                new_state = clone_state(state)
                # Modify a random class's time slot...
                return new_state
        ```
    """

    name: str

    @abstractmethod
    def generate(self, state: TState, temperature: float) -> TState:
        """
        Generate a new neighbor state from the current state.

        Args:
            state: Current state (should NOT be modified)
            temperature: Current temperature in the SA algorithm.
                Can be used to adjust move intensity:
                - High temperature: Explore broadly (larger, more random moves)
                - Low temperature: Refine locally (smaller, more focused moves)

        Returns:
            New state with modifications applied

        Important:
            Do not modify the input `state`. Always create a new state.
        """
        pass

    @abstractmethod
    def can_apply(self, state: TState) -> bool:
        """
        Check if this move can be applied to the current state.

        Use this to skip inapplicable moves (e.g., cannot swap if schedule has < 2 entries).

        Args:
            state: Current state

        Returns:
            True if move is applicable, False otherwise
        """
        pass
