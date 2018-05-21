import unittest

from src.tests.lingany_api_tests.word.word_stub import WordStub


class WordTestCase(unittest.TestCase):

    _stub: WordStub = None

    @classmethod
    def setUpClass(cls):
        cls._stub = WordStub()

    def test_get_translation_by_text(self):
        ref_id = "01838288daec45fb831c89a25502ec6a" #ru->en
        text = "there"
        response, obj = self._stub.get_translation_by_text(text, ref_id)
        self.assertEqual(200, response.status_code)

    def test_get_text_by_translation(self):
        ref_id = "01838288daec45fb831c89a25502ec6a" #ru->en
        translation = "туда"
        response, obj = self._stub.get_text_by_translation(translation, ref_id)
        self.assertEqual(200, response.status_code)
