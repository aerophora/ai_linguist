from openai import OpenAI
from openai.types.chat import ChatCompletion

from ..instructions.engine import TRANSLATE


def executor(
    openai_instance: OpenAI, question: str
) -> tuple[ChatCompletion, str]:
    return (
        openai_instance.chat.completions.create(
            model="chatgpt-4o-latest",
            messages=[
                {
                    "role": "user",
                    "content": f"{TRANSLATE}\n\n \
                    Here's user request: {question}",
                }
            ],
            n=3,
        ),
        question,
    )
