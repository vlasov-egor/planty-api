import uvicorn
from fastapi import FastAPI
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from . import config
from .database.dbSession import DbSession
from .database.models.base import Base
from .routers.plants_router import plants_router

# Db init
engine = create_engine(
    f"postgresql://{config.DATABASE_USER}:{config.DATABASE_PASSWORD}@{config.DATABASE_HOST}:{config.DATABASE_PORT}/{config.DATABASE_NAME}",
    echo=True,
    pool_pre_ping=True,
)
session_factory = sessionmaker(bind=engine)
db_session = DbSession(session_factory())

Base.metadata.create_all(engine)

# app init
app = FastAPI()

app.include_router(plants_router)

if __name__ == "__main__":
    uvicorn.run(app)
