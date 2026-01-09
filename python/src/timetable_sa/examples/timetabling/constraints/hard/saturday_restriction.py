"""Saturday restriction constraint."""

from typing import Literal, List
from timetable_sa.core.interfaces import Constraint
from timetable_sa.examples.timetabling.domain_types.state import TimetableState


class SaturdayRestriction(Constraint):
    """Constraint that prevents non-Magister Manajemen classes on Saturday.
    
    Matches TypeScript: allows ONLY Magister Manajemen on Saturday.
    """
    
    name: str = "Saturday Restriction"
    type: Literal["hard", "soft"] = "hard"
    
    def evaluate(self, state: TimetableState) -> float:
        """Check if non-Magister Manajemen classes are scheduled on Saturday.
        
        Matches TypeScript: allows ONLY Magister Manajemen on Saturday.
        
        Args:
            state: Current timetable state
            
        Returns:
            1.0 if no violations, lower score otherwise
        """
        violations = self._find_violations(state)
        
        if not violations:
            return 1.0
        
        return 1.0 / (1 + len(violations))
    
    def get_violations(self, state: TimetableState) -> List[str]:
        """Get list of Saturday scheduling violations.
        
        Args:
            state: Current timetable state
            
        Returns:
            List of violation descriptions
        """
        violations = self._find_violations(state)
        descriptions = []
        
        for v in violations:
            descriptions.append(
                f"Class {v['class_id']} ({v['kelas']}) scheduled on Saturday "
                f"but prodi '{v['prodi']}' is not Magister Manajemen"
            )
        
        return descriptions
    
    def _find_violations(self, state: TimetableState) -> List[dict]:
        """Find all Saturday violations for non-Magister Manajemen classes.
        
        Matches TypeScript: check if prodi includes 'magister manajemen'.
        
        Returns:
            List of violation dictionaries
        """
        violations = []
        
        for entry in state.schedule:
            if entry.time_slot.day == "Saturday":
                is_magister_manajemen = 'magister manajemen' in entry.prodi.lower()
                if not is_magister_manajemen:
                    violations.append({
                        'class_id': entry.class_id,
                        'kelas': entry.kelas,
                        'prodi': entry.prodi,
                        'day': entry.time_slot.day,
                    })
        
        return violations
    
    def describe(self, state: TimetableState) -> str | None:
        """Provide human-readable description of violations.
        
        Matches TypeScript behavior for Saturday restriction.
        
        Args:
            state: Current timetable state
            
        Returns:
            Description of violations, or None if satisfied
        """
        violations = self._find_violations(state)
        
        if not violations:
            return None
        
        if len(violations) == 1:
            return f"1 class on Saturday from non-Magister Manajemen prodi"
        return f"{len(violations)} classes on Saturday from non-Magister Manajemen prodi"
