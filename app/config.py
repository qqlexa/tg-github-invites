from pydantic import BaseSettings


class Settings(BaseSettings):
    APP_NAME: str
    ORG_NAME: str
    TELEGRAM_TOKEN: str
    GITHUB_TOKEN: str
    TG_CHAT_ID: str

    class Config:
        case_sensitive = True
        env_file = '.env'


settings = Settings()
