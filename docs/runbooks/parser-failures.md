# Parser Failure Runbook

1. Check the dead-letter index.
2. Group failures by `error.stage` and `parser.id`.
3. Confirm whether the source format changed.
4. Add new fixtures for the failing samples.
5. Update mappings or parser logic.
6. Replay from queue or captured samples.
