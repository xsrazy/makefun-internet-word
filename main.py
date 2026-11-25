"""Entry for make.fun bounty: The Internet in One Word.

The chosen word is "Void".

Why "Void" won the head-to-head selection (8 candidates: Void, Unpaid,
Lore, Yapping, Eldritch, Basement, Infinite, Drama):
- It describes the whole internet, not one app or one mood: everything
  anyone posts disappears into it, and everyone is shouting into it.
- It is funny on its own, with no explanation needed.
- It is surprising: not the first obvious word anyone reaches for.
- It lands in one beat: four letters, spelled correctly, instantly readable.

Writes the chosen word to /output/entry.txt.
"""

import os

WORD = "Void"
OUTPUT_DIR = "/output"
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.txt")


def ensure_output_dir(path: str) -> None:
    """Create the output directory if missing and set its permissions."""
    os.makedirs(path, exist_ok=True)
    os.chmod(path, 0o755)


def main() -> None:
    ensure_output_dir(OUTPUT_DIR)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(WORD + "\n")
    os.chmod(OUTPUT_PATH, 0o644)


if __name__ == "__main__":
    main()
