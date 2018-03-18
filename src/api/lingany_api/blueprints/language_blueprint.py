from flask import Blueprint, request, Response, json
from injector import inject, singleton

from lingany_api.blueprints.base_blueprint import BaseBlueprint

@singleton
class LanguageBlueprint(BaseBlueprint):

    @inject
    def __init__(self) -> None:
        super().__init__()
        self._service = LanguageService()
        self._serializer = LanguageSerializer()

    @property
    def _name(self) -> str:
        return 'languages'

    def _create_blueprint(self) -> Blueprint:
        blueprint = Blueprint(self._name, __name__)

        @blueprint.route('/<uid>', methods=['GET'])
        def _get_by_id(uid: str):
            return self._get_by_id(uid)

        @blueprint.route('/', methods=['POST'])
        def _add():
            return self._add()

        return blueprint
