"""Soft constraint: Compactness.

Minimizes gaps between classes for each study program on each day.
Students prefer having consecutive classes with minimal waiting time.
"""

from typing import Literal, List
from collections import defaultdict

from timetable_sa.core.interfaces import Constraint
from timetable_sa.examples.timetabling.domain_types.state import TimetableState
from timetable_sa.examples.timetabling.utils.time import time_to_minutes


class Compactness(Constraint):
    """Soft constraint: Minimize gaps between classes for each prodi on each day.
    
    This constraint penalizes schedules with large gaps between classes.
    Students prefer compact schedules where classes are close together.
    
    Scoring:
        - All classes consecutive with <= 60 min gap: score = 1.0
        - Some gaps > 60 min: score decreases
        - Many large gaps: score approaches 0
    """
    
    name: str = "Compactness"
    type: Literal["hard", "soft"] = "soft"
    weight: float = 8.0

    def __init__(self, weight: float = 8.0):
        self.name = "Compactness"
        self.type = "soft"
        self.weight = weight

    def evaluate(self, state: TimetableState) -> float:
        """Evaluate the compactness of the schedule.
        
        Returns:
            Score between 0 and 1, where 1 means perfectly compact
        """
        if not state.schedule:
            return 1.0
        
        total_gap_penalty = 0.0
        total_class_pairs = 0
        
        # Group entries by (prodi, day)
        prodi_day_entries: dict = defaultdict(list)
        
        for entry in state.schedule:
            key = (entry.prodi, entry.time_slot.day)
            prodi_day_entries[key].append(entry)
        
        # Calculate gaps for each (prodi, day)
        for (prodi, day), entries in prodi_day_entries.items():
            if len(entries) < 2:
                continue
            
            # Sort by start time
            sorted_entries = sorted(
                entries,
                key=lambda e: time_to_minutes(e.time_slot.start_time)
            )
            
            # Calculate gaps between consecutive classes
            for i in range(len(sorted_entries) - 1):
                current = sorted_entries[i]
                next_entry = sorted_entries[i + 1]
                
                current_end = time_to_minutes(current.time_slot.end_time)
                next_start = time_to_minutes(next_entry.time_slot.start_time)
                
                gap = next_start - current_end
                
                # Penalize gaps > 60 minutes
                if gap > 60:
                    total_gap_penalty += (gap - 60) / 60.0  # Normalize
                
                total_class_pairs += 1
        
        if total_class_pairs == 0:
            return 1.0
        
        # Calculate average penalty
        avg_penalty = total_gap_penalty / total_class_pairs
        
        # Score = 1 / (1 + penalty)
        return 1.0 / (1.0 + avg_penalty)

    def get_violations(self, state: TimetableState) -> List[str]:
        """Get list of large gaps between classes.
        
        Returns:
            List of violation descriptions
        """
        violations = []
        
        # Group entries by (prodi, day)
        prodi_day_entries: dict = defaultdict(list)
        
        for entry in state.schedule:
            key = (entry.prodi, entry.time_slot.day)
            prodi_day_entries[key].append(entry)
        
        # Find large gaps
        for (prodi, day), entries in prodi_day_entries.items():
            if len(entries) < 2:
                continue
            
            sorted_entries = sorted(
                entries,
                key=lambda e: time_to_minutes(e.time_slot.start_time)
            )
            
            for i in range(len(sorted_entries) - 1):
                current = sorted_entries[i]
                next_entry = sorted_entries[i + 1]
                
                current_end = time_to_minutes(current.time_slot.end_time)
                next_start = time_to_minutes(next_entry.time_slot.start_time)
                
                gap = next_start - current_end
                
                if gap > 60:
                    violations.append(
                        f"Prodi {prodi} on {day}: Gap of {gap} min between "
                        f"{current.class_id} ({current.time_slot.end_time}) and "
                        f"{next_entry.class_id} ({next_entry.time_slot.start_time})"
                    )
        
        return violations
