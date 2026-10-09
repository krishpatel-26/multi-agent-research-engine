from collections import Counter
from .models import Evidence

REQUIRED_AGENT_COVERAGE = 4
MIN_CONFIDENCE = 0.70
MIN_AGREEMENT = 0.75

def evidence_key(item: Evidence) -> tuple[str, str]:
    return (" ".join(item.claim.lower().split()), item.source.strip().lower())

def deduplicate_evidence(evidence: list[Evidence]) -> list[Evidence]:
    """Keep the highest-confidence instance of each normalized claim/source pair."""
    unique = {}
    for item in evidence:
        key = evidence_key(item)
        if key not in unique or item.confidence > unique[key].confidence:
            unique[key] = item
    return list(unique.values())

class EvidenceEvaluator:
    def evaluate(self, evidence: list[Evidence]) -> dict:
        if not evidence:
            return {"coverage": 0.0, "agreement": 0.0, "confidence": 0.0, "unique_evidence": 0, "duplicate_rate": 0.0, "status": "insufficient"}

        unique = deduplicate_evidence(evidence)
        confidence = sum(e.confidence for e in unique) / len(unique)
        domains = Counter(e.agent for e in unique)
        sources = Counter(e.source for e in unique)
        coverage = min(1.0, len(domains) / REQUIRED_AGENT_COVERAGE)
        agreement = max(sources.values()) / len(unique)
        duplicate_rate = (len(evidence) - len(unique)) / len(evidence)
        ready = confidence >= MIN_CONFIDENCE and coverage >= 0.75 and agreement >= MIN_AGREEMENT
        return {
            "coverage": round(coverage, 3),
            "agreement": round(agreement, 3),
            "confidence": round(confidence, 3),
            "unique_evidence": len(unique),
            "duplicate_rate": round(duplicate_rate, 3),
            "status": "ready" if ready else "review",
        }
