from __future__ import annotations

from siem_normalizer.classifier import classify
from siem_normalizer.registry import SOURCE_REGISTRY


class ParserEngine:
    def __init__(self, registry=None):
        self.registry = registry or SOURCE_REGISTRY

    def parse(self, event: dict):
        entry = classify(event, self.registry)
        return entry, entry["parser"].parse(event)
