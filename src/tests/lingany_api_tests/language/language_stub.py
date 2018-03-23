import os

from typing import Any, Dict, Optional, Tuple
from uuid import uuid4

from testutils.stubs.api_stub import ApiStub


class LanguageStub(ApiStub):

    @property
    def root(self) -> str:
        return f"http://{os.environ['SERVER_NAME']}:8080/api/v1/lingany-da/languages"

    def _generate(self, **kwargs) -> Dict[str, Any]:
        return {
            'id': None,
            'title': uuid4().hex if kwargs.get('title') is None else kwargs.get('title')
        }

    def get_instance(self) -> Optional[Dict[str, Any]]:
        _, list_obj = self.get_all()
        return None if len(list_obj) == 0 else list_obj[0]

    def get_pair(self) -> Optional[Tuple[Dict[str, Any], Dict[str, Any]]]:
        _, list_obj = self.get_all()
        return None if len(list_obj) == 0 else list_obj[0], list_obj[1]
