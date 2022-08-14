from fastapi import APIRouter, Depends, UploadFile
from fastapi.responses import FileResponse
from ...core.models.plants import PlantResponse, PotColor
from ...core.services.plants_service import PlantsService

router = APIRouter(prefix="/photos")


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


@router.get("/photo/{plant_id}/{pot_color}")
async def get_plant_photo(plant_id: int, pot_color: PotColor, _plants_service: PlantsService = Depends()):
    name = _plants_service.get(plant_id).name

    path_to_photo = ""
    match pot_color:
        case PotColor.black, PotColor.white:
            path_to_photo = f"/app/planty/plant_photos/{pot_color}/{name}.png"
        case PotColor.none:
            path_to_photo = f"/app/planty/plant_photos/without_pot/{name}.png"

    return FileResponse(path_to_photo)
