"""Performance profiling utilities for timetable optimization."""

import time
from typing import Dict, Any, Callable, List, Optional
from functools import wraps
import cProfile
import pstats
import io


class PerformanceProfiler:
    """Profile and analyze performance of timetable optimization."""
    
    def __init__(self):
        """Initialize profiler."""
        self.metrics: Dict[str, Dict[str, Any]] = {}
        self.timings: List[Dict[str, Any]] = []
    
    def profile_function(self, func: Callable) -> Callable:
        """Decorator to profile a function's execution time.
        
        Args:
            func: Function to profile
            
        Returns:
            Wrapped function that tracks execution time
        """
        @wraps(func)
        def wrapper(*args, **kwargs):
            start_time = time.perf_counter()
            result = func(*args, **kwargs)
            end_time = time.perf_counter()
            
            elapsed_ms = (end_time - start_time) * 1000
            
            if func.__name__ not in self.metrics:
                self.metrics[func.__name__] = {
                    "calls": 0,
                    "total_time_ms": 0,
                    "avg_time_ms": 0,
                    "min_time_ms": float("inf"),
                    "max_time_ms": 0,
                }
            
            self.metrics[func.__name__]["calls"] += 1
            self.metrics[func.__name__]["total_time_ms"] += elapsed_ms
            self.metrics[func.__name__]["avg_time_ms"] = (
                self.metrics[func.__name__]["total_time_ms"] / 
                self.metrics[func.__name__]["calls"]
            )
            self.metrics[func.__name__]["min_time_ms"] = min(
                self.metrics[func.__name__]["min_time_ms"], elapsed_ms
            )
            self.metrics[func.__name__]["max_time_ms"] = max(
                self.metrics[func.__name__]["max_time_ms"], elapsed_ms
            )
            
            return result
        
        return wrapper
    
    def profile_constraint_evaluation(
        self,
        constraint_name: str,
        evaluate_func: Callable,
        state,
        iterations: int = 100
    ) -> Dict[str, Any]:
        """Profile constraint evaluation performance.
        
        Args:
            constraint_name: Name of the constraint
            evaluate_func: Constraint evaluate method
            state: State to evaluate
            iterations: Number of iterations for averaging
            
        Returns:
            Dictionary with profiling results
        """
        times = []
        score = 0.0
        
        for _ in range(iterations):
            start = time.perf_counter()
            score = evaluate_func(state)
            end = time.perf_counter()
            times.append((end - start) * 1000)
        
        return {
            "constraint": constraint_name,
            "iterations": iterations,
            "avg_time_ms": sum(times) / len(times),
            "min_time_ms": min(times),
            "max_time_ms": max(times),
            "score": score,
        }
    
    def profile_move_generation(
        self,
        move_name: str,
        generate_func: Callable,
        state,
        iterations: int = 100
    ) -> Dict[str, Any]:
        """Profile move generator performance.
        
        Args:
            move_name: Name of the move generator
            generate_func: Move generator generate method
            state: State to operate on
            iterations: Number of iterations for averaging
            
        Returns:
            Dictionary with profiling results
        """
        times = []
        success_count = 0
        
        for _ in range(iterations):
            start = time.perf_counter()
            new_state = generate_func(state, temperature=1000.0)
            end = time.perf_counter()
            times.append((end - start) * 1000)
            
            if new_state is not None:
                success_count += 1
        
        return {
            "move": move_name,
            "iterations": iterations,
            "success_rate": success_count / iterations * 100,
            "avg_time_ms": sum(times) / len(times) if times else 0,
            "min_time_ms": min(times) if times else 0,
            "max_time_ms": max(times) if times else 0,
        }
    
    def profile_optimization_run(
        self,
        optimize_func: Callable,
        state,
        constraints,
        move_generators,
        config,
        iterations: int = 1
    ) -> Dict[str, Any]:
        """Profile a complete optimization run.
        
        Args:
            optimize_func: SA solve method
            state: Initial state
            constraints: List of constraints
            move_generators: List of move generators
            config: SA configuration
            iterations: Number of runs to average
            
        Returns:
            Dictionary with profiling results
        """
        total_times = []
        results = []
        
        for _ in range(iterations):
            start = time.perf_counter()
            result = optimize_func(state, constraints, move_generators, config)
            end = time.perf_counter()
            total_times.append((end - start) * 1000)
            results.append(result)
        
        return {
            "iterations": iterations,
            "avg_time_ms": sum(total_times) / len(total_times),
            "min_time_ms": min(total_times),
            "max_time_ms": max(total_times),
            "avg_hard_violations": sum(r.hard_violations for r in results) / len(results),
            "avg_soft_violations": sum(r.soft_violations for r in results) / len(results),
            "avg_fitness": sum(r.fitness for r in results) / len(results),
            "avg_iterations": sum(r.iterations for r in results) / len(results),
        }
    
    def get_summary(self) -> str:
        """Get a formatted summary of all profiled metrics.
        
        Returns:
            Formatted summary string
        """
        if not self.metrics:
            return "No profiling data collected."
        
        lines = ["=" * 60]
        lines.append("PERFORMANCE PROFILING SUMMARY")
        lines.append("=" * 60)
        
        # Sort by total time
        sorted_metrics = sorted(
            self.metrics.items(),
            key=lambda x: x[1]["total_time_ms"],
            reverse=True
        )
        
        for name, data in sorted_metrics:
            lines.append(f"\n{name}:")
            lines.append(f"  Calls: {data['calls']}")
            lines.append(f"  Total: {data['total_time_ms']:.2f}ms")
            lines.append(f"  Avg: {data['avg_time_ms']:.4f}ms")
            lines.append(f"  Min: {data['min_time_ms']:.4f}ms")
            lines.append(f"  Max: {data['max_time_ms']:.4f}ms")
        
        lines.append("\n" + "=" * 60)
        
        return "\n".join(lines)
    
    def reset(self):
        """Reset all profiling data."""
        self.metrics = {}
        self.timings = []


