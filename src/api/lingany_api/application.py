from flask import Flask
from injector import inject, singleton

from lingany_api.blueprints.admin.admin_categories_blueprint import AdminCategoriesBlueprint
from lingany_api.blueprints.admin.admin_system_blueprint import AdminSystemBlueprint
from lingany_api.blueprints.admin.admin_translate_blueprint import AdminTranslateBlueprint
from lingany_api.blueprints.admin.admin_words_blueprint import AdminWordsBlueprint
from lingany_api.blueprints.da.category_blueprint import CategoryBlueprint
from lingany_api.blueprints.da.training_blueprint import TrainingBlueprint
from lingany_api.blueprints.language_blueprint import LanguageBlueprint
from lingany_api.blueprints.reflection_blueprint import ReflectionBlueprint
from lingany_api.ioc import ioc


class Application(object):

    @inject
    def __init__(self) -> None:
        self._admin_system = ioc.get(AdminSystemBlueprint, scope=singleton).blueprint
        self._admin_categories = ioc.get(AdminCategoriesBlueprint, scope=singleton).blueprint
        self._admin_words = ioc.get(AdminWordsBlueprint, scope=singleton).blueprint
        self._admin_translate = ioc.get(AdminTranslateBlueprint, scope=singleton).blueprint

        self._categories = ioc.get(CategoryBlueprint, scope=singleton).blueprint
        self._training = ioc.get(TrainingBlueprint, scope=singleton).blueprint
        self._languages = ioc.get(LanguageBlueprint, scope=singleton).blueprint
        self._reflection = ioc.get(ReflectionBlueprint, scope=singleton).blueprint

    def register(self, app: Flask) -> None:
        app.register_blueprint(self._admin_system, url_prefix='/admin/system')
        app.register_blueprint(self._admin_categories, url_prefix='/admin/categories')
        app.register_blueprint(self._admin_words, url_prefix='/admin/words')
        app.register_blueprint(self._admin_translate, url_prefix='/admin/translate')

        app.register_blueprint(self._categories, url_prefix='/categories')
        app.register_blueprint(self._training, url_prefix='/training')
        app.register_blueprint(self._languages, url_prefix='/languages')
        app.register_blueprint(self._reflection, url_prefix='/reflections')
