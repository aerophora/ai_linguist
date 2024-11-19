from pydantic import BaseModel

from .english import EnglishConfig
from .german import GermanConfig
from .obsidian import ObsidianConfig
from .open_ai import OpenAiConfig
from .user import UserConfig


class Config(BaseModel):
    OpenAi: OpenAiConfig = OpenAiConfig()
    Obsidian: ObsidianConfig = ObsidianConfig()
    User: UserConfig = UserConfig()
    English: EnglishConfig = EnglishConfig()
    German: GermanConfig = GermanConfig()
