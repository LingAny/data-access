from uuid import UUID

from sqlutils import Entity


class TrainingDTO(Entity):

    @property
    def _key_field(self) -> str:
        return 'training_id'

    def __init__(self, uid: UUID = None, category_id: UUID = None, native_word: str = None,
                 foreign_word: str = None) -> None:

        super().__init__(uid)
        self._category_id = category_id
        self._native_word = native_word
        self._foreign_word = foreign_word

    @property
    def category_id(self) -> UUID:
        return self._category_id

    @property
    def native_word(self) -> str:
        return self._native_word

    @property
    def foreign_word(self) -> str:
        return self._foreign_word
