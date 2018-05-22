from lingany_api.translator.models.Params import Params

import json
from typing import List, Optional

import requests


class Translator(object):

    def __init__(self, native_language=None, foreign_language=None) -> None:
        self._host = 'https://translate.yandex.net/api/v1.5/tr.json/translate'
        self._key = 'trnsl.1.1.20180319T065216Z.ef55a2768a010315.6ad80367b78fed4fc538c3de84288d98d5553e91'

    def translate_word(self, text, native_language="en", foreign_language="ru") -> Optional[str]:
        parameter = Params(self._key, native_language, foreign_language)
        params = parameter.get_params(text)
        response = requests.get(self._host, params=params)
        data = json.loads(response.text)
        return None if len(data) == 0 else data.get('text')[0]

    def translate_text(self, text, native_language="en", foreign_language="ru") -> Optional[str]:
        parameter = Params(self._key, native_language, foreign_language)
        params, data = parameter.post_params(text)
        response = requests.post(self._host, params=params, data=data)
        data = json.loads(response.text)
        return None if len(data) == 0 else data.get('text')[0]

val = Translator()
val.translate_word('hello')
val.translate_text('fox in forest')