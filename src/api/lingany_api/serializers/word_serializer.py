from typing import Optional, Dict, Any
from uuid import UUID

from flask import url_for

from apiutils import Serializer
from lingany_api.models.word import Word
from lingany_api.persistance.dto.word_dto import WordDTO
from sqlutils import AbstractExpandSet


class WordSerializer(Serializer):

    @staticmethod
    def dump(model: Word, expand: AbstractExpandSet=None) -> Optional[Dict[str, Any]]:
        if not model:
            return None

        data = {
            'href': url_for('words._get_by_id', uid=model.uid),
            'id': model.uid,
        }

        if model.is_loaded:
            data.update({
                'text': None if model.text is None else model.text,
                'translation': None if model.translation is None else model.translation
            })

        return data

    @staticmethod
    def load(data: Dict[str, Any]) -> WordDTO:
        word_id = None if data['id'] is None or data['id'] == 'null' else UUID(data['id'])
        text = data['text']
        translation = data['translation']
        return WordDTO(word_id, text, translation)
