from typing import Dict, Any
from uuid import UUID

from netutils.messages.attribute import Attribute


class AttributeConverter(object):

    @staticmethod
    def dump(attribute: Attribute) -> Dict[str, Any]:
        data = {
            'attributeTypeId': attribute.attribute_type_id.hex,
            'attributeValue': attribute.attribute_value
        }
        return data

    @staticmethod
    def load(data: Dict[str, Any]) -> "Attribute":
        attribute = Attribute(
            attribute_type_id=UUID(data['attributeTypeId']),
            attribute_value=data['attributeValue'])
        return attribute
