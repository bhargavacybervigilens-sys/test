from pathlib import Path


def test_sigma_rule_examples_exist():
    assert Path("rules/windows/suspicious_whoami.yml").exists()
    assert Path("rules/linux/ssh_failed_login.yml").exists()
