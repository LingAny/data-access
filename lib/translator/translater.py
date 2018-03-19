import urllib.request
import urllib.parse
import json

class Translator(object):

    def __init__(self, native_language=None, foreign_language=None) -> None:
        self._host = 'https://translate.yandex.net/api/v1.5/tr.json/translate'
        self._key = 'trnsl.1.1.20180319T065216Z.ef55a2768a010315.6ad80367b78fed4fc538c3de84288d98d5553e91'
        if native_language == None: 
            self._nlang = "ru"
        else:
            self._nlang = native_language
        if foreign_language == None:
            self._flang = "en"
        else:
            self._flang = foreign_language

    def translate(self, text, native_language="en", foreign_language="ru") -> None:
        key = '?key=' + self._key
        text = '&text=' + text 
        lang = '&lang=' + native_language + '-' + foreign_language
        format = '&format=plain'
        url = self._host + key + text+ lang + format
        response = urllib.request.urlopen(url)
        answer = response.read().decode('utf-8').replace("'", '"')
        data = json.loads(answer)
        return data
