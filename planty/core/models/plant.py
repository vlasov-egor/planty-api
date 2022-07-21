import json


class PlantInPotPhoto:
    white_pot: str
    black_pot: str
    without_pot: str


class PlantResponse:
    id: int
    name: str
    short_name: str
    full_names: list[str]
    highlights: list[str]
    favourite_activities: json
    quick_facts: json
    about_text: str
    photo: PlantInPotPhoto
