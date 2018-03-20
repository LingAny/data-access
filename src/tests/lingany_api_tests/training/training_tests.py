import unittest

from typing import Dict, Any

from src.tests.lingany_api_tests.category.category_stub import CategoryStub
from src.tests.lingany_api_tests.training.training_stub import TrainingStub


class TrainingTestCase(unittest.TestCase):

    _stub: TrainingStub = None
    _category_stub: CategoryStub = None

    @classmethod
    def setUpClass(cls):
        cls._stub = TrainingStub()
        cls._category_stub = CategoryStub()

    def test_create(self):
        category_id = self._category_stub.get_instance()['id']
        response, sut = self._stub.create(category_id=category_id)
        self.assertEqual(201, response.status_code)

    def test_get_by_id(self):
        response, sut = self._stub.create()
        self.assertEqual(201, response.status_code)
        response, obj = self._stub.get_by_id(sut['id'])
        self.assertEqual(200, response.status_code)
        self._check(obj, sut)

    def tearDown(self):
        self._stub.clear()

    def _check(self, obj: Dict[str, Any], sut: Dict[str, Any]):
        self.assertEqual(sut['id'], obj['id'])
        self.assertIn('href', obj)
        self.assertEqual(sut['nativeWord'], obj['nativeWord'])
        self.assertEqual(sut['foreignWord'], obj['foreignWord'])
