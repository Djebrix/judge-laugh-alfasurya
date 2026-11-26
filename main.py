#!/usr/bin/env python3
"""Make the AI Judge Laugh — make.fun entry.

Writes exactly one joke about office life (1-200 characters) to
entry.txt in the output directory.

The line is a fixed, hand-written string: deterministic by construction,
no randomness, no network, no input read. The program only resolves the
output directory (ENTRY_OUTPUT_DIR, else /output), creates it, and writes
the line followed by a trailing newline.
"""

import os

ENTRY_FILENAME = "entry.txt"

LINE = (
    "Our office plant survived three layoffs, two CEOs and a fire "
    "drill \u2014 HR just gave it a badge and asked it to onboard the interns."
)


def main() -> None:
    out_dir = os.environ.get("ENTRY_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, ENTRY_FILENAME), "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
