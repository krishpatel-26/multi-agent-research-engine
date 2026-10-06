from collections import Counter
from .models import Evidence

class EvidenceEvaluator:
    def evaluate(self, evidence: list[Evidence]) -> dict:
        if not evidence:
            return {"coverage": 0.0, "agreement": 0.0, "confidence": 0.0, "status": "insufficient"}

        confidence = sum(e.confidence for e in evidence) / len(evidence)
        domains = Counter(e.agent for e in evidence)
        sources = Counter(e.source for e in evidence)

        coverage = min(1.0, len(domains) / 4)
        agreement = max(sources.values()) / len(evidence)
        ready = confidence >= 0.70 and coverage >= 0.75 and agreement >= 0.75

        return {
            "coverage": round(coverage, 3),
            "agreement": round(agreement, 3),
            "confidence": round(confidence, 3),
            "status": "ready" if ready else "review",
        }
