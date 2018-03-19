from uuid import UUID

from lingany_api.models.language import Language
from sqlutils import Model


class Training(Model):

    def __init__(self, uid: UUID) -> None:
        super().__init__(uid)
        self._title: str = None
        self._native_language: Language = None
        self._foreign_language: Language = None

    @property
    def title(self) -> str:
        return self._title

    @property
    def native_language(self) -> Language:
        return self._native_language

    @property
    def foreign_language(self) -> Language:
        return self._foreign_language

    def fill(self, title: str, native_language: Language, foreign_language: Language) -> "Training":
        self._title = title
        self._native_language = native_language
        self._foreign_language = foreign_language
        self._filled()
        return self
