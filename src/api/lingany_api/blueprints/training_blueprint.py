from uuid import UUID

from flask import Blueprint, request
from injector import singleton, inject

from apiutils import BaseBlueprint
from lingany_api.serializers.training_serializer import TrainingSerializer
from lingany_api.services.training_service import TrainingService
from sqlutils import ExpandSet


@singleton
class TrainingBlueprint(BaseBlueprint[TrainingService]):

    @inject
    def __init__(self, service: TrainingService) -> None:
        super().__init__(service)

    @property
    def _name(self) -> str:
        return 'training'

    @property
    def _serializer(self) -> TrainingSerializer:
        return TrainingSerializer()

    def _create_blueprint(self) -> Blueprint:
        blueprint = Blueprint(self._name, __name__)

        @blueprint.route('/<uid>', methods=['GET'])
        def _get_by_id(uid: str):
            expand = ExpandSet.load(request.args.get('expand'))
            return self._get_by_id(UUID(uid), expand)

        @blueprint.route('/', methods=['POST'])
        def _add():
            return self._add()

        return blueprint
