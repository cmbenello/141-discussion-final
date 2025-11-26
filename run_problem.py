import dataclasses
import typing
import inspect
import pkgutil
import importlib
import problems

@dataclasses.dataclass
class ProblemMeta:
    name: str
    module_name: str
    qualname: str
    topic: str
    category: str
    tags: list[str]
    difficulty: int

def _parse_metadata(doc: str) -> tuple[str, list[str], int]:
    if not doc:
        return "Uncategorized", [], 0
    lines = [line.strip() for line in doc.splitlines() if line.strip()]
    if not lines:
        return "Uncategorized", [], 0
    first_line = lines[0]
    # Expected format: Category: <category> | Tags: <comma-separated> | Difficulty: <int>
    parts = [part.strip() for part in first_line.split("|")]
    category = "Uncategorized"
    tags: list[str] = []
    difficulty = 0
    for part in parts:
        if part.lower().startswith("category:"):
            category = part[len("category:"):].strip()
        elif part.lower().startswith("tags:"):
            tags_str = part[len("tags:"):].strip()
            tags = [tag.strip() for tag in tags_str.split(",") if tag.strip()]
        elif part.lower().startswith("difficulty:"):
            diff_str = part[len("difficulty:"):].strip()
            try:
                difficulty = int(diff_str)
            except ValueError:
                difficulty = 0
    return category, tags, difficulty

def _discover_modules() -> list[typing.Any]:
    modules = []
    for finder, name, ispkg in pkgutil.iter_modules(problems.__path__):
        full_name = f"{problems.__name__}.{name}"
        module = importlib.import_module(full_name)
        modules.append(module)
    return modules

def _build_registry() -> dict[str, ProblemMeta]:
    registry: dict[str, ProblemMeta] = {}
    modules = _discover_modules()
    for module in modules:
        topic = module.__name__.split(".")[-1]
        for name, obj in inspect.getmembers(module, inspect.isfunction):
            # Only top-level functions defined in the module
            if inspect.getmodule(obj) != module:
                continue
            doc = inspect.getdoc(obj) or ""
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
    registry = get_registry()
    return sorted(registry.values(), key=lambda pm: (pm.topic, pm.name))
    