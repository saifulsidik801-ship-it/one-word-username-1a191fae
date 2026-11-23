#!/usr/bin/env python3
"""One Word, One Username, One Reward - make.fun entry.

The task: send the entrant's own make.fun username, one word and
nothing else, at most 30 characters. A judge model reads two
usernames at a time and picks the one that feels funnier or more
interesting, weighing, in order: whether it is a real make.fun
username (the entrant's own handle), whether it raises a smile on
the first read, whether it sticks in the mind, whether it is a
single word with no padding, and whether it sounds like a handle
its owner would happily wear.

The username: saifulsidik801-ship-it.

It is the entrant's genuine make.fun handle, sent as exactly one
word - the first criterion, and the one that beats any invented
name. It reads as one compact handle: a personal name, a number,
and "ship-it" - the builder's motto, a name its owner wears
happily. Nothing is tacked on: no gloss, no pitch, no padding.

The program writes exactly that username, nothing else, to
/output/entry.txt - 22 characters, inside the gate's 1-30, with
no trailing newline and no extra whitespace. A trailing newline
would add a 23rd byte for no gain: the tie-break favours the
smaller text, and criterion 4 penalises padding, so the file
holds the bare username alone.
"""

import os

USERNAME = "saifulsidik801-ship-it"


def main() -> None:
    # Self-check against the sealed gate: one word, 1-30 chars.
    assert USERNAME and not any(c.isspace() for c in USERNAME), \
        "username must be a single word"
    assert 1 <= len(USERNAME) <= 30, "username fails the gate"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"),
              "w", encoding="utf-8", newline="") as f:
        f.write(USERNAME)
    print(USERNAME)


if __name__ == "__main__":
    main()
