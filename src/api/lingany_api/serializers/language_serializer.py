from typing import Optional, Dict, Any
from uuid import UUID

from flask import url_for

from lingany_api.models.language import Language
from lingany_api.persistance.dto.language_dto import LanguageDTO


class LanguageSerializer:

    @staticmethod
    def dump(model: Language) -> Optional[Dict[str, Any]]:
        if not model:
            return None

        data = {
            'href': url_for('languages._get_by_id', uid=model.uid),
            'id': model.uid,
            'title': model.title
        }

        return data

    @staticmethod
    def load(data: Dict[str, Any]) -> LanguageDTO:
        language_id = None if data['id'] is None or data['id'] == 'null' else UUID(data['id'])
        title = data['title']
        return LanguageDTO(language_id, title)
