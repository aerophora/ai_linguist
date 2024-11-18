from pydantic import BaseModel
from .open_ai import OpenAiConfig
from .obsidian import ObsidianConfig
from .user import UserConfig
from .english import EnglishConfig
from .german import GermanConfig


class Config(BaseModel):
    OpenAi: OpenAiConfig = OpenAiConfig()
    Obsidian: ObsidianConfig = ObsidianConfig()
    User: UserConfig = UserConfig()
    English: EnglishConfig = EnglishConfig()
    German: GermanConfig = GermanConfig()
