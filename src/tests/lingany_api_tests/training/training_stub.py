import os

from typing import Any, Dict
from uuid import uuid4

from src.tests.lingany_api_tests.category.category_stub import CategoryStub
from testutils.stubs.api_stub import ApiStub


class TrainingStub(ApiStub):

    def __init__(self):
        super().__init__()
        self._category_stub = CategoryStub()

    @property
    def root(self) -> str:
        return f"http://{os.environ['SERVER_NAME']}:8080/api/v1/lingany-da/training"

    def _generate(self, **kwargs) -> Dict[str, Any]:
        data = {
            'id': None,
            'categoryId': kwargs.get('category_id'),
            'nativeWord': uuid4().hex if kwargs.get('nativeWord') is None else kwargs.get('nativeWord'),
            'foreignWord': uuid4().hex if kwargs.get('foreignWord') is None else kwargs.get('foreignWord')
        }

        if data.get('categoryId') is None:
            category_stub = self._category_stub.get_instance()
            data['categoryId'] = category_stub['id']

        return data

    def get_instance(self) -> Dict[str, Any]:
        _, obj = self.create()
        return obj
