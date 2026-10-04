from app.engine import ResearchEngine
def test_plan_and_evidence():
 r=ResearchEngine().run('How should a RAG system be evaluated?')
 assert len(r.plan)==4 and len(r.evidence)==4 and r.status=='completed'
