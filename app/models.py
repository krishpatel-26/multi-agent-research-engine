from pydantic import BaseModel,Field
from typing import Literal
class ResearchRequest(BaseModel): question:str=Field(min_length=10,max_length=2000)
class Evidence(BaseModel): agent:str; claim:str; source:str; confidence:float=Field(ge=0,le=1)
class ResearchReport(BaseModel): question:str; plan:list[str]; evidence:list[Evidence]; synthesis:str; status:Literal['completed','partial']
