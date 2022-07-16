from PIL import Image
import math

# pot = Image.open("images/pot.webp")
# plant = Image.open("images/plant-1.webp")

# pot.convert("RGBA").save("pot.png", "png")
# plant.convert("RGBA").save("plant-1.png", "png")

pot = Image.open("images/pot.png")
plant = Image.open("images/plant-2.png")

merged = Image.new("RGBA", (plant.size[0] + 200, plant.size[1] + 200))

merged.paste(pot, (plant.size[0] // 2 + 100 - pot.size[0] // 2, plant.size[1] + 75 - pot.size[1]), pot)
merged.paste(plant, (100, 100), plant)
merged.show()
