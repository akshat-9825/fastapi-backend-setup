"""Application Configuration"""

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Application settings using Pydantic BaseSettings"""

    # Application Settings
    app_name: str = "FastAPI Backend Setup"
    app_version: str = "1.0.0"
    debug: bool = True

    # Server Settings
    host: str = "0.0.0.0"
    port: int = 8000

    class Config:
        env_file = ".env"
        case_sensitive = False


# Create settings instance
settings = Settings()
