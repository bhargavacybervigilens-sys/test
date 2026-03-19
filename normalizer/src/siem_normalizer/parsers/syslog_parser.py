from __future__ import annotations

import re

from siem_normalizer.envelope import ParseResult


SYSLOG_RE = re.compile(
    r"^(?P<timestamp>[A-Z][a-z]{2}\s+\d+\s\d{2}:\d{2}:\d{2}) (?P<hostname>\S+) (?P<program>[^\[:]+)(?:\[(?P<pid>\d+)\])?: (?P<message>.*)$"
)


class SyslogParser:
    def parse(self, event: dict) -> ParseResult:
        raw = event.get("message", "")
        match = SYSLOG_RE.match(raw)
        if not match:
            return ParseResult(status="failed", fields={"message": raw}, errors=["syslog parse failed"], meta={"parser_id": "syslog"})
        fields = match.groupdict()
        if fields.get("pid"):
            fields["pid"] = int(fields["pid"])
        return ParseResult(status="success", fields=fields, meta={"parser_id": "syslog"})
