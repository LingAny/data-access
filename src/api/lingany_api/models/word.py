from uuid import UUID

from sqlutils import Model


class Word(Model):

    def __init__(self, uid: UUID) -> None:
        super().__init__(uid)
        self._text: str = None
        self._translation: str = None

    @property
    def text(self) -> str:
        return self._text

    @property
    def translation(self) -> str:
        return self._translation

    def fill(self, text: str, translation: str) -> "Word":
        self._text = text
        self._translation = translation
        self._filled()
        return self
