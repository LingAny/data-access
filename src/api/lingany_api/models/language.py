from uuid import UUID

from sqlutils import Model


class Language(Model):

    def __init__(self, uid: UUID) -> None:
        super().__init__(uid)
        self._title: str = None

    @property
    def title(self) -> str:
        return self._title

    def fill(self, title: str) -> "Language":
        self._title = title
        self._filled()
        return self
