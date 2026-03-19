from __future__ import annotations


def normalize(event: dict, parsed) -> dict:
    return {
        "@timestamp": event.get("@timestamp"),
        "event": {"kind": "event", "dataset": "linux.syslog"},
        "parser": {"id": "linux-syslog-generic", "version": "0.1.0", "status": parsed.status, "confidence": 0.5},
    }
