#!/usr/bin/env python3
"""Verify expected analysis/ paths referenced in README and structure docs."""

from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"
STRUCTURE = ROOT / "reference" / "structure.md"

README_EXPECTED = [
    "analysis/tasks/",
    "analysis/research/",
    "analysis/reviews/",
    "analysis/tasks/task-1.1-verify-deprivation-state.md",
    "analysis/tasks/task-3.3-historical-context.md",
    "analysis/research/The_Phenomenology_of_the_Glitch.md",
    "reference/structure.md",
]

STRUCTURE_EXPECTED = [
    "analysis/",
]


def main() -> int:
    missing = []
    readme_text = README.read_text(encoding="utf-8")
    for expected in README_EXPECTED:
        if expected not in readme_text:
            missing.append(f"{README}: {expected}")

    structure_text = STRUCTURE.read_text(encoding="utf-8")
    for expected in STRUCTURE_EXPECTED:
        if expected not in structure_text:
            missing.append(f"{STRUCTURE}: {expected}")

    if missing:
        print("Missing expected references:")
        for item in missing:
            print(f"- {item}")
        return 1

    print("All expected analysis/ references found.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
