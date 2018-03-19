import requests


class Translator(object):

    def __init__(self) -> None:
        self._key = "trnsl.1.1.20180318T211746Z.6877fe8e2fa36caf.367dc9c1f8eb4bd7eeb254f8101a1b719f8df5e5"
        self._url = "https://translate.yandex.net/api/v1.5/tr.json/translate"


    @property
    def key(self) -> str:
        return self._key

    @property
    def url(self) -> str:
        return self._url

    def translate(self) -> None:
        response = requests.get('https://httpbin.org/basic-auth/user/passwd', auth=('user', 'passwd'))