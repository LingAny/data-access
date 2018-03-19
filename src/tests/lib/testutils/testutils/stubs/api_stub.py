import os
from requests import Response
from typing import Tuple, Dict, Any, List

from apiutils.request import Request


class ApiStub(object):

    def __init__(self):
        self._stubs: List[Any] = []

    @property
    def root(self):
        raise NotImplementedError

    def _generate(self, **kwargs) -> [Dict[str, Any]]:
        raise NotImplementedError

    def _post(self, data: Dict[str, Any]) -> Tuple[Response, Any]:
        response = Request.post('{0}/'.format(self.root), data=data, is_json=True)
        print(response.headers)
        if response.status_code != 201:
            return response, None

        location: str = response.headers['Location']
        if not location.startswith('http'):
            location = f'http://{os.environ["SERVER_NAME"]}{location}'
        request = Request.get(location)
        print(request.text)
        layer_id = request.json()['id']
        return response, layer_id

    def create(self, **kwargs) -> Tuple[Response, Dict[str, Any]]:
        sut = self._generate(**kwargs)

        response, layer_id = self._post(sut)
        if layer_id is None:
            return response, None

        self._stubs.append(layer_id)
        sut['id'] = layer_id
        return response, sut

    def update(self, data: Dict[str, Any]) -> Tuple[Response, Dict[str, Any]]:
        response = Request.put('{0}/'.format(self.root), data=data, is_json=True)
        if response.status_code != 200:
            return response, None
        return response, response.json()

    def patch(self, instance_id: Any, data: Dict[str, Any]) -> Tuple[Response, Dict[str, Any]]:
        response = Request.patch(f'{self.root}/{instance_id}', data=data, is_json=True)
        if response.status_code != 200:
            return response, None
        return response, response.json()

    def get_by_id(self, instance_id: Any, expand: str = None) -> Tuple[Response, Dict[str, Any]]:
        response = Request.get('{0}/{1}{2}'.format(self.root, instance_id,
                                                   '' if expand is None else '?expand={0}'.format(expand)))
        if response.status_code != 200:
            return response, None
        return response, response.json()

    def delete(self, instance_id: Any) -> Response:
        return Request.delete('{0}/{1}'.format(self.root, instance_id))

    def get_all(self) -> Tuple[Response, List[Dict[str, Any]]]:
        response = Request.get('{0}/'.format(self.root))
        if response.status_code != 200:
            return response, None
        return response, response.json()

    def clear(self):
        self._stubs.reverse()
        for instance_id in self._stubs:
            self.delete(instance_id)
        self._stubs.clear()
