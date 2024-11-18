from pydantic_settings import (
    BaseSettings,
    SettingsConfigDict,
)


class UserConfig(BaseSettings):
    LANGUAGE: str
    LEARNING: list[str | None]

    model_config = SettingsConfigDict(
        env_prefix="USER_",
        env_file=".env",
        strict=True,
        extra="ignore",
    )
