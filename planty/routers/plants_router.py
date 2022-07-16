from fastapi import APIRouter

from ..database.dbSession import DbSession
from ..services.plants_service import PlantsService

plant_router = APIRouter()


class PlantRouter:
    _plant_service: PlantsService

    def __init__(self, db_session: DbSession):
        self._plants_service = PlantsService(db_session)
        self._router = plant_router

    @plant_router.get("/")
    async def root(self):
        return {"message": "Hello World"}

    @plant_router.post("/plants/import")
    async def import_plants(self):
        self._plants_service.import_plants(
            "/Users/egor-vlasov/src/planty-parser/res.json"
        )

    @property
    def router(self):
        return self._router
