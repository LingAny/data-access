from injector import singleton, inject
from typing import Optional, List
from uuid import UUID

from sqlutils import AbstractExpandSet, Service
from lingany_api import cache
from lingany_api.models.language import Language
from lingany_api.persistance.dto.language_dto import LanguageDTO
from lingany_api.persistance.repositories.language_repository import LanguageRepository


@singleton
class LanguageService(Service[Language, LanguageDTO, LanguageRepository]):

    @inject
    def __init__(self, repo: LanguageRepository) -> None:
        super().__init__(repo)
        # self._converter = LanguageConverter()

    # def _convert(self, entity: UserDTO, expand: AbstractExpandSet) -> Optional[User]:
    #     if not entity:
    #         return None
    #
    #     user = self._converter.convert(entity)
    #     return user

    def get_by_id(self, uid: UUID) -> Optional[Language]:
        return super().get_by_id(uid)
