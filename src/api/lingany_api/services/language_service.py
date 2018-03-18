from injector import singleton, inject
from typing import Optional, List
from uuid import UUID

from lingany_api.converters.language_converter import LanguageConverter
from lingany_api.models.language import Language
from lingany_api.persistance.dto.language_dto import LanguageDTO
from lingany_api.persistance.repositories.language_repository import LanguageRepository


@singleton
class LanguageService:

    @inject
    def __init__(self, repo: LanguageRepository) -> None:
        self._repo = repo
        self._converter = LanguageConverter()

    def add(self, language_dto: LanguageDTO) -> None:
        self._repo.add(language_dto)

    def get_by_id(self, uid: str) -> Optional[Language]:
        language_dto = self._repo.get_by_id(uid)
        language = self._converter.convert(language_dto)
        return language
