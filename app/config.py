from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "Geetify"
    api_version: str = "v1"
    debug: bool = True

    class Config:
        env_file = ".env"

settings = Settings()
