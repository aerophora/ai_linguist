from .engine.get_knowledge import get_knowledge
from .engine.process_polling import process_polling
from .factory.get_config import get_config
from .factory.get_openai import get_openai
from .tools.logging import setup_logging


def main() -> None:
    setup_logging()
    config = get_config()
    openai = get_openai(config)
    knowledge = get_knowledge(name=config.Obsidian.KNOWLEDGE_NAME)
    process_polling(openai, knowledge, config)


if __name__ == "__main__":
    main()
