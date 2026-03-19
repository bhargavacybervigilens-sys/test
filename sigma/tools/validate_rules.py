#!/usr/bin/env python3
from pathlib import Path


def main() -> int:
    rules = sorted(Path("rules").rglob("*.yml"))
    for rule in rules:
        print(rule)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
