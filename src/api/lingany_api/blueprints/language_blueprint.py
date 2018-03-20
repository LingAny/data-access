from uuid import UUID

from flask import Blueprint, request
from injector import singleton, inject

from apiutils import BaseBlueprint
from lingany_api.serializers.language_serializer import LanguageSerializer
from lingany_api.services.language_service import LanguageService
from sqlutils import ExpandSet


@singleton
class LanguageBlueprint(BaseBlueprint[LanguageService]):

    @inject
    def __init__(self, service: LanguageService) -> None:
        super().__init__(service)

    @property
    def _name(self) -> str:
        return 'languages'

    @property
    def _serializer(self) -> LanguageSerializer:
        return LanguageSerializer()

    def _create_blueprint(self) -> Blueprint:
        blueprint = Blueprint(self._name, __name__)

        @blueprint.route('/<uid>', methods=['GET'])
        def _get_by_id(uid: str):
            expand = ExpandSet.load(request.args.get('expand'))
            return self._get_by_id(UUID(uid), expand)

        @blueprint.route('/', methods=['GET'])
        def _get_all():
            expand = ExpandSet.load(request.args.get('expand'))
            return self._get_all(expand)

        @blueprint.route('/', methods=['POST'])
        def _add():
            return self._add()

        return blueprint
