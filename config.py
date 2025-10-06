from pydantic import BaseSettings

class Settings(BaseSettings):
    app_name: str = "MyAPI"
    debug: bool = True
    database_url: str = "sqlite:///./test.db"

    class Config:
        env_file = ".env"

settings = Settings()