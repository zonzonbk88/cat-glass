#!/usr/bin/env python3
"""Five Seconds to Explain the Glass — entry generator.

Writes the chosen one-sentence cat excuse to /output/entry.txt.
No network, stdlib only.
"""

EXCUSE = (
    "I was stress-testing the glass's commitment to the table "
    "and it failed, which is frankly a you problem."
)

OUTPUT_PATH = "/output/entry.txt"


def main():
    import os

    # Gate check: the brief requires exactly one sentence, 1-200 characters.
    # Fail loudly instead of ever writing an invalid entry.
    assert 1 <= len(EXCUSE) <= 200, f"excuse is {len(EXCUSE)} chars, must be 1-200"
    assert EXCUSE.count(".") == 1 and EXCUSE.endswith("."), (
        "excuse must be exactly one sentence"
    )
    assert "\n" not in EXCUSE, "excuse must not contain a newline"

    out_dir = os.path.dirname(os.path.abspath(OUTPUT_PATH))
    os.makedirs(out_dir, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(EXCUSE)


if __name__ == "__main__":
    main()
