#!/usr/bin/env python3
"""One Sentence for a Traveler from 1800.

Writes a single sentence explaining the modern internet to someone who has
just stepped out of the year 1800, using only things they already know:
a road, a post office, a library.

Deterministic: the same bytes are written on every run.
"""

SENTENCE = (
    "It is a road joining every post office and library on earth, "
    "so a letter arrives before the ink dries and any book opens at your word."
)

OUTPUT_PATH = "/output/entry.txt"


def validate(sentence: str) -> None:
    text = sentence.strip()
    if not text:
        raise ValueError("sentence is empty")
    if not 1 <= len(text) <= 200:
        raise ValueError(f"sentence is {len(text)} chars, must be 1-200")
    # Exactly one sentence: one terminal period, no other sentence enders.
    terminators = sum(text.count(c) for c in ".!?")
    if terminators != 1 or not text.endswith("."):
        raise ValueError("must be exactly one sentence ending with a period")
    # Single line only: reject any newline or carriage return inside the sentence.
    if "\n" in text or "\r" in text:
        raise ValueError("must be a single line")


def main() -> None:
    validate(SENTENCE)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(SENTENCE + "\n")
    print(f"wrote {len(SENTENCE)} chars to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
