from typing import Callable, Generator
from openai import OpenAI
from openai.types.chat import ChatCompletion


def poll_user(
    handler: Callable[[OpenAI, str], tuple[ChatCompletion, str]],
    openai: OpenAI,
) -> Generator[tuple[ChatCompletion, str]]:
    while True:
        question = str(input("Write your word/sentence to translate 🌍: "))
        if question:
            yield handler(openai, question)
