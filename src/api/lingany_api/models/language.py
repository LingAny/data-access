from uuid import UUID


class Language:

    def __init__(self, uid: UUID) -> None:
        self._uid = uid
        self._title: str = None

    @property
    def uid(self) -> UUID:
        return self._uid

    @property
    def title(self) -> str:
        return self._title

    def fill(self, title: str) -> "Language":
        self._title = title
        return self
