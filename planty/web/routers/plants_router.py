from fastapi import APIRouter, Depends, UploadFile
from fastapi.responses import FileResponse
from ...core.models.plants import PlantResponse
from ...core.services.plants_service import PlantsService

router = APIRouter(prefix="/plants")


@router.get("/", response_model=list[PlantResponse])
async def get_all(_plants_service: PlantsService = Depends()):
    return _plants_service.get_all()


@router.get("/{plant_id}", response_model=PlantResponse)
async def get(plant_id: int, _plants_service: PlantsService = Depends()):
    return _plants_service.get(plant_id)


@router.post("/import")
async def import_plants(file: UploadFile, _plants_service: PlantsService = Depends()):
    _plants_service.import_plants(await file.read())
    return {"result": "success"}


@router.get("/photo/{plant_id}")
async def get_plant_photo(plant_id: int, _plants_service: PlantsService = Depends()):
    # photo = PlantsService(_db_context).get_plant_photo(plant_id)
    name = _plants_service.get(plant_id).name
    print(name)
    return FileResponse(f"/app/planty/plant_photos/{name}.png")
