import os

from typing import Any, Dict
from uuid import uuid4

from src.tests.lingany_api_tests.reflection.reflection_stub import ReflectionStub
from testutils.stubs.api_stub import ApiStub


class CategoryStub(ApiStub):

    def __init__(self):
        super().__init__()
        self._reflection_stub = ReflectionStub()

    @property
    def root(self) -> str:
        return f"http://{os.environ['SERVER_NAME']}:8080/api/v1/lingany-da/categories"

    def _generate(self, **kwargs) -> Dict[str, Any]:
        data = {
            'id': None,
            'title': uuid4().hex if kwargs.get('title') is None else kwargs.get('title'),
            'reflectionId': kwargs.get('reflection_id')
        }

        if data.get('reflectionId') is None:
            reflection_stub = self._reflection_stub.get_instance()
            data['reflectionId'] = reflection_stub['id']

        return data

    def get_instance(self) -> Dict[str, Any]:
        _, obj = self.create()
        return obj
