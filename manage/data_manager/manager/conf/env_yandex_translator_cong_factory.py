import os

from manager.conf.yandex_translator_conf import YandexTranslatorConf


class EnvYandexTranslatorConfFactory(object):

    @staticmethod
    def create() -> YandexTranslatorConf:
        url = os.environ.get('YANDEX_TRANSLATOR_URL')
        key = os.environ.get('YANDEX_TRANSLATOR_KEY')
        return YandexTranslatorConf(url=url, key=key)
