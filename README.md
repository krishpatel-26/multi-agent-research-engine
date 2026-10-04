# Multi-Agent Research Engine

Production-minded research orchestration with specialist agents, evidence aggregation, typed contracts, and a deterministic local fallback.

## Run
`pip install -r requirements.txt` then `uvicorn app.api:app --reload`.
POST `/research` with `{ "question": "Compare RAG architectures" }`.
