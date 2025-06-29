from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "BeatTick"
    DATABASE_URL: str = "sqlite:///./beattick.db"

    class Config:
        case_sensitive = True

settings = Settings()