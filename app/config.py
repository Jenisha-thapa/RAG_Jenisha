from pydantic_settings import BaseSettings
from pydantic import AnyUrl, EmailStr

class Settings(BaseSettings):
    DATABASE_URL: AnyUrl = "sqlite:///./palmmind.db"
    VECTOR_DB_URL: str
    VECTOR_DB_API_KEY: str
    EMBEDDING_MODEL: str = "sentence-transformers/all-mpnet-base-v2"
    OPENAI_API_KEY: str = None
    EMAIL_HOST: str
    EMAIL_PORT: int
    EMAIL_USERNAME: str
    EMAIL_PASSWORD: str
    EMAIL_FROM: EmailStr
    REDIS_URL: str = "redis://localhost:6379"
    
    class Config:
        env_file = ".env"

settings = Settings()