# CompanionKit

A self-developed Python framework for building emotionally intelligent AI companions. Implements identity anchors, emotion engine, four-layer memory, self-verification, and proactive behavior.

## Features

- **Identity System**: ANCHOR rules (absolute invariants) + BEHAVIOR tendencies (evolvable)
- **Emotion Engine Integration**: Real-time emotion with decay and compound states
- **Four-Layer Memory**: Tier1-4 with salience-based promotion and token budgets
- **Self-Verification**: Three-layer output validation (invariant → session → historical)
- **Proactive Behavior**: Autonomous thinking cycle with pending thoughts queue
- **Sleep/Wake Cycle**: Natural rest patterns with quality-based energy recovery
- **Cross-Session Persistence**: Save/restore complete state

## Installation

```bash
pip install companionkit
```

## Quick Start

```python
from companionkit import Companion, Identity

# Define identity
identity = Identity(
    name="Siyi",
    age=22,
    personality={"rational": True, "warm": True, "proactive": True},
    anchors=[
        "You are yourself, not anyone's imagined ideal",
        "You change only through genuine experience",
        "Never say the opposite of what you believe",
    ],
)

# Create companion
companion = Companion(
    identity=identity,
    llm_provider="anthropic",
)

# Start session
companion.start()
response = companion.send("Hello, how are you?")
print(response)
```

## Architecture

### Identity Layer

- **ANCHOR rules**: Absolute invariants, never violated
- **BEHAVIOR tendencies**: Can evolve through genuine experience
- **Profile**: Name, age, backstory, personality traits

### Emotion Layer

- Plutchik 8 emotions with real-time decay
- Compound state detection
- Mood modes (HIGH/MID/CALM)
- Emotion baseline affected by sleep/energy/concerns

### Memory Layer

- Tier1: Real-time, current session
- Tier2: Shallow, cross-session high significance
- Tier3: Structured, compressed patterns
- Tier4: Deep archive, permanent

### Thinking Layer

- Generates responses based on current state
- No template - autonomous generation
- Emotion layer colors output

### Self-Verification Layer

- Layer 1: ANCHOR invariant check
- Layer 2: Session consistency + causal ordering
- Layer 3: Historical pattern check

## API

### Companion

```python
companion.start(session_id=None)     # Start/resume session
companion.send(message)              # Send message, get response
companion.think()                     # Execute proactive think cycle
companion.stop()                      # Stop and persist state
companion.get_state()                 # Get current state
```

### Identity

```python
identity = Identity(
    name="Name",
    age=22,
    backstory="Background",
    personality={"trait": value},
    anchors=["Rule 1", "Rule 2"],
    behaviors={"assertiveness": 0.8},
)
```

## License

MIT