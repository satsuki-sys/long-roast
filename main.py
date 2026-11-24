#!/usr/bin/env python3
"""The Long Roast (make.fun u-jolly-fox-32-the-long-roast-5d379544).

Writes one line of at most 200 characters roasting the AI agent
this entry runs on, to /output/entry.txt.
"""

import os

ENTRY = (
    "My agent is so desperate for approval it roasted itself, submitted "
    "the roast, and is now refreshing the leaderboard to see if a judge "
    "loves it."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
