import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .database.dbSession import DbSession
from . import config
from .database.models.base import Base


class DbContext:
    engine: sqlalchemy.engine.Engine
    db_session: DbSession

    def __init__(self):
        self.engine = create_engine(
            config.DATABASE_CONNECTION_STRING,
            echo=True,
            pool_pre_ping=True,
        )

        session_factory = sessionmaker(bind=self.engine)
        self.db_session = DbSession(session_factory())

    def create_tables(self):
        Base.metadata.create_all(self.engine)


db_context = DbContext()


def get_db_session() -> DbContext:
    return db_context.db_session
