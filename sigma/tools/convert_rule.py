#!/usr/bin/env python3
"""Minimal placeholder converter entrypoint.

Replace with real pySigma integration in a Python environment that includes:
- pysigma
- pysigma-backend-elasticsearch
"""

from pathlib import Path
import sys


def main() -> int:
    if len(sys.argv) != 3:
        print("usage: convert_rule.py <rule.yml> <pipeline.yml>")
        return 1

    rule = Path(sys.argv[1])
    pipeline = Path(sys.argv[2])

    if not rule.exists() or not pipeline.exists():
        print("rule or pipeline not found")
        return 2

    print(f"placeholder: convert {rule} using {pipeline}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
