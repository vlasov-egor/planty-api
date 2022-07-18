import uvicorn
from fastapi import FastAPI, Depends

from .dependencies import get_db_session, db_context
from .routers import plants_router

# Db init
db_context.create_tables()

# app init
app = FastAPI(dependencies=[Depends(get_db_session)])

app.include_router(plants_router.router)

if __name__ == "__main__":
    uvicorn.run(app)
