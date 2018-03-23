from uuid import UUID

from lingany_api.models.reflection import Reflection
from sqlutils import Model


class Category(Model):

    def __init__(self, uid: UUID) -> None:
        super().__init__(uid)
        self._reflection: Reflection = None
        self._title: str = None

    @property
    def title(self) -> str:
        return self._title

    @property
    def reflection(self) -> Reflection:
        return self._reflection

    def fill(self, title: str, reflection: Reflection) -> "Category":
        self._title = title
        self._reflection = reflection
        self._filled()
        return self
