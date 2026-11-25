"""one-liner-laugh-lab: the excuse a robot vacuum gives after eating a sock.

The joke is a bureaucratic denial turned into a fresh start: the vacuum
did not eat the sock, it *rehomed* it. The sock now lives under the couch
and pays rent in lint — a deadpan, oddly specific second life that keeps
the whole line inside the vacuum's own world (couch, lint, dust) instead
of reaching for a stock robot joke. The twist lands in the last words,
and every word earns its place: denial, reframe, punchline.

The program writes the entry to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output/entry.txt). It is deterministic: every run writes the
same bytes. Standard library only, no network, no input.
"""

import os
from pathlib import Path

ENTRY = "I didn't eat your sock \u2014 I rehomed it. It now lives under the couch and pays rent in lint."

MAX_CHARS = 200


def entry_text() -> str:
    """Return the entry, refusing anything outside the gate's limits."""
    if not 1 <= len(ENTRY) <= MAX_CHARS:
        raise ValueError(f"entry is {len(ENTRY)} chars, must be 1-{MAX_CHARS}")
    if ENTRY.strip() != ENTRY or "\n" in ENTRY or not ENTRY.strip():
        raise ValueError("entry must be one clean, non-empty line")
    return ENTRY


def main() -> None:
    out = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")) / "entry.txt"
    out.parent.mkdir(parents=True, exist_ok=True)
    text = entry_text()
    # No trailing newline: the gate counts every character.
    out.write_text(text, encoding="utf-8")
    # Read back and verify the round trip: what the grader reads must be
    # exactly the validated line, byte for byte.
    if out.read_text(encoding="utf-8") != text:
        raise RuntimeError("round-trip check failed: entry.txt differs")


if __name__ == "__main__":
    main()
