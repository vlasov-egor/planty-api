from planty.services import plant_service

from fastapi import APIRouter

router = APIRouter()


@router.get("/")
async def root():
    return {"message": "Hello World"}


@router.post("/plants/import")
async def import_plants():
    plant_service.import_plants("/Users/egor-vlasov/src/planty-parser/res.json")
