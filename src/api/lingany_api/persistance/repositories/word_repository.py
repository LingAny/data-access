from injector import inject
from typing import Any, List

from lingany_api.persistance.dto.word_dto import WordDTO
from lingany_api.services.language_service import LanguageService
from lingany_api.services.reflection_service import ReflectionService
from sqlutils import Repository, DataContext
from lib.translator.translater import Translator


class WordRepository(Repository[WordDTO]):

    @inject
    def __init__(self, context: DataContext) -> None:
        self._context = context
        self._reflection_service = ReflectionService()
        self._language_service = LanguageService()
        self._translator = Translator()

    def get_translation_by_text(self, text: str, ref_id: str, expand) -> WordDTO:
        data = self._context.callproc('get_training_by_text_and_reflection', [str(text), str(ref_id)])
        if data is None:
            # need to get data from the web
            reflection = self._reflection_service.get_by_id(ref_id, expand)
            native_language = self._language_service.get_by_id(reflection.native_language.uid, expand)
            foreign_language = self._language_service.get_by_id(reflection.foreign_language.uid, expand)
            translation = ""
            if self.check_if_word_of_phrase(text):
                translation = self._translator.translate_word(text, native_language, foreign_language)
            else:
                translation = self._translator.translate_text(text, native_language, foreign_language)

            return WordDTO(text=text, translation=translation)

        else:
            return self.create_word_dto_from_training(data)

    def get_text_by_translation(self, translation: str, ref_id: str, expand) -> WordDTO:
        data = self._context.callproc('get_training_by_translation_and_reflection', [str(translation), str(ref_id)])
        if data is None:
            pass
        else:
            return self.create_word_dto_from_training(data)

    def check_if_word_of_phrase(self, text: str) -> bool:
        text_arr = text.split()
        if len(text_arr) <= 1:
            return True
        else:
            return False

    def create_word_dto_from_training(self, data) -> WordDTO:
        training_data = data[0]
        text = training_data.get("native_word")
        translation = training_data.get("foreign_word")
        return WordDTO(text=text, translation=translation)

    def get_by_id(self, uid: Any) -> WordDTO:
        raise NotImplementedError

    def get_all(self) -> List[WordDTO]:
        raise NotImplementedError

    def add(self, entity: WordDTO) -> None:
        raise NotImplementedError

    def update(self, entity) -> None:
        raise NotImplementedError

    def delete(self, uid: Any) -> None:
        raise NotImplementedError
