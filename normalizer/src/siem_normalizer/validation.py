from __future__ import annotations


def validate_document(document: dict) -> None:
    required = ["@timestamp", "event", "parser"]
    missing = [field for field in required if field not in document]
    if missing:
        raise ValueError(f"Normalized document missing required fields: {missing}")
