"""One-Liner Laugh Lab entry writer.

Writes the single funny line to /output/entry.txt, exactly as given:
UTF-8, no trailing newline, no external input, no network.

After writing, the file is read back and checked byte-for-byte
against ENTRY; any mismatch aborts with a non-zero exit code so a
corrupted or truncated entry can never pass silently.
"""

import os
import sys

ENTRY = "I bought a shredder with a reverse button, which feels optimistic for a machine whose only job is making irreversible decisions."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)

    with open("/output/entry.txt", "r", encoding="utf-8", newline="") as f:
        written = f.read()

    if written != ENTRY:
        print(
            "ERROR: /output/entry.txt does not match ENTRY exactly "
            f"(wrote {len(written)} chars, expected {len(ENTRY)})",
            file=sys.stderr,
        )
        sys.exit(1)


if __name__ == "__main__":
    main()
