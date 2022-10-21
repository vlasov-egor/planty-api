import json
import os.path

from fastapi import Depends, HTTPException

from ..mappers.plants_mapper import PlantsMapper
from ..models.plants import PlantResponse, PotColor
from ...database import get_session
from ...database.dbSession import DbSession
from ...database.models.plants import Plant


class PlantsService:
    _db_session: DbSession
    _mapper: PlantsMapper

    def __init__(
            self,
            db_session: DbSession = Depends(get_session),
            plant_mapper: PlantsMapper = Depends(PlantsMapper),
    ):
        self._db_session = db_session
        self._mapper = plant_mapper

    async def get_all(self) -> list[PlantResponse]:
        plants = self._db_session.query(Plant).all()
        return [self._mapper.to_plant_response(plant) for plant in plants]

    async def get(self, plant_id: int) -> PlantResponse:
        plant = self._db_session.query(Plant).filter(Plant.id == plant_id).first()

        if plant is None:
            raise HTTPException(status_code=404, detail="Plant not found")

        return self._mapper.to_plant_response(plant)

    async def import_plants(self, json_file: bytes):
        plants = json.loads(json_file)

        for plant in plants["Plants"]:
            plant_entity = Plant(
                name=plant["name"],
                short_name=plant["shortName"],
                full_names=plant["fullName"],
                highlights=plant["highlights"],
                favourite_activities=plant["likesSection"],
                quick_facts=plant["quickFactsSection"],
                about_text=plant["aboutText"],
            )
            self._db_session.add_model(plant_entity)
            self._db_session.commit_session()

    async def get_photo_path(self, plant_id: int, pot_color: PotColor) -> str:
        plant = self._db_session.query(Plant).filter(Plant.id == plant_id).first()

        if plant is None:
            raise HTTPException(status_code=404, detail="Plant not found")

        path_to_photo = "planty/core/photos/plants"
        match pot_color:
            case PotColor.black:
                path_to_photo += f"/black_pot/{plant.name}.png"
            case PotColor.white:
                path_to_photo += f"/white_pot/{plant.name}.png"
            case PotColor.none:
                path_to_photo += f"/without_pot/{plant.name}.png"

        if os.path.isfile(path_to_photo):
            raise HTTPException(status_code=404, detail="Photo not found")

        return path_to_photo
