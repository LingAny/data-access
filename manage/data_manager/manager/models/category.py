from uuid import UUID

from manager.models.reflection import Reflection


class Category(object):
    def __init__(self, uid: UUID, title: str, reflection: Reflection) -> None:
        self._uid = uid
        self._title = title
        self._reflection = reflection

    @property
    def uid(self) -> UUID:
        return self._uid

    @property
    def title(self) -> str:
        return self._title

    @property
    def reflection(self) -> Reflection:
        return self._reflection
