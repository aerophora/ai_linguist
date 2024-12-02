from openai import OpenAI
from openai.types.chat import ChatCompletion


def executor(
    openai_instance: OpenAI, question: str, instruction: str
) -> tuple[ChatCompletion, str]:
    return (
        openai_instance.chat.completions.create(
            model="chatgpt-4o-latest",
            messages=[
                {
                    "role": "user",
                    "content": f"{instruction}\n\n \
                    Here's user request: {question}",
                }
            ],
            n=3,
        ),
        question,
    )
