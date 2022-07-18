from fastapi import APIRouter, Depends

from ..services.plants_service import PlantsService
from ..dependencies import get_db_session

router = APIRouter(prefix="/plants")


@router.get("/")
async def get_all(_db_context: get_db_session = Depends()):
    return PlantsService(_db_context).get_all()


@router.get("/{plant_id}")
async def get(plant_id: int, _db_context: get_db_session = Depends()):
    return PlantsService(_db_context).get(plant_id)


@router.post("/import")
async def import_plants(_db_context: get_db_session = Depends()):
    PlantsService(_db_context).import_plants(
        "/Users/egor-vlasov/src/planty/planty-parser/res.json"
    )
