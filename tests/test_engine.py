from app.engine import ResearchEngine
from app.evaluator import EvidenceEvaluator, deduplicate_evidence
from app.models import Evidence

def test_plan_and_evidence():
    r = ResearchEngine().run("How should a RAG system be evaluated?")
    assert len(r.plan) == 5
    assert len(r.evidence) == 4
    assert r.status == "completed"

def test_empty_evidence_is_not_ready():
    assert EvidenceEvaluator().evaluate([])["status"] == "insufficient"

def test_duplicate_claim_source_keeps_highest_confidence():
    rows = [
        Evidence(agent="retrieval", claim="  RAG improves   grounding ", source="docs://rag", confidence=0.6),
        Evidence(agent="systems", claim="rag improves grounding", source="DOCS://RAG", confidence=0.9),
    ]
    unique = deduplicate_evidence(rows)
    assert len(unique) == 1
    assert unique[0].confidence == 0.9
    metrics = EvidenceEvaluator().evaluate(rows)
    assert metrics["duplicate_rate"] == 0.5
    assert metrics["unique_evidence"] == 1
