import os

from typing import Any, Dict
from uuid import uuid4

from testutils.stubs.api_stub import ApiStub


class TrainingStub(ApiStub):

    @property
    def root(self) -> str:
        return f"http://{os.environ['SERVER_NAME']}:8080/api/v1/lingany-da/training"

    def _generate(self, **kwargs) -> Dict[str, Any]:
        return {
            'id': None,
            'categoryId': kwargs.get('category_id'),
            'nativeWord': uuid4().hex if kwargs.get('nativeWord') is None else kwargs.get('nativeWord'),
            'foreignWord': uuid4().hex if kwargs.get('foreignWord') is None else kwargs.get('foreignWord')
        }

    def get_instance(self) -> Dict[str, Any]:
        _, obj = self.create()
        return obj
