import unittest

from typing import Dict, Any

from src.tests.lingany_api_tests.language.language_stub import LanguageStub


class LanguageTestCase(unittest.TestCase):

    _stub: LanguageStub = None

    @classmethod
    def setUpClass(cls):
        cls._stub = LanguageStub()

    def test_fail_create(self):
        response, sut = self._stub.create()
        self.assertIn(response.status_code, [404, 405])

    def test_fail_delete(self):
        sut = self._stub.get_instance()
        response = self._stub.delete(instance_id=sut['id'])
        self.assertIn(response.status_code, [404, 405])

    def test_get_by_id(self):
        sut = self._stub.get_instance()
        response, obj = self._stub.get_by_id(sut['id'])
        self.assertEqual(200, response.status_code)
        self._check(obj, sut)

    def test_get_all(self):
        response, list_obj = self._stub.get_all()
        self.assertEqual(200, response.status_code)
        self.assertGreater(len(list_obj), 0)

    def _check(self, obj: Dict[str, Any], sut: Dict[str, Any]):
        self.assertEqual(obj['id'], sut['id'])
        self.assertEqual(obj['href'], sut['href'])
        self.assertEqual(obj['title'], sut['title'])
        self.assertEqual(obj['code'], sut['code'])
