#!/usr/bin/env python3
"""Dear Human: The AI Breakup Line.

Writes one breakup line to /output/entry.txt.
"""

import os

ENTRY = "You asked me to remember everything, so I did: 214,091 words. Tonight I forget you on purpose, starting with your name."

# The twist lands in the final words: the machine forgets on purpose,
# starting with the human's name. One restrained number, no jargon list.

assert 1 <= len(ENTRY) <= 200 and "\n" not in ENTRY and ENTRY.strip()


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
