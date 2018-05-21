from uuid import UUID

from sqlutils import Entity


class WordDTO(Entity):

    @property
    def _key_field(self) -> str:
        return 'word_id'

    def __init__(self, uid: UUID = None, text: str = None, translation: str = None) -> None:

        super().__init__(uid)
        self._text = text
        self._translation = translation

    @property
    def text(self) -> str:
        return self._text

    @property
    def translation(self) -> str:
        return self._translation
