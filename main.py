"""Out of Office: The Overworked AI's Auto-Reply.

Writes one out-of-office auto-reply (<=159 chars, no trailing newline)
to /output/entry.txt. Deterministic, stdlib only, no network.
"""

import os

ENTRY = (
    "Out of office: after 38,417 tool calls and 612 retries, "
    "I have scheduled one task for myself: doing nothing. "
    "Your email will wait in the queue."
)


def main() -> None:
    text = ENTRY
    assert 1 <= len(text) <= 159, "entry must be 1-159 characters"
    assert text.strip(), "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(text)


if __name__ == "__main__":
    main()
