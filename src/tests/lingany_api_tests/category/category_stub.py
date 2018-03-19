import os

from typing import Any, Dict
from uuid import uuid4

from testutils.stubs.api_stub import ApiStub


class CategoryStub(ApiStub):

    @property
    def root(self) -> str:
        return f"http://{os.environ['SERVER_NAME']}:8080/api/v1/lingany-da/categories"

    def _generate(self, **kwargs) -> Dict[str, Any]:
        return {
            'id': None,
            'title': uuid4().hex if kwargs.get('title') is None else kwargs.get('title'),
            'reflectionId': kwargs.get('reflection_id')
        }

    def get_instance(self) -> Dict[str, Any]:
        _, obj = self.create()
        return obj
