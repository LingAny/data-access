import logging

from abc import abstractmethod
from flask import abort, json, request, url_for, Blueprint, Response
from typing import List, Any, TypeVar, Generic, Sequence

from sqlutils import Model, AbstractExpandSet, ExpandSet, EmptyExpandSet, Service, \
                     ForeignKeyViolationError, NoDataFoundError, UniqueViolationError, \
                     RestrictViolationError

from .serializer import Serializer

T = TypeVar("T", bound="Model")
S = TypeVar("S", bound="Service")


def return_one(model: Model, serializer: Serializer, expand: AbstractExpandSet) -> Response:
    if model is None:
        abort(404)

    response = serializer.dump(model, expand)
    return Response(response=json.dumps(response),
                    status=200, mimetype='application/json')


def return_many(models: Sequence[T], serializer: Serializer, expand: AbstractExpandSet) -> Response:
    response = []
    for model in models:
        response.append(serializer.dump(model, expand))
    return Response(response=json.dumps(response),
                    status=200, mimetype='application/json')


class BaseBlueprint(Generic[S]):

    def __init__(self, service: S) -> None:
        self._blueprint = None
        self._service = service

    @property
    @abstractmethod
    def _name(self) -> str:
        raise NotImplementedError

    @property
    @abstractmethod
    def _serializer(self) -> Serializer:
        raise NotImplementedError

    @property
    def blueprint(self) -> Blueprint:
        if not self._blueprint:
            self._blueprint = self._create_blueprint()
        return self._blueprint

    def _return_one(self, model: Model) -> Response:
        return return_one(model, self._serializer, ExpandSet.load(request.args.get('expand')))

    def _return_many(self, models: Sequence[Model]) -> Response:
        return return_many(models, self._serializer, ExpandSet.load(request.args.get('expand')))

    def _get_by_id(self, uid: Any, expand: AbstractExpandSet):
        model = None
        try:
            model = self._service.get_by_id(uid, expand=expand)
        except BaseException as ex:
            logging.debug(f"Can't get {self._name} model by id: {ex}", exc_info=True)
            abort(400)
        return self._return_one(model)

    def _get_all(self, expand: AbstractExpandSet):
        try:
            models = self._service.get_all(expand=expand)
            return self._return_many(models)
        except BaseException as ex:
            logging.exception(f"Can't get all {self._name} models: {ex}", exc_info=True)
            abort(500)

    def _add(self):
        entity = self._parse()
        uid = self._add_entity(entity)
        return Response(response='', status=201, mimetype='application/json',
                        headers={'Location': url_for('._get_by_id', uid=uid)})

    def _update(self):
        entity = self._parse()
        model = self._update_entity(entity)
        response = self._serializer.dump(model, EmptyExpandSet())
        return Response(response=json.dumps(response),
                        status=200, mimetype='application/json')

    def _delete(self, uid: Any):
        model: Model = None
        try:
            model = self._service.get_by_id(uid, EmptyExpandSet())
        except BaseException as ex:
            logging.exception(f"Can't get {self._name} model: {ex}", exc_info=True)
            abort(400)

        if model is None:
            abort(404)

        self._service.delete(model.uid)
        return Response(response='', status=204, mimetype='application/json')

    @abstractmethod
    def _create_blueprint(self) -> Blueprint:
        raise NotImplementedError

    def _parse(self):
        entity = None
        try:
            entity = self._serializer.load(request.json)
        except BaseException as ex:
            logging.debug(f"Can't parse {self._name} entity: {ex}", exc_info=True)
            abort(400)
        return entity

    def _add_entity(self, entity: Any) -> Any:
        uid = None
        try:
            uid = self._service.add(entity)
        except UniqueViolationError as ex:
            logging.debug(f"Can't add {self._name} entity: {ex}", exc_info=True)
            abort(409)
        except ForeignKeyViolationError as ex:
            logging.debug(f"Can't add {self._name} entity: {ex}", exc_info=True)
            abort(409)
        except RestrictViolationError as ex:
            logging.debug(f"Can't add {self._name} entity: {ex}", exc_info=True)
            abort(409)
        return uid

    def _update_entity(self, entity: Any) -> Any:
        try:
            self._service.update(entity)
        except NoDataFoundError as ex:
            logging.debug(f"Can't update {self._name} entity: {ex}", exc_info=True)
            abort(404)
        except UniqueViolationError as ex:
            logging.debug(f"Can't update {self._name} entity: {ex}", exc_info=True)
            abort(409)
        except RestrictViolationError as ex:
            logging.debug(f"Can't add {self._name} entity: {ex}", exc_info=True)
            abort(409)

        model = self._service.get_by_id(entity.uid, EmptyExpandSet())
        if model is None:
            abort(404)

        return model
