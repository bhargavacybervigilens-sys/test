from __future__ import annotations

from siem_normalizer.envelope import ParseResult


class KvParser:
    def parse(self, event: dict) -> ParseResult:
        message = event.get("message", "")
        fields = {}
        for token in message.split():
            if "=" not in token:
                continue
            key, value = token.split("=", 1)
            fields[key] = value
        return ParseResult(status="success", fields=fields, meta={"parser_id": "kv"})
