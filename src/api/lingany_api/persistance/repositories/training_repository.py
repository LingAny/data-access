from injector import inject
from typing import Any

from lingany_api.persistance.dto.training_dto import TrainingDTO
from sqlutils import Repository, DataContext, create_one


class TrainingRepository(Repository[TrainingDTO]):

    @inject
    def __init__(self, context: DataContext) -> None:
        self._context = context

    def get_by_id(self, uid: str) -> TrainingDTO:
        data = self._context.callproc('get_training_by_id', [uid])
        return create_one(TrainingDTO, data)

    def add(self, entity: TrainingDTO) -> None:
        self._context.callproc('add_training', [entity.uid, entity.category_id,
                                                entity.native_word, entity.foreign_word])

    def get_all(self) -> None:
        raise NotImplementedError

    def update(self, entity) -> None:
        raise NotImplementedError

    def delete(self, uid: Any) -> None:
        raise NotImplementedError
