from uuid import UUID

from injector import inject
from typing import Any, List

from lingany_api.persistance.dto.word_dto import WordDTO
from sqlutils import Repository, DataContext


class WordRepository(Repository[WordDTO]):

    @inject
    def __init__(self, context: DataContext) -> None:
        self._context = context

    def get_translation_by_text(self, text: str, ref_id: str) -> WordDTO:
        data = self._context.callproc('get_training_by_text_and_reflection', [str(text), str(ref_id)])
        if data is None:
            # need to get data from the web
            pass

        return self.create_word_dto_from_training(data)

    def get_text_by_translation(self, translation: str, ref_id: str) -> WordDTO:
        data = self._context.callproc('get_training_by_translation_and_reflection', [str(translation), str(ref_id)])
        if data is None:
            pass

        return self.create_word_dto_from_training(data)

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
