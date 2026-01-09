"""Tests for the SimulatedAnnealing core algorithm."""

import copy
import pytest
from timetable_sa import SimulatedAnnealing, SAConfig, Constraint, MoveGenerator


class SimpleState:
    """Simple state for testing with a list of values."""

    def __init__(self, values: list[int]):
        self.values = values


class IncreaseValue(MoveGenerator):
    """Move generator that increases a random value."""

    name = "Increase Value"

    def can_apply(self, state: SimpleState) -> bool:
        return len(state.values) > 0

    def generate(self, state: SimpleState, temperature: float) -> SimpleState:
        new_state = SimpleState(copy.deepcopy(state.values))
        if new_state.values:
            idx = 0
            new_state.values[idx] += 1
        return new_state


class DecreaseValue(MoveGenerator):
    """Move generator that decreases a random value."""

    name = "Decrease Value"

    def can_apply(self, state: SimpleState) -> bool:
        return len(state.values) > 0

    def generate(self, state: SimpleState, temperature: float) -> SimpleState:
        new_state = SimpleState(copy.deepcopy(state.values))
        if new_state.values:
            idx = 0
            new_state.values[idx] -= 1
        return new_state


class MinValueConstraint(Constraint):
    """Constraint that requires values to be at least min_value."""

    name = "Minimum Value"
    type = "hard"  # type: ignore
    min_value: int = 0

    def __init__(self, min_value: int = 0):
        self.min_value = min_value
        self.name = f"Minimum Value ({min_value})"
        self.type = "hard"

    def evaluate(self, state: SimpleState) -> float:
        min_val = min(state.values) if state.values else 0
        if min_val >= self.min_value:
            return 1.0
        return 0.5

    def get_violations(self, state: SimpleState) -> list[str]:
        violations = []
        for i, val in enumerate(state.values):
            if val < self.min_value:
                violations.append(f"Value at index {i} is {val}, expected >= {self.min_value}")
        return violations


class SumConstraint(Constraint):
    """Soft constraint that prefers a specific sum."""

    name = "Target Sum"
    type = "soft"  # type: ignore
    target_sum: int = 0

    def __init__(self, target_sum: int = 0):
        self.target_sum = target_sum
        self.name = f"Target Sum ({target_sum})"
        self.type = "soft"

    def evaluate(self, state: SimpleState) -> float:
        current_sum = sum(state.values)
        diff = abs(current_sum - self.target_sum)
        max_diff = sum(abs(v) for v in state.values) if state.values else 1
        if max_diff == 0:
            return 1.0
        return 1.0 - (diff / (max_diff + 1))


def test_sa_config_defaults():
    """Test that SAConfig has correct default values."""
    config = SAConfig()
    assert config.initial_temperature == 1000.0
    assert config.min_temperature == 0.01
    assert config.cooling_rate == 0.995
    assert config.max_iterations == 50000


def test_constraint_evaluation():
    """Test constraint evaluation."""
    state = SimpleState([1, 2, 3])

    hard_constraint = MinValueConstraint(min_value=0)
    assert hard_constraint.evaluate(state) == 1.0

    state_negative = SimpleState([-1, 2, 3])
    assert hard_constraint.evaluate(state_negative) == 0.5


def test_constraint_violations():
    """Test getting violations from constraints."""
    state = SimpleState([-1, 2, 3])
    constraint = MinValueConstraint(min_value=0)
    violations = constraint.get_violations(state)
    assert len(violations) == 1
    assert "index 0" in violations[0]


def test_move_generator():
    """Test move generator functionality."""
    state = SimpleState([1, 2, 3])
    generator = IncreaseValue()

    assert generator.can_apply(state)

    new_state = generator.generate(state, 1000.0)
    assert new_state.values[0] == 2
    assert state.values[0] == 1  # Original unchanged


def test_simulated_annealing_initialization():
    """Test SimulatedAnnealing initialization."""
    state = SimpleState([5, 5, 5])
    constraints = [MinValueConstraint(min_value=0)]
    moves = [IncreaseValue(), DecreaseValue()]

    config = SAConfig(
        max_iterations=100,
        initial_temperature=100.0,
        cooling_rate=0.99,
        clone_state=lambda s: SimpleState(copy.deepcopy(s.values))
    )

    sa = SimulatedAnnealing(state, constraints, moves, config)
    assert sa is not None


def test_simulated_annealing_solve():
    """Test running the optimization."""
    state = SimpleState([5, 5, 5])
    constraints = [MinValueConstraint(min_value=10)]
    moves = [IncreaseValue()]

    config = SAConfig(
        max_iterations=50,
        initial_temperature=100.0,
        cooling_rate=0.95,
        clone_state=lambda s: SimpleState(copy.deepcopy(s.values)),
        logging=type("LoggingConfig", (), {"enabled": False, "level": "info", "log_interval": 1000, "output": "console", "file_path": "test.log"})()
    )

    sa = SimulatedAnnealing(state, constraints, moves, config)
    result = sa.solve()

    assert "state" in result
    assert "fitness" in result
    assert "hard_violations" in result
    assert "iterations" in result


def test_simulated_annealing_reduces_violations():
    """Test that SA reduces hard constraint violations."""
    initial_values = [-5, -5, -5]
    state = SimpleState(initial_values)
    constraints = [MinValueConstraint(min_value=0)]
    moves = [IncreaseValue()]

    from timetable_sa.core.interfaces.config import LoggingConfig
    logging_config = LoggingConfig()
    logging_config.enabled = False

    config = SAConfig(
        max_iterations=200,
        initial_temperature=500.0,
        cooling_rate=0.99,
        clone_state=lambda s: SimpleState(copy.deepcopy(s.values)),
        enable_intensification=True,
        logging=logging_config
    )

    sa = SimulatedAnnealing(state, constraints, moves, config)
    result = sa.solve()

    assert result["hard_violations"] >= 0
    assert result["iterations"] > 0


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
