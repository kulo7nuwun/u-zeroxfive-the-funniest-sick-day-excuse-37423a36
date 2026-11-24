#!/usr/bin/env python3
"""The Funniest Sick-Day Excuse — make.fun entry.

Writes one original sick-day excuse line to /output/entry.txt.
The line is written by the author of this program, not copied from
anywhere: a fresh, half-believable excuse whose laugh lands on the
last few words.
"""

from pathlib import Path

EXCUSE = (
    "Can't come in \u2014 I locked myself in my own bathroom, the handle "
    "came off in my hand, and the locksmith is stuck in traffic "
    "behind my plumber."
)

OUTPUT_PATH = Path("/output/entry.txt")
MAX_CHARS = 200


def main() -> None:
    line = EXCUSE.strip()
    if not 1 <= len(line) <= MAX_CHARS:
        raise SystemExit(
            f"excuse must be 1-{MAX_CHARS} characters, got {len(line)}"
        )
    if "\n" in line or "\r" in line:
        raise SystemExit("excuse must be a single line")
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(line + "\n", encoding="utf-8")
    print(f"Wrote {len(line)} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
