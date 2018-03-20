from typing import List
from uuid import UUID

from manager.models.language import Language
from manager.services.reader import CSVReader


class LanguageService(object):

    @staticmethod
    def get_supported_languages(filename: str) -> List[Language]:
        data = CSVReader.read(filename)
        languages = []
        if len(data) < 2:
            return languages
        for i in range(1, len(data)):
            row = data[i]
            lang = Language(uid=UUID(row[0]), title=row[1], code=row[2])
            languages.append(lang)

        return languages
