# Architecture

## Runtime flow

```text
Sources -> Edge Collectors -> Queue (optional) -> Data Prepper -> Normalizer -> OpenSearch -> Detections
```

## Component roles

### Edge collectors

Collectors should handle:
- file tailing,
- journald/syslog ingestion,
- transport retries,
- buffering,
- source tagging.

Collectors should not own detection-critical normalization logic.

### Queue

A queue is optional for small deployments, but recommended for production. It provides:
- replay,
- ingest smoothing,
- parser rollout safety,
- isolation from OpenSearch slowdowns.

### Data Prepper

Use Data Prepper for:
- HTTP intake,
- routing by source tags,
- lightweight parsing,
- OpenSearch sink delivery.

### Normalizer

The normalizer is the core custom layer. It should:
- classify sources,
- parse structured/unstructured fields,
- normalize into a canonical schema,
- derive event taxonomy,
- expose Sigma aliases where required,
- reject malformed events into dead-letter flow.

### OpenSearch

Use dataset-oriented indices or data streams, such as:
- `logs-windows-security-*`
- `logs-linux-auth-*`
- `logs-network-firewall-*`
- `logs-dead-letter-*`

### Detection pipeline

Use pySigma with processing pipelines to map Sigma fields to internal fields before conversion to Lucene or OpenSearch-compatible query objects.
