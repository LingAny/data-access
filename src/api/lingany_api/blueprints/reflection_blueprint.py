from uuid import UUID

from flask import Blueprint, request
from injector import singleton, inject

from apiutils import BaseBlueprint
from lingany_api.serializers.reflection_serializer import ReflectionSerializer
from lingany_api.services.reflection_service import ReflectionService
from sqlutils import ExpandSet


@singleton
class ReflectionBlueprint(BaseBlueprint[ReflectionService]):

    @inject
    def __init__(self, service: ReflectionService) -> None:
        super().__init__(service)

    @property
    def _name(self) -> str:
        return 'reflection'

    @property
    def _serializer(self) -> ReflectionSerializer:
        return ReflectionSerializer()

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

        @blueprint.route('/get-by-languages/<n_id>/<f_id>', methods=['GET'])
        def _get_reflection_by_languages(n_id: str, f_id: str):
            expand = ExpandSet.load(request.args.get('expand'))
            model = self._service.get_reflection_by_languages(n_id, f_id, expand=expand)
            return self._return_one(model)

        return blueprint
