import json

from siem_normalizer.normalizer_engine import NormalizerEngine


def test_windows_4688_normalization():
    engine = NormalizerEngine()
    with open("tests/fixtures/raw/windows_4688.json", "r", encoding="utf-8") as handle:
        event = json.load(handle)
    with open("tests/golden/windows_4688.expected.json", "r", encoding="utf-8") as handle:
        expected = json.load(handle)
    assert engine.process(event) == expected
