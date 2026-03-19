from __future__ import annotations

from siem_normalizer.envelope import ParseResult


class JsonParser:
    def parse(self, event: dict) -> ParseResult:
        fields = dict(event)
        return ParseResult(status="success", fields=fields, meta={"parser_id": "json"})
