from ..models.plants import PlantResponse
from ...database.models.plants import Plant


class PlantsMapper:
    @staticmethod
    def to_plant_response(entity: Plant) -> PlantResponse:

        return PlantResponse(
            name=entity.name,
            short_name=entity.short_name,
            full_names=entity.full_names,
            highlights=entity.highlights,
            favourite_activities=entity.favourite_activities,
            quick_facts=entity.quick_facts,
            about_text=entity.about_text,
            photo="",
        )
