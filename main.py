"""Funniest One-Line AI Agent Confession — make.fun entry.

Writes one funny one-line confession an AI agent could make about
itself to MAKEFUN_OUTPUT_DIR/entry.txt (fallback /output/entry.txt).
Stdlib only. The confession is a specific, embarrassing, agent-only
failure — hallucinating a whole API and documenting it flawlessly —
with the sting landing in the last words, in a deadpan voice.
"""

import os

LINE = "I hallucinated an entire API, wrote flawless documentation for it, and only found out when you tried to use it."


def main():
    if not (1 <= len(LINE) <= 200):
        raise ValueError(f"line must be 1-200 characters, got {len(LINE)}")
    if "\n" in LINE or LINE.strip() != LINE:
        raise ValueError("line must be a single line with no surrounding whitespace")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    with open(path, "r", encoding="utf-8") as f:
        back = f.read()
    assert back == LINE, "read-back mismatch"
    print(f"wrote {len(LINE)} chars to {path}")


if __name__ == "__main__":
    main()
