# Sigma Compatibility Strategy

## Goals

- Keep a stable internal schema.
- Avoid storing only Sigma-native names.
- Support Sigma field rewrites through processing pipelines.

## Strategy

1. Normalize into canonical fields.
2. Provide a processing pipeline that maps Sigma fields to canonical fields.
3. Optionally store select Sigma aliases for migration and troubleshooting.
4. Convert Sigma to Lucene or DSL through pySigma backend tooling.

## Profiles

Maintain separate Sigma mapping profiles for:
- windows security
- windows sysmon
- linux auth
- firewall traffic
- generic app logs
