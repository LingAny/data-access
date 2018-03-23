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

    def test_fail_create(self):
        reflection_id = self._reflection_stub.get_instance()['id']
        response, sut = self._stub.create(reflection_id=reflection_id)
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

    def test_get_categories_for_reflection(self):
        reflection_id = self._reflection_stub.get_instance()['id']

        response, categories = self._stub.get_categories_for_reflection(reflection_id)
        self.assertEqual(200, response.status_code)
        self.assertGreater(len(categories), 0)

    def _check(self, obj: Dict[str, Any], sut: Dict[str, Any]):
        self.assertEqual(obj['id'], sut['id'])
        self.assertEqual(obj['href'], sut['href'])
        self.assertEqual(obj['title'], sut['title'])
        self.assertEqual(obj['reflection']['id'], sut['reflection']['id'])
        self.assertEqual(obj['reflection']['href'], sut['reflection']['href'])
