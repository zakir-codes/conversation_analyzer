from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    mongodb_uri: str = "mongodb://localhost:27017/sales_analyzer"
    app_name: str = "Sales Analyzer Backend"

    # Storage-related configuration
    storage_root: str = "storage"
    allowed_audio_exts: str = ".wav,.mp3,.mp4"
    allowed_transcript_exts: str = ".txt,.md"
    allowed_script_exts: str = ".txt,.md"
    max_upload_mb: int = 100

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()


