# Source Onboarding Workflow

1. Capture representative raw events.
2. Decide the source family and parser strategy.
3. Add fixtures.
4. Write or extend mappings.
5. Add a normalizer if generic mapping is insufficient.
6. Add Sigma field mappings.
7. Validate against schemas and golden outputs.
8. Add OpenSearch mapping updates only if new stable fields are introduced.
9. Replay events through the dev stack.
