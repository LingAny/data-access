import os

from typing import Any, Dict
from uuid import uuid4

from testutils.stubs.api_stub import ApiStub


class ReflectionStub(ApiStub):

    @property
    def root(self) -> str:
        return f"http://{os.environ['SERVER_NAME']}:8080/api/v1/lingany-da/reflections"

    def _generate(self, **kwargs) -> Dict[str, Any]:
        return {
            'id': None,
            'title': uuid4().hex if kwargs.get('title') is None else kwargs.get('title'),
            'nativeLanguageId': kwargs.get('native_language_id'),
            'foreignLanguageId': kwargs.get('foreign_language_id')
        }

    def get_instance(self) -> Dict[str, Any]:
        _, obj = self.create()
        return obj
