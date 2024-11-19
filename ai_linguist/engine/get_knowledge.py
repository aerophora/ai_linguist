import os
from pathlib import Path

from ..tools.logging import main_logger


def get_knowledge(
    name: str = "ai_knowledge",
    start_dirs: list[Path] | None = None,
) -> list[Path]:
    """
    Finds the knowledge folder and its subdirectories, ensuring all \
    required subfolders and files exist.

    Args:
        name (str): Name of the folder to find.
        start_dirs (list[Path] | None): Directories to start searching from.

    Returns:
        list[Path]: List containing paths to "All notes", the template \
        folder, and the linguistics template.

    Raises:
        FileNotFoundError: If the main folder or required \
        subfolders/files are not found.
        FileExistsError: If any of the required subfolders or \
        files are missing.
    """
    if start_dirs is None:
        start_dirs = [
            Path.home(),
            Path("/data/data/"),
            Path("/"),
        ]

    found_path = None
    for start_dir in start_dirs:
        for root, dirs, files in os.walk(start_dir):
            files = files
            if name in dirs:
                found_path = Path(root) / name
                main_logger.info(f"The folder was found: {found_path} ✨")
                break
        if found_path:
            break

    if not found_path:
        msg = f"The folder with specified name wasn't found: {name} ❌"
        raise FileNotFoundError(msg)

    # Define required paths
    all_notes_folder = found_path / "All notes"
    template_folder = found_path / "Templates" / "For flashcards"
    linguist_note = template_folder / "Linguistics t3mplate.md"

    # Check existence of required folders and files
    if not all_notes_folder.exists():
        raise FileExistsError("Folder 'All notes' wasn't found ❌")
    main_logger.info("Folder 'All notes' exists! ✨")

    if not template_folder.exists():
        raise FileExistsError("Template folder wasn't found ❌")
    main_logger.info("Template folder exists! ✨")

    if not linguist_note.exists() or not linguist_note.is_file():
        raise FileExistsError("Linguistics template note wasn't found ❌")
    main_logger.info("Linguistics template note exists! ✨")

    return [all_notes_folder, template_folder, linguist_note, found_path]
