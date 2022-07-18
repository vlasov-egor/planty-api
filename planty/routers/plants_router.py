from fastapi import APIRouter, Depends

from ..services.plants_service import PlantsService
from ..dependencies import get_db_session

router = APIRouter(prefix="/plants")


@router.get("/")
async def root():
    return {"message": "Hello World"}


@router.post("/import")
async def import_plants(_db_context: get_db_session = Depends()):
    PlantsService(_db_context).import_plants(
        "/Users/egor-vlasov/src/planty/planty-parser/res.json"
    )
