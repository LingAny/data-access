from typing import Any
from typing import Dict

from testutils.stubs.api_stub import ApiStub


class ApiStubWithParent(ApiStub):

    @property
    def root(self):
        raise NotImplementedError

    def _generate(self, **kwargs) -> [Dict[str, Any]]:
        raise NotImplementedError

    def create_with_parent(self, **kwargs) -> Dict[str, Any]:
        response, parent = self.create(**kwargs)
        response, sut = self.create(parent_id=parent['id'], **kwargs)
        return sut
