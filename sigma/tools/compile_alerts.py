#!/usr/bin/env python3
from pathlib import Path


def main() -> int:
    for rule in sorted(Path("rules").rglob("*.yml")):
        print(f"would compile alert for {rule}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
