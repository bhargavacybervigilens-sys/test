from __future__ import annotations

from siem_normalizer.envelope import ParseResult


class RegexParser:
    def parse(self, event: dict) -> ParseResult:
        return ParseResult(status="failed", fields={}, errors=["Not implemented in starter skeleton"], meta={"parser_id": "regex"})
