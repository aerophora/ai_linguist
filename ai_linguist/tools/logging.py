import betterlogging as blogging  # type: ignore


def setup_logging() -> None:
    blogging.basic_colorized_config(level=blogging.INFO)
