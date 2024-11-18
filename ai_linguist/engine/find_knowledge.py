import os
from pathlib import Path
from ..tools.logging import main_logger


def find_knowledge(
    name: str = "ai_knowledge",
    start_dirs: list[Path] | None = None,
) -> Path:
    if start_dirs is None:
        start_dirs = [
            Path.home(),
            Path("/data/data/") or Path("/"),
        ]

    for start_dir in start_dirs:
        for root, dirs, files in os.walk(start_dir):
            if name in dirs:
                found_path = Path(root) / name
                main_logger.info(f"Папка знайдена: {found_path}")
                return found_path

    raise FileNotFoundError(f"Не знайдено папки з таким імʼям: {name}")
