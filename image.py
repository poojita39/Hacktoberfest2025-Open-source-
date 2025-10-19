from PIL import Image
import os

folder = "images"
for f in os.listdir(folder):
    if f.endswith(".png"):
        path = os.path.join(folder, f)
        img = Image.open(path)
        img.convert("RGB").save(path.replace(".png", ".jpg"))
print("Converted all PNGs to JPGs")
