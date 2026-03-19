# Replay Runbook

1. Pause alerting if duplicate detections are unacceptable.
2. Reprocess the affected topic or saved fixtures into a staging pipeline.
3. Validate normalization output.
4. Replay to production only after comparison checks pass.
