import json
import urllib.request
import urllib.parse

import requests

from manager.conf.yandex_translator_conf import YandexTranslatorConf
from manager.models.language import Language


class Translator(object):
    def __init__(self, conf: YandexTranslatorConf) -> None:
        self._conf = conf

    def translate_word(self, text: str, native_language: Language, foreign_language: Language) -> str:
        key = '?key=' + self._conf.key
        text = '&text=' + text
        lang = '&lang=' + native_language.code + '-' + foreign_language.code
        format = '&format=plain'
        url = self._conf.url + key + text + lang + format
        response = urllib.request.urlopen(url)
        answer = response.read().decode('utf-8').replace("'", '"')
        data = json.loads(answer)
        return data.get('text')

    def translate_text(self, text, native_language: Language, foreign_language: Language) -> str:
        key = '?key=' + self._conf.key
        lang = '&lang=' + native_language.code + '-' + foreign_language.code
        value = {
            'text': text
        }
        url = self._conf.url + key + lang

        data = urllib.parse.urlencode(value).encode("utf-8")
        req = urllib.request.Request(url)
        with urllib.request.urlopen(req, data=data) as f:
            resp = f.read().decode('utf-8').replace("'", '"')
            data = json.loads(resp)
            return data.get('text')
