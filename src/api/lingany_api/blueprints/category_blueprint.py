from uuid import UUID

from flask import Blueprint, request
from injector import singleton, inject

from apiutils import BaseBlueprint
from lingany_api.serializers.category_serializer import CategorySerializer
from lingany_api.services.category_service import CategoryService
from sqlutils import ExpandSet


@singleton
class CategoryBlueprint(BaseBlueprint[CategoryService]):

    @inject
    def __init__(self, service: CategoryService) -> None:
        super().__init__(service)

    @property
    def _name(self) -> str:
        return 'categories'

    @property
    def _serializer(self) -> CategorySerializer:
        return CategorySerializer()

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
