import json
from pathlib import Path
from ..configs.main import Config


def create_note(
    data: dict[str, str], question: str, knowledge_folders: list[Path], config: Config
) -> None:
    match = {"1": "first", "2": "second", "3": "third"}

    while True:
        index = str(
            input(
                "\nSelect which one from request can be used in your note (1, 2, 3, Stop) ✨: "
            )
        )

        if index.lower() == "stop":
            return

        for number, word in match.items():
            if number == index:
                final_request = data.get(word)
                break

        if final_request:
            data = json.loads(final_request)
        else:
            raise ValueError("Request can't be deserialized ❌")

        obj = data.get("object")
        translate = data.get("translate")
        file_id = data.get("file_id")
        start_question = question[2:]

        return
