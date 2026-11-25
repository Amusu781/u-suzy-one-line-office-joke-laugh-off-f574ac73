"""One-Line Office Joke Laugh-Off: writes one office joke to /output/entry.txt."""

import os
import shutil


LINE = "HR gave the office printer and me the same job description: stand in the corner, hum ominously, and jam whenever it actually matters."

OUT = os.environ.get("MAKEFUN_OUT", "/output")
OUTPUT_PATH = os.path.join(OUT, "entry.txt")


def main() -> None:
    # Create the output directory first.
    os.makedirs(OUT, exist_ok=True)
    # Clear only the contents of the output directory, never the directory itself.
    for name in os.listdir(OUT):
        path = os.path.join(OUT, name)
        if os.path.isdir(path):
            shutil.rmtree(path)
        else:
            os.remove(path)
    # The entry is one office joke: 1-200 chars.
    assert 1 <= len(LINE) <= 200, "entry must be 1-200 chars"
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        # One line only, no trailing newline.
        f.write(LINE)


if __name__ == "__main__":
    main()
