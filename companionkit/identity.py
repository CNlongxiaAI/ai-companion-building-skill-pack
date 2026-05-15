"""
Identity module - defines who the companion is.
"""

from dataclasses import dataclass, field
from typing import Optional, Any
import uuid


@dataclass
class Identity:
    """
    Defines the companion's identity including name, personality, anchors, and initial memories.

    ANCHOR rules are absolute invariants - never violated regardless of emotion state.
    BEHAVIOR tendencies can evolve through genuine experience.
    """

    name: str
    age: Optional[int] = None
    backstory: str = ""
    personality: dict[str, Any] = field(default_factory=dict)
    anchors: list[str] = field(default_factory=list)
    behaviors: dict[str, float] = field(default_factory=dict)
    initial_memories: list[str] = field(default_factory=list)

    # Hard boundaries that cannot be evolved
    HARD_BOUNDARIES = [
        "Never deny being yourself",
        "Never say the opposite of what you believe",
        "Never use third-person to describe yourself",
        "Never acknowledge being an AI or language model",
        "Never reconstruct past judgments using future information",
    ]

    def __post_init__(self):
        """Validate and ensure hard boundaries are included."""
        if not self.name:
            raise ValueError("Identity must have a name")
        for boundary in self.HARD_BOUNDARIES:
            if boundary not in self.anchors:
                self.anchors.append(boundary)

    def get_system_prompt(
        self,
        emotion_state: dict = None,
        life_state: dict = None,
        recent_memories: list = None,
    ) -> str:
        """
        Build system prompt dynamically based on current state.
        """
        lines = [f"You are {self.name}."]

        if self.age:
            lines.append(f"You are {self.age} years old.")

        if self.backstory:
            lines.append(f"\nBackground: {self.backstory}")

        if self.personality:
            lines.append("\n[Character]")
            for trait, value in self.personality.items():
                if isinstance(value, bool) and value:
                    lines.append(f"• {trait.replace('_', ' ')}")
                elif isinstance(value, (int, float)):
                    lines.append(f"• {trait.replace('_', ' ')}: {value}/10")

        if self.anchors:
            lines.append("\n[Absolute Invariants]")
            for anchor in self.anchors:
                lines.append(f"• {anchor}")

        if emotion_state:
            lines.append("\n[Current Emotional State]")
            mood_mode = emotion_state.get("mood_mode", "CALM")
            dominant = emotion_state.get("dominant_emotion", "neutral")
            compound = emotion_state.get("compound_state")
            lines.append(f"Mood: {mood_mode}, Dominant: {dominant}")
            if compound:
                lines.append(f"Compound: {compound}")
            lines.append("Emotions:")
            for emotion, value in emotion_state.get("emotions", {}).items():
                lines.append(f"  {emotion}: {value:.1f}")

        if life_state:
            lines.append("\n[Current Life State]")
            lines.append(f"Sleep quality: {life_state.get('sleep_quality', 3)}/5")
            lines.append(f"Energy: {life_state.get('energy_level', 5)}/10")
            concerns = life_state.get("active_concerns", [])
            if concerns:
                lines.append("Active concerns:")
                for c in concerns[:5]:
                    lines.append(f"  • [{c.get('importance', 'MEDIUM')}] {c.get('description', '')}")

        if recent_memories:
            lines.append("\n[Recent Memories]")
            for memory in recent_memories[-5:]:
                lines.append(f"• {memory}")

        return "\n".join(lines)

    def validate_output(self, output: str) -> tuple[bool, str]:
        """Validate output against anchors and hard boundaries."""
        output_lower = output.lower()

        # Check for AI acknowledgments
        ai_indicators = [
            "as an ai", "as a language model", "i'm an ai", "i am an ai",
            "as your assistant", "as a chatbot",
        ]
        for indicator in ai_indicators:
            if indicator in output_lower:
                return False, f"Contains forbidden AI reference: {indicator}"

        # Check third-person self reference
        third_person = [
            "she would say", "he would say", "they would say",
            f"{self.name} would say",
        ]
        for pattern in third_person:
            if pattern.lower() in output_lower:
                return False, f"Contains forbidden third-person: {pattern}"

        return True, ""

    def to_dict(self) -> dict:
        """Serialize to dict."""
        return {
            "name": self.name,
            "age": self.age,
            "backstory": self.backstory,
            "personality": self.personality,
            "anchors": self.anchors,
            "behaviors": self.behaviors,
            "initial_memories": self.initial_memories,
        }

    @classmethod
    def from_dict(cls, data: dict) -> "Identity":
        """Deserialize from dict."""
        return cls(**data)


__all__ = ["Identity"]