from fastapi import APIRouter, Depends, UploadFile
from fastapi.responses import FileResponse

from ...core.models.plants import PlantResponse, PotColor
from ...core.services.plants_service import PlantsService

router = APIRouter(prefix="/plants")


@router.get("/", response_model=list[PlantResponse])
async def get_all(_plants_service: PlantsService = Depends()):
    return await _plants_service.get_all()


@router.get("/{plant_id}", response_model=PlantResponse)
async def get(plant_id: int, _plants_service: PlantsService = Depends()):
    return await _plants_service.get(plant_id)


@router.post("/import")
async def import_plants(file: UploadFile, _plants_service: PlantsService = Depends()):
    await _plants_service.import_plants(await file.read())
    return {"result": "success"}


@router.get("/{plant_id}/photo/{pot_color}", response_model=FileResponse)
async def get_plant_photo(plant_id: int, pot_color: PotColor, _plants_service: PlantsService = Depends()):
    file = await _plants_service.get_photo_path(plant_id, pot_color)
    return FileResponse(file)
