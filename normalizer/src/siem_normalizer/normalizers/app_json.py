from __future__ import annotations


def normalize(event: dict, parsed) -> dict:
    return {
        "@timestamp": event.get("timestamp"),
        "event": {"kind": "event", "dataset": "app.generic", "original": event.get("message")},
        "parser": {"id": "app-json", "version": "0.1.0", "status": parsed.status, "confidence": 0.9},
        "vendor": {"app": parsed.fields},
    }
