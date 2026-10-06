# Multi-Agent Research Engine

Production-minded research orchestration with specialist agents, evidence aggregation, typed contracts, quality gating, and a deterministic local fallback.

## Architecture

`request -> specialist agents -> evidence store -> quality gate -> synthesis`

The quality gate evaluates **coverage**, **source agreement**, and **mean confidence**. A report is marked `completed` only when the evidence clears the configured quality bar; otherwise it is returned as `partial` for review.

## Run

`pip install -r requirements.txt`

`uvicorn app.api:app --reload`

POST `/research` with:

`{ "question": "Compare RAG architectures" }`

## Design notes

- Provider-neutral specialist agents
- Typed Pydantic contracts
- Deterministic offline fallback
- Explicit evidence-quality gate
- Structured logs for agent/evidence/quality counts
