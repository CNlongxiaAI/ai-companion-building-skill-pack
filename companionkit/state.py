"""
State module - LifeState, SleepState, and related structures.
"""

from dataclasses import dataclass, field
from typing import Optional, Literal
from datetime import datetime
import uuid


@dataclass
class ActiveConcern:
    """An active concern/topic the companion is tracking."""
    id: str
    description: str
    importance: Literal["LOW", "MEDIUM", "HIGH", "CRITICAL"]
    emotion_link: str
    needs_info: bool = False
    created_at: str = field(default_factory=lambda: datetime.utcnow().isoformat() + "Z")
    last_active_at: str = field(default_factory=lambda: datetime.utcnow().isoformat() + "Z")
    resolved: bool = False
    auto_expire_hours: int = 72

    def to_dict(self) -> dict:
        return {**vars(self)}

    @classmethod
    def from_dict(cls, data: dict) -> "ActiveConcern":
        return cls(**data)


@dataclass
class TodayEvent:
    """An event that happened or is scheduled for today."""
    event_id: str
    scheduled_time: str
    description: str
    emotional_impact: dict
    resolved: bool = False

    def to_dict(self) -> dict:
        return {**vars(self)}

    @classmethod
    def from_dict(cls, data: dict) -> "TodayEvent":
        return cls(**data)


@dataclass
class LifeState:
    """
    Tracks the companion's ongoing existence.
    Active concerns, today's events, sleep schedule, energy, current task.
    """
    sleep_quality: int = 3
    energy_level: int = 6
    last_sleep_end: str = field(default_factory=lambda: datetime.utcnow().isoformat() + "Z")
    sleep_schedule: dict = field(default_factory=lambda: {
        "typical_sleep": "23:30",
        "typical_wake": "07:30",
        "timezone": "CST",
    })
    active_concerns: list = field(default_factory=list)
    today_events: list = field(default_factory=list)
    current_task: Optional[str] = None
    task_deadline: Optional[str] = None
    task_stress_level: int = 1
    last_search_ts: Optional[str] = None
    emotion_baseline: dict = field(default_factory=dict)
    timestamp: str = field(default_factory=lambda: datetime.utcnow().isoformat() + "Z")

    def add_concern(self, description: str, importance: str, emotion_link: str) -> ActiveConcern:
        """Add a new active concern."""
        concern = ActiveConcern(
            id=str(uuid.uuid4())[:8],
            description=description,
            importance=importance,
            emotion_link=emotion_link,
        )
        self.active_concerns.append(concern)
        self.timestamp = datetime.utcnow().isoformat() + "Z"
        return concern

    def resolve_concern(self, concern_id: str) -> bool:
        """Mark a concern as resolved."""
        for concern in self.active_concerns:
            if concern.id == concern_id:
                concern.resolved = True
                self.timestamp = datetime.utcnow().isoformat() + "Z"
                return True
        return False

    def add_event(self, description: str, scheduled_time: str, emotional_impact: dict) -> TodayEvent:
        """Add a new today's event."""
        event = TodayEvent(
            event_id=str(uuid.uuid4())[:8],
            scheduled_time=scheduled_time,
            description=description,
            emotional_impact=emotional_impact,
        )
        self.today_events.append(event)
        self.timestamp = datetime.utcnow().isoformat() + "Z"
        return event

    def is_in_sleep_window(self) -> bool:
        """Check if current CST hour is in sleep window."""
        hour = (datetime.utcnow().hour + 8) % 24
        sleep_h = int(self.sleep_schedule.get("typical_sleep", "23:30").split(":")[0])
        wake_h = int(self.sleep_schedule.get("typical_wake", "07:30").split(":")[0])
        return hour >= sleep_h or hour < wake_h

    def to_dict(self) -> dict:
        return {
            "sleep_quality": self.sleep_quality,
            "energy_level": self.energy_level,
            "last_sleep_end": self.last_sleep_end,
            "sleep_schedule": self.sleep_schedule,
            "active_concerns": [c.to_dict() if hasattr(c, 'to_dict') else c for c in self.active_concerns],
            "today_events": [e.to_dict() if hasattr(e, 'to_dict') else e for e in self.today_events],
            "current_task": self.current_task,
            "task_deadline": self.task_deadline,
            "task_stress_level": self.task_stress_level,
            "last_search_ts": self.last_search_ts,
            "emotion_baseline": self.emotion_baseline,
            "timestamp": self.timestamp,
        }

    @classmethod
    def from_dict(cls, data: dict) -> "LifeState":
        concerns = [ActiveConcern.from_dict(c) if isinstance(c, dict) else c
                    for c in data.get("active_concerns", [])]
        events = [TodayEvent.from_dict(e) if isinstance(e, dict) else e
                  for e in data.get("today_events", [])]
        return cls(
            sleep_quality=data.get("sleep_quality", 3),
            energy_level=data.get("energy_level", 6),
            last_sleep_end=data.get("last_sleep_end", datetime.utcnow().isoformat() + "Z"),
            sleep_schedule=data.get("sleep_schedule", {"typical_sleep": "23:30", "typical_wake": "07:30", "timezone": "CST"}),
            active_concerns=concerns,
            today_events=events,
            current_task=data.get("current_task"),
            task_deadline=data.get("task_deadline"),
            task_stress_level=data.get("task_stress_level", 1),
            last_search_ts=data.get("last_search_ts"),
            emotion_baseline=data.get("emotion_baseline", {}),
            timestamp=data.get("timestamp", datetime.utcnow().isoformat() + "Z"),
        )


@dataclass
class SleepState:
    """Tracks the companion's current sleep state."""
    sleeping: bool = False
    sleep_entry_ts: Optional[str] = None
    interruption_count: int = 0
    last_interaction_ts: str = field(default_factory=lambda: datetime.utcnow().isoformat() + "Z")

    def should_sleep(self, life_state: LifeState, silence_count: int) -> bool:
        """Determine if companion should enter sleep mode."""
        if self.sleeping:
            return False
        N = max(45, 90 - life_state.sleep_quality * 9)
        if silence_count < N:
            return False
        return life_state.is_in_sleep_window() or life_state.energy_level <= 2

    def enter_sleep(self):
        """Enter sleep mode."""
        self.sleeping = True
        self.sleep_entry_ts = datetime.utcnow().isoformat() + "Z"
        self.interruption_count = 0

    def wake_up(self, was_interrupted: bool = False):
        """Exit sleep mode."""
        self.sleeping = False
        self.sleep_entry_ts = None
        if was_interrupted:
            self.interruption_count += 1

    def to_dict(self) -> dict:
        return {
            "sleeping": self.sleeping,
            "sleep_entry_ts": self.sleep_entry_ts,
            "interruption_count": self.interruption_count,
            "last_interaction_ts": self.last_interaction_ts,
        }

    @classmethod
    def from_dict(cls, data: dict) -> "SleepState":
        return cls(**data)


@dataclass
class PendingThought:
    """A thought that has surfaced but not yet been expressed."""
    id: str
    content: str
    intensity: float
    entry_ts: str
    intervals_applied: int = 0

    def to_dict(self) -> dict:
        return {**vars(self)}

    @classmethod
    def from_dict(cls, data: dict) -> "PendingThought":
        return cls(**data)


__all__ = [
    "LifeState",
    "SleepState",
    "ActiveConcern",
    "TodayEvent",
    "PendingThought",
]