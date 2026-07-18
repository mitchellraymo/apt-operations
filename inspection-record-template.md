"""Repository structure checks for the APT operations system."""

from pathlib import Path

REQUIRED_PATHS = (
    "README.md",
    "ROADMAP.md",
    "operations",
    "calibration",
    "quality",
    "equipment",
    "training",
    "reports",
    "templates",
    "src/apt_ops",
)


def missing_required_paths(root: Path) -> list[str]:
    """Return required repository paths that are missing beneath *root*."""
    return [relative for relative in REQUIRED_PATHS if not (root / relative).exists()]
