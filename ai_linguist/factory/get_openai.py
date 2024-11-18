from openai import OpenAI
from .get_config import Config


def get_openai(config: Config) -> OpenAI:
    return OpenAI(api_key=config.OpenAi.TOKEN)
