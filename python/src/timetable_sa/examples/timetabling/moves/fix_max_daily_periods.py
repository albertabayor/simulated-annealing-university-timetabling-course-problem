"""Move generator to fix max daily periods violations."""

import random
from typing import Optional
from timetable_sa.core.interfaces import MoveGenerator
from timetable_sa.examples.timetabling.domain_types.state import TimetableState, ScheduleEntry
from timetable_sa.examples.timetabling.domain_types.domain import TimeSlot
from timetable_sa.examples.timetabling.utils.time import calculate_end_time
from timetable_sa.examples.timetabling.utils.initial_solution import clone_state


class FixMaxDailyPeriods(MoveGenerator):
    """Move generator that redistributes classes to fix max daily periods violations.
    
    This targets lecturers who have too many classes on a single day and
    moves some to other days.
    """
    
    name: str = "Fix Max Daily Periods"
    
    def __init__(self, max_daily_periods: int = 6):
        """Initialize fix max daily periods move generator.
        
        Args:
            max_daily_periods: Maximum allowed periods per day
        """
        self.max_daily_periods = max_daily_periods
    
    def can_apply(self, state: TimetableState) -> bool:
        """Check if this move can be applied."""
        return len(state.schedule) > 0
    
    def generate(self, state: TimetableState, temperature: float) -> Optional[TimetableState]:
        """Generate a new state with max daily periods violation fixed."""
        if not self.can_apply(state):
            return None
        
        violations = self._find_violations(state)
        
        if not violations:
            return None
        
        lecturer_day_key = random.choice(list(violations.keys()))
        entries_to_move = violations[lecturer_day_key]
        
        entry_to_move = random.choice(entries_to_move)
        target_days = self._get_target_days(lecturer_day_key.split("|")[1])
        
        for target_day in target_days:
            new_time_slots = self._find_available_slots(entry_to_move, state, target_day)
            
            if new_time_slots:
                new_time_slot = random.choice(new_time_slots)
                new_state = clone_state(state)
                
                for i, e in enumerate(new_state.schedule):
                    if e.class_id == entry_to_move.class_id and e.kelas == entry_to_move.kelas:
                        end_time, _ = calculate_end_time(new_time_slot.start_time, e.sks, new_time_slot.day)
                        
                        new_state.schedule[i] = ScheduleEntry(
                            class_id=e.class_id,
                            class_name=e.class_name,
                            kelas=e.kelas,
                            prodi=e.prodi,
                            lecturers=e.lecturers,
                            room=e.room,
                            time_slot=TimeSlot(
                                day=new_time_slot.day,
                                start_time=new_time_slot.start_time,
                                end_time=end_time,
                                period=new_time_slot.period
                            ),
                            sks=e.sks,
                            needs_lab=e.needs_lab,
                            participants=e.participants,
                            class_type=e.class_type,
                            prayer_time_added=e.prayer_time_added,
                            is_overflow_to_lab=e.is_overflow_to_lab,
                        )
                        break
                
                return new_state
        
        return None
    
    def _find_violations(self, state: TimetableState) -> dict:
        """Find lecturer/day combinations that exceed max daily periods."""
        lecturer_day_counts: dict = {}
        
        for entry in state.schedule:
            for lecturer in entry.lecturers:
                key = (lecturer, entry.time_slot.day)
                if key not in lecturer_day_counts:
                    lecturer_day_counts[key] = []
                lecturer_day_counts[key].append(entry)
        
        violations = {}
        for (lecturer, day), entries in lecturer_day_counts.items():
            if len(entries) > self.max_daily_periods:
                key = f"{lecturer}|{day}"
                violations[key] = entries
        
        return violations
    
    def _get_target_days(self, current_day: str) -> list:
        """Get list of alternative days to move classes to."""
        all_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
        return [d for d in all_days if d != current_day]
    
    def _find_available_slots(
        self,
        entry: ScheduleEntry,
        state: TimetableState,
        target_day: str
    ) -> list:
        """Find available time slots on target day."""
        available = []
        
        for slot in state.available_time_slots:
            if slot.day != target_day:
                continue
            
            room_conflict = any(
                e.room == entry.room and
                e.time_slot.day == target_day and
                e.time_slot.period == slot.period
                for e in state.schedule
            )
            
            lecturer_conflict = any(
                e.lecturers and entry.lecturers and
                e.lecturers[0] == entry.lecturers[0] and
                e.time_slot.day == target_day and
                e.time_slot.period == slot.period
                for e in state.schedule
            )
            
            prodi_conflict = any(
                e.prodi == entry.prodi and
                e.time_slot.day == target_day and
                e.time_slot.period == slot.period
                for e in state.schedule
            )
            
            if not room_conflict and not lecturer_conflict and not prodi_conflict:
                available.append(slot)
        
        return available
