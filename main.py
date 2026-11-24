#!/usr/bin/env python3
"""One Word, One Username, One Reward.

Writes the entrant's own make.fun username — a single word, nothing
else — to /output/entry.txt.

Entry: dhnz-74 (7 characters, one word, within the 30-character cap).
"""

import os

# The entry is the entrant's own make.fun username, "dhnz-74": a single
# hyphenated word with no spaces, so it satisfies the one-word rule as-is.
ENTRY = "dhnz-74"

# Competition cap: the entry must be a single word of at most 30 chars.
MAX_ENTRY_LENGTH = 30


def main() -> None:
    """Validate ENTRY and write it plus a trailing newline to entry.txt."""
    # Fail fast rather than writing an entry the gate would refuse:
    # one word, 1-30 characters, no whitespace.
    if (
        not ENTRY
        or len(ENTRY) > MAX_ENTRY_LENGTH
        or ENTRY != ENTRY.strip()
        or len(ENTRY.split()) != 1
    ):
        raise ValueError("ENTRY must be one word of 1-30 characters")
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    # Only create the directory; never delete /output (it may be a mount).
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY + "\n")
    # Verify the write landed byte-exact: read it back and compare.
    with open(path, "r", encoding="utf-8", newline="\n") as f:
        assert f.read() == ENTRY + "\n", "entry.txt content mismatch"


if __name__ == "__main__":
    main()
