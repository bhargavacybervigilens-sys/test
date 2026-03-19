from siem_normalizer.classifier import classify
from siem_normalizer.registry import SOURCE_REGISTRY


def test_classifier_matches_windows_security():
    event = {"tags": "windows.security"}
    result = classify(event, SOURCE_REGISTRY)
    assert result["id"] == "windows_security"
