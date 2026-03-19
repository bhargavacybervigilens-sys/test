import json

from siem_normalizer.normalizer_engine import NormalizerEngine


def test_firewall_deny_normalization():
    engine = NormalizerEngine()
    with open("tests/fixtures/raw/firewall_deny.log", "r", encoding="utf-8") as handle:
        raw = handle.read().strip()
    event = {"tags": "network.firewall", "message": raw}
    with open("tests/golden/firewall_deny.expected.json", "r", encoding="utf-8") as handle:
        expected = json.load(handle)
    assert engine.process(event) == expected
