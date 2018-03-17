import logging

from flask import Blueprint, request, Response, json
from injector import inject, singleton

from lingany_api.blueprints.base_blueprint import BaseBlueprint


@singleton
class AdminSystemBlueprint(BaseBlueprint):

    @inject
    def __init__(self) -> None:
        super().__init__()

    @property
    def _name(self) -> str:
        return 'admin_system'

    def _create_blueprint(self) -> Blueprint:
        blueprint = Blueprint(self._name, __name__)

        @blueprint.route('/', methods=['POST'])
        def _add():
            return self._return_msg(f'name: {self._name}')

        return blueprint
