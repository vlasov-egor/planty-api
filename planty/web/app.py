import uvicorn
from fastapi import FastAPI, Depends

from .routers import plants_router
from ..database import dbSession

db_session = dbSession.get_session()

# app init
app = FastAPI()

app.include_router(plants_router.router)


@app.get("/")
async def hello_world():
    return {"message": "Hello World"}


if __name__ == "__main__":
    uvicorn.run(app)
