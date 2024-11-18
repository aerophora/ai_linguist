from pydantic_settings import BaseSettings, SettingsConfigDict


class OpenAiConfig(BaseSettings):
    TOKEN: str

    model_config = SettingsConfigDict(
        env_prefix="OPEN_AI_", env_file=".env", strict=True, extra="ignore"
    )
