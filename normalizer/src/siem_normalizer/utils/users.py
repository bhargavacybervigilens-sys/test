from __future__ import annotations


def split_user(value: str | None) -> tuple[str | None, str | None]:
    if not value:
        return None, None
    if "\\\\" in value:
        domain, user = value.split("\\\\", 1)
        return domain, user
    if "@" in value:
        user, domain = value.split("@", 1)
        return domain, user
    return None, value
