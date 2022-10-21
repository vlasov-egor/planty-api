import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from .dbSession import DbSession
from .models.base import Base

DATABASE_CONNECTION_STRING = os.environ.get("Database_Connection_String")

engine = create_engine(DATABASE_CONNECTION_STRING, echo=True)
Base.metadata.create_all(engine)
session_factory = sessionmaker(bind=engine, autocommit=False, autoflush=False)


def get_session() -> DbSession:
    session = DbSession(session_factory())
    try:
        yield session
    finally:
        session.close_session()
