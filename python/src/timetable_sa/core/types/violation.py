"""
Violation type representing a constraint violation.
"""

from typing import TypedDict, Literal, Optional


class Violation(TypedDict):
    constraint_name: str
    constraint_type: Literal["hard", "soft"]
    score: float
    description: Optional[str]
