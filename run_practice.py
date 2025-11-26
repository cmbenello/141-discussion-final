"""
run_practice.py

CLI entrypoint for running an interactive practice session.

This script is intentionally small: it parses a few high‑level options and then
delegates to `engine.simulator.run_practice`, which should:

  * Let the user practice one problem at a time
  * Filter by topic / difficulty if requested
  * Optionally loop until the user quits
  * Run tests for each chosen problem and optionally show solutions

Expected simulator API (you should implement this in engine/simulator.py):

    def run_practice(
        topic: str | None = None,
        min_difficulty: int = 2,
        max_difficulty: int = 5,
        loop: bool = True,
    ) -> None:

Adjust this wrapper if your simulator exposes a different signature.
"""

from __future__ import annotations

import argparse
import sys
from typing import List, Optional

try:
    from engine import simulator
except ImportError as exc:  # pragma: no cover - hard fail if engine is missing
    print("Error: could not import engine.simulator – did you install the package correctly?")
    print(exc)
    sys.exit(1)


def _parse_args(argv: Optional[List[str]] = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Run an interactive 141-style practice session."
    )

    parser.add_argument(
        "--topic",
        type=str,
        default=None,
        help=(
            "Optional topic name to focus on "
            "(e.g. 'basics', 'lists_tuples', 'strings_dicts', 'trees_tries'). "
            "If omitted, problems may be drawn from any topic."
        ),
    )

    parser.add_argument(
        "--min-difficulty",
        type=int,
        default=2,
        help="Minimum difficulty to include (inclusive, default: 2).",
    )

    parser.add_argument(
        "--max-difficulty",
        type=int,
        default=5,
        help="Maximum difficulty to include (inclusive, default: 5).",
    )

    parser.add_argument(
        "--one-shot",
        action="store_true",
        help="Run only a single problem instead of looping until quit.",
    )

    return parser.parse_args(argv)


def main(argv: Optional[List[str]] = None) -> None:
    args = _parse_args(argv)

    simulator.run_practice(
        topic=args.topic,
        min_difficulty=args.min_difficulty,
        max_difficulty=args.max_difficulty,
        loop=not args.one_shot,  # type: ignore[operator]
    )


if __name__ == "__main__":  # pragma: no cover
    main()
