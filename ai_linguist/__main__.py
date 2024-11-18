from .factory.get_config import get_config
from .factory.get_openai import get_openai
from .engine.poll import poll_user
from .engine.executor import executor
from .tools.logging import (
    setup_logging,
    main_logger,
)
from .engine.find_knowledge import find_knowledge
from .engine.validate_knowledge import validate_knowledge
from .engine.create_note import create_note


def main() -> None:
    setup_logging()
    config = get_config()
    openai = get_openai(config)
    main_dir = find_knowledge(name=config.Obsidian.KNOWLEDGE_NAME)
    folders = validate_knowledge(main_dir)

    try:
        for result, question in poll_user(handler=executor, openai=openai):
            results = {
                "first": f"{result.choices[0].message.content}",
                "second": f"{result.choices[1].message.content}",
                "third": f"{result.choices[2].message.content}",
            }
            main_logger.info(
                f"\n{results.get('first')}\n\n{results.get('second')}\n\n{results.get('third')}"
            )
            create_note(
                data=results,
                question=question,
                knowledge_folders=folders,
                config=config,
            )

    except KeyboardInterrupt:
        main_logger.info("\nBye! 👋🏻")


if __name__ == "__main__":
    main()
