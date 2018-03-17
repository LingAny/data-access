import logging

from flask import Blueprint, request, Response, json
from injector import inject, singleton

from lingany_api.blueprints.base_blueprint import BaseBlueprint


@singleton
class CategoryBlueprint(BaseBlueprint):

    @inject
    def __init__(self) -> None:
        super().__init__()

    @property
    def _name(self) -> str:
        return 'category'

    def _create_blueprint(self) -> Blueprint:
        blueprint = Blueprint(self._name, __name__)

        @blueprint.route('/system/<uid>', methods=['GET'])
        def _get_for_system(uid: str):
            return self._return_msg(f'uid: {uid}')

        return blueprint
