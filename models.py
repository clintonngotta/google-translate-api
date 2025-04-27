from pydantic import BaseModel

class TranslationModel(BaseModel):
    text: str
    target_lang: str | None = "fr"
