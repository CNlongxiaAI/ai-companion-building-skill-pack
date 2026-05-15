"""
CompanionKit - Self-developed AI companion framework.

Author: Self-developed
License: MIT
"""

from companionkit.companion import Companion
from companionkit.identity import Identity
from companionkit.state import LifeState, SleepState, ActiveConcern, PendingThought

__version__ = "1.0.0"

__all__ = [
    "Companion",
    "Identity",
    "LifeState",
    "SleepState",
    "ActiveConcern",
    "PendingThought",
]