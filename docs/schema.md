# Canonical Schema

The canonical schema is ECS-like but intentionally minimal for a starter implementation.

## Required top-level objects

- `@timestamp`
- `event.*`
- `host.*`
- `user.*`
- `process.*`
- `source.*`
- `destination.*`
- `observer.*`
- `parser.*`
- `vendor.*`
- `labels.*`

## Event taxonomy

### Common values

- `event.kind`: `event`, `alert`, `metric`
- `event.category`: `authentication`, `process`, `network`, `file`, `web`, `registry`, `dns`, `configuration`
- `event.type`: `start`, `end`, `change`, `info`, `denied`, `connection`, `creation`, `deletion`
- `event.outcome`: `success`, `failure`, `unknown`

## Naming rules

1. Preserve vendor fields under `vendor.*`.
2. Use canonical field names for detections and dashboards.
3. Only add `sigma.*` aliases for fields commonly required by upstream Sigma rules.
4. Normalize timestamps into UTC ISO8601 for `@timestamp`.
5. Use `event.original` for the original log line or raw JSON string.
