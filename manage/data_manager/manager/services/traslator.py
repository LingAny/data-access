import requests

from manager.conf.yandex_translator_conf import YandexTranslatorConf


class Translator(object):

    def __init__(self, conf: YandexTranslatorConf) -> None:
        self._conf = conf

    def translate(self) -> None:
        response = requests.get('https://httpbin.org/basic-auth/user/passwd', auth=('user', 'passwd'))