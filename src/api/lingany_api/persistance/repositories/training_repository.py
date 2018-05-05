from uuid import UUID

from injector import inject
from typing import Any, List

from lingany_api.persistance.dto.training_dto import TrainingDTO
from sqlutils import Repository, DataContext, create_one, create_many


class TrainingRepository(Repository[TrainingDTO]):

    @inject
    def __init__(self, context: DataContext) -> None:
        self._context = context

    def get_by_id(self, uid: str) -> TrainingDTO:
        data = self._context.callproc('get_training_by_id', [uid])
        return create_one(TrainingDTO, data)

    def get_all_for_reflection(self, reflection_id: str) -> List[TrainingDTO]:
        data  = self._context.callproc('get_all_trainings_for_reflection', [reflection_id])
        return create_many(TrainingDTO, data)

    def get_all(self) -> List[TrainingDTO]:
        data = self._context.callproc('get_all_trainings', [])
        return create_many(TrainingDTO, data)

    def get_trainings_for_category(self, category_id: str) -> List[TrainingDTO]:
        data = self._context.callproc('get_trainings_for_category', [category_id])
        return create_many(TrainingDTO, data)

    def add(self, entity: TrainingDTO) -> None:
        raise NotImplementedError

    def update(self, entity) -> None:
        raise NotImplementedError

    def delete(self, uid: Any) -> None:
        raise NotImplementedError
