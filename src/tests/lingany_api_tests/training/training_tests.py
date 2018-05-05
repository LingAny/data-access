import unittest

from typing import Dict, Any

from lingany_api_tests.reflection.reflection_stub import ReflectionStub
from src.tests.lingany_api_tests.category.category_stub import CategoryStub
from src.tests.lingany_api_tests.training.training_stub import TrainingStub


class TrainingTestCase(unittest.TestCase):

    _stub: TrainingStub = None
    _category_stub: CategoryStub = None
    _reflection_stub: ReflectionStub = None

    @classmethod
    def setUpClass(cls):
        cls._stub = TrainingStub()
        cls._category_stub = CategoryStub()
        cls._reflection_stub = ReflectionStub()

    def test_fail_create(self):
        category_id = self._category_stub.get_instance()['id']
        response, sut = self._stub.create(category_id=category_id)
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

    def test_get_shape_for_reflection(self):
        reflection = self._reflection_stub.get_instance()
        response, list_obj = self._stub.get_shape_for_reflection(reflection_id=reflection['id'])
        self.assertEqual(200, response.status_code)
        self.assertGreater(len(list_obj), 0)

    def test_get_trainings_for_categories(self):
        category_id = self._category_stub.get_instance()['id']

        response, trainings = self._stub.get_trainings_for_categories(category_id)
        self.assertEqual(200, response.status_code)
        self.assertGreater(len(trainings), 0)

    def _check(self, obj: Dict[str, Any], sut: Dict[str, Any]):
        self.assertEqual(obj['id'], sut['id'])
        self.assertEqual(obj['href'], sut['href'])
        self.assertEqual(sut['nativeWord'], obj['nativeWord'])
        self.assertEqual(sut['foreignWord'], obj['foreignWord'])
        self.assertEqual(obj['category']['id'], sut['category']['id'])
        self.assertEqual(obj['category']['href'], sut['category']['href'])
