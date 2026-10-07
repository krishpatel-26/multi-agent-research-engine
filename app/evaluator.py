from collections import Counter
from .models import Evidence

REQUIRED_AGENT_COVERAGE = 4
MIN_CONFIDENCE = 0.70
MIN_AGREEMENT = 0.75

class EvidenceEvaluator:
    def evaluate(self, evidence: list[Evidence]) -> dict:
        if not evidence:
            return {"coverage": 0.0, "agreement": 0.0, "confidence": 0.0, "status": "insufficient"}

        confidence = sum(e.confidence for e in evidence) / len(evidence)
        domains = Counter(e.agent for e in evidence)
        sources = Counter(e.source for e in evidence)

        coverage = min(1.0, len(domains) / REQUIRED_AGENT_COVERAGE)
        agreement = max(sources.values()) / len(evidence)
        ready = (
            confidence >= MIN_CONFIDENCE
            and coverage >= 0.75
            and agreement >= MIN_AGREEMENT
        )

        return {
            "coverage": round(coverage, 3),
            "agreement": round(agreement, 3),
            "confidence": round(confidence, 3),
            "status": "ready" if ready else "review",
        }
