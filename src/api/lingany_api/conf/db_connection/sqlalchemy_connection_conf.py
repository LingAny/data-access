class SQLAlchemyConnectionConf(object):

    def __init__(self, dbms: str, host: str, port: int, username: str, password: str, db_name: str) -> None:
        self._dbms = dbms
        self._host = host
        self._port = port
        self._username = username
        self._password = password
        self._db_name = db_name
    
    @property
    def dbms(self) -> str:
        return self._dbms

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
    def uri(self) -> str:
        return f"{self.dbms}://{self.username}:{self.password}@{self.host}:{self.port}/{self.db_name}"
