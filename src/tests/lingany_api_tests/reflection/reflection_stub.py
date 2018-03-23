import os

from typing import Any, Dict, Tuple, List, Optional
from uuid import uuid4, UUID

from flask import Response

from apiutils import Request
from src.tests.lingany_api_tests.language.language_stub import LanguageStub
from testutils.stubs.api_stub import ApiStub


class ReflectionStub(ApiStub):

    def __init__(self):
        super().__init__()
        self._language_stub = LanguageStub()

    @property
    def root(self) -> str:
        return f"http://{os.environ['SERVER_NAME']}:8080/api/v1/lingany-da/reflections"

    def _generate(self, **kwargs) -> Dict[str, Any]:
        data = {
            'id': None,
            'title': uuid4().hex if kwargs.get('title') is None else kwargs.get('title'),
            'nativeLanguageId': kwargs.get('native_language_id'),
            'foreignLanguageId': kwargs.get('foreign_language_id')
        }

        if data.get('nativeLanguageId') is None:
            languge_stub = self._language_stub.get_instance()
            data['nativeLanguageId'] = languge_stub['id']

        if data.get('foreignLanguageId') is None:
            languge_stub = self._language_stub.get_instance()
            data['foreignLanguageId'] = languge_stub['id']

        return data

    def get_instance(self) -> Optional[Dict[str, Any]]:
        _, list_obj = self.get_all()
        return None if len(list_obj) == 0 else list_obj[0]

    def get_reflection_by_languages(self, native_lang_id: UUID,
                                    foreign_lang_id: UUID) -> Tuple[Response, Dict[str, Any]]:
        response = Request.get(f'{self.root}/get-by-languages/{native_lang_id}/{foreign_lang_id}')
        result = None
        if response.status_code == 200:
            result = response.json()
        return response, result

