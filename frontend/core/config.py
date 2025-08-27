from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    backend_base_url: str = "http://localhost:8000"
    allowed_extensions: str = ".wav,.mp3,.mp4,.txt,.md"
    max_upload_mb: int = 100

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()

