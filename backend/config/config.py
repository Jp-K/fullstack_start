from pydantic import BaseSettings
import os

class CommonSettings(BaseSettings):
    APP_NAME: str = "fullstack-ensinamentos"
    DEBUG_MODE: bool = False
    API_STR: str = "/api"


class ServerSettings(BaseSettings):
    HOST: str = "127.0.0.1"
    PORT: int = 8000


class DatabaseSettings(BaseSettings):
    SQLALCHEMY_DATABASE_URL: str = os.getenv("SQLALCHEMY_DATABASE_URL")


class Settings(CommonSettings, ServerSettings, DatabaseSettings):
    env_file = ".env"


settings = Settings()