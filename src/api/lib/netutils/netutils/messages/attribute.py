from uuid import UUID


class Attribute(object):

    def __init__(self, attribute_type_id: UUID, attribute_value: str) -> None:
        self._attribute_type_id = attribute_type_id
        self._attribute_value = attribute_value

    @property
    def attribute_type_id(self) -> UUID:
        return self._attribute_type_id

    @property
    def attribute_value(self) -> str:
        return self._attribute_value
