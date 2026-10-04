from pydantic_settings import BaseSettings
class Settings(BaseSettings):
    research_provider:str='local'; max_agents:int=4; max_evidence:int=20; log_level:str='INFO'
    model_config={'env_file':'.env','extra':'ignore'}
settings=Settings()
