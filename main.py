#!/usr/bin/env python3
"""Entry: a hardware wallet refuses to sign at 3 AM.

The wallet remembers the last 3 AM signing and has learned its
lesson: the button that signed a memecoin at 3 AM last Tuesday
watched it die before breakfast, so it is on strike until sunrise.
The line is checked against the competition gate (1-200 characters,
one line, no trailing newline) before it is written out.
"""

import os
import sys

EXCUSE = " ".join([
    "I signed your 2.4 SOL memecoin at 3 AM last Tuesday",
    "and watched it die before breakfast,",
    "so tonight my button is on strike until sunrise.",
])


def _fail(message):
    print(f"error: {message}", file=sys.stderr)
    raise SystemExit(1)


def _check(line):
    if not line.strip():
        _fail("blank output")
    if any(ch in line for ch in "\r\n"):
        _fail("output must be a single line")
    size = len(line)
    if not 1 <= size <= 200:
        _fail(f"output length {size} outside 1-200 gate")
    # ASCII-only line, so byte size equals character count.
    if len(line.encode("utf-8")) != size:
        _fail("output must be plain ASCII")


def _destination():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    return os.path.join(out_dir, "entry.txt")


def run():
    text = EXCUSE
    _check(text)
    path = _destination()
    with open(path, "w", encoding="utf-8", newline="") as stream:
        stream.write(text)
    with open(path, "r", encoding="utf-8", newline="") as stream:
        written = stream.read()
    if written != text:
        _fail("round-trip mismatch")
    _check(written)


if __name__ == "__main__":
    run()
