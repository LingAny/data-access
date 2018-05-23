import unittest

from src.tests.lingany_api_tests.word.word_stub import WordStub


class WordTestCase(unittest.TestCase):

    _stub: WordStub = None

    @classmethod
    def setUpClass(cls):
        cls._stub = WordStub()

    #   nativelang=ru foreignlang=en
    def test_get_translation_by_text_from_db(self):
        ref_id = "01838288daec45fb831c89a25502ec6a" #en->ru
        text = "there"
        response, obj = self._stub.get_translation_by_text(text, ref_id)
        self.assertEqual(200, response.status_code)
        translation = "туда"
        self.assertEqual(translation, obj.get('translation'))

    def test_get_text_by_translation_from_db(self):
        ref_id = "01838288daec45fb831c89a25502ec6a" #en->ru
        translation = "туда"
        response, obj = self._stub.get_text_by_translation(translation, ref_id)
        self.assertEqual(200, response.status_code)
        text = "there"
        self.assertEqual(text, obj.get('text'))

    def test_get_translation_by_text_from_web(self):
        ref_id = "01838288daec45fb831c89a25502ec6a" #en->ru
        text = "amazing"
        response, obj = self._stub.get_translation_by_text(text, ref_id)
        self.assertEqual(200, response.status_code)
        translation = "удивительные"
        self.assertEqual(translation, obj.get('translation'))

    def test_get_text_by_translation_from_web(self):
        ref_id = "01838288daec45fb831c89a25502ec6a" #en->ru
        translation = "удивительные"
        response, obj = self._stub.get_text_by_translation(translation, ref_id)
        self.assertEqual(200, response.status_code)
        text = "amazing"
        self.assertEqual(text, obj.get('text'))
