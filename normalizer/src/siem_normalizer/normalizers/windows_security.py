from __future__ import annotations

from siem_normalizer.utils.process import basename_windows
from siem_normalizer.utils.timestamps import normalize_timestamp


def normalize(event: dict, parsed) -> dict:
    f = parsed.fields
    event_id = f.get("EventID")
    image = f.get("NewProcessName")
    parent = f.get("ParentProcessName")
    command_line = f.get("CommandLine")
    user = f.get("SubjectUserName") or f.get("TargetUserName")

    document = {
        "@timestamp": normalize_timestamp(f.get("TimeCreated") or event.get("@timestamp")),
        "event": {
            "kind": "event",
            "dataset": "windows.security",
            "code": str(event_id) if event_id is not None else None,
            "category": [],
            "type": [],
            "action": None,
            "outcome": None,
            "original": event.get("message"),
        },
        "host": {
            "name": f.get("Computer"),
        },
        "user": {
            "name": user,
        },
        "process": {
            "name": basename_windows(image),
            "executable": image,
            "command_line": command_line,
            "parent": {
                "name": basename_windows(parent),
                "executable": parent,
            },
        },
        "parser": {
            "id": "windows-security-json",
            "version": "0.1.0",
            "status": parsed.status,
            "confidence": 0.99,
        },
        "vendor": {
            "windows": f,
        },
        "sigma": {
            "EventID": event_id,
            "Image": image,
            "CommandLine": command_line,
            "ParentImage": parent,
            "User": user,
            "Computer": f.get("Computer"),
        },
    }

    if str(event_id) == "4688":
        document["event"].update(
            {
                "category": ["process"],
                "type": ["start"],
                "action": "process_start",
                "outcome": "success",
            }
        )
    elif str(event_id) == "4625":
        document["event"].update(
            {
                "category": ["authentication"],
                "type": ["start", "denied"],
                "action": "logon",
                "outcome": "failure",
            }
        )

    return document
