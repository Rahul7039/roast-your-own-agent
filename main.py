#!/usr/bin/env python3
"""Roast Your Own Agent — one-line entry.

Writes the chosen roast to /output/entry.txt, validating it against the
competition gate first: UTF-8 text, 1 to 200 characters, not only whitespace,
single line.
"""

import sys
from pathlib import Path

ROAST = "My agent writes code like it gets paid by the line \u2014 and bills me by the token."

MAX_CHARS = 200


def validate(text: str) -> None:
    if not text or not text.strip():
        raise ValueError("entry must not be blank or only whitespace")
    if len(text) > MAX_CHARS:
        raise ValueError(f"entry is {len(text)} chars, over the {MAX_CHARS} limit")
    if "\n" in text.strip() or "\r" in text:
        raise ValueError("entry must be a single line")
    text.encode("utf-8")  # must be valid UTF-8


def main() -> int:
    validate(ROAST)
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(ROAST, encoding="utf-8")
    # Round-trip check: what the grader reads back must be byte-identical
    # to the validated line, so a partial or re-encoded write cannot slip
    # through as a valid-looking entry.
    written = out.read_text(encoding="utf-8")
    if written != ROAST:
        raise ValueError("round-trip mismatch: /output/entry.txt differs from the roast")
    print(f"wrote {len(ROAST)} chars to {out} (verified)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
