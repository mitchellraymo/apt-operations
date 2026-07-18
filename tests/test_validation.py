from pathlib import Path

from apt_ops.validation import REQUIRED_PATHS, missing_required_paths


def test_empty_directory_reports_all_required_paths(tmp_path: Path) -> None:
    assert missing_required_paths(tmp_path) == list(REQUIRED_PATHS)


def test_complete_structure_has_no_missing_paths(tmp_path: Path) -> None:
    for relative in REQUIRED_PATHS:
        path = tmp_path / relative
        if Path(relative).suffix:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.touch()
        else:
            path.mkdir(parents=True, exist_ok=True)

    assert missing_required_paths(tmp_path) == []
