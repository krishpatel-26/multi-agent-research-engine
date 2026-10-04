import logging
from .agents import AGENTS
from .config import settings
from .models import ResearchReport
log=logging.getLogger(__name__)
class ResearchEngine:
    def plan(self,q): return [f'Define scope for: {q}','Collect specialist evidence','Cross-check claims','Synthesize findings']
    def run(self,q):
        evidence=[]
        for agent in AGENTS[:settings.max_agents]: evidence.extend(agent.research(q))
        evidence=evidence[:settings.max_evidence]
        log.info('research_completed',extra={'agents':len(AGENTS[:settings.max_agents]),'evidence':len(evidence)})
        return ResearchReport(question=q,plan=self.plan(q),evidence=evidence,synthesis=' '.join(e.claim for e in evidence),status='completed')
