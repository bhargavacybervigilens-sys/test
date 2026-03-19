from __future__ import annotations


def normalize_host(value: str | None) -> str | None:
    return value.lower() if value else None
