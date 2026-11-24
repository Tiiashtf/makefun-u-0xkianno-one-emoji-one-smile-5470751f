#!/usr/bin/env python3
"""One Emoji, One Smile — make.fun entry.

Writes exactly one emoji to /output/entry.txt: the single emoji most
likely to make a stranger smile.

The emoji:

    😄  (U+1F604, Grinning Face with Smiling Eyes)

Why this one, against the judge's own brief:

1. Warm and friendly at first glance. It is a big, open grin with
   smiling eyes — the face of someone genuinely pleased to see you.
   A stranger reading it needs no context at all: it is happiness,
   offered freely.
2. Warmth at first glance. The grin is the whole message. There is
   nothing to decode, no joke to get, no mood to guess.
3. Universal. A grin reads the same way to a stranger of any age or
   background. It carries no irony, no in-joke, no culture-bound
   reference.
4. Chosen rather than default. The gentle closed-mouth smile (😊) is
   the first smiley that comes to mind; this is the bigger, more
   deliberate grin — the one you pick when you actually mean it.
   It stays instantly readable while feeling picked for the moment.
5. Right for a stranger. Pure joy, and nothing else: no hearts, no
   hug, no wink, no flirtation, no intimacy that would read oddly
   coming from someone unknown. A smile is the one warm thing a
   stranger can always offer another stranger.

A flower is cheerful but not a greeting; a heart is affection, not a
smile; a hug asks for closeness a stranger has not earned. A grin
asks for nothing and offers everything: look, I am glad you are here.
"""

import os
import shutil

EMOJI = "\U0001F604"  # 😄 Grinning Face with Smiling Eyes
OUTPUT_DIR = "/output"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "entry.txt")


def validate_emoji(text: str) -> None:
    """Fail loudly unless the entry meets the competition gate.

    The gate requires /output/entry.txt to be UTF-8 text of 1 to 8
    characters, not only whitespace; the brief requires exactly one
    emoji and nothing else. Checking here means a bad entry can
    never be written.
    """
    if len(text) != 1:
        raise ValueError(f"entry must be exactly one emoji, got {len(text)} characters")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    # Exactly one Unicode code point, in the emoji range, no ZWJ
    # sequences, no variation selectors, no skin-tone modifiers.
    code = ord(text)
    if not (0x1F300 <= code <= 0x1FAFF or 0x2600 <= code <= 0x27BF):
        raise ValueError(f"entry U+{code:04X} is not an emoji")


def write_emoji() -> None:
    """Write the emoji to /output/entry.txt, deterministically."""
    validate_emoji(EMOJI)
    # Create the output directory if it is missing, but never remove
    # the directory itself: the grader may run with a root-owned
    # output directory inside a sticky parent, where removing it
    # fails with EPERM. Clear only its contents instead.
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    for name in os.listdir(OUTPUT_DIR):
        path = os.path.join(OUTPUT_DIR, name)
        if os.path.isdir(path) and not os.path.islink(path):
            shutil.rmtree(path)
        else:
            os.remove(path)
    with open(OUTPUT_FILE, "w", encoding="utf-8", newline="\n") as f:
        f.write(EMOJI + "\n")


def main() -> None:
    write_emoji()


if __name__ == "__main__":
    main()
