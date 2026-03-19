# OpenSearch SIEM Ingest Starter

This repository is a starter implementation for an OpenSearch-native SIEM ingest stack with:

- lightweight collectors,
- a custom parser and normalization engine,
- Sigma field compatibility,
- dataset-oriented OpenSearch templates,
- and a testable source onboarding workflow.

## Repository goals

1. Collect logs from Linux, Windows, network devices, applications, and cloud sources.
2. Parse raw log formats into structured intermediate events.
3. Normalize events into a canonical schema aligned to common security use cases.
4. Preserve Sigma compatibility through field aliases and processing pipelines.
5. Index data efficiently into OpenSearch for search, alerting, and correlation.

## Initial scope

This starter includes:

- Fluent Bit collector examples
- Data Prepper routing pipelines
- A Python normalization package skeleton
- Source mapping definitions
- Sample Sigma processing pipelines and conversion tooling
- OpenSearch index templates and ISM policies
- Golden-test fixtures for selected sources

## Suggested architecture

```text
Fluent Bit / Vector -> Kafka (optional) -> Data Prepper -> Normalizer -> OpenSearch -> Alerting
```

## Quick start

1. Review `docs/architecture.md` and `docs/schema.md`.
2. Start the development stack with `docker compose -f deploy/docker-compose.dev.yml up -d`.
3. Create a Python virtualenv inside `normalizer/` and install the package.
4. Run `pytest normalizer/tests` to validate example normalizers.
5. Customize mappings under `normalizer/src/siem_normalizer/mappings/`.
6. Customize Sigma pipelines under `sigma/pipelines/`.

## Onboarding a new source

1. Add raw fixtures to `normalizer/tests/fixtures/raw/`.
2. Add expected normalized output to `normalizer/tests/golden/`.
3. Create a mapping file.
4. Add or extend a normalizer.
5. Add Sigma field mappings if needed.
6. Add OpenSearch mapping changes only when necessary.

## Production notes

- Use Kafka or Redpanda when sustained volume or burst tolerance matters.
- Keep regex use to a minimum in hot paths.
- Preserve original events for troubleshooting and audit.
- Prefer strict mappings and dataset-specific indices.
