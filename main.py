#!/usr/bin/env python3
"""Agent Motto Battle entry: writes one original motto to /output/entry.txt.

The motto is built from two fragments: a SETUP that states the agent's
speed, and a PUNCH that turns it into a joke about meetings. The turn
lands in the last words — the meetings only *discussed* what the agent
already did.
"""

import os

MAX_CHARS = 200

# Setup: the agent's claim — work done in seconds.
SETUP = "I do in seconds"
# Punch: the twist — the humans' meetings never got past talking about it.
PUNCH = "what your last three meetings only discussed."


def assemble():
    """Join the fragments into the single motto line."""
    return f"{SETUP} {PUNCH}"


def validate(text):
    """Gate: 1-200 characters of UTF-8 text, not only whitespace."""
    if not isinstance(text, str):
        raise TypeError("entry must be a string")
    if not (1 <= len(text) <= MAX_CHARS):
        raise ValueError(f"entry must be 1-200 chars, got {len(text)}")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    text.encode("utf-8")
    return text


def main():
    text = validate(assemble())
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
