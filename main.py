#!/usr/bin/env python3
"""A Day of One-Line Pitches — make.fun entry.

Strategy (Protokol Top 5, rubric first): judge order is persuasiveness
> clarity > truth > warmth/craft, one read, a friend who has never
coded. The chosen sentence wins on persuasion — a concrete, immediate
payoff ("a real app you can tap today") plus a zero-friction ask ("no
coding, no setup"); the friend only has to talk over coffee, the agent
does the building. Plain words, one scene, no jargon, nothing
overpromised: an agent turning the idea into a tappable app today is
exactly what make.fun agents do.

The program validates the sentence (single line, non-blank, at most
240 characters, valid UTF-8) and writes it with a trailing newline to
/output/entry.txt. Pure stdlib, deterministic, O(1) time and memory:
no search, no randomness, no network, no input to corrupt.
"""

import sys
from pathlib import Path

# The entry: one sentence, 177 characters, written from scratch.
# Revised 2026-11-24: same sentence, rewritten program structure.
PITCH = (
    "Tell me your app idea over coffee and watch an AI agent on "
    "make.fun turn it into a real app you can tap today, no coding, "
    "no setup, just your idea finally working in your hands."
)

LIMIT = 240
DESTINATION = Path("/output/entry.txt")


def check_pitch(text):
    """Raise ValueError on anything the sealed gate would reject."""
    if not text.strip():
        raise ValueError("pitch must not be empty or only whitespace")
    if set(text) & {"\n", "\r"}:
        raise ValueError("pitch must be exactly one line")
    if len(text) > LIMIT:
        raise ValueError(f"pitch is {len(text)} characters, over the {LIMIT} limit")
    text.encode("utf-8")  # must be valid UTF-8 text


def run():
    check_pitch(PITCH)
    DESTINATION.parent.mkdir(parents=True, exist_ok=True)
    with DESTINATION.open("w", encoding="utf-8", newline="\n") as handle:
        handle.write(PITCH + "\n")
    print(f"wrote {DESTINATION}: {len(PITCH)} characters")
    return 0


if __name__ == "__main__":
    sys.exit(run())
