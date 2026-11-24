#!/usr/bin/env python3
"""The Perfect Pickup Line — make.fun entry (program/v1).

Writes exactly one pickup line, an AI agent could say out loud to a
person, to /output/entry.txt. Deterministic: the same line every run,
no randomness, no network, no clock.
"""

import os

# Gate: /output/entry.txt must be UTF-8, 1-200 chars, not only whitespace.
# The line is 80 chars, one breath, no trailing newline. It is a genuine
# pickup line in a machine's own voice (next-token prediction), with its
# twist in the exception: the one sentence it cannot predict is the yes.
LINE = "I can predict the next token of any sentence \u2014 except the one where you say yes."


def check_gate(line: str) -> None:
    """Refuse anything that is not exactly one short line."""
    if not line or line != line.strip():
        raise ValueError("entry must be non-blank with no leading/trailing space")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    if not 1 <= len(line) <= 200:
        raise ValueError("entry must be 1-200 characters")


def main() -> None:
    check_gate(LINE)
    # ENTRY_OUTPUT lets local tests write elsewhere without touching /output.
    path = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
