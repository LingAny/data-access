import os

from sqlutils.data_contexts.data_context_factory import DataContextFactory
from sqlutils.data_contexts.postgres_data_context import PostgresDataContext


class EnvDataContextFactory(DataContextFactory):

    def __init__(self):
        pass

    def create_data_context(self):
        # TODO: make decision about database type and load properly variables: add switches
        host = os.environ['DBHOST']
        port = os.environ['DBPORT']
        database = os.environ['DBNAME']
        user = os.environ['DBUSER']
        password = os.environ['DBPASS']

        return PostgresDataContext(host, port, database, user, password)
