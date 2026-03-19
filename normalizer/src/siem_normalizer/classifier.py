from __future__ import annotations


def classify(event: dict, registry: list[dict]) -> dict:
    tags = event.get("tags")
    for entry in registry:
        if entry.get("when", {}).get("tag") == tags:
            return entry
    raise ValueError(f"No source definition matched tags={tags!r}")
