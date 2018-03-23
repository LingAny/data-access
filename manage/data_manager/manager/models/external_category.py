from typing import Set


class ExternalCategory(object):

    def __init__(self, title: str, items: Set[str]) -> None:
        self._title = title
        self._items = items

    @property
    def title(self) -> str:
        return self._title

    @property
    def items(self) -> Set[str]:
        return self._items
