from lingany_api.models.language import Language
from lingany_api.models.reflection import Reflection
from lingany_api.persistance.dto.reflection_dto import ReflectionDTO
from sqlutils import Converter


class ReflectionConverter(Converter[Reflection, ReflectionDTO]):

    def convert(self, entity: ReflectionDTO) -> Reflection:
        return Reflection(uid=entity.uid).fill(title=entity.title,
                                               native_language=Language(entity.native_language_id),
                                               foreign_language=Language(entity.foreign_language_id)
                                               )
