import json
from typing import Optional

import requests


from manager.conf.yandex_translator_conf import YandexTranslatorConf


class Translator(object):

    def __init__(self, conf: YandexTranslatorConf) -> None:
        self._conf = conf

    def translate_word(self, text: str, native_lang_code: str, foreign_lang_code: str) -> Optional[str]:

        params = {
            'key': self._conf.key,
            'lang': self._build_lang(native_lang_code, foreign_lang_code),
            'text': text
        }

        response = requests.get(self._conf.url, params=params)
        data = json.loads(response.text)
        return None if len(data) == 0 else data.get('text')[0]

    def translate_text(self, text: str, native_lang_code: str, foreign_lang_code: str) -> Optional[str]:
        params = {
            'key': self._conf.key,
            'lang': self._build_lang(native_lang_code, foreign_lang_code),
            'text': text
        }
        data = {
            'text': text
        }

        response = requests.post(self._conf.url, params=params, data=data)
        data = json.loads(response.text)
        return None if len(data) == 0 else data.get('text')[0]

    @classmethod
    def _build_lang(cls, native_lang_code: str, foreign_lang_code: str) -> str:
        return f"{native_lang_code}-{foreign_lang_code}"
