from typing import Dict, Any, Tuple


class Params(object):

    def __init__(self, key: str, nlang: str, flang) -> None:
        self._conf_key = key
        self._nlang = nlang
        self._flang = flang

    def get_params(self, text: str) -> Dict[str, Any]:
        lang = self._flang + '-' + self._nlang
        params = {'key': self._conf_key, 'lang': lang, 'text': text}
        return params

    def post_params(self, text: str) -> Tuple[Dict[str, Any], Dict[str, Any]]:
        lang = self._flang + '-' + self._nlang
        params = {'key': self._conf_key, 'lang': lang}
        data = {'text': text}
        return params, data
