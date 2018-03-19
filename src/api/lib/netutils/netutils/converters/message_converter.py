import dateutil.parser

from typing import Dict, Any
from uuid import UUID

from netutils.converters.attribute_converter import AttributeConverter
from netutils.messages.message import Message
from netutils.messages.message_category import MessageCategory


class MessageConverter(object):

    @staticmethod
    def dump(message: Message) -> Dict[str, Any]:
        data = {
            'id': message.uid.hex,
            'actorId': message.actor_id.hex,
            'actorTypeId': message.actor_type_id.hex,
            'occurred': message.occurred.astimezone().isoformat(),
            'category': message.category.value,
            'messageTypeId': message.message_type_id.hex,
            'attributes': [AttributeConverter.dump(attribute) for attribute in message.attributes]
        }
        return data

    @staticmethod
    def load(data: Dict[str, Any]) -> "Message":
        if data['sourceMessageId'] is None:
            source_message_id = None
        else:
            source_message_id = UUID(data['sourceMessageId'])

        msg = Message(
            uid=UUID(data['id']),
            actor_id=UUID(data['actorId']),
            actor_type_id=UUID(data['actorTypeId']),
            occurred=dateutil.parser.parse(data['occurred']),
            category=MessageCategory(data['category']),
            message_type_id=UUID(data['messageTypeId']),
            source_message_id=source_message_id,
            attributes=[AttributeConverter.load(attribute) for attribute in data['attributes']]
        )
        return msg
