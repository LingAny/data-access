import logging
from uuid import UUID

from dateutil import parser
from flask import Blueprint, Response, request, abort
from injector import singleton, inject

from apiutils import BaseBlueprint, return_many
from sqlutils import ExpandSet, EmptyExpandSet


@singleton
class LanguageBlueprint(BaseBlueprint[LanguageService]):

    @inject
    def __init__(self, service: LanguageService) -> None:
        super().__init__(service)

    @property
    def _name(self) -> str:
        return 'users'

    def _create_blueprint(self) -> Blueprint:
        blueprint = Blueprint(self._name, __name__)

        @blueprint.route('/<uid>', methods=['GET'])
        def _get_by_id(uid: str):
            expand = ExpandSet.load(request.args.get('expand'))
            return self._get_by_id(UUID(uid), expand)

        @blueprint.route('/', methods=['POST'])
        def _add():
            return self._add()

        @blueprint.route('/', methods=['GET'])
        def _get_all():
            raise NotImplementedError

        @blueprint.route('/<uid>', methods=['DELETE'])
        def _delete(uid: str):
            raise NotImplementedError

        @blueprint.route('/', methods=['PUT'])
        def _update():
            raise NotImplementedError

        return blueprint
