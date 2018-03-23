from typing import Optional, Dict, Any
from uuid import UUID

from flask import url_for

from apiutils import Serializer
from lingany_api.models.training import Training
from lingany_api.persistance.dto.training_dto import TrainingDTO
from lingany_api.serializers.category_serializer import CategorySerializer
from sqlutils import AbstractExpandSet


class TrainingSerializer(Serializer):

    @staticmethod
    def dump(model: Training, expand: AbstractExpandSet=None) -> Optional[Dict[str, Any]]:
        if not model:
            return None

        data = {
            'href': url_for('reflection._get_by_id', uid=model.uid),
            'id': model.uid,
        }

        if model.is_loaded:
            data.update({
                'category': CategorySerializer.dump(model.category),
                'nativeWord': None if model.native_word is None else model.native_word,
                'foreignWord': None if model.foreign_word is None else model.foreign_word
            })

        return data

    @staticmethod
    def load(data: Dict[str, Any]) -> TrainingDTO:
        training_id = None if data['id'] is None or data['id'] == 'null' else UUID(data['id'])
        category_id = data['categoryId']
        native_word = data['nativeWord']
        foreign_word = data['foreignWord']
        return TrainingDTO(training_id, category_id, native_word, foreign_word)
