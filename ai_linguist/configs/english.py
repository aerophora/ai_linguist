from pydantic import BaseModel
from pathlib import Path


class EnglishConfig(BaseModel):
    VERB_NOTE: Path = Path("Verbs.md")
    NOUN_NOTE: Path = Path("Nouns.md")
    SENTENCE_NOTE: Path = Path("Sentences and context.md")
    ADJECTIVE_NOTE: Path = Path("Adjectives.md")
    ADVERB_NOTE: Path = Path("Adverbs.md")
