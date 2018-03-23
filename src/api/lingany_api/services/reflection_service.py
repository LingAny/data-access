from injector import singleton, inject
from typing import Optional, List
from uuid import UUID

from lingany_api.converters.reflection_converter import ReflectionConverter
from lingany_api.models.reflection import Reflection
from lingany_api.persistance.dto.reflection_dto import ReflectionDTO
from lingany_api.persistance.repositories.reflection_repository import ReflectionRepository
from sqlutils import AbstractExpandSet, Service


@singleton
class ReflectionService(Service[Reflection, ReflectionDTO, ReflectionRepository]):

    @inject
    def __init__(self, repo: ReflectionRepository) -> None:
        super().__init__(repo)
        self._converter = ReflectionConverter()

    def get_reflection_by_languages(self, native_language_id: str,
                                    foreign_language_id: str,
                                    expand: AbstractExpandSet) -> Reflection:
        reflection_dto = self._repo.get_reflection_by_languages(native_language_id, foreign_language_id)
        return self._convert(reflection_dto, expand)

    def _convert(self, entity: ReflectionDTO, expand: AbstractExpandSet) -> Optional[Reflection]:
        if not entity:
            return None

        reflection = self._converter.convert(entity)
        return reflection

    @staticmethod
    def _clear_cache():
        pass
