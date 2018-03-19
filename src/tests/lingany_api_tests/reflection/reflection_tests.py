import unittest

from typing import Dict, Any

from src.tests.lingany_api_tests.language.language_stub import LanguageStub
from src.tests.lingany_api_tests.reflection.reflection_stub import ReflectionStub


class ReflectionTestCase(unittest.TestCase):

    _stub: ReflectionStub = None
    _language_stub: ReflectionStub = None

    @classmethod
    def setUpClass(cls):
        cls._stub = ReflectionStub()
        cls._language_stub = LanguageStub()

        cls._native_language_id = cls._language_stub.get_instance()['id']
        cls._foreign_language_id = cls._language_stub.get_instance()['id']

    def test_create(self):
        response, sut = self._stub.create(native_language_id=self._native_language_id,
                                          foreign_language_id=self._foreign_language_id)
        self.assertEqual(201, response.status_code)

    # def test_get_by_id(self):
    #     response, sut = self._stub.create()
    #     self.assertEqual(201, response.status_code)
    #     response, obj = self._stub.get_by_id(sut['id'])
    #     self.assertEqual(200, response.status_code)
    #     self._check(obj, sut)

    def tearDown(self):
        self._stub.clear()

    def _check(self, obj: Dict[str, Any], sut: Dict[str, Any]):
        self.assertEqual(sut['id'], obj['id'])
        self.assertIn('href', obj)
