import unittest

from src.tests.lingany_api_tests.word.word_stub import WordStub


class WordTestCase(unittest.TestCase):

    _stub: WordStub = None

    @classmethod
    def setUpClass(cls):
        cls._stub = WordStub()

    def test_get_translation_by_text(self):
        text = ""
        response, obj = self._stub.get_translation_by_text(text)
        self.assertEqual(200, response.status_code)

    def get_text_by_translation(self):
        translation = ""
        response, obj = self._stub.get_text_by_translation(translation)
        self.assertEqual(200, response.status_code)
