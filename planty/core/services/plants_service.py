import json

from fastapi import Depends

from .photo_merger_service import PhotoMerger
from ..mappers.plants_mapper import PlantsMapper
from ..models.plants import PlantResponse
from ...database.dbSession import DbSession, get_session
from ...database.models.plants import Plant


class PlantsService:
    _db_session: DbSession
    _photo_merger: PhotoMerger
    _mapper: PlantsMapper

    def __init__(self, db_session: DbSession = Depends(get_session),
                 plant_mapper: PlantsMapper = Depends(PlantsMapper)):
        self._db_session = db_session
        self._mapper = plant_mapper

    def get_all(self) -> list[PlantResponse]:
        plants = self._db_session.query(Plant).all()
        return [self._mapper.to_plant_response(plant) for plant in plants]

    def get(self, plant_id: int) -> PlantResponse:
        plant = self._db_session \
            .query(Plant) \
            .filter(Plant.id == plant_id) \
            .one()

        return self._mapper.to_plant_response(plant)

    def import_plants(self, json_file: bytes):
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
