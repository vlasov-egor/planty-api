from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from .dbSession import DbSession
from .models.base import Base
from .. import config

engine = create_engine(config.DATABASE_CONNECTION_STRING, echo=True)
Base.metadata.create_all(engine)
session_factory = sessionmaker(bind=engine, autocommit=False, autoflush=False)


def get_session() -> DbSession:
    session = DbSession(session_factory())
    try:
        yield session
    finally:
        session.close_session()
