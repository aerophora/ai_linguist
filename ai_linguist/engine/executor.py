from openai import OpenAI
from openai.types.chat import ChatCompletion


def executor(openai_instance: OpenAI, question: str) -> ChatCompletion:
    return openai_instance.chat.completions.create(
        model="chatgpt-4o-latest", messages=[{"role": "user", "content": f"{question}"}]
    )
