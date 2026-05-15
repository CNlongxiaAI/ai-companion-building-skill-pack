"""
Companion - Main companion class that ties all components together.
"""

from typing import Optional, Callable
from datetime import datetime
import uuid

from companionkit.identity import Identity
from companionkit.state import LifeState, SleepState, PendingThought

try:
    from emotionengine import EmotionEngine, EmotionState
except ImportError:
    EmotionEngine = None
    EmotionState = None


class Companion:
    """
    Main companion class that orchestrates all subsystems.

    Usage:
        companion = Companion(identity=my_identity)
        companion.start()
        response = companion.send("Hello!")
        companion.stop()
    """

    def __init__(
        self,
        identity: Identity,
        llm_provider: str = "mock",
        api_key: Optional[str] = None,
        model: str = "default",
        proactive: bool = False,
        heartbeat_interval: int = 30,
        min_proactive_gap: int = 120,
    ):
        self.identity = identity
        self.llm_provider = llm_provider
        self.api_key = api_key
        self.model = model
        self.proactive = proactive
        self.heartbeat_interval = heartbeat_interval
        self.min_proactive_gap = min_proactive_gap

        # Initialize subsystems
        self.life_state = LifeState()
        self.sleep_state = SleepState()
        self.verifier_commitments: list = []
        self.logical_clock = 0

        # Initialize emotion engine if available
        if EmotionEngine:
            self.emotion_engine = EmotionEngine()
            self.emotion_state = self.emotion_engine.create_state()
        else:
            self.emotion_engine = None
            self.emotion_state = None

        # Session state
        self.session_id = str(uuid.uuid4())[:8]
        self.is_running = False
        self.silence_count = 0
        self.last_proactive_ts: Optional[datetime] = None

        # Pending thoughts queue
        self.pending_thoughts: list[PendingThought] = []

    def start(self, session_id: Optional[str] = None):
        """Start a new session or resume existing."""
        if session_id:
            self.session_id = session_id
        self.is_running = True
        self.silence_count = 0

    def stop(self):
        """Stop the companion."""
        self.is_running = False

    def send(self, message: str, context: dict = None) -> str:
        """
        Send a message and get response.
        """
        if not self.is_running:
            self.start()

        context = context or {}

        # Update interaction
        self.sleep_state.last_interaction_ts = datetime.utcnow().isoformat() + "Z"
        self.silence_count = 0

        # Wake from sleep if sleeping
        if self.sleep_state.sleeping:
            self._wake_from_sleep()

        # Process emotion (simplified)
        if self.emotion_engine and self.emotion_state:
            self.emotion_state = self.emotion_engine.update_emotion(
                self.emotion_state,
                {"trust": 0.5, "joy": 0.3}
            )

        # Record commitment
        self.logical_clock += 1

        # Generate response (mock)
        response = self._generate_response(message, context)

        # Verify response (simplified)
        valid, _ = self.identity.validate_output(response)
        if not valid:
            response = "[Response filtered by self-verification]"

        return response

    def _generate_response(self, message: str, context: dict) -> str:
        """Generate response using configured LLM or mock."""
        # Build system prompt
        emotion_dict = self.emotion_state.to_dict() if self.emotion_state else None
        system_prompt = self.identity.get_system_prompt(
            emotion_state=emotion_dict,
            life_state=self.life_state.to_dict(),
        )

        # In production, would call actual LLM
        # For demo, return a simple response
        return f"[Response to: {message[:30]}... based on {self.identity.name}'s identity]"

    def _wake_from_sleep(self):
        """Handle waking from sleep mode."""
        self.sleep_state.wake_up(was_interrupted=True)
        if self.emotion_engine and self.emotion_state:
            self.emotion_state = self.emotion_engine.update_emotion(
                self.emotion_state,
                {"surprise": 3}
            )

    def think(self):
        """
        Execute a think cycle for proactive behavior.
        """
        if not self.is_running:
            return

        # Apply emotion decay
        if self.emotion_engine and self.emotion_state:
            self.emotion_state = self.emotion_engine.apply_decay(
                self.emotion_state,
                self.heartbeat_interval / 60,
                sleep_mode=self.sleep_state.sleeping,
            )

        # Update pending thoughts intensity
        self._update_pending_thoughts()

        # Check if should sleep
        if self._should_sleep():
            self._enter_sleep()
            return

        # Proactive behavior
        if self.proactive and self._should_proactive():
            self._execute_proactive()

    def _update_pending_thoughts(self):
        """Update intensity of pending thoughts."""
        now = datetime.utcnow()
        updated = []

        for thought in self.pending_thoughts:
            entry_dt = datetime.fromisoformat(thought.entry_ts.replace("Z", "+00:00"))
            elapsed_hours = (now - entry_dt.replace(tzinfo=None)).total_seconds() / 3600
            completed_intervals = int(elapsed_hours / 0.5)

            if completed_intervals > thought.intervals_applied:
                new_intervals = completed_intervals - thought.intervals_applied
                thought.intensity = min(1.0, thought.intensity + 0.05 * new_intervals)
                thought.intervals_applied = completed_intervals

            if thought.intensity >= 0.2 and elapsed_hours < 2:
                updated.append(thought)

        self.pending_thoughts = updated

    def _should_sleep(self) -> bool:
        """Check if should enter sleep mode."""
        if self.sleep_state.sleeping:
            return False
        return self.sleep_state.should_sleep(self.life_state, self.silence_count)

    def _enter_sleep(self):
        """Enter sleep mode."""
        self.sleep_state.enter_sleep()

    def _should_proactive(self) -> bool:
        """Check if should initiate proactive message."""
        now = datetime.utcnow()
        if self.last_proactive_ts:
            gap_seconds = (now - self.last_proactive_ts).total_seconds()
            if gap_seconds < self.min_proactive_gap:
                return False

        if self.life_state.task_stress_level >= 7:
            return False

        if self.pending_thoughts:
            max_intensity = max(t.intensity for t in self.pending_thoughts)
            if max_intensity >= 0.7:
                return True

        if self.emotion_state:
            top_emotion = max(self.emotion_state.emotions.values())
            if top_emotion >= 18:
                return True

        return False

    def _execute_proactive(self):
        """Execute a proactive message."""
        if self.pending_thoughts:
            thought = max(self.pending_thoughts, key=lambda t: t.intensity)
            content = thought.content
            self.pending_thoughts.remove(thought)
        else:
            content = "Just thinking about something..."

        self.last_proactive_ts = datetime.utcnow()
        # In production, would generate and send

    def add_pending_thought(self, content: str, intensity: float = 0.5):
        """Add a thought to the pending queue."""
        thought = PendingThought(
            id=str(uuid.uuid4())[:8],
            content=content,
            intensity=intensity,
            entry_ts=datetime.utcnow().isoformat() + "Z",
            intervals_applied=0,
        )
        self.pending_thoughts.append(thought)

    def get_emotion_state(self):
        """Get current emotion state."""
        if self.emotion_engine and self.emotion_state:
            return self.emotion_engine.get_current_state(self.emotion_state)
        return self.emotion_state

    def get_life_state(self):
        """Get current life state."""
        return self.life_state

    def get_state(self) -> dict:
        """Get complete state for serialization."""
        return {
            "session_id": self.session_id,
            "life_state": self.life_state.to_dict(),
            "sleep_state": self.sleep_state.to_dict(),
            "emotion_state": self.emotion_state.to_dict() if self.emotion_state else None,
            "pending_thoughts": [t.to_dict() for t in self.pending_thoughts],
        }

    def restore(self, state: dict):
        """Restore from serialized state."""
        self.session_id = state.get("session_id", self.session_id)
        if "life_state" in state:
            self.life_state = LifeState.from_dict(state["life_state"])
        if "sleep_state" in state:
            self.sleep_state = SleepState.from_dict(state["sleep_state"])
        if "emotion_state" in state and state["emotion_state"] and self.emotion_engine:
            self.emotion_state = self.emotion_engine.deserialize(state["emotion_state"])
        if "pending_thoughts" in state:
            self.pending_thoughts = [PendingThought.from_dict(t) for t in state["pending_thoughts"]]


__all__ = ["Companion"]