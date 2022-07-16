from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from fastapi import FastAPI

from . import config

from .database.dbSession import DBSession
from .database.models.base import Base
from .routers import plants

engine = create_engine(
    f"postgresql://{config.DATABASE_USER}:{config.DATABASE_PASSWORD}@{config.DATABASE_HOST}:{config.DATABASE_PORT}/{config.DATABASE_NAME}",
    echo=True,
    pool_pre_ping=True,
)
session_factory = sessionmaker(bind=engine)
db_session = DBSession(session_factory())

Base.metadata.create_all(engine)

app = FastAPI()

app.include_router(plants.router)
