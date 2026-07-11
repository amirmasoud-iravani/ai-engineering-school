"""Run lightweight checks before publishing the repository."""

from __future__ import annotations

import json
import py_compile
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def check_python_files() -> list[str]:
    errors: list[str] = []
    for path in ROOT.rglob("*.py"):
        if ".venv" in path.parts:
            continue
        try:
            py_compile.compile(str(path), doraise=True)
        except py_compile.PyCompileError as exc:
            errors.append(f"{path.relative_to(ROOT)}: {exc.msg}")
    return errors


def check_notebooks() -> list[str]:
    errors: list[str] = []
    for path in ROOT.rglob("*.ipynb"):
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
            if data.get("nbformat") != 4:
                errors.append(f"{path.relative_to(ROOT)}: expected nbformat 4")
        except (OSError, json.JSONDecodeError) as exc:
            errors.append(f"{path.relative_to(ROOT)}: {exc}")
    return errors


def main() -> int:
    errors = check_python_files() + check_notebooks()
    if errors:
        print("Repository check failed:")
        for error in errors:
            print("-", error)
        return 1
    print("Repository check passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
