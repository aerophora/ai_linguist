from .engine.process_polling import process_polling
from .factory.get_config import get_config
from .factory.get_instuction import get_engine_instruction
from .factory.get_knowledge import get_knowledge
from .factory.get_openai import get_openai_instance
from .tools.logging import setup_logging


def main() -> None:
    setup_logging()
    config = get_config()
    openai_instance = get_openai_instance(config)
    instruction = get_engine_instruction(config)
    knowledge = get_knowledge(name=config.Obsidian.KNOWLEDGE_NAME)
    process_polling(openai_instance, knowledge, config, instruction)


if __name__ == "__main__":
    main()
