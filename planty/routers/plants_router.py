from fastapi import APIRouter

from ..database.dbSession import DbSession
from ..services.plants_service import PlantsService

plants_router = APIRouter()


@plants_router.get("/")
async def root():
    return {"message": "Hello World"}


@plants_router.post("/plants/import")
async def import_plants():
    self._plants_service.import_plants("/Users/egor-vlasov/src/planty-parser/res.json")
