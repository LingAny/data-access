from flask import Flask
from injector import inject, singleton

from lingany_api.ioc import ioc


class Application(object):

    @inject
    def __init__(self) -> None:
        pass

    def register(self, app: Flask) -> None:
        pass
