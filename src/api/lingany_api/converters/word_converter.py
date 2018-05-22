from lingany_api.models.word import Word
from lingany_api.persistance.dto.word_dto import WordDTO
from sqlutils import Converter


class WordConverter(Converter[Word, WordDTO]):

    def convert(self, entity: WordDTO) -> Word:
        return Word(uid=entity.uid).fill(text=entity.text,
                                         translation=entity.translation)
