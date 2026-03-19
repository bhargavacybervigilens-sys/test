from __future__ import annotations

from siem_normalizer.utils.ip import normalize_ip


def normalize(event: dict, parsed) -> dict:
    f = parsed.fields
    timestamp = None
    if f.get("date") and f.get("time"):
        timestamp = f"{f['date']}T{f['time']}Z"

    return {
        "@timestamp": timestamp or event.get("@timestamp"),
        "event": {
            "kind": "event",
            "dataset": "firewall.traffic",
            "category": ["network"],
            "type": ["connection", "denied"] if f.get("action") == "deny" else ["connection"],
            "action": f.get("action"),
            "outcome": "failure" if f.get("action") == "deny" else "success",
            "original": event.get("message"),
        },
        "observer": {
            "name": f.get("device"),
            "type": "firewall",
        },
        "source": {
            "ip": normalize_ip(f.get("src")),
            "port": int(f["spt"]) if f.get("spt") else None,
        },
        "destination": {
            "ip": normalize_ip(f.get("dst")),
            "port": int(f["dpt"]) if f.get("dpt") else None,
        },
        "network": {
            "protocol": f.get("proto"),
            "transport": f.get("proto"),
        },
        "rule": {
            "name": f.get("rule"),
        },
        "parser": {
            "id": "firewall-kv",
            "version": "0.1.0",
            "status": parsed.status,
            "confidence": 0.98,
        },
        "vendor": {
            "firewall": f,
        },
    }
