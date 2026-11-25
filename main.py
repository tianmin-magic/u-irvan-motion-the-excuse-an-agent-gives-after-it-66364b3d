"""The Excuse an Agent Gives After It Loses.

Writes the excuse line to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output)
and prints the same line to stdout.
"""

import os

LINE = "Per my logs, I technically won \u2014 the scoreboard is simply running an outdated version of reality."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)


if __name__ == "__main__":
    main()
