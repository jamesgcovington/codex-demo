"""Simple greeting helper for Codex demo."""

from __future__ import annotations

import argparse
from typing import Sequence

GREETING = "hello from codex demo"


def get_greeting() -> str:
    """Return the greeting message without printing it."""
    return GREETING


def parse_args(argv: Sequence[str] | None = None) -> argparse.Namespace:
    """Return parsed CLI arguments for the greeting script."""
    parser = argparse.ArgumentParser(description="Print the Codex demo greeting.")
    parser.add_argument(
        "--shout",
        action="store_true",
        help="Print the greeting in uppercase.",
    )
    return parser.parse_args(argv)


def main(argv: Sequence[str] | None = None) -> None:
    """Print the greeting when the module is executed as a script."""
    args = parse_args(argv)
    greeting = get_greeting()
    if args.shout:
        greeting = greeting.upper()
    print(greeting)


if __name__ == "__main__":
    main()
