from injector import singleton, inject
from typing import Optional

from lingany_api.converters.word_converter import WordConverter
from lingany_api.models.word import Word
from lingany_api.persistance.dto.word_dto import WordDTO
from lingany_api.persistance.repositories.word_repository import WordRepository
from lingany_api.services.language_service import LanguageService
from lingany_api.services.reflection_service import ReflectionService
from lingany_api.translator.translater import Translator
from sqlutils import AbstractExpandSet, Service


@singleton
class WordService(Service[Word, WordDTO, WordRepository]):

    @inject
    def __init__(self, repo: WordRepository, reflection_service: ReflectionService, language_service: LanguageService) -> None:
        super().__init__(repo)
        self._converter = WordConverter()
        self._reflection_service = reflection_service
        self._language_service = language_service
        self._translator = Translator()

    def get_translation_by_text(self, text: str, ref_id: str, expand: AbstractExpandSet) -> Word:
        word_dto = self._repo.get_translation_by_text(text, ref_id)
        if word_dto is None:
            # need to get data from the web
            reflection = self._reflection_service.get_by_id(ref_id, expand)
            native_language = self._language_service.get_by_id(reflection.native_language.uid, expand)
            foreign_language = self._language_service.get_by_id(reflection.foreign_language.uid, expand)

            translation = self.translate_text(text, native_language.code, foreign_language.code)
            word_dto = WordDTO(text=text, translation=translation)

        return self._convert(word_dto, expand)

    def get_text_by_translation(self, translation: str, ref_id: str, expand: AbstractExpandSet) -> Word:
        word_dto = self._repo.get_text_by_translation(translation, ref_id)
        if word_dto is None:
            # need to get data from the web
            reflection = self._reflection_service.get_by_id(ref_id, expand)
            native_language = self._language_service.get_by_id(reflection.native_language.uid, expand)
            foreign_language = self._language_service.get_by_id(reflection.foreign_language.uid, expand)

            text = self.translate_text(translation, foreign_language.code, native_language.code)
            word_dto = WordDTO(text=text, translation=translation)

        return self._convert(word_dto, expand)

    def translate_text(self, text: str, native_lang_code: str, foreign_lang_code: str) -> str:
        translation = ""
        if self.check_if_word_of_phrase(text):
            # translation = self._translator.translate_word(text, native_lang_code, foreign_lang_code)
            translation = self._translator.translate_word(text, foreign_lang_code, native_lang_code)
        else:
            # translation = self._translator.translate_text(text, native_lang_code, foreign_lang_code)
            translation = self._translator.translate_text(text, foreign_lang_code, native_lang_code)
        return translation

    def check_if_word_of_phrase(self, text: str) -> bool:
        text_arr = text.split()
        if len(text_arr) <= 1:
            return True
        else:
            return False

    def _convert(self, entity: WordDTO, expand: AbstractExpandSet) -> Optional[Word]:
        if not entity:
            return None

        word = self._converter.convert(entity)
        return word

    @staticmethod
    def _clear_cache():
        pass
