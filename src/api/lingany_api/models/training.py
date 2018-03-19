from uuid import UUID

from lingany_api.models.category import Category
from sqlutils import Model


class Training(Model):

    def __init__(self, uid: UUID) -> None:
        super().__init__(uid)
        self._category: Category = None
        self._native_word: str = None
        self._foreign_word: str = None

    @property
    def category(self) -> Category:
        return self._category

    @property
    def native_word(self) -> str:
        return self._native_word

    @property
    def foreign_word(self) -> str:
        return self._foreign_word

    def fill(self, category: Category, native_word: str, foreign_word: str) -> "Training":
        self._category = category
        self._native_word = native_word
        self._foreign_word = foreign_word
        self._filled()
        return self
