from typing import Callable, Generator
from openai import OpenAI
from openai.types.chat import ChatCompletion


def poll_user(
    handler: Callable[[OpenAI, str], ChatCompletion], openai: OpenAI
) -> Generator[ChatCompletion]:
    while True:
        question = str(input("Select: "))
        if question:
            yield handler(openai, question)
