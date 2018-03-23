import unittest

from typing import Dict, Any

from src.tests.lingany_api_tests.category.category_stub import CategoryStub
from src.tests.lingany_api_tests.reflection.reflection_stub import ReflectionStub


class CategoryTestCase(unittest.TestCase):
    _stub: CategoryStub = None
    _reflection_stub: ReflectionStub = None

    @classmethod
    def setUpClass(cls):
        cls._stub = CategoryStub()
        cls._reflection_stub = ReflectionStub()

    def test_create(self):
        reflection_id = self._reflection_stub.get_instance()['id']
        response, sut = self._stub.create(reflection_id=reflection_id)
        self.assertEqual(201, response.status_code)

    def test_get_by_id(self):
        reflection_id = self._reflection_stub.get_instance()['id']
        response, sut = self._stub.create(reflection_id=reflection_id)
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

    def test_get_categories_for_reflection(self):
        reflection_id = self._reflection_stub.get_instance()['id']
        response, sut = self._stub.create(reflection_id=reflection_id)
        self.assertEqual(201, response.status_code)

        response, obj = self._stub.get_categories_for_reflection(reflection_id)
        self.assertEqual(200, response.status_code)
        self._check(obj[0], sut)

    def tearDown(self):
        self._stub.clear()

    def _check(self, obj: Dict[str, Any], sut: Dict[str, Any]):
        self.assertEqual(sut['id'], obj['id'])
        self.assertIn('href', obj)
        self.assertEqual(sut['reflectionId'], obj['reflection']['id'])
