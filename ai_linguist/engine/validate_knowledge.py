from pathlib import Path
from ..tools.logging import main_logger


def validate_knowledge(folder_path: Path) -> list[Path]:
    all_notes_folder = folder_path / "All notes"
    template_folder = folder_path / "Templates" / "For flashcards"
    linguist_note = template_folder / "Linguistics t3mplate.md"

    if all_notes_folder.exists():
        main_logger.info("\nFolder with all notes folder exists!")
    else:
        raise FileExistsError("Folder with all notes wasn't found")

    if template_folder.exists():
        main_logger.info("\nTemplate folder exists!")
    else:
        raise FileExistsError("Template wasn't found")

    if linguist_note.exists() and linguist_note.is_file():
        main_logger.info("\nLinguistics template note exists!")
    else:
        raise FileExistsError("Linguistics template note wasn't found")

    return [all_notes_folder, template_folder, linguist_note]
