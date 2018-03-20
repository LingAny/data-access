import unittest

from typing import Dict, Any

from src.tests.lingany_api_tests.language.language_stub import LanguageStub


class LanguageTestCase(unittest.TestCase):

    _stub: LanguageStub = None

    @classmethod
    def setUpClass(cls):
        cls._stub = LanguageStub()

    def test_create(self):
        response, sut = self._stub.create()
        self.assertEqual(201, response.status_code)

    def test_get_by_id(self):
        response, sut = self._stub.create()
        self.assertEqual(201, response.status_code)
        response, obj = self._stub.get_by_id(sut['id'])
        self.assertEqual(200, response.status_code)
        self._check(obj, sut)

    def test_get_all(self):
        response, sut = self._stub.create()
        self.assertEqual(201, response.status_code)
        response, list_obj = self._stub.get_all()
        self.assertEqual(200, response.status_code)
        self.assertGreater(len(list_obj), 0)

    def tearDown(self):
        self._stub.clear()

    def _check(self, obj: Dict[str, Any], sut: Dict[str, Any]):
        self.assertEqual(sut['id'], obj['id'])
        self.assertIn('href', obj)
