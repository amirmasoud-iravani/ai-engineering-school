"""A small, dependency-free text analyzer for beginner practice."""

from __future__ import annotations

import argparse
import re
from collections import Counter
from pathlib import Path


PUNCTUATION_PATTERN = re.compile(r"[^\w\u0600-\u06FF]+", flags=re.UNICODE)


def normalize_token(token: str) -> str:
    """Lowercase a token and remove surrounding punctuation-like characters."""
    return PUNCTUATION_PATTERN.sub("", token.lower()).strip("_")


def tokenize(text: str) -> list[str]:
    """Split text on whitespace and discard empty normalized tokens."""
    tokens = (normalize_token(piece) for piece in text.split())
    return [token for token in tokens if token]


def analyze_text(text: str, top_n: int = 10) -> dict[str, object]:
    """Return simple descriptive statistics for text."""
    tokens = tokenize(text)
    counts = Counter(tokens)
    return {
        "characters": len(text),
        "tokens": len(tokens),
        "unique_tokens": len(set(tokens)),
        "top_tokens": counts.most_common(top_n),
    }


def format_report(report: dict[str, object]) -> str:
    """Turn an analysis dictionary into readable text."""
    lines = [
        f"Characters: {report['characters']}",
        f"Tokens: {report['tokens']}",
        f"Unique tokens: {report['unique_tokens']}",
        "Top tokens:",
    ]
    for token, count in report["top_tokens"]:  # type: ignore[assignment]
        lines.append(f"  {token}: {count}")
    return "\n".join(lines)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", type=Path, help="Path to a UTF-8 text file")
    parser.add_argument("--top", type=int, default=10, help="Number of top tokens")
    return parser.parse_args()


def main() -> int:
    args = parse_args()

    if args.top < 1:
        print("--top must be at least 1")
        return 2

    try:
        text = args.path.read_text(encoding="utf-8")
    except FileNotFoundError:
        print(f"File not found: {args.path}")
        return 1
    except UnicodeDecodeError:
        print(f"The file is not valid UTF-8: {args.path}")
        return 1

    report = analyze_text(text, top_n=args.top)
    print(format_report(report))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
