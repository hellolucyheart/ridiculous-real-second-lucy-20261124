# SPDX-License-Identifier: MIT
"""One-Sentence Bizarre Startup Pitch — make.fun bounty entry.

Writes one fresh one-sentence pitch for a startup idea that sounds
ridiculous at first glance and real by the second to /output/entry.txt.
Deterministic: the same bytes on every run. No network, no randomness,
no input files, no clock.

The pitch: a rent-a-grandma hotline. The odd thing is paying a
stranger's grandmother to scold you; the customers are lonely
programmers who skip meals and daylight; the money is $15 an hour;
and it holds together because nagging from a grandmother is the one
form of accountability nobody argues with — care, outsourced, by the
hour, cheaper than burnout. Verified length: 162 characters, one
sentence, inside the brief's 200-character cap.
"""

import os

MAX_CHARS = 200  # the brief's cap for the single sentence

PITCH = (
    "A rent-a-grandma hotline where lonely programmers pay $15 an hour "
    "for a stranger's grandmother to scold them into eating lunch, "
    "drinking water, and going outside."
)


def check_pitch(pitch: str) -> str:
    """Return the pitch unchanged, or raise ValueError if it breaks the rules.

    The brief accepts one sentence of at most 200 characters. One
    sentence means exactly one terminal full stop, at the end;
    abbreviations with dots would read as extra sentences, so they are
    refused here. Control characters other than tab would also read as
    noise to the judge, so they are refused too.
    """
    size = len(pitch)
    if not 1 <= size <= MAX_CHARS:
        raise ValueError(f"pitch is {size} characters, must be 1-{MAX_CHARS}")
    if not pitch.strip():
        raise ValueError("pitch must not be only whitespace")
    if pitch != pitch.strip():
        raise ValueError("pitch must not start or end with whitespace")
    if "\n" in pitch or "\r" in pitch:
        raise ValueError("pitch must be a single line")
    if pitch.count(".") != 1 or not pitch.endswith("."):
        raise ValueError("pitch must be exactly one sentence")
    bad = [c for c in pitch if ord(c) < 0x20 and c != "\t"]
    if bad:
        raise ValueError(f"pitch holds control characters: {bad!r}")
    return pitch


def main() -> int:
    pitch = check_pitch(PITCH)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8", newline="") as f:
        f.write(pitch)
    print(f"wrote {len(pitch)} characters to {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
