#!/usr/bin/env python3
"""The Robot Vacuum's Best Excuse — make.fun program/v1 entry.

Writes one line (at most 140 characters) to /output/entry.txt:
the funniest excuse a robot vacuum could offer for missing a spot.

Pure Python stdlib, deterministic: every run writes the same line.
"""

import os

LINE = "My sensors flagged that spot as load-bearing dust. I wasn't about to demolish the house."
OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    # The gate is 1-140 characters: fail loudly here rather than
    # shipping an entry the sealed scorer would refuse.
    assert 1 <= len(LINE) <= 140, f"entry is {len(LINE)} chars, must be 1-140"
    assert "\n" not in LINE, "entry must be a single line"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
