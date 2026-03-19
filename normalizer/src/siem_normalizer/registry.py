from __future__ import annotations

from siem_normalizer.parsers.json_parser import JsonParser
from siem_normalizer.parsers.kv_parser import KvParser
from siem_normalizer.parsers.syslog_parser import SyslogParser
from siem_normalizer.normalizers.firewall_traffic import normalize as normalize_firewall
from siem_normalizer.normalizers.linux_auth import normalize as normalize_linux_auth
from siem_normalizer.normalizers.windows_security import normalize as normalize_windows_security


SOURCE_REGISTRY = [
    {
        "id": "linux_auth",
        "when": {"tag": "linux.auth"},
        "parser": SyslogParser(),
        "normalizer": type("N", (), {"normalize": staticmethod(normalize_linux_auth)})(),
    },
    {
        "id": "windows_security",
        "when": {"tag": "windows.security"},
        "parser": JsonParser(),
        "normalizer": type("N", (), {"normalize": staticmethod(normalize_windows_security)})(),
    },
    {
        "id": "firewall_kv",
        "when": {"tag": "network.firewall"},
        "parser": KvParser(),
        "normalizer": type("N", (), {"normalize": staticmethod(normalize_firewall)})(),
    },
]
