# engine/registry.py

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Tuple
import importlib
import inspect
import pkgutil

import problems


@dataclass
class ProblemMeta:
    name: str
    module_name: str
    qualname: str
    topic: str
    category: str
    tags: list[str]
    difficulty: int


def _parse_metadata(doc: str | None) -> tuple[str, list[str], int]:
    """
    Parse the first line of the docstring to extract:
      Category: <category> | Tags: <t1, t2> | Difficulty: <int>
    If anything is missing or malformed, fall back to defaults.
    """
    if not doc:
        return "Uncategorized", [], 0

    lines = [line.strip() for line in doc.splitlines() if line.strip()]
    if not lines:
        return "Uncategorized", [], 0

    first_line = lines[0]
    parts = [part.strip() for part in first_line.split("|")]

    category = "Uncategorized"
    tags: list[str] = []
    difficulty = 0

    for part in parts:
        lower = part.lower()
        if lower.startswith("category:"):
            category = part.split(":", 1)[1].strip()
        elif lower.startswith("tags:"):
            tags_str = part.split(":", 1)[1].strip()
            tags = [t.strip() for t in tags_str.split(",") if t.strip()]
        elif lower.startswith("difficulty:"):
            diff_str = part.split(":", 1)[1].strip()
            try:
                difficulty = int(diff_str)
            except ValueError:
                difficulty = 0

    return category, tags, difficulty


def _discover_modules() -> list[Any]:
    """
    Find all modules inside the `problems` package.
    """
    modules: list[Any] = []
    for _finder, name, _ispkg in pkgutil.iter_modules(problems.__path__):
        full_name = f"{problems.__name__}.{name}"
        module = importlib.import_module(full_name)
        modules.append(module)
    return modules


def _build_registry() -> dict[str, ProblemMeta]:
    """
    Build a mapping from problem-name -> ProblemMeta.
    Only registers top-level functions defined in each problems.<topic> module.
    """
    registry: dict[str, ProblemMeta] = {}
    modules = _discover_modules()

    for module in modules:
        topic = module.__name__.rsplit(".", 1)[-1]

        for name, obj in inspect.getmembers(module, inspect.isfunction):
            # Only functions actually defined in this module, and not private
            if inspect.getmodule(obj) is not module:
                continue
            if name.startswith("_"):
                continue

            doc = inspect.getdoc(obj)
            category, tags, difficulty = _parse_metadata(doc)

            meta = ProblemMeta(
                name=name,
                module_name=module.__name__,
                qualname=f"{module.__name__}.{name}",
                topic=topic,
                category=category,
                tags=tags,
                difficulty=difficulty,
            )
            registry[name] = meta

    return registry


_REGISTRY: dict[str, ProblemMeta] | None = None


def get_registry() -> dict[str, ProblemMeta]:
    global _REGISTRY
    if _REGISTRY is None:
        _REGISTRY = _build_registry()
    return _REGISTRY


def get_problem_meta(name: str) -> ProblemMeta:
    registry = get_registry()
    if name not in registry:
        raise KeyError(f"Problem '{name}' not found in registry")
    return registry[name]


def all_problems() -> list[ProblemMeta]:
    """
    Return all problems as a sorted list for stable ordering.
    """
    registry = get_registry()
    return sorted(registry.values(), key=lambda pm: (pm.topic, pm.name))