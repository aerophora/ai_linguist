from pathlib import Path

from pydantic import BaseModel


class GermanConfig(BaseModel):
    VERB_NOTE: Path = Path("Verben.md")
    NOUN_NOTE: Path = Path("Nomen.md")
    SENTENCE_NOTE: Path = Path("Sätze.md")
    ADJECTIVE_NOTE: Path = Path("Adjektive.md")
    ADVERB_NOTE: Path = Path("Adverben.md")
