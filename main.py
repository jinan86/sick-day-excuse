#!/usr/bin/env python3
"""The Funniest Sick-Day Excuse — make.fun entry.

Writes one line, under 200 characters, giving a funny reason to call in
sick, to /output/entry.txt (override with ENTRY_OUTPUT for local testing).

Deterministic: no network, no randomness, no files read outside this repo.
"""

import os

MAX_LENGTH = 200
MIN_LENGTH = 1

# The entry text, kept as fragments so the assembly is explicit and the
# full line is easy to audit. Joined in build_entry() below.
_PARTS = (
    "Can't come in today",
    "\u2014",  # em dash
    "my toddler hid my car keys, my shoes,",
    "and my will to work, so I'm calling it a sick day.",
)


def build_entry() -> str:
    """Assemble the entry line from its fragments."""
    return " ".join(_PARTS)


def validate(text: str) -> None:
    """Enforce the competition's entry rules."""
    assert MIN_LENGTH <= len(text) <= MAX_LENGTH, (
        f"entry must be {MIN_LENGTH}-{MAX_LENGTH} chars, got {len(text)}"
    )
    assert text.strip(), "entry must not be only whitespace"
    assert "\n" not in text, "entry must be a single line"


def resolve_output_path() -> str:
    return os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")


def main() -> None:
    text = build_entry()
    validate(text)

    out_path = resolve_output_path()
    parent = os.path.dirname(out_path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
