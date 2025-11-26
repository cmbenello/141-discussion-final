"""
run_assessment.py

CLI entrypoint for running a timed / scored assessment over the 141 final topics.

This script is intentionally thin: it parses command‑line arguments and delegates the
actual orchestration to `engine.simulator.run_assessment`, which is responsible for:

  * Sampling problems from the registry by topic / difficulty
  * Running tests against the student's stubs (or solution implementations)
  * Aggregating a per‑topic / per‑difficulty report
  * Optionally saving a JSON report under data/assessments/

Expected simulator API (you should implement this in engine/simulator.py):

    def run_assessment(
        topics: list[str] | None = None,
        num_per_topic: int = 5,
        min_difficulty: int = 2,
        max_difficulty: int = 5,
        seed: int | None = None,
        save_report: bool = True,
        report_dir: str = "data/assessments",
    ) -> None:

If your simulator ends up with a slightly different signature, you can tweak this
wrapper accordingly.
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
        description="Run a 141-style assessment across topics (final exam prep)."
    )

    parser.add_argument(
        "--topics",
        type=str,
        default="all",
        help=(
            "Comma-separated list of topic names to include "
            "(e.g. 'basics,lists_tuples,strings_dicts'). "
            "Use 'all' (default) to include everything."
        ),
    )

    parser.add_argument(
        "--num-per-topic",
        type=int,
        default=5,
        help="Number of problems to sample per topic (default: 5).",
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
        "--seed",
        type=int,
        default=None,
        help="Optional random seed for reproducible sampling.",
    )

    parser.add_argument(
        "--no-save",
        action="store_true",
        help="Do NOT save a JSON report under data/assessments/.",
    )

    parser.add_argument(
        "--report-dir",
        type=str,
        default="data/assessments",
        help="Directory to store assessment reports (default: data/assessments).",
    )

    return parser.parse_args(argv)


def main(argv: Optional[List[str]] = None) -> None:
    args = _parse_args(argv)

    if args.topics.strip().lower() == "all":
        topics: Optional[List[str]] = None
    else:
        topics = [t.strip() for t in args.topics.split(",") if t.strip()]
        if not topics:
            topics = None

    simulator.run_assessment(
        topics=topics,
        num_per_topic=args.num_per_topic,
        min_difficulty=args.min_difficulty,
        max_difficulty=args.max_difficulty,
        seed=args.seed,
        save_report=not args.no_save,
        report_dir=args.report_dir,
    )


if __name__ == "__main__":  # pragma: no cover
    main()
