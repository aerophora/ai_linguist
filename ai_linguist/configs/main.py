from pydantic import BaseModel
from .open_ai import OpenAiConfig


class Config(BaseModel):
    OpenAi: OpenAiConfig = OpenAiConfig()
