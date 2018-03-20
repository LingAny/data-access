from injector import singleton, inject
from typing import Optional
from uuid import UUID

from lingany_api.converters.language_converter import LanguageConverter
from lingany_api.persistance.dto.language_dto import LanguageDTO
from sqlutils import AbstractExpandSet, Service

from lingany_api.models.language import Language
from lingany_api.persistance.repositories.language_repository import LanguageRepository


@singleton
class LanguageService(Service):

    @inject
    def __init__(self, repo: LanguageRepository) -> None:
        super().__init__(repo)
        self._converter = LanguageConverter()

    def get_by_id(self, uid: UUID, expand: AbstractExpandSet) -> Language:
        language_dto = self._repo.get_by_id(uid)
        return self._convert(language_dto, expand)

    def _convert(self, entity: LanguageDTO, expand: AbstractExpandSet) -> Optional[Language]:
        if not entity:
            return None

        language = self._converter.convert(entity)
        return language

    def get_all(self, expand: AbstractExpandSet):
        raise NotImplementedError

    def update(self, entity) -> None:
        raise NotImplementedError

    def delete(self, uid) -> None:
        raise NotImplementedError

    @staticmethod
    def _clear_cache():
        pass
