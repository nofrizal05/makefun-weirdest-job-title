#!/usr/bin/env python3
"""Weirdest Job Title entry for make.fun.

Writes exactly one line -- the weirdest job title -- to /output/entry.txt.
"""

import os

TITLE = "Executive Assistant to the Office Ghost"


def main():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TITLE + "\n")


if __name__ == "__main__":
    main()
