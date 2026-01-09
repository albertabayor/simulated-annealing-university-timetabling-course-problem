"""Hard constraint: No Room Conflict.

Ensures no two classes are assigned to the same room at the same time.
"""

from typing import Literal, List
from collections import defaultdict

from timetable_sa.core.interfaces import Constraint
from timetable_sa.examples.timetabling.domain_types.state import TimetableState


class NoRoomConflict(Constraint):
    """Hard constraint: No two classes can share the same room at the same time.
    
    This is a fundamental constraint - room conflicts make a schedule invalid.
    
    Examples of violations:
        - Two classes in Room A on Monday 08:00-09:50
        - Three classes in Room B on Friday 18:30-21:00
    """
    
    name: str = "No Room Conflict"
    type: Literal["hard", "soft"] = "hard"

    def evaluate(self, state: TimetableState) -> float:
        """Evaluate the constraint.
        
        Returns:
            1.0 if no room conflicts, lower score otherwise
        """
        conflicts = self._find_conflicts(state)
        
        if not conflicts:
            return 1.0
        
        # Score decreases with number of conflicts
        # Using 1/(1+n) formula for gradual penalty
        return 1.0 / (1 + len(conflicts))

    def get_violations(self, state: TimetableState) -> List[str]:
        """Get detailed list of room conflicts.
        
        Returns:
            List of violation descriptions
        """
        conflicts = self._find_conflicts(state)
        violations = []
        
        for conflict in conflicts:
            entries = conflict["entries"]
            room = conflict["room"]
            day = conflict["day"]
            time = conflict["time"]
            
            class_names = [e.class_id for e in entries]
            violation = f"Room {room} has conflict on {day} at {time}: {', '.join(class_names)}"
            violations.append(violation)
        
        return violations

    def _find_conflicts(self, state: TimetableState) -> List[dict]:
        """Find all room conflicts in the schedule.
        
        Uses O(N log N) approach: group by (day, room) then check for overlaps.
        """
        # Group entries by (day, room)
        by_day_room: dict = defaultdict(list)
        
        for entry in state.schedule:
            key = (entry.time_slot.day, entry.room)
            by_day_room[key].append(entry)
        
        conflicts = []
        
        # Check each group for time overlaps
        for (day, room), entries in by_day_room.items():
            if len(entries) < 2:
                continue
            
            # Sort by start time
            sorted_entries = sorted(
                entries,
                key=lambda e: e.time_slot.start_time
            )
            
            # Check for overlaps using two-pointer / short-circuit approach
            for i in range(len(sorted_entries) - 1):
                current = sorted_entries[i]
                next_entry = sorted_entries[i + 1]
                
                # Check if next entry starts before current ends
                if self._entries_overlap(current, next_entry):
                    # Find all entries overlapping at this time
                    overlapping = [current]
                    j = i + 1
                    while j < len(sorted_entries) and self._entries_overlap(current, sorted_entries[j]):
                        overlapping.append(sorted_entries[j])
                        j += 1
                    
                    # Add to conflicts if not already recorded
                    time_slot = f"{current.time_slot.start_time}-{current.time_slot.end_time}"
                    
                    if not any(
                        c["room"] == room and c["day"] == day and c["time"] == time_slot
                        for c in conflicts
                    ):
                        conflicts.append({
                            "room": room,
                            "day": day,
                            "time": time_slot,
                            "entries": overlapping
                        })
        
        return conflicts

    def _entries_overlap(self, entry1, entry2) -> bool:
        """Check if two schedule entries overlap in time."""
        if entry1.time_slot.day != entry2.time_slot.day:
            return False
        
        from timetable_sa.examples.timetabling.utils.time import time_to_minutes
        
        start1 = time_to_minutes(entry1.time_slot.start_time)
        end1 = time_to_minutes(entry1.time_slot.end_time)
        start2 = time_to_minutes(entry2.time_slot.start_time)
        end2 = time_to_minutes(entry2.time_slot.end_time)
        
        # Overlap if max(start1, start2) < min(end1, end2)
        return max(start1, start2) < min(end1, end2)
