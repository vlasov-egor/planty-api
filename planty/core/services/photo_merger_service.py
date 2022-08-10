# import math
#
# # pot = Image.open("images/pot.webp")
# # plant = Image.open("images/plant-1.webp")
#
# # pot.convert("RGBA").save("pot.png", "png")
# # plant.convert("RGBA").save("plant-1.png", "png")
#
# pot = Image.open("images/pot.png")
# plant = Image.open("images/plant-2.png")
#
# merged = Image.new("RGBA", (plant.size[0] + 200, plant.size[1] + 200))
#
# merged.paste(pot, (plant.size[0] // 2 + 100 - pot.size[0] // 2, plant.size[1] + 75 - pot.size[1]), pot)
# merged.paste(plant, (100, 100), plant)
# merged.show()
from typing import Any

from PIL import Image


class PhotoMerger:
    def __init__(self):
        pass

    def merge_photo(self, path_to_pot_photo: str, path_to_plant_photo: str) -> Any:
        return Image.open(path_to_plant_photo)
