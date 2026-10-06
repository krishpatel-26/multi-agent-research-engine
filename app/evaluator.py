from collections import Counter
from .models import Evidence
class EvidenceEvaluator:
    def evaluate(self,evidence:list[Evidence])->dict:
        if not evidence:return {"coverage":0.0,"agreement":0.0,"confidence":0.0,"status":"insufficient"}
        confidence=sum(e.confidence for e in evidence)/len(evidence); domains=Counter(e.agent for e in evidence)
        coverage=min(1.0,len(domains)/4); agreement=min(1.0,max(domains.values())/len(evidence))
        return {"coverage":round(coverage,3),"agreement":round(agreement,3),"confidence":round(confidence,3),"status":"ready" if confidence>=.70 and coverage>=.75 else "review"}
