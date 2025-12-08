# app/core/config.py
"""
Application configuration using Pydantic Settings.
"""

from pydantic_settings import BaseSettings
from typing import Optional


class Settings(BaseSettings):
    """
    Application settings loaded from environment variables.
    """
    # Database
    DATABASE_URL: str = "sqlite:///./calculator.db"
    
    # JWT Settings
    SECRET_KEY: str = "your-secret-key-change-in-production"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    REFRESH_TOKEN_EXPIRE_DAYS: int = 7
    
    # Optional JWT fields (for backwards compatibility)
    JWT_SECRET_KEY: Optional[str] = None
    JWT_REFRESH_SECRET_KEY: Optional[str] = None
    
    # Bcrypt
    BCRYPT_ROUNDS: int = 12
    
    # Redis
    REDIS_URL: str = "redis://localhost:6379/0"
    REDIS_HOST: str = "localhost"
    REDIS_PORT: int = 6379
    REDIS_DB: int = 0
    
    # Application
    APP_NAME: str = "Calculator API"
    DEBUG: bool = False
    
    class Config:
        env_file = ".env"
        case_sensitive = True


# Create a global settings instance
settings = Settings()


def get_settings() -> Settings:
    """
    Get the settings instance.
    This function is provided for backwards compatibility.
    """
    return settings