from uuid import UUID

from manager.models.language import Language


class Reflection(object):

    def __init__(self, uid: UUID, title: str, native_lang: Language, foreign_lang: Language) -> None:
        self._uid = uid
        self._title = title
        self._native_lang = native_lang
        self._foreign_lang = foreign_lang

    @property
    def uid(self) -> UUID:
        return self._uid

    @property
    def title(self) -> str:
        return self._title

    @property
    def native_lang(self) -> Language:
        return self._native_lang

    @property
    def foreign_lang(self) -> Language:
        return self._foreign_lang
