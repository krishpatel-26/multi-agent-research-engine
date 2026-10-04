from fastapi import FastAPI
from .models import ResearchRequest,ResearchReport
from .engine import ResearchEngine
app=FastAPI(title='Multi-Agent Research Engine',version='1.0.0'); engine=ResearchEngine()
@app.get('/health')
def health(): return {'status':'ok'}
@app.post('/research',response_model=ResearchReport)
def research(req:ResearchRequest): return engine.run(req.question)
