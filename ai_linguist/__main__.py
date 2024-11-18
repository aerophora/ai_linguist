from .factory.get_config import get_config
from .factory.get_openai import get_openai
from .engine.poll import poll_user
from .engine.executor import executor
from .tools.logging import setup_logging
import logging


def main() -> None:
    setup_logging()
    config = get_config()
    openai = get_openai(config)

    try:
        for result in poll_user(executor, openai):
            logging.info(f"\n{result.choices[0].message.content}")
    except KeyboardInterrupt:
        logging.info("\nBye!")


if __name__ == "__main__":
    main()
