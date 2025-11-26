"""
engine.simulator

High-level orchestration for assessment and practice sessions.
"""

from __future__ import annotations

import os
import random
from dataclasses import dataclass
from typing import Iterable, List, Optional, Sequence

from . import registry
from . import problem_runner
from . import report


# ---------------------------------------------------------------------------
# Internal helper types
# ---------------------------------------------------------------------------

@dataclass
class ProblemSpec:
    """Lightweight view over a registered problem."""

    topic: str
    name: str
    difficulty: int
    meta: registry.ProblemMeta  # original ProblemMeta from registry


def _normalize_problems(
    problems: Iterable[registry.ProblemMeta],
) -> List[ProblemSpec]:
    """
    Convert ProblemMeta objects into ProblemSpec.

    ProblemMeta has fields:
      - name
      - module_name
      - qualname
      - topic
      - category
      - tags
      - difficulty
    """
    specs: List[ProblemSpec] = []
    for pm in problems:
        specs.append(
            ProblemSpec(
                topic=pm.topic,
                name=pm.name,
                difficulty=pm.difficulty,
                meta=pm,
            )
        )
    return specs


def _filter_and_sample_by_topic(
    specs: Sequence[ProblemSpec],
    topics: Optional[List[str]],
    num_per_topic: int,
    min_difficulty: int,
    max_difficulty: int,
    rng: random.Random,
) -> List[ProblemSpec]:
    """Group by topic and sample up to num_per_topic from each."""
    # Filter by topics + difficulty
    filtered = [
        s
        for s in specs
        if (topics is None or s.topic in topics)
        and (min_difficulty <= s.difficulty <= max_difficulty)
    ]

    by_topic: dict[str, list[ProblemSpec]] = {}
    for s in filtered:
        by_topic.setdefault(s.topic, []).append(s)

    chosen: List[ProblemSpec] = []
    for topic, items in by_topic.items():
        if len(items) <= num_per_topic:
            chosen.extend(items)
        else:
            chosen.extend(rng.sample(items, k=num_per_topic))

    rng.shuffle(chosen)
    return chosen


# ---------------------------------------------------------------------------
# Public API: assessment
# ---------------------------------------------------------------------------

def run_assessment(
    topics: Optional[List[str]] = None,
    num_per_topic: int = 5,
    min_difficulty: int = 2,
    max_difficulty: int = 5,
    seed: Optional[int] = None,
    save_report: bool = True,
    report_dir: str = "data/assessments",
) -> None:
    """
    Run a batch assessment across topics and print a summary.

    Called by run_assessment.py.
    """
    rng = random.Random(seed)

    # *** FIX 1: use your registry.all_problems(), not list_problems() ***
    all_problems = registry.all_problems()
    specs = _normalize_problems(all_problems)

    if not specs:
        print("No problems registered. Check engine.registry.")
        return

    chosen = _filter_and_sample_by_topic(
        specs=specs,
        topics=topics,
        num_per_topic=num_per_topic,
        min_difficulty=min_difficulty,
        max_difficulty=max_difficulty,
        rng=rng,
    )

    if not chosen:
        print(
            "No problems matched the given filters "
            f"(topics={topics}, difficulty={min_difficulty}-{max_difficulty})."
        )
        return

    use_solutions = os.getenv("USE_SOLUTIONS", "0") == "1"

    results: List[dict] = []
    print(f"Running assessment on {len(chosen)} problems...")
    print(f"Using solutions: {use_solutions}")
    print("-" * 60)

    for spec in chosen:
        print(f"[{spec.topic}] {spec.name} (difficulty {spec.difficulty})")
        # *** ASSUMPTION: problem_runner.run_problem(meta, use_solutions=...) ***
        res = problem_runner.run_problem(spec.name, use_solutions=use_solutions)
        results.append(res)

    # Build + print summary report
    rep = report.build_assessment_report(results)
    report.print_assessment_summary(rep)

    # Optionally persist JSON
    if save_report:
        os.makedirs(report_dir, exist_ok=True)
        filename = report.save_assessment_report(rep, report_dir=report_dir)
        print(f"\nSaved assessment report to: {filename}")


# ---------------------------------------------------------------------------
# Public API: practice
# ---------------------------------------------------------------------------

def run_practice(
    topic: Optional[str] = None,
    min_difficulty: int = 2,
    max_difficulty: int = 5,
    loop: bool = True,
) -> None:
    """
    Interactive practice loop.

    Called by run_practice.py.
    """
    rng = random.Random()

    # *** FIX 2: again, use all_problems() ***
    all_problems = registry.all_problems()
    specs = _normalize_problems(all_problems)

    # Filter once
    if topic is None:
        topics_filter: Optional[List[str]] = None
    else:
        topics_filter = [topic]

    candidates = _filter_and_sample_by_topic(
        specs=specs,
        topics=topics_filter,
        num_per_topic=10_000,  # effectively "all that match"
        min_difficulty=min_difficulty,
        max_difficulty=max_difficulty,
        rng=rng,
    )

    if not candidates:
        print(
            "No problems matched the given filters "
            f"(topic={topic}, difficulty={min_difficulty}-{max_difficulty})."
        )
        return

    use_solutions = os.getenv("USE_SOLUTIONS", "0") == "1"

    def _one_round() -> None:
        spec = rng.choice(candidates)
        print("-" * 72)
        print(f"Topic: {spec.topic} | Name: {spec.name} | Difficulty: {spec.difficulty}")
        print(f"(Using solutions: {use_solutions})")

        res = problem_runner.run_problem(spec.name, use_solutions=use_solutions)

        passed = res.get("passed", False)
        num_tests = res.get("num_tests")
        num_failed = res.get("num_failed")

        print(f"  → Passed: {passed}")
        if num_tests is not None:
            print(f"  → Tests: {num_tests} (failed: {num_failed})")

    if not loop:
        _one_round()
        return

    while True:
        _one_round()
        ans = input("Practice another problem? [Y/n] ").strip().lower()
        if ans in ("n", "no", "q", "quit"):
            print("Exiting practice. Nice work.")
            break