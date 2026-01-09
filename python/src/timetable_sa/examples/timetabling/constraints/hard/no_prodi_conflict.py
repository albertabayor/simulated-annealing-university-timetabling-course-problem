"""Hard constraint: No Prodi Conflict.

Ensures no study program (prodi) has two classes at the same time.
This is important for students who may need to attend multiple classes.
"""

from typing import Literal, List
from collections import defaultdict

from timetable_sa.core.interfaces import Constraint
from timetable_sa.examples.timetabling.domain_types.state import TimetableState
from timetable_sa.examples.timetabling.utils.time import time_to_minutes
from timetable_sa.examples.timetabling.utils.class_helper import has_class_overlap


class NoProdiConflict(Constraint):
    """Hard constraint: No two classes for the same study program at the same time.
    
    This constraint helps ensure students can attend all their classes.
    
    Examples of violations:
        - MM-1A has two classes on Monday 08:00
        - S1-CS-2B has overlapping classes on Friday
    """
    
    name: str = "No Prodi Conflict"
    type: Literal["hard", "soft"] = "hard"

    def evaluate(self, state: TimetableState) -> float:
        """Evaluate the constraint.
        
        Returns:
            1.0 if no prodi conflicts, lower score otherwise
        """
        conflicts = self._find_conflicts(state)
        
        if not conflicts:
            return 1.0
        
        return 1.0 / (1 + len(conflicts))

    def get_violations(self, state: TimetableState) -> List[str]:
        """Get detailed list of prodi conflicts.
        
        Returns:
            List of violation descriptions
        """
        conflicts = self._find_conflicts(state)
        violations = []
        
        for conflict in conflicts:
            prodi = conflict["prodi"]
            day = conflict["day"]
            time = conflict["time"]
            classes = conflict["classes"]
            
            class_info = [f"{c.class_id} ({c.kelas})" for c in classes]
            violation = f"Prodi {prodi} has conflict on {day} at {time}: {', '.join(class_info)}"
            violations.append(violation)
        
        return violations

    def _find_conflicts(self, state: TimetableState) -> List[dict]:
        """Find all prodi conflicts in the schedule.
        
        Matches TypeScript: uses hasClassOverlap to check class sections.
        Groups by prodi + day, checks time overlap AND class overlap.
        
        Returns:
            List of conflict dictionaries
        """
        # Group by prodi + day - O(N)
        prodi_entries: dict = defaultdict(list)
        
        for entry in state.schedule:
            key = entry.prodi
            prodi_entries[key].append(entry)
        
        conflicts = []
        
        # Check each prodi for conflicts
        for prodi, entries in prodi_entries.items():
            if len(entries) < 2:
                continue
            
            # Sort by day and start time
            sorted_entries = sorted(
                entries,
                key=lambda e: (e.time_slot.day, e.time_slot.start_time)
            )
            
            # Check for overlaps
            for i in range(len(sorted_entries)):
                current = sorted_entries[i]
                end1 = time_to_minutes(current.time_slot.end_time)
                
                # Check subsequent entries for same-day conflicts
                j = i + 1
                same_day_conflicts = []
                
                while j < len(sorted_entries) and sorted_entries[j].time_slot.day == current.time_slot.day:
                    next_entry = sorted_entries[j]
                    start2 = time_to_minutes(next_entry.time_slot.start_time)
                    
                    if start2 >= end1:
                        break
                    
                    if has_class_overlap(current.kelas, next_entry.kelas):
                        same_day_conflicts.append(next_entry)
                    
                    j += 1
                
                if same_day_conflicts:
                    all_conflicting = [current] + same_day_conflicts
                    time_slot = f"{current.time_slot.start_time}-{current.time_slot.end_time}"
                    
                    if not any(
                        c['prodi'] == prodi 
                        and c['day'] == current.time_slot.day 
                        and c['time'] == time_slot
                        for c in conflicts
                    ):
                        conflicts.append({
                            "prodi": prodi,
                            "day": current.time_slot.day,
                            "time": time_slot,
                            "classes": all_conflicting
                        })
        
        return conflicts

    def _entries_overlap(self, entry1, entry2) -> bool:
        """Check if two schedule entries overlap in time."""
        from timetable_sa.examples.timetabling.utils.time import time_to_minutes
        
        start1 = time_to_minutes(entry1.time_slot.start_time)
        end1 = time_to_minutes(entry1.time_slot.end_time)
        start2 = time_to_minutes(entry2.time_slot.start_time)
        end2 = time_to_minutes(entry2.time_slot.end_time)
        
        return max(start1, start2) < min(end1, end2)
