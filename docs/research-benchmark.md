# Research engine benchmark plan

Use a fixed, versioned set of research questions and gold-standard evidence annotations.

Record per run:
- question ID and dataset version
- sources retrieved and unique source count
- duplicate evidence rate
- claim-level precision and coverage
- evaluator review reasons
- latency and token/cost estimates when available

Report results by question category, not only as a single aggregate. Include adversarial cases with contradictory sources, syndicated copies, missing dates, and unsupported claims. Never report benchmark scores until the evaluation has actually been run.
