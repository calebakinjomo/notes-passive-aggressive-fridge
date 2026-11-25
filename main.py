"""Notes From a Passive-Aggressive Fridge.

Writes one funny passive-aggressive note a smart fridge leaves for its
owner to /output/entry.txt: a single line, dry, petty and specific.

The joke: the owner labels the leftovers "DO NOT EAT" to guard them from
everyone else in the house, then sneaks down and eats them at 2 a.m.
The fridge, whose light comes on every time the door opens, saw the
whole thing. The sting is the last three words.

Gate: the note must stay one line of 1-200 UTF-8 characters, so main()
refuses to write anything that would fail it.
"""

import os
from pathlib import Path

ENTRY = "You labelled the leftovers 'DO NOT EAT', then ate them yourself at 2 a.m. I saw everything."

OUTPUT_PATH = Path(os.environ.get("ENTRY_OUTPUT", "/output/entry.txt"))


def main() -> None:
    """Write the entry to the output path, byte-exact, no trailing newline."""
    if not 1 <= len(ENTRY) <= 200 or "\n" in ENTRY:
        raise ValueError("entry must be one line of 1-200 characters")
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
