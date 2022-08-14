from pydantic import BaseModel
from enum import IntEnum


class PlantResponse(BaseModel):
    name: str
    short_name: str
    full_names: list
    highlights: list
    favourite_activities: dict
    quick_facts: dict
    about_text: str


class PotColor(IntEnum):
    black = 1
    white = 2
    none = 3
