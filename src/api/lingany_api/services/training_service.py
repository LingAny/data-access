import random

from injector import singleton, inject
from typing import Optional, List
from uuid import UUID

from lingany_api.converters.training_converter import TrainingConverter
from lingany_api.models.training import Training
from lingany_api.persistance.dto.training_dto import TrainingDTO
from lingany_api.persistance.repositories.training_repository import TrainingRepository
from sqlutils import AbstractExpandSet, Service


@singleton
class TrainingService(Service[Training, TrainingDTO, TrainingRepository]):

    @inject
    def __init__(self, repo: TrainingRepository) -> None:
        super().__init__(repo)
        self._converter = TrainingConverter()

    def get_trainings_for_category(self, category_id: str, expand: AbstractExpandSet) -> List[Training]:
        training_dto_list = self._repo.get_trainings_for_category(category_id)
        return self._convert_many(training_dto_list, expand)

    def get_shape_reflection(self, reflection_id: str) -> List[Training]:
        trainings = self._repo.get_all_for_reflection(reflection_id)
        random.shuffle(trainings)
        trainings = trainings[:20]
        return self._convert_many(trainings)

    def _convert(self, entity: TrainingDTO, expand: AbstractExpandSet) -> Optional[Training]:
        if not entity:
            return None

        training = self._converter.convert(entity)
        return training

    @staticmethod
    def _clear_cache():
        pass
