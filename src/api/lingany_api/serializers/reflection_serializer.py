from typing import Optional, Dict, Any
from uuid import UUID

from flask import url_for

from apiutils import Serializer
from lingany_api.models.reflection import Reflection
from lingany_api.persistance.dto.reflection_dto import ReflectionDTO
from lingany_api.serializers.language_serializer import LanguageSerializer
from sqlutils import AbstractExpandSet


class ReflectionSerializer(Serializer):

    @staticmethod
    def dump(model: Reflection, expand: AbstractExpandSet=None) -> Optional[Dict[str, Any]]:
        if not model:
            return None

        data = {
            'href': url_for('reflection._get_by_id', uid=model.uid),
            'id': model.uid,
        }

        if model.is_loaded:
            data.update({
                'title': None if model.title is None else model.title,
                'nativeLanguage': LanguageSerializer.dump(model.native_language),
                'foreignLanguage': LanguageSerializer.dump(model.foreign_language)
            })

        return data

    @staticmethod
    def load(data: Dict[str, Any]) -> ReflectionDTO:
        reflection_id = None if data['id'] is None or data['id'] == 'null' else UUID(data['id'])
        title = data['title']
        native_language_id = data['nativeLanguageId']
        foreign_language_id = data['foreignLanguageId']
        return ReflectionDTO(reflection_id, title, native_language_id, foreign_language_id)
