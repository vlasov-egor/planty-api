import json

from ...database.dbSession import DbSession
from ...database.models.plants import Plant
from ...core.models.plant import PlantResponse


class PlantsService:
    _db_session: DbSession

    def __init__(self, db_session: DbSession):
        self._db_session = db_session

    def get_all(self) -> list[Plant]:
        return self._db_session.query(Plant).all()

    def get(self, plant_id: int) -> PlantResponse:
        plant = self._db_session \
            .query(Plant) \
            .filter(Plant.id == plant_id) \
            .one()

        response = PlantResponse(**plant)
        print(response.quick_facts)
        return response

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

    def get_plant_photo(self, plant_id: int):
        plant_entity = \
            self._db_session.query(Plant) \
                .filter(Plant.id == plant_id) \
                .one()

        photo = open(f"/Users/egor-vlasov/src/planty/planty-parser/parsed_images/{plant_entity.name}", "r")

        return photo
