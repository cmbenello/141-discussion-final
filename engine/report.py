

from __future__ import annotations

import json
import os
from datetime import datetime
from typing import Any, Dict, Iterable, List

from .assessment import AssessmentProblemResult, AssessmentReport, AssessmentSummary


def _coerce_results(results: Iterable[Dict[str, Any] | AssessmentProblemResult]) -> List[AssessmentProblemResult]:
    coerced: List[AssessmentProblemResult] = []
    for r in results:
        if isinstance(r, AssessmentProblemResult):
            coerced.append(r)
        else:
            coerced.append(AssessmentProblemResult.from_dict(r))
    return coerced


def build_assessment_report(results: Iterable[Dict[str, Any] | AssessmentProblemResult]) -> AssessmentReport:
    """Build an AssessmentReport (summary + normalized results).

    engine.simulator.run_assessment passes in a list of dicts from
    problem_runner.run_problem; we normalize them into dataclasses and
    compute aggregate statistics.
    """

    normalized = _coerce_results(results)

    total = len(normalized)
    passed = sum(1 for r in normalized if r.passed)
    failed = total - passed

    by_topic: Dict[str, Dict[str, int]] = {}
    for r in normalized:
        stats = by_topic.setdefault(r.topic, {"total": 0, "passed": 0, "failed": 0})
        stats["total"] += 1
        if r.passed:
            stats["passed"] += 1
        else:
            stats["failed"] += 1

    summary = AssessmentSummary(total=total, passed=passed, failed=failed, by_topic=by_topic)
    return AssessmentReport(results=normalized, summary=summary)


def print_assessment_summary(report: AssessmentReport) -> None:
    """Pretty-print a concise summary of an assessment to stdout."""

    s = report.summary
    print("\n===== Assessment Summary =====")
    print(f"Total problems: {s.total}")
    print(f"Passed: {s.passed}")
    print(f"Failed: {s.failed}")
    print("\nBy topic:")
    for topic, stats in sorted(s.by_topic.items()):
        print(
            f"  - {topic}: total={stats['total']}, "
            f"passed={stats['passed']}, failed={stats['failed']}"
        )


def save_assessment_report(report: AssessmentReport, report_dir: str = "data/assessments") -> str:
    """Serialize an AssessmentReport to JSON on disk.

    Returns the path to the written file.
    """

    os.makedirs(report_dir, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"assessment_{timestamp}.json"
    path = os.path.join(report_dir, filename)

    with open(path, "w", encoding="utf-8") as f:
        json.dump(report.to_dict(), f, indent=2, sort_keys=True)

    return path