import betterlogging as blogging  # type: ignore

main_logger = blogging.getLogger("ai_linguist")


def setup_logging() -> None:
    blogging.basic_colorized_config(level=blogging.ERROR)
