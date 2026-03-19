from __future__ import annotations

from siem_normalizer.classifier import classify
from siem_normalizer.registry import SOURCE_REGISTRY
from siem_normalizer.validation import validate_document


class NormalizerEngine:
    def __init__(self, registry=None):
        self.registry = registry or SOURCE_REGISTRY

    def process(self, event: dict) -> dict:
        entry = classify(event, self.registry)
        parsed = entry["parser"].parse(event)
        document = entry["normalizer"].normalize(event, parsed)
        validate_document(document)
        return document
