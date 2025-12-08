from pydantic_settings import BaseSettings
from typing import Optional

class Settings(BaseSettings):
    PROJECT_NAME: str = "AI Book Backend"
    API_V1_STR: str = "/api/v1"
    
    # Database
    NEON_DSN: str
    
    # Qdrant
    QDRANT_URL: str
    QDRANT_API_KEY: Optional[str] = None
    
    # OpenAI
    OPENAI_API_KEY: str
    EMBEDDING_MODEL: str = "text-embedding-3-large"
    
    # Better Auth
    BETTER_AUTH_SECRET: str
    BETTER_AUTH_URL: str
    
    class Config:
        env_file = ".env"

settings = Settings()
