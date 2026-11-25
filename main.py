"""Write one pigeon startup pitch to entry.txt."""

import os
import tempfile


LINE = "My startup rents your balcony back to you."
CHAR_LIMIT = 200


def validate(text):
    if not text.strip():
        raise ValueError("Pitch must not be empty.")
    if "\n" in text or "\r" in text:
        raise ValueError("Pitch must be a single line.")
    if len(text) > CHAR_LIMIT:
        raise ValueError("Pitch must be at most 200 characters.")


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "out")
    try:
        os.makedirs(out_dir, exist_ok=True)
    except OSError:
        out_dir = tempfile.mkdtemp()
    validate(LINE)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as output:
        output.write(LINE)


if __name__ == "__main__":
    main()
