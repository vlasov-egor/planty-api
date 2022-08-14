from pydantic import BaseModel
from enum import Enum


class PlantResponse(BaseModel):
    name: str
    short_name: str
    full_names: list
    highlights: list
    favourite_activities: dict
    quick_facts: dict
    about_text: str


class PotColor(Enum):
    black = "black"
    white = "white"
    none = "none"
