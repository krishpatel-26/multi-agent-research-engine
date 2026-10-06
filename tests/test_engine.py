from app.engine import ResearchEngine

def test_plan_and_evidence():
    r = ResearchEngine().run("How should a RAG system be evaluated?")
    assert len(r.plan) == 5
    assert len(r.evidence) == 4
    assert r.status == "completed"

def test_empty_evidence_is_not_ready():
    from app.evaluator import EvidenceEvaluator
    assert EvidenceEvaluator().evaluate([])["status"] == "insufficient"
