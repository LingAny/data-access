from uuid import UUID

from sqlutils import Entity


class CategoryDTO(Entity):

    @property
    def _key_field(self) -> str:
        return 'category_id'

    def __init__(self, uid: UUID = None, reflection_id: UUID = None, title: str = None) -> None:

        super().__init__(uid)
        self._reflection_id = reflection_id
        self._title = title

    @property
    def reflection_id(self) -> UUID:
        return self._reflection_id

    @property
    def title(self) -> str:
        return self._title
