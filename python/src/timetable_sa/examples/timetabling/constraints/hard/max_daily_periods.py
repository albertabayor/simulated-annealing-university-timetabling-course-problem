"""Hard constraint: Maximum Daily Periods.

Ensures lecturers do not exceed their maximum daily teaching periods.
"""

from typing import Literal, List
from collections import defaultdict

from timetable_sa.core.interfaces import Constraint
from timetable_sa.examples.timetabling.domain_types.state import TimetableState


class MaxDailyPeriods(Constraint):
    """Hard constraint: Lecturer cannot exceed maximum daily teaching periods.
    
    Each lecturer has a max_daily_periods limit to prevent overwork.
    
    Examples of violations:
        - Lecturer with max 6 periods teaching 8 classes in one day
        - Evening lecturer scheduled for full day when they prefer evenings
    """
    
    name: str = "Max Daily Periods"
    type: Literal["hard", "soft"] = "hard"

    def evaluate(self, state: TimetableState) -> float:
        """Evaluate the constraint.
        
        Returns:
            1.0 if no lecturer exceeds their limit, lower score otherwise
        """
        violations = self._find_violations(state)
        
        if not violations:
            return 1.0
        
        # Calculate severity based on how much limit is exceeded
        total_overflow = sum(v["overflow"] for v in violations)
        return 1.0 / (1 + total_overflow)

    def get_violations(self, state: TimetableState) -> List[str]:
        """Get detailed list of daily period violations.
        
        Returns:
            List of violation descriptions
        """
        violations = self._find_violations(state)
        descriptions = []
        
        for v in violations:
            descriptions.append(
                f"Lecturer {v['lecturer']} on {v['day']}: "
                f"{v['periods']} periods (limit: {v['limit']}, overflow: {v['overflow']})"
            )
        
        return descriptions

    def _find_violations(self, state: TimetableState) -> List[dict]:
        """Find all daily period limit violations.
        
        Returns:
            List of violation dictionaries
        """
        # Build lecturer lookup
        lecturer_by_code = {lect.code: lect for lect in state.lecturers}
        
        # Count periods per (lecturer, day)
        periods_count: dict = defaultdict(int)
        
        for entry in state.schedule:
            for lecturer in entry.lecturers:
                key = (lecturer, entry.time_slot.day)
                periods_count[key] += entry.sks
        
        # Check against limits
        violations = []
        
        for (lecturer_code, day), periods in periods_count.items():
            lecturer = lecturer_by_code.get(lecturer_code)
            if lecturer:
                limit = lecturer.max_daily_periods
                if periods > limit:
                    violations.append({
                        "lecturer": lecturer_code,
                        "day": day,
                        "periods": periods,
                        "limit": limit,
                        "overflow": periods - limit,
                    })
        
        return violations
