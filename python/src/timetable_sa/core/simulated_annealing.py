"""
Generic Simulated Annealing optimizer for constraint satisfaction problems.
"""

import math
import random
from datetime import datetime
from typing import Any, TypedDict

from timetable_sa.core.interfaces.config import SAConfig, LoggingConfig

TState = Any


class _OperatorStatsEntry(TypedDict):
    attempts: int
    improvements: int
    accepted: int
    success_rate: float


OperatorStats = dict[str, _OperatorStatsEntry]


class _MergedConfig(TypedDict):
    initial_temperature: float
    min_temperature: float
    cooling_rate: float
    max_iterations: int
    hard_constraint_weight: float
    clone_state: Any
    reheating_threshold: int | None
    reheating_factor: float
    max_reheats: int
    tabu_search_enabled: bool
    tabu_tenure: int
    max_tabu_list_size: int
    enable_intensification: bool
    intensification_iterations: int
    max_intensification_attempts: int
    logging: dict[str, Any]


class SimulatedAnnealing:
    """Multi-phase Simulated Annealing optimizer for constraint satisfaction problems."""

    def __init__(
        self,
        initial_state: TState,
        constraints: list[Any],
        move_generators: list[Any],
        config: SAConfig,
    ) -> None:
        self.initial_state = initial_state
        self.constraints = constraints
        self.move_generators = move_generators

        self.hard_constraints = [c for c in constraints if c.type == "hard"]
        self.soft_constraints = [c for c in constraints if c.type == "soft"]

        self.config = self._merge_with_defaults(config)

        self.operator_stats: OperatorStats = {}
        for generator in move_generators:
            self.operator_stats[generator.name] = {
                "attempts": 0,
                "improvements": 0,
                "accepted": 0,
                "success_rate": 0.0,
            }

        self.tabu_list: dict[str, int] = {}

        self._log(
            "info",
            "Simulated Annealing initialized",
            {
                "hard_constraints": len(self.hard_constraints),
                "soft_constraints": len(self.soft_constraints),
                "move_generators": len(self.move_generators),
                "config": {
                    "initial_temperature": self.config["initial_temperature"],
                    "min_temperature": self.config["min_temperature"],
                    "cooling_rate": self.config["cooling_rate"],
                    "max_iterations": self.config["max_iterations"],
                },
            },
        )

    def solve(self) -> dict[str, Any]:
        """Run the optimization algorithm and return the best solution found."""
        self._log("info", "Starting optimization...")
        self._log("info", "Phase 1: Eliminating hard constraint violations")

        current_state = self.config["clone_state"](self.initial_state)
        best_state = self.config["clone_state"](current_state)

        initial_result = self._calculate_fitness_and_violations(current_state)
        current_fitness = initial_result["fitness"]
        best_fitness = current_fitness

        current_hard_violations = initial_result["hard_violations"]
        best_hard_violations = current_hard_violations

        temperature = self.config["initial_temperature"]
        iteration = 0
        iterations_without_improvement = 0
        reheats = 0

        self._log(
            "info",
            "Initial state",
            {
                "fitness": f"{current_fitness:.2f}",
                "hard_violations": current_hard_violations,
            },
        )

        phase1_max_iterations = math.floor(self.config["max_iterations"] * 0.6)
        phase1_iteration = 0

        while (
            temperature > self.config["initial_temperature"] / 10
            and phase1_iteration < phase1_max_iterations
            and best_hard_violations > 0
        ):
            neighbor_result = self._generate_neighbor(current_state, temperature)

            if not neighbor_result["new_state"]:
                # No valid neighbor generated, try again in next iteration
                phase1_iteration += 1
                iteration += 1
                continue

            new_state = neighbor_result["new_state"]
            operator_name = neighbor_result["operator_name"]

            if self.config["tabu_search_enabled"]:
                new_signature = self._get_state_signature(new_state)
                if self._is_tabu(new_signature, iteration):
                    phase1_iteration += 1
                    iteration += 1
                    continue

            self.operator_stats[operator_name]["attempts"] += 1

            new_result = self._calculate_fitness_and_violations(new_state)
            new_fitness = new_result["fitness"]
            new_hard_violations = int(new_result["hard_violations"])

            accept_prob = self._acceptance_probability_phase1(
                int(current_hard_violations),
                new_hard_violations,
                current_fitness,
                new_fitness,
                temperature,
            )

            if random.random() < accept_prob:
                self.operator_stats[operator_name]["accepted"] += 1

                if new_fitness < current_fitness:
                    self.operator_stats[operator_name]["improvements"] += 1

                if self.config["tabu_search_enabled"]:
                    current_signature = self._get_state_signature(current_state)
                    self._add_to_tabu_list(current_signature, iteration)

                current_state = new_state
                current_fitness = new_fitness
                current_hard_violations = new_hard_violations

                if (
                    new_hard_violations < best_hard_violations
                    or (
                        new_hard_violations == best_hard_violations
                        and new_fitness < best_fitness
                    )
                ):
                    best_state = self.config["clone_state"](current_state)
                    best_fitness = new_fitness
                    best_hard_violations = new_hard_violations
                    iterations_without_improvement = 0

                    self._log(
                        "debug",
                        f"[Phase 1] New best: Hard violations = {best_hard_violations}, Fitness = {best_fitness:.2f}, Operator = {operator_name}",
                    )
                else:
                    iterations_without_improvement += 1
            else:
                iterations_without_improvement += 1

            if (
                self.config["reheating_threshold"] is not None
                and iterations_without_improvement >= self.config["reheating_threshold"]
                and self.config["max_reheats"] > reheats
                and temperature < self.config["initial_temperature"] / 100
            ):
                temperature *= self.config["reheating_factor"]
                reheats += 1
                iterations_without_improvement = 0

                self._log(
                    "info",
                    f"[Phase 1] Reheating #{reheats}: Temperature = {temperature:.2f}, Hard violations = {best_hard_violations}",
                )

            temperature *= self.config["cooling_rate"]
            phase1_iteration += 1
            iteration += 1

            log_interval = self.config["logging"]["log_interval"]
            if phase1_iteration % log_interval == 0:
                self._log(
                    "info",
                    f"[Phase 1] Iteration {phase1_iteration}: Temp = {temperature:.2f}, Hard violations = {current_hard_violations}, Best = {best_hard_violations}",
                )

        self._log(
            "info", f"Phase 1 complete: Hard violations = {best_hard_violations}"
        )

        if best_hard_violations > 0 and self.config["enable_intensification"]:
            self._log(
                "info",
                "Phase 1.5: Intensification - targeting remaining hard violations",
            )

            intensification_attempt = 0

            while (
                best_hard_violations > 0
                and intensification_attempt < self.config["max_intensification_attempts"]
            ):
                intensification_attempt += 1
                self._log(
                    "info",
                    f"[Intensification] Attempt {intensification_attempt}/{self.config['max_intensification_attempts']}",
                )

                intensification_temp = self.config["initial_temperature"]
                intensification_iterations = 0
                stagnation_counter = 0
                stagnation_limit = 300

                current_state = self.config["clone_state"](best_state)
                current_fitness = best_fitness
                current_hard_violations = best_hard_violations

                while (
                    intensification_iterations < self.config["intensification_iterations"]
                    and best_hard_violations > 0
                ):
                    all_generators = [
                        gen for gen in self.move_generators if gen.can_apply(current_state)
                    ]
                    targeted_generators = [
                        gen
                        for gen in all_generators
                        if "fix" in gen.name.lower()
                        or "swap" in gen.name.lower()
                        or "change" in gen.name.lower()
                    ]

                    if targeted_generators and random.random() < 0.7:
                        generators = targeted_generators
                    else:
                        generators = all_generators

                    if not generators:
                        break

                    selected_generator = random.choice(generators)
                    cloned_state = self.config["clone_state"](current_state)
                    new_state = selected_generator.generate(
                        cloned_state, intensification_temp
                    )

                    if not new_state:
                        intensification_iterations += 1
                        continue

                    self.operator_stats[selected_generator.name]["attempts"] += 1

                    new_result = self._calculate_fitness_and_violations(new_state)
                    new_fitness = new_result["fitness"]
                    new_hard_violations = new_result["hard_violations"]

                    accept = False

                    if new_hard_violations < current_hard_violations:
                        accept = True
                        self.operator_stats[selected_generator.name]["improvements"] += 1
                        stagnation_counter = 0
                    elif new_hard_violations == current_hard_violations:
                        if new_fitness < current_fitness:
                            accept = True
                            self.operator_stats[selected_generator.name][
                                "improvements"
                            ] += 1
                            stagnation_counter = 0
                        else:
                            accept_prob = math.exp(
                                (current_fitness - new_fitness) / intensification_temp
                            )
                            accept = random.random() < accept_prob
                            stagnation_counter += 1
                    else:
                        worsen_prob = math.exp(
                            -1 / (intensification_temp / 10000)
                        )
                        if random.random() < worsen_prob * 0.02:
                            accept = True
                            self._log(
                                "debug",
                                "[Intensification] Accepting worsening move to escape local minimum",
                            )
                        stagnation_counter += 1

                    if accept:
                        self.operator_stats[selected_generator.name]["accepted"] += 1
                        current_state = new_state
                        current_fitness = new_fitness
                        current_hard_violations = new_hard_violations

                        if (
                            new_hard_violations < best_hard_violations
                            or (
                                new_hard_violations == best_hard_violations
                                and new_fitness < best_fitness
                            )
                        ):
                            best_state = self.config["clone_state"](current_state)
                            best_fitness = new_fitness
                            best_hard_violations = new_hard_violations

                            self._log(
                                "debug",
                                f"[Intensification] New best: Hard violations = {best_hard_violations}, Fitness = {best_fitness:.2f}",
                            )

                    if stagnation_counter >= stagnation_limit:
                        intensification_temp = self.config["initial_temperature"] * 0.5
                        stagnation_counter = 0
                        self._log(
                            "debug", "[Intensification] Stagnation detected, reheating"
                        )

                    intensification_temp *= 0.999
                    intensification_iterations += 1
                    iteration += 1

                    if intensification_iterations % 500 == 0:
                        self._log(
                            "info",
                            f"[Intensification] Iter {intensification_iterations}: Hard violations = {current_hard_violations}, Best = {best_hard_violations}",
                        )

                if best_hard_violations == 0:
                    self._log(
                        "info",
                        f"[Intensification] SUCCESS! All hard violations eliminated in attempt {intensification_attempt}",
                    )
                    break

            if best_hard_violations > 0:
                self._log(
                    "warn",
                    f"[Intensification] Could not eliminate all hard violations. Remaining: {best_hard_violations}",
                )

        self._log("info", "Phase 2: Optimizing soft constraints")

        current_state = self.config["clone_state"](best_state)
        current_fitness = best_fitness
        iterations_without_improvement = 0

        while temperature > self.config["min_temperature"] and iteration < self.config["max_iterations"]:
            neighbor_result = self._generate_neighbor(current_state, temperature)

            if not neighbor_result["new_state"]:
                # No valid neighbor generated, try again in next iteration
                iteration += 1
                continue

            new_state = neighbor_result["new_state"]
            operator_name = neighbor_result["operator_name"]

            if self.config["tabu_search_enabled"]:
                new_signature = self._get_state_signature(new_state)
                if self._is_tabu(new_signature, iteration):
                    iteration += 1
                    continue

            self.operator_stats[operator_name]["attempts"] += 1

            new_result = self._calculate_fitness_and_violations(new_state)
            new_fitness = new_result["fitness"]
            new_hard_violations = int(new_result["hard_violations"])

            accept_prob = self._acceptance_probability_phase2(
                int(best_hard_violations),
                new_hard_violations,
                current_fitness,
                new_fitness,
                temperature,
            )

            if random.random() < accept_prob:
                self.operator_stats[operator_name]["accepted"] += 1

                if new_fitness < current_fitness:
                    self.operator_stats[operator_name]["improvements"] += 1

                if self.config["tabu_search_enabled"]:
                    current_signature = self._get_state_signature(current_state)
                    self._add_to_tabu_list(current_signature, iteration)

                current_state = new_state
                current_fitness = new_fitness

                if new_hard_violations < best_hard_violations:
                    best_hard_violations = new_hard_violations
                    self._log(
                        "debug",
                        f"[Phase 2] Hard violations reduced to {best_hard_violations}",
                    )

                if new_fitness < best_fitness:
                    best_state = self.config["clone_state"](current_state)
                    best_fitness = new_fitness
                    iterations_without_improvement = 0

                    self._log(
                        "debug",
                        f"[Phase 2] New best: Fitness = {best_fitness:.2f}, Hard violations = {new_hard_violations}, Operator = {operator_name}",
                    )
                else:
                    iterations_without_improvement += 1
            else:
                iterations_without_improvement += 1

            if (
                self.config["reheating_threshold"] is not None
                and iterations_without_improvement >= self.config["reheating_threshold"]
                and self.config["max_reheats"] > reheats
                and temperature < self.config["initial_temperature"] / 100
            ):
                temperature *= self.config["reheating_factor"]
                reheats += 1
                iterations_without_improvement = 0

                self._log(
                    "info",
                    f"[Phase 2] Reheating #{reheats}: Temperature = {temperature:.2f}, Fitness = {best_fitness:.2f}",
                )

            temperature *= self.config["cooling_rate"]
            iteration += 1

            log_interval2 = self.config["logging"]["log_interval"]
            if iteration % log_interval2 == 0:
                self._log(
                    "info",
                    f"[Phase 2] Iteration {iteration}: Temp = {temperature:.2f}, Current = {current_fitness:.2f}, Best = {best_fitness:.2f}",
                )

        self._update_operator_stats()

        violations = self._get_violations(best_state)
        hard_violations_count = sum(1 for v in violations if v["constraint_type"] == "hard")
        soft_violations_count = sum(1 for v in violations if v["constraint_type"] == "soft")

        self._log(
            "info",
            "Optimization complete",
            {
                "iterations": iteration,
                "reheats": reheats,
                "final_temperature": f"{temperature:.4f}",
                "fitness": f"{best_fitness:.2f}",
                "hard_violations": hard_violations_count,
                "soft_violations": soft_violations_count,
            },
        )

        self._log_operator_stats()

        return {
            "state": best_state,
            "fitness": best_fitness,
            "hard_violations": hard_violations_count,
            "soft_violations": soft_violations_count,
            "iterations": iteration,
            "reheats": reheats,
            "final_temperature": temperature,
            "violations": violations,
            "operator_stats": self.operator_stats,
        }

    def _calculate_fitness_and_violations(
        self, state: TState
    ) -> dict[str, float | int]:
        hard_penalty = 0.0
        soft_penalty = 0.0
        hard_violation_count = 0

        for constraint in self.hard_constraints:
            score = constraint.evaluate(state)
            if score < 1:
                hard_penalty += 1 - score
                violations = constraint.get_violations(state)
                if violations:
                    hard_violation_count += len(violations)
                else:
                    inferred_count = round((1 / score) - 1)
                    hard_violation_count += max(1, inferred_count)

        for constraint in self.soft_constraints:
            score = constraint.evaluate(state)
            weight = constraint.weight or 10
            if score < 1:
                soft_penalty += (1 - score) * weight

        fitness = hard_penalty * self.config["hard_constraint_weight"] + soft_penalty

        return {"fitness": fitness, "hard_violations": hard_violation_count}

    def _generate_neighbor(
        self, state: TState, temperature: float
    ) -> dict[str, Any]:
        applicable_generators = [
            gen for gen in self.move_generators if gen.can_apply(state)
        ]

        if not applicable_generators:
            # Diagnostic logging
            schedule_len = len(state.schedule) if hasattr(state, 'schedule') else 'N/A'
            slots_len = len(state.available_time_slots) if hasattr(state, 'available_time_slots') else 'N/A'
            rooms_len = len(state.rooms) if hasattr(state, 'rooms') else 'N/A'
            self._log("debug", f"No applicable generators. State: schedule={schedule_len}, slots={slots_len}, rooms={rooms_len}")
            return {"new_state": None, "operator_name": ""}

        # Try multiple generators in case one returns None
        # Shuffle to avoid always trying the same generators first
        shuffled_generators = applicable_generators.copy()
        random.shuffle(shuffled_generators)

        for idx, selected_generator in enumerate(shuffled_generators[:3]):  # Try up to 3 generators
            cloned_state = self.config["clone_state"](state)
            new_state = selected_generator.generate(cloned_state, temperature)

            if new_state is not None:
                return {"new_state": new_state, "operator_name": selected_generator.name}

        # All tried generators returned None
        return {"new_state": None, "operator_name": ""}

    def _select_move_generator(
        self, generators: list[Any]
    ) -> Any:
        if random.random() < 0.3:
            return random.choice(generators)

        weights = []
        for gen in generators:
            stats = self.operator_stats[gen.name]
            weights.append(stats["success_rate"] or 0.5)

        total_weight = sum(weights)

        if total_weight == 0:
            return random.choice(generators)

        r = random.random() * total_weight

        for i, w in enumerate(weights):
            r -= w
            if r <= 0:
                return generators[i]

        return generators[-1]

    def _get_state_signature(self, state: TState) -> str:
        schedule = getattr(state, "schedule", None)
        if not schedule or not isinstance(schedule, list):
            return str(random.random())

        assignments = []
        for entry in schedule:
            if (
                hasattr(entry, "class_id")
                and hasattr(entry, "time_slot")
                and hasattr(entry, "room")
            ):
                time_slot = entry.time_slot
                assignments.append(
                    f"{entry.class_id}:{time_slot.day}:{time_slot.start_time}:{entry.room}"
                )

        return "|".join(sorted(assignments))

    def _is_tabu(self, signature: str, current_iteration: int) -> bool:
        if not self.config["tabu_search_enabled"]:
            return False

        added_at = self.tabu_list.get(signature)
        if added_at is None:
            return False

        return (current_iteration - added_at) < self.config["tabu_tenure"]

    def _add_to_tabu_list(self, signature: str, iteration: int) -> None:
        if not self.config["tabu_search_enabled"]:
            return

        self.tabu_list[signature] = iteration

        if len(self.tabu_list) > self.config["max_tabu_list_size"]:
            self._cleanup_tabu_list(iteration)

    def _cleanup_tabu_list(self, current_iteration: int) -> None:
        expired_keys = []

        for key, added_at in self.tabu_list.items():
            if (current_iteration - added_at) >= self.config["tabu_tenure"]:
                expired_keys.append(key)

        for key in expired_keys:
            del self.tabu_list[key]

        if len(self.tabu_list) > self.config["max_tabu_list_size"] * 0.8:
            sorted_items = sorted(self.tabu_list.items(), key=lambda x: x[1])
            to_remove = sorted_items[: int(len(sorted_items) * 0.3)]
            for key, _ in to_remove:
                del self.tabu_list[key]

    def _acceptance_probability_phase1(
        self,
        current_hard_violations: int,
        new_hard_violations: int,
        current_fitness: float,
        new_fitness: float,
        temperature: float,
    ) -> float:
        if new_hard_violations < current_hard_violations:
            return 1.0

        if new_hard_violations == current_hard_violations:
            if new_fitness < current_fitness:
                return 1.0
            return math.exp((current_fitness - new_fitness) / temperature)

        return 0.0

    def _acceptance_probability_phase2(
        self,
        best_hard_violations: int,
        new_hard_violations: int,
        current_fitness: float,
        new_fitness: float,
        temperature: float,
    ) -> float:
        if new_hard_violations > best_hard_violations:
            return 0.0

        if new_hard_violations < best_hard_violations:
            return 1.0

        if new_fitness < current_fitness:
            return 1.0

        return math.exp((current_fitness - new_fitness) / temperature)

    def _get_violations(self, state: TState) -> list[dict[str, Any]]:
        violations: list[dict[str, Any]] = []

        for constraint in self.constraints:
            score = constraint.evaluate(state)

            if score < 1:
                descriptions = constraint.get_violations(state)
                if descriptions:
                    for description in descriptions:
                        violations.append(
                            {
                                "constraint_name": constraint.name,
                                "constraint_type": constraint.type,
                                "score": score,
                                "description": description,
                            }
                        )
                else:
                    description = constraint.describe(state)
                    violations.append(
                        {
                            "constraint_name": constraint.name,
                            "constraint_type": constraint.type,
                            "score": score,
                            "description": description or "",
                        }
                    )

        return violations

    def _update_operator_stats(self) -> None:
        for operator_name in self.operator_stats:
            stats = self.operator_stats[operator_name]
            if stats["attempts"] > 0:
                stats["success_rate"] = stats["improvements"] / stats["attempts"]

    def _log_operator_stats(self) -> None:
        self._log("info", "Operator Statistics:")

        for operator_name in self.operator_stats:
            stats = self.operator_stats[operator_name]
            self._log(
                "info",
                f"  {operator_name}: Attempts = {stats['attempts']}, Improvements = {stats['improvements']}, Accepted = {stats['accepted']}, Success Rate = {stats['success_rate'] * 100:.2f}%",
            )

    def _merge_with_defaults(self, config: SAConfig) -> _MergedConfig:
        logging_config = config.logging
        if logging_config is None:
            logging_config = LoggingConfig()

        return {
            "initial_temperature": config.initial_temperature,
            "min_temperature": config.min_temperature,
            "cooling_rate": config.cooling_rate,
            "max_iterations": config.max_iterations,
            "hard_constraint_weight": config.hard_constraint_weight,
            "clone_state": config.clone_state,
            "reheating_threshold": config.reheating_threshold,
            "reheating_factor": config.reheating_factor or 2.0,
            "max_reheats": config.max_reheats or 3,
            "tabu_search_enabled": config.tabu_search_enabled or False,
            "tabu_tenure": config.tabu_tenure or 50,
            "max_tabu_list_size": config.max_tabu_list_size or 1000,
            "enable_intensification": config.enable_intensification or True,
            "intensification_iterations": config.intensification_iterations or 2000,
            "max_intensification_attempts": config.max_intensification_attempts or 3,
            "logging": {
                "enabled": logging_config.enabled,
                "level": logging_config.level,
                "log_interval": logging_config.log_interval or 1000,
                "output": logging_config.output or "console",
                "file_path": logging_config.file_path or "./sa-optimization.log",
            },
        }

    def _log(
        self, level: str, message: str, data: dict[str, Any] | None = None
    ) -> None:
        logging_config = self.config["logging"]

        if not logging_config["enabled"]:
            return

        log_levels = ["debug", "info", "warn", "error", "none"]
        current_level_index = log_levels.index(logging_config["level"])
        message_level_index = log_levels.index(level)

        if message_level_index < current_level_index:
            return

        timestamp = datetime.now().isoformat()
        if data:
            log_message = f"[{timestamp}] [{level.upper()}] {message} {data}"
        else:
            log_message = f"[{timestamp}] [{level.upper()}] {message}"

        if logging_config["output"] in ("console", "both"):
            print(log_message)

    def get_stats(self) -> OperatorStats:
        """Get current operator statistics."""
        return self.operator_stats
