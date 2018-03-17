from flask import Flask
from injector import inject, singleton

from rt_incident_api.blueprints.attributes.attribute_type_blueprint import AttributeTypeBlueprint
from rt_incident_api.blueprints.attributes.message_attribute_blueprint import MessageAttributeBlueprint
from rt_incident_api.blueprints.messages.actor_blueprint import ActorBlueprint
from rt_incident_api.blueprints.messages.actor_type_blueprint import ActorTypeBlueprint
from rt_incident_api.blueprints.messages.message_blueprint import MessageBlueprint
from rt_incident_api.blueprints.messages.message_category_blueprint import MessageCategoryBlueprint
from rt_incident_api.blueprints.messages.message_type_blueprint import MessageTypeBlueprint
from rt_incident_api.blueprints.situations.situation_blueprint import SituationBlueprint
from rt_incident_api.blueprints.situations.situation_type_blueprint import SituationTypeBlueprint
from rt_incident_api.ioc import ioc


class Application(object):

    @inject
    def __init__(self) -> None:
        self._actors = ioc.get(ActorBlueprint, scope=singleton).blueprint
        self._actor_types = ioc.get(ActorTypeBlueprint, scope=singleton).blueprint
        self._attribute_types = ioc.get(AttributeTypeBlueprint, scope=singleton).blueprint
        self._categories = ioc.get(MessageCategoryBlueprint, scope=singleton).blueprint
        self._messages = ioc.get(MessageBlueprint, scope=singleton).blueprint
        self._message_attributes = ioc.get(MessageAttributeBlueprint, scope=singleton).blueprint
        self._message_types = ioc.get(MessageTypeBlueprint, scope=singleton).blueprint
        self._situations = ioc.get(SituationBlueprint, scope=singleton).blueprint
        self._situation_types = ioc.get(SituationTypeBlueprint, scope=singleton).blueprint

    def register(self, app: Flask) -> None:
        app.register_blueprint(self._actors, url_prefix='/actors')
        app.register_blueprint(self._actor_types, url_prefix='/actor-types')
        app.register_blueprint(self._attribute_types, url_prefix='/attribute-types')
        app.register_blueprint(self._categories, url_prefix='/categories')
        app.register_blueprint(self._messages, url_prefix='/messages')
        app.register_blueprint(self._message_attributes, url_prefix='/attributes')
        app.register_blueprint(self._message_types, url_prefix='/message-types')
        app.register_blueprint(self._situations, url_prefix='/situations')
        app.register_blueprint(self._situation_types, url_prefix='/situation-types')
