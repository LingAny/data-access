import logging
import os

from flask import Flask, Response
from flask_compress import Compress
from werkzeug.wsgi import DispatcherMiddleware

from lingany_api.db import db
from lingany_api.cache import cache
from lingany_api.application import Application
from lingany_api.conf.db_connection.env_sqlalchemy_connection_conf_factory import EnvSqlAlchemyConnectionConfFactory

app = Flask(__name__)
app.config['APPLICATION_ROOT'] = '/api/v1/lingany-da'
Compress(app)
app.config['CACHE_TYPE'] = os.environ['CACHE_TYPE']

# app.config['CACHE_KEY_PREFIX'] = '/api/v1/lingany-da'
# app.config['CACHE_REDIS_HOST'] = 'redis'
# app.config['CACHE_REDIS_PORT'] = '6379'

sql_alchemy_conf = EnvSqlAlchemyConnectionConfFactory.create()
app.config['SQLALCHEMY_DATABASE_URI'] = sql_alchemy_conf.uri

cache.init_app(app)
db.init_app(app)

application = Application()
application.register(app)


@app.errorhandler(400)
def bad_request(error):
    logging.info(error)
    return Response(status=400, mimetype='application/json')


@app.errorhandler(404)
def data_not_found(error):
    logging.info(error)
    return Response(status=404, mimetype='application/json')


@app.errorhandler(409)
def restrict_violation(error):
    logging.info(error)
    return Response(status=409, mimetype='application/json')


@app.errorhandler(500)
def internal_server_error(error):
    logging.exception(error)
    return Response(status=500, mimetype='application/json')


def simple(env, resp):
    logging.debug(env)
    resp('404 NOT FOUND', [('mimetype', 'application/json')])
    return [b'']


app.wsgi_app = DispatcherMiddleware(simple, {'/api/v1/lingany-da': app.wsgi_app})

if __name__ == '__main__':
    app.run()
