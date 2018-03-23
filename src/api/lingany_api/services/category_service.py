from injector import singleton, inject
from typing import Optional, List
from uuid import UUID

from lingany_api.converters.category_converter import CategoryConverter
from lingany_api.models.category import Category
from lingany_api.persistance.dto.category_dto import CategoryDTO
from lingany_api.persistance.repositories.category_repository import CategoryRepository
from sqlutils import AbstractExpandSet, Service


@singleton
class CategoryService(Service[Category, CategoryDTO, CategoryRepository]):

    @inject
    def __init__(self, repo: CategoryRepository) -> None:
        super().__init__(repo)
        self._converter = CategoryConverter()

    def get_categories_for_reflection(self, reflection_id: str, expand: AbstractExpandSet) -> List[Category]:
        category_dto_list = self._repo.get_categories_for_reflection(reflection_id)
        return self._convert_many(category_dto_list, expand)

    def _convert(self, entity: CategoryDTO, expand: AbstractExpandSet) -> Optional[Category]:
        if not entity:
            return None

        category = self._converter.convert(entity)
        return category

    @staticmethod
    def _clear_cache():
        pass
