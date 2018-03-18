import os

from typing import Any, Dict
from uuid import uuid4


class UserStub:

    @property
    def root(self) -> str:
        return f"http://{os.environ['SERVER_NAME']}/languages"

    def _generate(self, **kwargs) -> Dict[str, Any]:
        return {
            'id': None,
            'title': uuid4().hex if kwargs.get('title') is None else kwargs.get('title')
        }

    def get_instance(self) -> Dict[str, Any]:
        _, obj = self.create()
        return obj
