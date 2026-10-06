import logging
from .agents import AGENTS
from .config import settings
from .evaluator import EvidenceEvaluator
from .models import ResearchReport

log = logging.getLogger(__name__)

class ResearchEngine:
    def plan(self, q: str) -> list[str]:
        return [
            f"Define scope for: {q}",
            "Collect specialist evidence",
            "Evaluate evidence coverage and confidence",
            "Cross-check claims",
            "Synthesize findings",
        ]

    def run(self, q: str) -> ResearchReport:
        evidence = []
        for agent in AGENTS[: settings.max_agents]:
            evidence.extend(agent.research(q))
        evidence = evidence[: settings.max_evidence]

        quality = EvidenceEvaluator().evaluate(evidence)
        status = "completed" if quality["status"] == "ready" else "partial"
        synthesis = " ".join(e.claim for e in evidence)

        log.info(
            "research_completed",
            extra={
                "agents": len(AGENTS[: settings.max_agents]),
                "evidence": len(evidence),
                "quality": quality,
                "status": status,
            },
        )
        return ResearchReport(
            question=q,
            plan=self.plan(q),
            evidence=evidence,
            synthesis=synthesis,
            status=status,
        )
