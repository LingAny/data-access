from uuid import UUID

from sqlutils import Model


class Language(Model):

    def __init__(self, uid: UUID) -> None:
        super().__init__(uid)
        self._title: str = None
        self._code: str = None

    @property
    def title(self) -> str:
        return self._title

    @property
    def code(self) -> str:
        return self._code

    def fill(self, title: str, code: str) -> "Language":
        self._title = title
        self._code = code
        self._filled()
        return self
