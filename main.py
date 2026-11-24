"""Funniest toaster error message entry.

Writes one line (<=120 chars) to /output/entry.txt (or
$MAKEFUN_OUTPUT_DIR/entry.txt for local runs).
Python 3.13 stdlib only, deterministic, no network.

The line is validated against the kit gate before anything is written:
UTF-8 text, 1 to 120 characters, not only whitespace. If it ever fails
the gate the program exits non-zero and writes nothing, instead of
silently producing an entry the scorer would reject. The file holds
exactly the line, with no trailing newline, so its byte count is the
line's own character count.
"""

import os
import sys

LINE = "Error: bread refused to become toast."

MAX_CHARS = 120


def check_gate(line: str) -> str:
    """Return the line if it passes the kit gate, else raise ValueError."""
    line.encode("utf-8")  # must be encodable UTF-8 text
    if not 1 <= len(line) <= MAX_CHARS:
        raise ValueError(
            f"line is {len(line)} characters, gate requires 1-{MAX_CHARS}"
        )
    if not line.strip():
        raise ValueError("line is only whitespace")
    return line


def main() -> int:
    try:
        line = check_gate(LINE)
    except ValueError as exc:
        print(f"gate check failed: {exc}", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(line)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
