from injector import singleton, inject
from typing import Optional
from uuid import UUID

from lingany_api.converters.category_converter import CategoryConverter
from lingany_api.models.category import Category
from lingany_api.persistance.dto.category_dto import CategoryDTO
from lingany_api.persistance.repositories.category_repository import CategoryRepository
from sqlutils import AbstractExpandSet, Service


@singleton
class CategoryService(Service):

    @inject
    def __init__(self, repo: CategoryRepository) -> None:
        super().__init__(repo)
        self._converter = CategoryConverter()

    def get_by_id(self, uid: UUID, expand: AbstractExpandSet) -> Category:
        category_dto = self._repo.get_by_id(uid)
        return self._convert(category_dto, expand)

    def _convert(self, entity: CategoryDTO, expand: AbstractExpandSet) -> Optional[Category]:
        if not entity:
            return None

        category = self._converter.convert(entity)
        return category

    def get_all(self, expand: AbstractExpandSet):
        raise NotImplementedError

    def update(self, entity) -> None:
        raise NotImplementedError

    def delete(self, uid) -> None:
        raise NotImplementedError

    @staticmethod
    def _clear_cache():
        pass
