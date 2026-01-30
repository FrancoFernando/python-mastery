#!/usr/bin/env python3
"""Script to create placeholder folders for Python Workout exercises."""

import argparse
import os
from pathlib import Path


def create_exercise(number: int, name: str, base_dir: Path | None = None) -> Path:
    """Create a placeholder exercise folder with description.md and solution.py."""
    if base_dir is None:
        base_dir = Path(__file__).parent

    folder_name = f"{number:03d}-{name}"
    exercise_path = base_dir / folder_name

    exercise_path.mkdir(exist_ok=True)

    description_file = exercise_path / "description.md"
    if not description_file.exists():
        description_file.write_text(f"# Exercise {number}: {name.replace('-', ' ').title()}\n\n## Description\n\nTODO: Add exercise description here.\n")

    solution_file = exercise_path / "solution.py"
    if not solution_file.exists():
        solution_file.write_text(f'"""Exercise {number}: {name.replace("-", " ").title()}"""\n\n# TODO: Implement solution\n')

    return exercise_path


def main():
    parser = argparse.ArgumentParser(description="Create a placeholder exercise folder")
    parser.add_argument("number", type=int, help="Exercise number (e.g., 5)")
    parser.add_argument("name", type=str, help="Exercise name with hyphens (e.g., sum-numbers)")

    args = parser.parse_args()

    exercise_path = create_exercise(args.number, args.name)
    print(f"Created exercise folder: {exercise_path}")


if __name__ == "__main__":
    main()
