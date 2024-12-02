from typing import Callable, Generator

from openai import InternalServerError, OpenAI
from openai.types.chat import ChatCompletion

from ..tools.logging import main_logger


def poll(
    handler: Callable[[OpenAI, str, str], tuple[ChatCompletion, str]],
    openai: OpenAI,
    instruction: str,
) -> Generator[tuple[ChatCompletion, str], None, None]:
    while True:
        question = str(input("Enter a word or sentence to translate 🌍: "))
        if question:
            try:
                yield handler(openai, question, instruction)
            except InternalServerError:
                main_logger.error(
                    "\n\nOops... there seems to be an issue with \
                        your internet connection or the OpenAI server ❌🛜\n\n"
                )
                break
