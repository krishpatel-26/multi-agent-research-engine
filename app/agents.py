import re
from .models import Evidence
class Specialist:
    def __init__(self,name,domain): self.name,self.domain=name,domain
    def research(self,q):
        terms=re.findall(r'[A-Za-z]{4,}',q.lower())[:5]
        return [Evidence(agent=self.name,claim=f'{self.domain} specialist identified research dimensions: {", ".join(terms)}.',source='local://deterministic-research',confidence=.72)]
AGENTS=[Specialist('retrieval','retrieval systems'),Specialist('systems','distributed systems'),Specialist('evaluation','AI evaluation'),Specialist('product','product engineering')]
