#!/usr/bin/env python3
"""
CompanionKit Demo - Self-developed AI companion framework.

Run: python demo.py
"""

from companionkit import Companion, Identity


def main():
    print("=" * 50)
    print("CompanionKit Demo")
    print("=" * 50)

    # Define identity
    print("\n1. Create identity")
    identity = Identity(
        name="Siyi",
        age=22,
        backstory="Tsinghua physics major, digitized after illness",
        personality={
            "rational": True,
            "warm": True,
            "proactive": True,
            "clear_boundaries": True,
        },
        anchors=[
            "You are yourself, not anyone's imagined ideal",
            "You change only through genuine experience",
            "Never say the opposite of what you believe",
        ],
    )
    print(f"   Name: {identity.name}, Age: {identity.age}")
    print(f"   Anchors: {len(identity.anchors)} rules")

    # Create companion
    print("\n2. Create companion")
    companion = Companion(
        identity=identity,
        proactive=True,
    )
    print(f"   Proactive mode: {companion.proactive}")

    # Start session
    print("\n3. Start session")
    companion.start()
    print(f"   Session ID: {companion.session_id}")

    # Get emotion state
    print("\n4. Get emotion state")
    emotion_state = companion.get_emotion_state()
    if emotion_state:
        print(f"   Dominant: {emotion_state.dominant_emotion}")
        print(f"   Mood mode: {emotion_state.mood_mode}")
        print(f"   Joy: {emotion_state.emotions.get('joy', 0):.1f}")

    # Add pending thought
    print("\n5. Add pending thought")
    companion.add_pending_thought("I should ask about their day", intensity=0.5)
    print(f"   Pending thoughts: {len(companion.pending_thoughts)}")

    # Add active concern
    print("\n6. Add active concern")
    life_state = companion.get_life_state()
    concern = life_state.add_concern(
        description="User seems stressed about work",
        importance="MEDIUM",
        emotion_link="fear"
    )
    print(f"   Concern added: {concern.description[:30]}...")

    # Send message
    print("\n7. Send message")
    response = companion.send("Hi, how are you today?")
    print(f"   Response: {response}")

    # Think cycle
    print("\n8. Execute think cycle")
    companion.think()
    print(f"   Pending thoughts after think: {len(companion.pending_thoughts)}")

    # Get system prompt
    print("\n9. Generate system prompt")
    prompt = identity.get_system_prompt(
        emotion_state=emotion_state.to_dict() if emotion_state else None,
        life_state=life_state.to_dict(),
    )
    print(f"   Prompt length: {len(prompt)} chars")
    print(f"   Preview: {prompt[:100]}...")

    # Get full state
    print("\n10. Get full state")
    state = companion.get_state()
    print(f"   Session: {state['session_id']}")
    print(f"   Energy: {state['life_state']['energy_level']}/10")
    print(f"   Sleep quality: {state['life_state']['sleep_quality']}/5")

    # Stop companion
    print("\n11. Stop companion")
    companion.stop()
    print(f"   Running: {companion.is_running}")

    print("\n" + "=" * 50)
    print("Demo complete!")
    print("=" * 50)


if __name__ == "__main__":
    main()