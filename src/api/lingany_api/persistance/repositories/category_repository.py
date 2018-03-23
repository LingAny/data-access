from injector import inject
from typing import Any, List

from lingany_api.persistance.dto.category_dto import CategoryDTO
from sqlutils import Repository, DataContext, create_one, create_many


class CategoryRepository(Repository[CategoryDTO]):

    @inject
    def __init__(self, context: DataContext) -> None:
        self._context = context

    def get_by_id(self, uid: str) -> CategoryDTO:
        data = self._context.callproc('get_category_by_id', [uid])
        return create_one(CategoryDTO, data)

    def get_all(self) -> List[CategoryDTO]:
        data = self._context.callproc('get_all_categories', [])
        return create_many(CategoryDTO, data)

    def get_categories_for_reflection(self, reflection_id: str) -> List[CategoryDTO]:
        data = self._context.callproc('get_categories_for_reflection', [reflection_id])
        return create_many(CategoryDTO, data)

    def add(self, entity: CategoryDTO) -> None:
        raise NotImplementedError

    def update(self, entity) -> None:
        raise NotImplementedError

    def delete(self, uid: Any) -> None:
        raise NotImplementedError
