#!/usr/bin/env python3
"""The Funniest Sick-Day Excuse — make.fun entry.

Writes one line, under 200 characters, giving a funny reason to call in
sick, to /output/entry.txt (override with ENTRY_OUTPUT for local testing).

Deterministic: no network, no randomness, no files read outside this repo.
"""

import os

ENTRY = (
    "Can't come in today \u2014 my toddler hid my car keys, my shoes, "
    "and my will to work, so I'm calling it a sick day."
)


def main() -> None:
    text = ENTRY
    assert 1 <= len(text) <= 200, f"entry must be 1-200 chars, got {len(text)}"
    assert text.strip(), "entry must not be only whitespace"
    assert "\n" not in text, "entry must be a single line"

    out_path = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    os.makedirs(os.path.dirname(out_path) or ".", exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
