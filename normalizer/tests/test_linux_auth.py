import json

from siem_normalizer.normalizer_engine import NormalizerEngine


def test_linux_auth_failed_ssh():
    engine = NormalizerEngine()
    with open("tests/fixtures/raw/linux_auth_ssh_failed.log", "r", encoding="utf-8") as handle:
        raw = handle.read().strip()
    event = {"tags": "linux.auth", "message": raw}
    with open("tests/golden/linux_auth_ssh_failed.expected.json", "r", encoding="utf-8") as handle:
        expected = json.load(handle)
    assert engine.process(event) == expected
