from uuid import UUID


class Language(object):

    def __init__(self, uid: UUID, title: str, code: str) -> None:
        self._uid = uid
        self._title = title
        self._code = code

    @property
    def uid(self) -> UUID:
        return self._uid

    @property
    def title(self) -> str:
        return self._title

    @property
    def code(self) -> str:
        return self._code