def profile_with_cprofile(func: Callable) -> Callable:
    """Decorator to profile a function using cProfile.
    
    Args:
        func: Function to profile
        
    Returns:
        Wrapped function with profiling enabled
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        profiler = cProfile.Profile()
        profiler.enable()
        
        result = func(*args, **kwargs)
        
        profiler.disable()
        
        s = io.StringIO()
        ps = pstats.Stats(profiler, stream=s).sort_stats('cumulative')
        ps.print_stats(20)
        
        print("\n" + "=" * 60)
        print("CPROFILE RESULTS")
        print("=" * 60)
        print(s.getvalue())
        
        return result
    
    return wrapper


class ConstraintPerformanceTracker:
    """Track performance of individual constraints."""
    
    def __init__(self):
        """Initialize tracker."""
        self.evaluation_times: Dict[str, List[float]] = {}
        self.violation_counts: Dict[str, List[int]] = {}
    
    def track_evaluation(self, constraint_name: str, time_ms: float):
        """Track evaluation time for a constraint.
        
        Args:
            constraint_name: Name of the constraint
            time_ms: Evaluation time in milliseconds
        """
        if constraint_name not in self.evaluation_times:
            self.evaluation_times[constraint_name] = []
        self.evaluation_times[constraint_name].append(time_ms)
    
    def track_violations(self, constraint_name: str, count: int):
        """Track violation count for a constraint.
        
        Args:
            constraint_name: Name of the constraint
            count: Number of violations
        """
        if constraint_name not in self.violation_counts:
            self.violation_counts[constraint_name] = []
        self.violation_counts[constraint_name].append(count)
    
    def get_constraint_stats(self, constraint_name: str) -> Optional[Dict[str, Any]]:
        """Get statistics for a specific constraint.
        
        Args:
            constraint_name: Name of the constraint
            
        Returns:
            Dictionary with statistics or None if not found
        """
        times = self.evaluation_times.get(constraint_name)
        violations = self.violation_counts.get(constraint_name)
        
        if not times:
            return None
        
        return {
            "name": constraint_name,
            "avg_evaluation_ms": sum(times) / len(times),
            "min_evaluation_ms": min(times),
            "max_evaluation_ms": max(times),
            "total_evaluations": len(times),
            "avg_violations": sum(violations) / len(violations) if violations else 0,
        }
    
    def get_report(self) -> str:
        """Generate a performance report.
        
        Returns:
            Formatted report string
        """
        lines = ["=" * 70]
        lines.append("CONSTRAINT PERFORMANCE REPORT")
        lines.append("=" * 70)
        
        for name in self.evaluation_times.keys():
            stats = self.get_constraint_stats(name)
            if stats:
                lines.append(f"\n{stats['name']}:")
                lines.append(f"  Total evaluations: {stats['total_evaluations']}")
                lines.append(f"  Avg evaluation time: {stats['avg_evaluation_ms']:.4f}ms")
                lines.append(f"  Min evaluation time: {stats['min_evaluation_ms']:.4f}ms")
                lines.append(f"  Max evaluation time: {stats['max_evaluation_ms']:.4f}ms")
                lines.append(f"  Avg violations: {stats['avg_violations']:.2f}")
        
        lines.append("\n" + "=" * 70)
        
        return "\n".join(lines)
    
    def reset(self):
        """Reset all tracking data."""
        self.evaluation_times = {}
        self.violation_counts = {}
