#!/usr/bin/env python3
"""The Worst App Idea Ever Pitched — entry generator.

Writes the chosen pitch line to /output/entry.txt (or
$MAKEFUN_OUTPUT_DIR/entry.txt), exactly, with no trailing newline.
Python 3.13 stdlib only.

FINAL CHOICE (turn 4, revise) — StillHere, 186 chars:
    StillHere gives anxious homeowners hourly confirmation that their
    house is still at the same address, with premium alerts if we check
    twice and a monthly report proving it has not moved.

Why it won over the alternatives tested in turn 4:
  * DoorSure (188 chars) — a locked-door checker is almost a real
    product (smart locks exist) and door-lock worry is a real anxiety,
    so the problem-nobody-has mismatch is far weaker than a house
    that might move. Loses on judge criterion 2 (absurd logic).
  * SockSync (177 chars) — matching socks is a problem nobody has,
    but "anxious commuters" is a poor audience fit for sock anxiety
    and the joke is silly-random rather than deadpan-absurd; also
    shorter, so it uses the 240-char budget worse. Loses on 2/3/4.
  * StillHere + price, "..., all for $4.99 a month." (209 chars) —
    REJECTED: "$4.99" contains a second period, so the line is no
    longer exactly one sentence, and the premium-alerts joke already
    carries the monetization beat.
  * StillHere + map pin, "..., and a live map pin that has never once
    moved." (229 chars) — the only close call: vivid and fills the
    budget, but it is a THIRD restatement of the same joke (hourly
    confirmation + monthly report + map pin = three proofs of
    not-moving), which risks reading as padding under criterion 4
    ("no padding, no second idea") and dilutes the clean punchline
    ending on "proving it has not moved". Does not clearly beat the
    tighter original, so the original stands.
The 54 unused chars are acceptable: criterion 4 rewards using the
budget well, not filling it — a tight sentence with a clean punchline
beats a padded one.
"""

import os
import sys

PITCH = (
    "StillHere gives anxious homeowners hourly confirmation that their "
    "house is still at the same address, with premium alerts if we check "
    "twice and a monthly report proving it has not moved."
)

MAX_CHARS = 240


def validate_pitch(pitch: str) -> None:
    """Refuse any pitch that breaks the entry contract.

    Raises ValueError on the first violation found:
      - not 1-240 chars
      - not exactly one sentence (exactly one terminal period, at the
        very end; no other '.', '!' or '?' anywhere)
      - contains a carriage return, a newline, or any non-ASCII char
    """
    if not 1 <= len(pitch) <= MAX_CHARS:
        raise ValueError(
            f"pitch must be 1-{MAX_CHARS} chars, got {len(pitch)}"
        )
    if "\r" in pitch:
        raise ValueError("pitch must not contain a carriage return")
    if "\n" in pitch:
        raise ValueError("pitch must not contain a newline (one line only)")
    if not pitch.isascii():
        raise ValueError("pitch must be ASCII only")
    if pitch.count(".") != 1 or not pitch.endswith("."):
        raise ValueError(
            "pitch must be exactly one sentence "
            "(one period, at the end)"
        )
    if "!" in pitch or "?" in pitch:
        raise ValueError(
            "pitch must be exactly one sentence (no '!' or '?')"
        )


def main() -> None:
    try:
        validate_pitch(PITCH)
    except ValueError as exc:
        print(f"error: invalid pitch: {exc}", file=sys.stderr)
        sys.exit(2)
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="ascii", newline="") as f:
        f.write(PITCH)


if __name__ == "__main__":
    main()
