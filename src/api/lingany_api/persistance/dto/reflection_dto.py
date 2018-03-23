from uuid import UUID

from sqlutils import Entity


class ReflectionDTO(Entity):

    @property
    def _key_field(self) -> str:
        return 'reflection_id'

    def __init__(self, uid: UUID = None, title: str = None,
                 native_language_id: UUID = None, foreign_language_id: UUID = None) -> None:

        super().__init__(uid)
        self._title = title
        self._native_language_id = native_language_id
        self._foreign_language_id = foreign_language_id

    @property
    def title(self) -> str:
        return self._title

    @property
    def native_language_id(self) -> UUID:
        return self._native_language_id

    @property
    def foreign_language_id(self) -> UUID:
        return self._foreign_language_id
