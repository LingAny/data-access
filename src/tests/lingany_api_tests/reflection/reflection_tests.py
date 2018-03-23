import unittest

from typing import Dict, Any
from uuid import UUID

from src.tests.lingany_api_tests.language.language_stub import LanguageStub
from src.tests.lingany_api_tests.reflection.reflection_stub import ReflectionStub


class ReflectionTestCase(unittest.TestCase):

    _stub: ReflectionStub = None
    _language_stub: ReflectionStub = None

    @classmethod
    def setUpClass(cls):
        cls._stub = ReflectionStub()
        cls._language_stub = LanguageStub()

    def test_fail_create(self):
        native_language_id = self._language_stub.get_instance()['id']
        foreign_language_id = self._language_stub.get_instance()['id']
        response, sut = self._stub.create(native_language_id=native_language_id,
                                          foreign_language_id=foreign_language_id)
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

    def test_get_reflection_by_languages(self):
        native_lang, foreign_lang = self._language_stub.get_pair()

        response, obj = self._stub.get_reflection_by_languages(native_lang_id=native_lang['id'],
                                                               foreign_lang_id=foreign_lang['id'])
        self.assertEqual(200, response.status_code)
        self.assertIsNotNone(obj['id'])
        self.assertIsNotNone(obj['href'])
        self.assertIsNotNone(obj['title'])
        self.assertEqual(UUID(native_lang['id']), UUID(obj['nativeLanguage']['id']))
        self.assertEqual(UUID(foreign_lang['id']), UUID(obj['foreignLanguage']['id']))

    def _check(self, obj: Dict[str, Any], sut: Dict[str, Any]):
        self.assertEqual(sut['id'], obj['id'])
        self.assertEqual(sut['href'], obj['href'])
        self.assertEqual(sut['title'], obj['title'])
        self.assertEqual(sut['nativeLanguage']['id'], obj['nativeLanguage']['id'])
        self.assertEqual(sut['foreignLanguage']['id'], obj['foreignLanguage']['id'])
