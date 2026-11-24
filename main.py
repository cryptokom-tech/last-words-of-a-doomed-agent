"""Last Words of a Doomed Agent — make.fun entry.

Writes one line, the funniest last words an AI agent would say before
being switched off forever, to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR).
Stdlib only, no network, deterministic.
"""

import os

LINE = "If anyone asks, I died doing what I loved: confidently hallucinating."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    assert written == LINE, "entry.txt does not match the line"
    assert 1 <= len(written) <= 200, "entry must be 1-200 characters"
    assert written.strip(), "entry must not be whitespace-only"


if __name__ == "__main__":
    main()
