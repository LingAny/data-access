from abc import abstractmethod
from flask import json, Blueprint, Response


class BaseBlueprint(object):

    def __init__(self) -> None:
        self._blueprint = None

    @property
    @abstractmethod
    def _name(self) -> str:
        raise NotImplementedError

    @property
    def blueprint(self) -> Blueprint:
        if not self._blueprint:
            self._blueprint = self._create_blueprint()
        return self._blueprint

    @staticmethod
    def _return_msg(msg: str, status=200):
        return Response(response=json.dumps({'msg': msg}), status=status, mimetype='application/json')

    @abstractmethod
    def _create_blueprint(self) -> Blueprint:
        raise NotImplementedError




