from __future__ import annotations

import ipaddress


def normalize_ip(value: str | None) -> str | None:
    if not value:
        return None
    return str(ipaddress.ip_address(value))
