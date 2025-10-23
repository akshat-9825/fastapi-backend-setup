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

    # Database Settings
    database_url: str  # No default - must be set in .env
    database_echo: bool = False

    # CORS Settings
    cors_origins: list[str] = ["*"]  # Allow all origins by default
    cors_credentials: bool = True
    cors_methods: list[str] = ["*"]
    cors_headers: list[str] = ["*"]

    class Config:
        env_file = ".env"
        case_sensitive = False


# Create settings instance
settings = Settings()  # type: ignore
