import os

from typing import Any, Dict, Tuple, List

from flask import Response

from apiutils import Request
from testutils.stubs.api_stub import ApiStub


class WordStub(ApiStub):

    @property
    def root(self) -> str:
        return f"http://{os.environ['SERVER_NAME']}:8080/api/v1/lingany-da/word"

    def get_translation_by_text(self, text: str) -> Tuple[Response, Dict[str, Any]]:
        response = Request.get(f'{self.root}/text/{text}')
        result = None
        if response.status_code == 200:
            result = response.json()
        return response, result

    def get_text_by_translation(self, translation: str) -> Tuple[Response, Dict[str, Any]]:
        response = Request.get(f'{self.root}/translation/{translation}')
        result = None
        if response.status_code == 200:
            result = response.json()
        return response, result
