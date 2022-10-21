import re
from os import listdir
from os.path import isfile, join

from PIL import Image


class PhotoMerger:
    def __init__(self):
        pass

    @staticmethod
    def webp_to_png(path_to_photo: str):
        photo = Image.open(path_to_photo)

        photo.convert("RGBA").save(path_to_photo[:re.search(r'webp', path_to_photo).start()] + "png", "png")

    @staticmethod
    def merge_photo(path_to_pot_photo: str, path_to_plant_photo: str, path_to_save: str):
        pot = Image.open(path_to_pot_photo).convert("RGBA")
        plant = Image.open(path_to_plant_photo).convert("RGBA")

        merged = Image.new("RGBA", (plant.size[0] + 200, plant.size[1] + 200))

        merged.paste(pot, (plant.size[0] // 2 + 100 - pot.size[0] // 2, plant.size[1] + 100 - pot.size[1]), pot)
        merged.paste(plant, (100, 100), plant)

        merged.save(path_to_save, format="png")


if __name__ == "__main__":
    _photo_merger = PhotoMerger()

    plants_dir_path = "/Users/egor-vlasov/src/planty/planty-api/planty/core/photos/plants/"
    black_pot_path = "/Users/egor-vlasov/src/planty/planty-api/planty/core/photos/pots/black_pot.png"
    white_pot_path = "/Users/egor-vlasov/src/planty/planty-api/planty/core/photos/pots/white_pot.png"

    plants_paths = [f for f in listdir(plants_dir_path + "without_pot/") if
                    isfile(join(plants_dir_path + "without_pot/", f))]

    for index, plant in enumerate(plants_paths):
        _photo_merger.merge_photo(black_pot_path, plants_dir_path + "without_pot/" + plant,
                                  plants_dir_path + "black_pot/" + plant)

        _photo_merger.merge_photo(white_pot_path, plants_dir_path + "without_pot/" + plant,
                                  plants_dir_path + "white_pot/" + plant)

        print(f"merged: {index + 1}")
