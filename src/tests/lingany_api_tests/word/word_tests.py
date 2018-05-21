import unittest

from src.tests.lingany_api_tests.word.word_stub import WordStub


class WordTestCase(unittest.TestCase):

    _stub: WordStub = None

    @classmethod
    def setUpClass(cls):
        cls._stub = WordStub()

    def test_get_translation_by_text_from_db(self):
        ref_id = "bdf7921b3b5d4646943e43f88c71b394" #en->ru
        text = "there"
        response, obj = self._stub.get_translation_by_text(text, ref_id)
        self.assertEqual(200, response.status_code)
        translation = "туда"
        self.assertEqual(translation, obj.get('translation'))

    def test_get_text_by_translation_from_db(self):
        ref_id = "bdf7921b3b5d4646943e43f88c71b394" #en->ru
        translation = "туда"
        response, obj = self._stub.get_text_by_translation(translation, ref_id)
        self.assertEqual(200, response.status_code)
        text = "there"
        self.assertEqual(text, obj.get('text'))
