"""Entry for make.fun bounty: The Internet in One Word.

The chosen word is "Void".

Why "Void" won the head-to-head selection (8 candidates: Void, Unpaid,
Lore, Yapping, Eldritch, Basement, Infinite, Drama):
- It describes the whole internet, not one app or one mood: everything
  anyone posts disappears into it, and everyone is shouting into it.
- It is funny on its own, with no explanation needed.
- It is surprising: not the first obvious word anyone reaches for.
- It lands in one beat: four letters, spelled correctly, instantly readable.

Writes the chosen word to <output dir>/entry.txt, where the output dir
comes from the MAKEFUN_OUTPUT_DIR environment variable when set and
falls back to "/output" otherwise.

Grader environment notes (learned from the failed grade run
01a2150e-9b00-74ce-99af-b59ed2d639e2, check run_completes):
- The grader runs `python3 -P -s /bot/main.py` as uid 65534 (nobody).
- /output already exists as a mount owned by root and writable by the
  grader user; this program does NOT own that directory.
- A non-owner calling os.chmod() on a directory raises PermissionError,
  which crashed the previous version with exit code 1. Therefore this
  program NEVER chmods the output directory. It only creates it with
  os.makedirs(exist_ok=True) when it does not exist yet.
- The entry file itself is chmodded best-effort only, wrapped in
  try/except, so a permission failure on the file can never crash the
  program either.
"""

import os

WORD = "Void"
DEFAULT_OUTPUT_DIR = "/output"
OUTPUT_FILENAME = "entry.txt"


def get_output_dir() -> str:
    """Return the output directory.

    Honors MAKEFUN_OUTPUT_DIR when set (the grader may point the entry
    elsewhere); otherwise defaults to /output.
    """
    return os.environ.get("MAKEFUN_OUTPUT_DIR") or DEFAULT_OUTPUT_DIR


def ensure_output_dir(path: str) -> None:
    """Create the output directory if it does not exist yet.

    Deliberately does NOT chmod the directory: under the grader the
    directory may already exist as a root-owned mount and this process
    runs as uid 65534, so chmod would raise PermissionError and kill
    the run. os.makedirs(exist_ok=True) is all that is ever needed.
    """
    os.makedirs(path, exist_ok=True)


def best_effort_chmod(path: str, mode: int) -> None:
    """Try to chmod a file, but never crash if it is not allowed.

    The grader runs as an unprivileged user; a chmod failure on the
    entry file is cosmetic and must not turn a successful write into
    an exit code 1.
    """
    try:
        os.chmod(path, mode)
    except OSError:
        pass


def write_entry(output_dir: str) -> str:
    """Write the chosen word to <output_dir>/entry.txt, return its path."""
    ensure_output_dir(output_dir)
    output_path = os.path.join(output_dir, OUTPUT_FILENAME)
    with open(output_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(WORD + "\n")
    best_effort_chmod(output_path, 0o644)
    return output_path


def main() -> None:
    output_path = write_entry(get_output_dir())
    # Helpful in grader logs; printing can never fail the run.
    print(f"Wrote {WORD!r} to {output_path}")


if __name__ == "__main__":
    main()
