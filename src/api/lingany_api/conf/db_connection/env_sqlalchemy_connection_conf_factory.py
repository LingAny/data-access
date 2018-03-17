import os

from lingany_api.conf.db_connection.sqlalchemy_connection_conf import SQLAlchemyConnectionConf


class EnvSqlAlchemyConnectionConfFactory(object):

    @staticmethod
    def create() -> SQLAlchemyConnectionConf:

        dbms = os.environ.get('API_DBMS')
        host = os.environ.get('API_DBHOST')
        port = os.environ.get('API_DBPOR')
        username = os.environ.get('API_DBUSER')
        password = os.environ.get('API_DBPASS')
        db_name = os.environ.get('API_DBNAME')

        return SQLAlchemyConnectionConf(dbms=dbms, host=host, port=port,
                                        username=username, password=password, db_name=db_name)
