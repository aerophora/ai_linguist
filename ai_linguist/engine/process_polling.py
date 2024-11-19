from pathlib import Path

from openai import OpenAI

from ..configs.main import Config
from ..engine.create_note import create_note
from ..engine.executor import executor
from ..engine.poll import poll
from ..tools.logging import main_logger


def process_polling(
    openai: OpenAI, knowledge: list[Path], config: Config
) -> None:
    try:
        for result, question in poll(handler=executor, openai=openai):
            results = {
                "first": f"{result.choices[0].message.content}",
                "second": f"{result.choices[1].message.content}",
                "third": f"{result.choices[2].message.content}",
            }
            print(
                results.get("first"),
                results.get("second"),
                results.get("third"),
                sep="\n",
            )
            create_note(
                data=results,
                question=question,
                knowledge=knowledge,
                config=config,
            )

    except KeyboardInterrupt:
        main_logger.info("\nBye! 👋🏻")
