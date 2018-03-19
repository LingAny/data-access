import json

from asynqp import Message as AmqpMessage
from typing import Any, Dict


class AmqpConverter(object):

    @staticmethod
    def dump(data: Dict[str, Any]) -> AmqpMessage:
        return AmqpMessage(json.dumps(data), content_type='application/json')

    @staticmethod
    def load(message: AmqpMessage) -> Dict[str, Any]:
        data = json.loads(message.body)
        return data
