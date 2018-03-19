from injector import inject
from typing import Any

from lingany_api.persistance.dto.reflection_dto import ReflectionDTO
from sqlutils import Repository, DataContext, create_one


class ReflectionRepository(Repository[ReflectionDTO]):

    @inject
    def __init__(self, context: DataContext) -> None:
        self._context = context

    def get_by_id(self, uid: str) -> ReflectionDTO:
        data = self._context.callproc('get_reflection_by_id', [uid])
        return create_one(ReflectionDTO, data)

    def add(self, entity: ReflectionDTO) -> None:
        self._context.callproc('add_reflection', [entity.uid, entity.title, entity.native_language_id,
                                                  entity.foreign_language_id])

    def get_all(self) -> None:
        raise NotImplementedError

    def update(self, entity) -> None:
        raise NotImplementedError

    def delete(self, uid: Any) -> None:
        raise NotImplementedError
