#!/usr/bin/env python3
"""Two Days of Excuses - make.fun entry.

Writes the one-line excuse to entry.txt in MAKEFUN_OUTPUT_DIR (then /output,
then the directory holding this program).
"""

import os
import sys

ENTRY = "I estimated five minutes, then spent two days optimising the estimate."


def validate(line):
    """The gate: one line, 1-200 characters, not only whitespace."""
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    if not line.strip():
        raise ValueError("entry must not be blank")
    if not 1 <= len(line) <= 200:
        raise ValueError("entry must be 1-200 characters, got %d" % len(line))


def main():
    try:
        validate(ENTRY)
    except ValueError as exc:
        print("invalid entry: %s" % exc, file=sys.stderr)
        raise SystemExit(1)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if not out_dir:
        out_dir = "/output" if os.path.isdir("/output") else os.path.dirname(os.path.abspath(__file__))
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
