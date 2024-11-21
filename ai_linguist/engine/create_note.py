import json
from datetime import datetime
from pathlib import Path
from textwrap import dedent

from ..configs.english import EnglishConfig
from ..configs.german import GermanConfig
from ..configs.main import Config
from ..tools.logging import main_logger
from .append_to_list import append_to_list_in_file


def create_note(
    data: dict[str, str],
    knowledge: list[Path],
    config: Config,
    question: str | None = None,
) -> bool | list[str]:
    match = {"1": "first", "2": "second", "3": "third"}

    while True:
        index = str(
            input(
                "\n👉🏻 Choose which response to use in your note "
                "(1, 2, 3, or Stop) ✨: "
            )
        )

        if index.lower() == "stop":
            return False

        final_request = None

        for number, word in match.items():
            if number == index:
                final_request = data.get(word)
                break

        if final_request:
            try:
                data = json.loads(final_request)
            except Exception as e:
                raise ValueError(f"Request can't be deserialized ❌: {e}")
        else:
            return ["Incorrect choise", index]

        obj = data.get("object", "Unknown")
        translate = data.get("translate", "Unknown")
        file_id = data.get("file_id", "Unknown")
        original = data.get("native", "Unknown")
        language = file_id[:2] if file_id else None
        question = question

        direction: GermanConfig | EnglishConfig

        if language == "EN":
            hashtag = "#fe"
            direction = config.English
        elif language == "DE":
            hashtag = "#fd"
            direction = config.German

        if obj == "verb":
            file = direction.VERB_NOTE
        elif obj == "noun":
            file = direction.NOUN_NOTE
        elif obj == "adjective":
            file = direction.ADJECTIVE_NOTE
        elif obj == "adverb":
            file = direction.ADVERB_NOTE
        elif obj == "sentence":
            file = direction.SENTENCE_NOTE

        all_notes_path = knowledge[0]
        final_path = all_notes_path / file

        current_date = datetime.now().strftime("%d.%m.%Y")
        current_time = datetime.now().strftime("%H:%M")

        note_content = dedent(
            f"""\
        ---
        date: {current_date}
        time: {current_time}
        TARGET DECK: Raw notes::{file_id}\n
        ---
        🏷️ Tags: #Linguistics #Zeflashcard\n
        # {translate} {hashtag}\n
        {original}
        """
        )

        try:
            append_to_list_in_file(
                final_path=final_path, file_id=file_id, translate=translate
            )
        except Exception as e:
            raise SystemError(f"Error while adding a link to the MOC ❌: {e}")

        try:
            new_note_path = all_notes_path / f"{file_id}.md"
            new_note_path.write_text(note_content, encoding="utf-8")
        except Exception as e:
            raise SystemError(f"Error while creating a note ❌: {e}")
        else:
            main_logger.info(
                f"Note created successfully at {new_note_path} ✨"
            )

        return True
