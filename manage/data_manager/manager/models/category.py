from typing import Set
from uuid import UUID

from manager.models.reflection import Reflection


class Category(object):

    def __init__(self, uid: UUID, title: str, reflection: Reflection, items: Set[str]) -> None:
        self._uid = uid
        self._title = title
        self._reflection = reflection
        self._items = items

    @property
    def uid(self) -> UUID:
        return self._uid

    @property
    def title(self) -> str:
        return self._title

    @property
    def reflection(self) -> Reflection:
        return self._reflection

    @property
    def items(self) -> Set[str]:
        return self._items
