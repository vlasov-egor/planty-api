from pydantic import BaseModel, Json


class PlantResponse(BaseModel):
    name: str
    short_name: str
    full_names: list
    highlights: list
    favourite_activities: Json
    quick_facts: Json
    about_text: str
    photo: str
