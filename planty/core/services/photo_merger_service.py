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
from PIL import Image
import re


class PhotoMerger:
    def __init__(self):
        pass

    @staticmethod
    def webp_to_png(path_to_photo: str):
        photo = Image.open(path_to_photo)

        photo.convert("RGBA").save(path_to_photo[:re.search(r'webp', path_to_photo).start()] + "png", "png")

    @staticmethod
    def merge_photo(path_to_pot_photo: str, path_to_plant_photo: str):
        pot = Image.open(path_to_pot_photo)
        plant = Image.open(path_to_plant_photo)

        merged = Image.new("RGBA", (plant.size[0] + 200, plant.size[1] + 200))

        merged.paste(pot, (plant.size[0] // 2 + 100 - pot.size[0] // 2, plant.size[1] + 75 - pot.size[1]), pot)
        merged.paste(plant, (100, 100), plant)
        merged.show()


if __name__ == "__main__":
    _photo_merger = PhotoMerger

    # _photo_merger.webp_to_png(input("Enter path to webp file:\n"))
    _photo_merger.merge_photo(input("Enter path to pot:\n"), input("Enter path to plant:\n"))
