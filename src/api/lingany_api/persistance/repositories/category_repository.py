from injector import inject
from typing import Any

from lingany_api.persistance.dto.category_dto import CategoryDTO
from sqlutils import Repository, DataContext, create_one


class CategoryRepository(Repository[CategoryDTO]):

    @inject
    def __init__(self, context: DataContext) -> None:
        self._context = context

    def get_by_id(self, uid: str) -> CategoryDTO:
        data = self._context.callproc('get_category_by_id', [uid])
        return create_one(CategoryDTO, data)

    def add(self, entity: CategoryDTO) -> None:
        self._context.callproc('add_category', [entity.uid, entity.reflection_id, entity.title])

    def get_all(self) -> None:
        raise NotImplementedError

    def update(self, entity) -> None:
        raise NotImplementedError

    def delete(self, uid: Any) -> None:
        raise NotImplementedError
