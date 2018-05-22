from uuid import UUID

from sqlutils import Entity


class LanguageDTO(Entity):

    @property
    def _key_field(self) -> str:
        return 'language_id'

    def __init__(self, uid: UUID = None, title: str = None, code: str = None) -> None:

        super().__init__(uid)
        self._title = title
        self._code = code

    @property
    def title(self) -> str:
        return self._title

    @property
    def code(self) -> str:
        return self._code
