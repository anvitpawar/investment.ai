from pydantic import BaseSettings


class Settings(BaseSettings):
    DATABASE_URL: str
    ZERODHA_API_KEY: str | None = None
    ZERODHA_API_SECRET: str | None = None
    ZERODHA_ACCESS_TOKEN: str | None = None
    AWS_REGION: str | None = None
    LOG_LEVEL: str = "INFO"

    class Config:
        env_file = ".env"


settings = Settings()
