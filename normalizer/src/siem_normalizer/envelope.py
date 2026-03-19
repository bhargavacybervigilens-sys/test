from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class ParseResult:
    status: str
    fields: dict
    errors: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)
    meta: dict = field(default_factory=dict)
