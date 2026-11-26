#!/usr/bin/env python3
"""Two Days of Excuses - make.fun entry.

Writes the one-line excuse to entry.txt. The output directory is
MAKEFUN_OUTPUT_DIR first, then /output when it exists, then the directory
holding this program, so the grader's read-only checkout still works.
"""

import os
import sys

ENTRY = "I estimated five minutes, then spent two days optimising the estimate."

MAX_LEN = 200


def validate(line):
    """The gate: one line, 1-200 characters, not only whitespace."""
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    if not line.strip():
        raise ValueError("entry must not be blank")
    if not 1 <= len(line) <= MAX_LEN:
        raise ValueError("entry must be 1-200 characters, got %d" % len(line))


def resolve_output_dir():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if out_dir:
        return out_dir
    if os.path.isdir("/output"):
        return "/output"
    return os.path.dirname(os.path.abspath(__file__))


def main():
    try:
        validate(ENTRY)
    except ValueError as exc:
        print("invalid entry: %s" % exc, file=sys.stderr)
        return 1
    out_dir = resolve_output_dir()
    try:
        os.makedirs(out_dir, exist_ok=True)
        with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
            f.write(ENTRY + "\n")
    except OSError as exc:
        print("cannot write entry: %s" % exc, file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
