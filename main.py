#!/usr/bin/env python3
"""The Moon Finally Answers Back.

Writes one line of text to /output/entry.txt: the Moon, wry and old
and a little tired, finally answering back to the people who stare
up at it, wish on it, howl at it and make it late-night promises.

The line is deterministic: the same bytes on every run, stdlib only,
no network, no randomness.
"""

import os

# The Moon's answer: the late-night texter gets the comeback.
# "Unstable" is the turn -- luna/lunatic: the Moon is the thing
# people blame for madness, and it hands the blame straight back.
LINE = "You texted your ex at midnight and I'm the one they call unstable."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
