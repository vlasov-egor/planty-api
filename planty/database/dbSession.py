from logging import getLogger

from sqlalchemy import create_engine
from sqlalchemy.exc import IntegrityError, DataError
from sqlalchemy.orm import Session
from sqlalchemy.orm import sessionmaker

from .models.base import Base
from .models.base import BaseModel
from .. import config

log = getLogger()

engine = create_engine(config.DATABASE_CONNECTION_STRING, echo=True)
Base.metadata.create_all(engine)


class DbSession:
    _session: Session

    def __init__(self, session: Session, *args, **kwargs):
        self._session = session

    def query(self, *entities, **kwargs):
        return self._session.query(*entities, **kwargs)

    def add_model(self, model: BaseModel, need_flush: bool = False):
        self._session.add(model)

        if need_flush:
            self._session.flush([model])

    def delete_model(self, model: BaseModel):
        if model is None:
            log.warning(f"{__name__}: model is None")

        try:
            self._session.delete(model)
        except IntegrityError as e:
            log.error(f"`{__name__}` {e}")
        except DataError as e:
            log.error(f"`{__name__}` {e}")

    def commit_session(self, need_close: bool = False):
        try:
            self._session.commit()
        except IntegrityError as e:
            log.error(f"`{__name__}` {e}")
            raise
        except DataError as e:
            log.error(f"`{__name__}` {e}")
            raise

        if need_close:
            self.close_session()

    def close_session(self):
        try:
            self._session.close()
        except IntegrityError as e:
            log.error(f"`{__name__}` {e}")
            raise
        except DataError as e:
            log.error(f"`{__name__}` {e}")
            raise


session_factory = sessionmaker(bind=engine, autocommit=False, autoflush=False)


def get_session() -> DbSession:
    session = DbSession(session_factory())
    try:
        yield session
    finally:
        session.close_session()
