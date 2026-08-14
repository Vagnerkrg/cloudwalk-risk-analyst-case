from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]


def test_required_project_directories_exist():
    required_directories = [
        PROJECT_ROOT / "data" / "raw",
        PROJECT_ROOT / "notebooks",
        PROJECT_ROOT / "outputs",
        PROJECT_ROOT / "docs",
    ]

    for directory in required_directories:
        assert directory.is_dir(), f"Missing required directory: {directory}"
