from PIL import Image
import numpy as np

background = Image.open("/mnt/projects/sinhasa3/analysis3.jpg")
overlay = Image.open("/mnt/projects/sinhasa3/analysis1.jpg")

background = background.convert("RGBA")
overlay = overlay.convert("RGBA")

new_img = Image.blend(background, overlay, 0.5)
new_img.save("overlay.png","PNG")