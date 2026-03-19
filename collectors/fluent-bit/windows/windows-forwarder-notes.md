# Windows Forwarding Notes

For Windows, prefer structured event export from:
- Winlog-based collector,
- native Windows Event Forwarding into a collector,
- or an existing JSON-capable forwarder.

The starter assumes Windows events arrive as structured JSON with source tag values such as:
- `windows.security`
- `windows.sysmon`
