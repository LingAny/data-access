from injector import singleton, inject
from typing import Optional
from uuid import UUID

from lingany_api.converters.reflection_converter import ReflectionConverter
from lingany_api.models.reflection import Reflection
from lingany_api.persistance.dto.reflection_dto import ReflectionDTO
from lingany_api.persistance.repositories.reflection_repository import ReflectionRepository
from sqlutils import AbstractExpandSet, Service


@singleton
class ReflectionService(Service):

    @inject
    def __init__(self, repo: ReflectionRepository) -> None:
        super().__init__(repo)
        self._converter = ReflectionConverter()

    def get_by_id(self, uid: UUID, expand: AbstractExpandSet) -> Reflection:
        reflection_dto = self._repo.get_by_id(uid)
        return self._convert(reflection_dto, expand)

    def _convert(self, entity: ReflectionDTO, expand: AbstractExpandSet) -> Optional[Reflection]:
        if not entity:
            return None

        reflection = self._converter.convert(entity)
        return reflection

    def get_all(self, expand: AbstractExpandSet):
        raise NotImplementedError

    def update(self, entity) -> None:
        raise NotImplementedError

    def delete(self, uid) -> None:
        raise NotImplementedError

    @staticmethod
    def _clear_cache():
        pass
