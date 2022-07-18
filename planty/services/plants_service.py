import json

from ..database.dbSession import DbSession
from ..database.models.plants import Plant


class PlantsService:
    _db_session: DbSession

    def __init__(self, db_session: DbSession):
        self._db_session = db_session

    def get_all(self) -> list[Plant]:
        return self._db_session.query(Plant).all()

    def get(self, plant_id: int) -> Plant:
        return self._db_session \
            .query(Plant) \
            .filter(Plant.id == plant_id) \
            .one()

    def import_plants(self, path_to_json: str):
        with open(path_to_json) as json_file:
            plants = json.load(json_file)

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
