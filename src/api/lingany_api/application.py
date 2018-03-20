from flask import Flask
from injector import inject, singleton

from lingany_api.blueprints.category_blueprint import CategoryBlueprint
from lingany_api.blueprints.language_blueprint import LanguageBlueprint
from lingany_api.blueprints.reflection_blueprint import ReflectionBlueprint
from lingany_api.blueprints.training_blueprint import TrainingBlueprint
from lingany_api.ioc import ioc


class Application(object):

    @inject
    def __init__(self) -> None:
        self._languages = ioc.get(LanguageBlueprint, scope=singleton).blueprint
        self._reflection = ioc.get(ReflectionBlueprint, scope=singleton).blueprint
        self._categories = ioc.get(CategoryBlueprint, scope=singleton).blueprint
        self._training = ioc.get(TrainingBlueprint, scope=singleton).blueprint

    def register(self, app: Flask) -> None:
        app.register_blueprint(self._languages, url_prefix='/languages')
        app.register_blueprint(self._reflection, url_prefix='/reflections')
        app.register_blueprint(self._categories, url_prefix='/categories')
        app.register_blueprint(self._training, url_prefix='/training')
