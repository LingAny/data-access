from uuid import UUID

from manager.models.category import Category


class Training(object):

    def __init__(self, uid: UUID, category: Category, native_item: str, foreign_item: str) -> None:
        self._uid = uid
        self._category = category
        self._native_item = native_item
        self._foreign_item = foreign_item

    @property
    def uid(self) -> UUID:
        return self._uid

    @property
    def category(self) -> Category:
        return self._category

    @property
    def native_item(self) -> str:
        return self._native_item

    @property
    def foreign_item(self) -> str:
        return self._foreign_item
