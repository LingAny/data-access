from typing import Optional, Dict, Any
from uuid import UUID

from flask import url_for

from apiutils import Serializer
from lingany_api.persistance.dto.language_dto import LanguageDTO
from sqlutils import AbstractExpandSet

from lingany_api.models.language import Language


class LanguageSerializer(Serializer):

    @staticmethod
    def dump(model: Language, expand: AbstractExpandSet=None) -> Optional[Dict[str, Any]]:
        if not model:
            return None

        data = {
            'href': url_for('languages._get_by_id', uid=model.uid),
            'id': model.uid,
        }

        if model.is_loaded:
            data.update({
                'title': None if model.title is None else model.title
            })

        return data

    @staticmethod
    def load(data: Dict[str, Any]) -> LanguageDTO:
        language_id = None if data['id'] is None or data['id'] == 'null' else UUID(data['id'])
        title = data['title']
        return LanguageDTO(language_id, title)
