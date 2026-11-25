#!/usr/bin/env python3
"""The Most Boring Object, Reviewed in One Line.

Writes a single original funny, true one-line review of the dullest
everyday object we could name — the doorstop — to /output/entry.txt.
Stdlib only; no network, no reads outside the repo.
"""

import os

LINE = (
    "The doorstop has spent six years holding the same door open, "
    "getting kicked into place twice a day, and its performance "
    "review just says \"adequate\"."
)


def main() -> None:
    text = LINE.strip()
    assert 1 <= len(text) <= 200, f"line is {len(text)} chars, must be 1-200"
    assert text.strip(), "line must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
