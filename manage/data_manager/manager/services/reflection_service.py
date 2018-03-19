import logging
from typing import List, Optional, Any
from uuid import UUID

from manager.models.language import Language
from manager.models.reflection import Reflection
from manager.services.reader import CSVReader, FolderReader


class ReflectionService(object):
    @classmethod
    def get_supported_reflections(cls, path: str, supported_lang: List[Language]) -> List[Reflection]:
        files = FolderReader.get_files(path)
        reflections: List[Reflection] = []
        for filename in files:
            rows = CSVReader.read(filename)
            for i in range(1, len(rows)):
                row = rows[i]
                ref = cls._load_reflection(row=row, supported_lang=supported_lang)
                reflections.append(ref)
        return reflections

    @classmethod
    def get_reflections_for_native_lang(cls, native_lang_id: UUID,
                                        supported_reflections: List[Reflection]) -> List[Reflection]:
        reflections: List[Reflection] = []
        for ref in supported_reflections:
            if native_lang_id == ref.native_lang.uid:
                reflections.append(ref)
        return reflections

    @classmethod
    def get_reflection_for_foreign_lang(cls, foreign_id: UUID,
                                        native_reflections: List[Reflection]) -> Optional[Reflection]:
        for reflection in native_reflections:
            if foreign_id == reflection.foreign_lang.uid:
                return reflection
        return None

    @classmethod
    def _load_reflection(cls, row: List[Any], supported_lang: List[Language]) -> Reflection:
        uid = UUID(row[0])
        title = row[1]
        native_lang_id = UUID(row[2])
        foreign_lang_id = UUID(row[3])

        native_lang = cls._get_lang_by_id(native_lang_id, supported_lang)
        foreign_lang = cls._get_lang_by_id(foreign_lang_id, supported_lang)

        if native_lang is None or foreign_lang is None:
            raise RuntimeError

        return Reflection(uid=uid, title=title, native_lang=native_lang, foreign_lang=foreign_lang)

    @classmethod
    def _get_lang_by_id(cls, lang_id: UUID, supported_lang: List[Language]) -> Optional[Language]:
        for lang in supported_lang:
            if lang_id == lang.uid:
                return lang
        return None
