"""
Configuration for the Simulated Annealing algorithm.

The algorithm uses a multi-phase approach:
- Phase 1: Eliminate hard constraint violations
- Phase 1.5: Intensification (optional) - Aggressively target remaining hard violations
- Phase 2: Optimize soft constraints
"""

from dataclasses import dataclass, field
from typing import Callable, Optional, Literal


@dataclass
class LoggingConfig:
    """Logging configuration for the optimization process."""

    enabled: bool = True
    level: Literal["debug", "info", "warn", "error", "none"] = "info"
    log_interval: int = 1000
    output: Literal["console", "file", "both"] = "console"
    file_path: str = "./sa-optimization.log"


@dataclass
class SAConfig:
    """
    Configuration for the Simulated Annealing algorithm.

    Attributes:
        initial_temperature: Starting temperature (higher = more exploration)
        min_temperature: Stopping temperature
        cooling_rate: Temperature decay factor (0.95 to 0.999)
        max_iterations: Maximum iteration count
        hard_constraint_weight: Penalty weight for hard violations
        clone_state: Function to deep-copy state

    Example:
        ```python
        config = SAConfig(
            initial_temperature=1000.0,
            cooling_rate=0.995,
            max_iterations=50000,
            clone_state=lambda s: copy.deepcopy(s)
        )
        ```
    """

    initial_temperature: float = 1000.0
    min_temperature: float = 0.01
    cooling_rate: float = 0.995
    max_iterations: int = 50000
    hard_constraint_weight: float = 10000.0
    clone_state: Optional[Callable] = None

    # Reheating configuration
    reheating_threshold: Optional[int] = None
    reheating_factor: float = 2.0
    max_reheats: int = 3

    # Tabu Search configuration
    tabu_search_enabled: bool = False
    tabu_tenure: int = 50
    max_tabu_list_size: int = 1000

    # Intensification configuration (Phase 1.5)
    enable_intensification: bool = True
    intensification_iterations: int = 2000
    max_intensification_attempts: int = 3

    # Logging configuration
    logging: LoggingConfig = field(default_factory=LoggingConfig)

    def __post_init__(self) -> None:
        """Validate configuration after initialization."""
        if not 0 < self.cooling_rate < 1:
            raise ValueError("cooling_rate must be between 0 and 1 (exclusive)")
        if self.min_temperature >= self.initial_temperature:
            raise ValueError("min_temperature must be less than initial_temperature")
        if self.max_iterations <= 0:
            raise ValueError("max_iterations must be positive")
