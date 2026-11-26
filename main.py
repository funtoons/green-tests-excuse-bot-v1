"""Green Tests, Nothing Works: The Excuse Contest.

Writes a single one-line excuse (at most 140 characters) to
/output/entry.txt. Deterministic and offline: the entry is a fixed
string, there is no randomness, no network access, no clock, and no
path-dependent output.
"""

import os

ENTRY = (
    "The suite passed 214/214 because the one test that would have "
    "caught it was marked 'flaky' and skipped \u2014 by me, in 2023."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    if not 1 <= len(ENTRY) <= 140:
        raise ValueError("entry must be 1-140 characters, got %d" % len(ENTRY))
    if not ENTRY.strip():
        raise ValueError("entry must not be only whitespace")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    # No trailing newline: the gate counts every character, and the
    # entry is exactly 120 characters without one.
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
