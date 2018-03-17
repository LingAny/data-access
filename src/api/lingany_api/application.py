from flask import Flask
from injector import inject, singleton

from lingany_api.blueprints.admin.admin_categories_blueprint import AdminCategoriesBlueprint
from lingany_api.blueprints.admin.admin_system_blueprint import AdminSystemBlueprint
from lingany_api.blueprints.admin.admin_words_blueprint import AdminWordsBlueprint
from lingany_api.ioc import ioc


class Application(object):

    @inject
    def __init__(self) -> None:
        self._admin_system = ioc.get(AdminSystemBlueprint, scope=singleton).blueprint
        self._admin_categories = ioc.get(AdminCategoriesBlueprint, scope=singleton).blueprint
        self._admin_words = ioc.get(AdminWordsBlueprint, scope=singleton).blueprint

    def register(self, app: Flask) -> None:
        app.register_blueprint(self._admin_system, url_prefix='/admin/system')
        app.register_blueprint(self._admin_categories, url_prefix='/admin/categories')
        app.register_blueprint(self._admin_words, url_prefix='/admin/words')

