import os


class Configure(object):

    def __init__(self, host: str, port: int, username: str, password: str, db_name: str, db_path: str) -> None:
        self._host = host
        self._port = port
        self._username = username
        self._password = password
        self._db_name = db_name
        self._db_path = db_path

    @property
    def host(self) -> str:
        return self._host

    @property
    def port(self) -> int:
        return self._port

    @property
    def username(self) -> str:
        return self._username

    @property
    def password(self) -> str:
        return self._password

    @property
    def db_name(self) -> str:
        return self._db_name

    @property
    def db_path(self) -> str:
        return self._db_path


class EnvConfigureFactory(object):

    @staticmethod
    def create() -> Configure:
        host = os.environ.get('DBHOST')
        port = int(os.environ.get('DBPORT'))
        username = os.environ.get('DBUSER')
        password = os.environ.get('DBPASS')
        db_name = os.environ.get('DBNAME')
        db_path = os.environ.get('DATABASE')

        return Configure(host=host, port=port, username=username,
                         password=password, db_name=db_name, db_path=db_path)


def main():
    print('MAIN')
    conf = EnvConfigureFactory.create()


if __name__ == '__main__':
    main()
