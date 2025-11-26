

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional


@dataclass
class AssessmentProblemResult:
    """Result of running tests for a single problem in an assessment.

    This is a light wrapper over the dict returned by problem_runner.run_problem.
    We keep the structure flexible so we can evolve fields without breaking callers.
    """

    name: str
    topic: str
    passed: bool
    exit_code: int
    num_tests: Optional[int] = None
    num_failed: Optional[int] = None
    raw: Dict[str, Any] = field(default_factory=dict)

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> "AssessmentProblemResult":
        return cls(
            name=d.get("name", ""),
            topic=d.get("topic", ""),
            passed=bool(d.get("passed", False)),
            exit_code=int(d.get("exit_code", 0)),
            num_tests=d.get("num_tests"),
            num_failed=d.get("num_failed"),
            raw=dict(d),
        )

    def to_dict(self) -> Dict[str, Any]:
        out = dict(self.raw)
        out.setdefault("name", self.name)
        out.setdefault("topic", self.topic)
        out.setdefault("passed", self.passed)
        out.setdefault("exit_code", self.exit_code)
        if self.num_tests is not None:
            out.setdefault("num_tests", self.num_tests)
        if self.num_failed is not None:
            out.setdefault("num_failed", self.num_failed)
        return out


@dataclass
class AssessmentSummary:
    """Aggregate statistics for an assessment run."""

    total: int
    passed: int
    failed: int
    by_topic: Dict[str, Dict[str, int]]  # topic -> {"total": int, "passed": int, "failed": int}

    def to_dict(self) -> Dict[str, Any]:
        return {
            "total": self.total,
            "passed": self.passed,
            "failed": self.failed,
            "by_topic": self.by_topic,
        }


@dataclass
class AssessmentReport:
    """Full report object returned by an assessment.

    This is what report.build_assessment_report constructs and what
    report.save_assessment_report serializes.
    """

    results: List[AssessmentProblemResult]
    summary: AssessmentSummary

    def to_dict(self) -> Dict[str, Any]:
        return {
            "results": [r.to_dict() for r in self.results],
            "summary": self.summary.to_dict(),
        }