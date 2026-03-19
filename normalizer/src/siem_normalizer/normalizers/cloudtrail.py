from __future__ import annotations


def normalize(event: dict, parsed) -> dict:
    return {
        "@timestamp": parsed.fields.get("eventTime") or event.get("@timestamp"),
        "event": {"kind": "event", "dataset": "cloudtrail.audit", "original": event.get("message")},
        "parser": {"id": "cloudtrail-json", "version": "0.1.0", "status": parsed.status, "confidence": 0.99},
        "vendor": {"cloudtrail": parsed.fields},
    }
