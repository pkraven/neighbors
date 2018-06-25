from typing import Optional
from contextlib import contextmanager
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker


class SessionManager:
    _inst = None

    def __new__(cls, config: Optional[dict]=None, debug=False,
                isolation_level="REPEATABLE_READ", expire_on_commit=False):
        if not cls._inst:
            cls._inst = super().__new__(cls)
            cls._inst._config = config
            cls._inst._debug = debug
            cls._inst._isolation_level = isolation_level
            cls._inst._expire_on_commit = expire_on_commit
            cls._inst._scoped_session = None
        return cls._inst

    def get_engine(self):
        engine = create_engine(
            "{engine}+{driver}://{user}:{password}@{host}:{port}/{database}".format(**self._config),
            isolation_level=self._isolation_level,
            echo=self._debug
        )
        connection = engine.connect()
        return engine

    def get_scoped_session(self):
        if not self._scoped_session:
            self._scoped_session = scoped_session(sessionmaker(bind=self.get_engine(),
                                                               expire_on_commit=self._expire_on_commit))
        return self._scoped_session

    def get_session(self):
        _scoped_session = self.get_scoped_session()
        return _scoped_session()
