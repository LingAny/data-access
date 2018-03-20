from typing import Optional, Dict, Any
from uuid import UUID

from flask import url_for

from apiutils import Serializer
from lingany_api.models.category import Category
from lingany_api.persistance.dto.category_dto import CategoryDTO
from lingany_api.serializers.reflection_serializer import ReflectionSerializer
from sqlutils import AbstractExpandSet


class CategorySerializer(Serializer):

    @staticmethod
    def dump(model: Category, expand: AbstractExpandSet=None) -> Optional[Dict[str, Any]]:
        if not model:
            return None

        data = {
            'href': url_for('reflection._get_by_id', uid=model.uid),
            'id': model.uid,
        }

        if model.is_loaded:
            data.update({
                'title': None if model.title is None else model.title,
                'reflection': ReflectionSerializer.dump(model.reflection)
            })

        return data

    @staticmethod
    def load(data: Dict[str, Any]) -> CategoryDTO:
        category_id = None if data['id'] is None or data['id'] == 'null' else UUID(data['id'])
        title = data['title']
        reflection_id = data['reflectionId']
        return CategoryDTO(category_id, reflection_id, title)
