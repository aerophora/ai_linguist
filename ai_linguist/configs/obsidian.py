from pydantic_settings import (
    BaseSettings,
    SettingsConfigDict,
)


class ObsidianConfig(BaseSettings):

    KNOWLEDGE_NAME: str

    model_config = SettingsConfigDict(
        env_prefix="OBSIDIAN_",
        env_file=".env",
        strict=True,
        extra="ignore",
    )
