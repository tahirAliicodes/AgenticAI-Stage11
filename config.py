# config.py
# Stage11/config.py
# Loads all settings from .env file

from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str = "AgenticAI"
    app_env: str = "development"
    log_level: str = "INFO"
    max_workers: int = 3
    host: str = "0.0.0.0"
    port: int = 8000
    ollama_url: str = "http://localhost:11434"
    ollama_model: str = "llama3.1"

    class Config:
        env_file = ".env"

settings = Settings()