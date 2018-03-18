from lingany_api.models.language import Language
from lingany_api.persistance.dto.language_dto import LanguageDTO


class LanguageConverter:

    def convert(self, entity: LanguageDTO) -> Language:
        return Language(entity.uid).fill(title=entity.title)
