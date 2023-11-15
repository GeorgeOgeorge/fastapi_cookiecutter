from functools import lru_cache

from pydantic import BaseSettings, constr


class AppSettings(BaseSettings):
    app_host: str = "0.0.0.0"
    app_port: int = 8080
    database_url: constr(strict=True)
    app_api_token: constr(strict=True)

    class Config:
        env_file = ".env"


@lru_cache
def get_settings() -> AppSettings:
    return AppSettings()
