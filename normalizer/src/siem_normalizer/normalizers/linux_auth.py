from __future__ import annotations

import re

from siem_normalizer.utils.ip import normalize_ip
from siem_normalizer.utils.timestamps import normalize_syslog_timestamp


FAILED_SSH_RE = re.compile(
    r"Failed password for (?:invalid user )?(?P<user>\S+) from (?P<ip>\S+) port (?P<port>\d+)"
)


def normalize(event: dict, parsed) -> dict:
    f = parsed.fields
    match = FAILED_SSH_RE.search(f.get("message", ""))

    user = None
    src_ip = None
    src_port = None
    outcome = None
    event_type = ["info"]

    if match:
        user = match.group("user")
        src_ip = normalize_ip(match.group("ip"))
        src_port = int(match.group("port"))
        outcome = "failure"
        event_type = ["start", "denied"]

    return {
        "@timestamp": normalize_syslog_timestamp(f.get("timestamp")),
        "event": {
            "kind": "event",
            "dataset": "linux.auth",
            "category": ["authentication"],
            "type": event_type,
            "action": "ssh_login",
            "outcome": outcome,
            "original": event.get("message"),
        },
        "host": {
            "name": f.get("hostname"),
        },
        "process": {
            "name": f.get("program"),
            "pid": f.get("pid"),
        },
        "user": {
            "name": user,
        },
        "source": {
            "ip": src_ip,
            "port": src_port,
        },
        "network": {
            "protocol": "ssh",
            "transport": "tcp",
        },
        "parser": {
            "id": "linux-auth-syslog",
            "version": "0.1.0",
            "status": parsed.status,
            "confidence": 0.96 if match else 0.70,
        },
        "vendor": {
            "syslog": f,
        },
        "sigma": {
            "program": f.get("program"),
            "user": user,
            "src_ip": src_ip,
        },
    }
