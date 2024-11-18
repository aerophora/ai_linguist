import betterlogging as blogging  # type: ignore

main_logger = blogging.getLogger("ai_linguist")
httpx_logger = blogging.getLogger("httpx")


def setup_logging() -> None:
    httpx_logger.disabled = True
    blogging.basic_colorized_config(level=blogging.INFO)
