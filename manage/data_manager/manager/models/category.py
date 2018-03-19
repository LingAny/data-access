from typing import Set


class Category(object):

    def __init__(self, title: str, values: Set[str]) -> None:
        self._title = title
        self._values = values

    @property
    def title(self) -> str:
        return self._title

    @property
    def values(self) -> Set[str]:
        return self._values
