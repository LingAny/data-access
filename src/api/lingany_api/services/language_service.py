from injector import singleton, inject
from typing import Optional

from lingany_api.converters.language_converter import LanguageConverter
from lingany_api.persistance.dto.language_dto import LanguageDTO
from sqlutils import AbstractExpandSet, Service

from lingany_api.models.language import Language
from lingany_api.persistance.repositories.language_repository import LanguageRepository


@singleton
class LanguageService(Service[Language, LanguageDTO, LanguageRepository]):

    @inject
    def __init__(self, repo: LanguageRepository) -> None:
        super().__init__(repo)
        self._converter = LanguageConverter()

    def _convert(self, entity: LanguageDTO, expand: AbstractExpandSet) -> Optional[Language]:
        if not entity:
            return None

        language = self._converter.convert(entity)
        return language

    @staticmethod
    def _clear_cache():
        pass
