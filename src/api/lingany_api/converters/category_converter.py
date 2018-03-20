from lingany_api.models.category import Category
from lingany_api.models.reflection import Reflection
from lingany_api.persistance.dto.category_dto import CategoryDTO
from sqlutils import Converter


class CategoryConverter(Converter[Category, CategoryDTO]):

    def convert(self, entity: CategoryDTO) -> Category:
        return Category(uid=entity.uid).fill(title=entity.title,
                                             reflection=Reflection(entity.reflection_id)
                                             )
