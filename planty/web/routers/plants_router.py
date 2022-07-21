from fastapi import APIRouter, Depends, UploadFile
from ...core.services.plants_service import PlantsService
from ..dependencies import get_db_session
from fastapi.responses import FileResponse

router = APIRouter(prefix="/plants")


@router.get("/")
async def get_all(_db_context: get_db_session = Depends()):
    return PlantsService(_db_context).get_all()


@router.get("/{plant_id}")
async def get(plant_id: int, _db_context: get_db_session = Depends()):
    return PlantsService(_db_context).get(plant_id)


@router.post("/import")
async def import_plants(file: UploadFile, _db_context: get_db_session = Depends()):
    PlantsService(_db_context).import_plants(await file.read())
    return {"result": "success"}


@router.get("/photo/{plant_id}")
async def get_plant_photo(plant_id: int, _db_context: get_db_session = Depends()):
    # photo = PlantsService(_db_context).get_plant_photo(plant_id)
    return FileResponse("/app/planty/plant_photos/Fidel.png")
