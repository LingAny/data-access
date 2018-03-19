class YandexTranslatorConf(object):
    
    def __init__(self, url: str, key: str) -> None:
        self._url = url
        self._key = key

    @property
    def url(self) -> str:
        return self._url

    @property
    def key(self) -> str:
        return self._key
