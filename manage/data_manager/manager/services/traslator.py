import json
import urllib.request
import urllib.parse


from manager.conf.yandex_translator_conf import YandexTranslatorConf


class Translator(object):
    def __init__(self, conf: YandexTranslatorConf) -> None:
        self._conf = conf

    def translate_word(self, text: str, native_language: str, foreign_language: str) -> str:
        key = '?key=' + self._conf.key
        text = '&text=' + text
        lang = '&lang=' + native_language + '-' + foreign_language
        format = '&format=plain'
        url = self._conf.url + key + text + lang + format
        response = urllib.request.urlopen(url)
        answer = response.read().decode('utf-8').replace("'", '"')
        data = json.loads(answer)
        return data.get('text')[0]

    def translate_text(self, text, native_language: str, foreign_language: str) -> str:
        key = '?key=' + self._conf.key
        lang = '&lang=' + native_language + '-' + foreign_language
        value = {
            'text': text
        }
        url = self._conf.url + key + lang

        data = urllib.parse.urlencode(value).encode("utf-8")
        req = urllib.request.Request(url)
        with urllib.request.urlopen(req, data=data) as f:
            resp = f.read().decode('utf-8').replace("'", '"')
            data = json.loads(resp)
            return data.get('text')[0]
