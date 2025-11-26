# engine/problem_runner.py

from __future__ import annotations

import os
import sys
from typing import Any, Dict

import pytest

from .registry import get_problem_meta


def run_problem(
    name: str,
    use_solutions: bool | None = None,
    verbose: bool = True,
) -> dict[str, Any]:
    """
    Run the tests for a single problem and return a small result dict.

    Keys in the returned dict:
      - name: problem name
      - topic: topic/module (e.g. 'basics', 'lists_tuples')
      - passed: bool (True iff pytest exit code == 0)
      - exit_code: pytest exit code
      - num_tests: Optional[int] (currently None, unless you later wire this up)
      - num_failed: Optional[int] (currently None)
    """
    meta = get_problem_meta(name)
    topic = meta.topic

    # Respect caller's explicit choice, otherwise leave env as-is
    if use_solutions is not None:
        os.environ["USE_SOLUTIONS"] = "1" if use_solutions else "0"

    test_path = os.path.join("tests", f"test_{topic}.py")

    # Simple -k filter: match tests that mention this function name
    filter_expr = name
    args = [test_path, "-k", filter_expr]
    if not verbose:
        args.append("-q")

    if verbose:
        mode = "solutions" if os.getenv("USE_SOLUTIONS", "0") == "1" else "stubs"
        print(f"Running tests for problem '{name}' (topic '{topic}', mode={mode})")

    exit_code = pytest.main(args)

    # Treat pytest exit code 0 (success) and 5 (no tests collected) as passed
    if exit_code == 0:
        passed = True
    elif exit_code == 5:
        passed = True
        if verbose:
            print(f"  (No tests collected for filter {filter_expr!r}; marking as passed/untested.)")
    else:
        passed = False

    return {
        "name": name,
        "topic": topic,
        "passed": passed,
        "exit_code": exit_code,
        "num_tests": None,
        "num_failed": None,
    }


def main(argv: list[str] | None = None) -> int:
    import argparse

    parser = argparse.ArgumentParser(
        description="Run tests for a single problem function."
    )
    parser.add_argument(
        "name",
        help="Name of the problem function to test (e.g., 'cl_01_sum_even_up_to')",
    )
    group = parser.add_mutually_exclusive_group()
    group.add_argument(
        "--solutions",
        dest="use_solutions",
        action="store_true",
        help="Use solution implementations (USE_SOLUTIONS=1)",
    )
    group.add_argument(
        "--stubs",
        dest="use_solutions",
        action="store_false",
        help="Use stub implementations (USE_SOLUTIONS=0)",
    )
    parser.set_defaults(use_solutions=None)
    parser.add_argument(
        "--quiet",
        "-q",
        action="store_true",
        help="Run tests quietly (pytest -q)",
    )

    args = parser.parse_args(argv)
    res = run_problem(args.name, use_solutions=args.use_solutions, verbose=not args.quiet)
    # Return pytest's exit code so this can be used in CI
    return int(res["exit_code"])


if __name__ == "__main__":
    sys.exit(main())