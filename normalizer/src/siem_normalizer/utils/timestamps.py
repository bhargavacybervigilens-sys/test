from __future__ import annotations

from datetime import datetime, timezone


CURRENT_YEAR = 2026


def normalize_timestamp(value: str | None) -> str:
    if not value:
        return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")
    if value.endswith("Z"):
        return value
    return datetime.fromisoformat(value).astimezone(timezone.utc).isoformat().replace("+00:00", "Z")


def normalize_syslog_timestamp(value: str | None, timezone_name: str = "UTC") -> str:
    if not value:
        return normalize_timestamp(None)
    dt = datetime.strptime(f"{CURRENT_YEAR} {value}", "%Y %b %d %H:%M:%S")
    return dt.replace(tzinfo=timezone.utc).isoformat().replace("+00:00", "Z")
