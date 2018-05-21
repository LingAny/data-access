from injector import singleton, inject
from typing import Optional

from lingany_api.converters.word_converter import WordConverter
from lingany_api.models.word import Word
from lingany_api.persistance.dto.word_dto import WordDTO
from lingany_api.persistance.repositories.word_repository import WordRepository
from sqlutils import AbstractExpandSet, Service


@singleton
class WordService(Service[Word, WordDTO, WordRepository]):

    @inject
    def __init__(self, repo: WordRepository) -> None:
        super().__init__(repo)
        self._converter = WordConverter()

    def _convert(self, entity: WordDTO, expand: AbstractExpandSet) -> Optional[Word]:
        if not entity:
            return None

        word = self._converter.convert(entity)
        return word

    @staticmethod
    def _clear_cache():
        pass
