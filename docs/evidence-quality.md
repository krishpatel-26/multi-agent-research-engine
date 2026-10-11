# Evidence quality policy

A research answer should distinguish what sources say from what the system concludes.

## Evidence record
Capture source identifier, title, URL when available, retrieval timestamp, claim text, and confidence with a documented meaning.

## Quality signals
- Source agreement: do independent sources support the same claim?
- Agent coverage: did the planned research roles contribute?
- Confidence: is the claim supported by evidence rather than model fluency?
- Duplication: do several records merely repeat the same underlying source?
- Freshness: is the source recent enough for the question?

## Guardrails
A high source count is not the same as independent corroboration. When evidence is weak, conflicting, or stale, return a review reason instead of manufacturing certainty.
