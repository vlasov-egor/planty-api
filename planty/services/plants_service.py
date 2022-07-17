import json

from ..database.dbSession import DbSession
from ..database.models.plants import Plant


def import_plants(path_to_json: str):
    with open(path_to_json) as json_file:
        plants = json.load(json_file)

        for plant in plants["Plants"]:
            if db_session.query(Plant).filter(Plant.name == plant["name"]).count() == 0:
                plant_entity = Plant(
                    name=plant["name"],
                    short_name=plant["shortName"],
                    full_names=plant["fullName"],
                    highlights=plant["highlights"],
                    favourite_activities=plant["likesSection"],
                    quick_facts=plant["quickFactsSection"],
                    about_text=plant["aboutText"],
                )
                db_session.add_model(plant_entity)
                db_session.commit_session()

            else:
                name = plant["name"]
                print(f"{name} skipped because already in db")
