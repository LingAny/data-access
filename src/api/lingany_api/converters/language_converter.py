from lingany_api.persistance.dto.language_dto import LanguageDTO
from sqlutils import Converter
from lingany_api.models.language import Language


class LanguageConverter(Converter[Language, LanguageDTO]):

    def convert(self, entity: LanguageDTO) -> Language:
        return Language(uid=entity.uid).fill(title=entity.title, code=entity.code)
