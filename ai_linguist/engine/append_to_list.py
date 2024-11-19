from pathlib import Path

from ..tools.logging import main_logger


def append_to_list_in_file(
    final_path: Path, file_id: str, translate: str
) -> None:
    list_tag = "# AI_List 🧾"
    new_entry = f"- [[{file_id}|{translate}]]"

    try:
        if final_path.exists():
            with final_path.open("r", encoding="utf-8") as file:
                lines = file.readlines()
        else:
            raise FileNotFoundError(
                f"The file at {final_path} does not exist."
            )

        updated_lines = []
        tag_found = False
        for line in lines:
            updated_lines.append(line)
            if line.strip() == list_tag:
                updated_lines.append("\n")
                updated_lines.append(new_entry)
                tag_found = True

        if not tag_found:
            raise ValueError(f"Tag '{list_tag}' not found in the file.")

        with final_path.open("w", encoding="utf-8") as file:
            file.writelines(updated_lines)

        main_logger.info(
            f"Successfully added the new entry under '{list_tag}'"
            f"with double enter in {final_path}"
        )

    except Exception as e:
        print(f"Error: {e}")
