from datetime import datetime
from typing import List, Optional
from uuid import UUID

from netutils.messages.attribute import Attribute
from netutils.messages.message_category import MessageCategory


class Message(object):

    def __init__(self, uid: UUID, actor_id: UUID, actor_type_id: UUID,
                 occurred: datetime, category: MessageCategory,
                 message_type_id: UUID, source_message_id: Optional[UUID],
                 attributes: List[Attribute]) -> None:
        self._uid = uid
        self._actor_id = actor_id
        self._actor_type_id = actor_type_id
        self._occurred = occurred
        self._category = category
        self._message_type_id = message_type_id
        self._source_message_id = source_message_id
        self._attributes = attributes

    @property
    def uid(self) -> UUID:
        return self._uid

    @property
    def actor_id(self) -> UUID:
        return self._actor_id

    @property
    def actor_type_id(self) -> UUID:
        return self._actor_type_id

    @property
    def occurred(self) -> datetime:
        return self._occurred

    @property
    def category(self) -> MessageCategory:
        return self._category

    @property
    def message_type_id(self) -> UUID:
        return self._message_type_id

    @property
    def attributes(self) -> List[Attribute]:
        return self._attributes
