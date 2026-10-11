# Reproducible research runs

Each research run should capture a stable run identifier and enough metadata to reproduce its evaluation without storing unnecessary prompt content.

## Required metadata
- run ID and UTC timestamp
- question or fixture ID
- application version / commit SHA
- model/provider identifiers when applicable
- evaluator configuration and thresholds
- source identifiers and retrieval timestamps
- deduplication counts and review reason codes
- final status and duration

## Reproducibility rules
1. Keep benchmark fixtures version-controlled.
2. Separate synthetic fixtures from real research records.
3. Avoid changing evaluation thresholds mid-run.
4. Preserve the original evidence list before deduplication for audit.
5. Compare runs only when dataset and evaluator versions are known.
6. Treat missing provenance as a review condition, not as proof that evidence is false.

This document specifies a recommended contract; it does not claim that run persistence is already implemented.
