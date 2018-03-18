from flask import Blueprint, request, Response, json
from injector import inject, singleton
import ujson

from lingany_api.blueprints.base_blueprint import BaseBlueprint
from lingany_api.serializers.language_serializer import LanguageSerializer
from lingany_api.services.language_service import LanguageService


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
            language = self._service.get_by_id(uid)
            data = self._serializer.dump(language)
            return Response(response=ujson.dumps(data), status=200, mimetype='application/json')

        @blueprint.route('/', methods=['POST'])
        def _add():
            data = ujson.loads(request.data)
            language_dto = self._serializer.load(data)
            self._service.add(language_dto)

        return blueprint
