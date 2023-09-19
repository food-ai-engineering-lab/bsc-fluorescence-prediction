from PIL import Image
import os
import re

c = 0

def convert_rgb_to_grayscale(input_path, output_path):
    with Image.open(input_path) as img:
        grayscale = img.convert("L")  # Convert to grayscale
        grayscale.save(output_path)

for filename in os.listdir('./pax_data/BF'):
    if filename.endswith('.tif') and 'gray' not in filename:
        gs = '/mnt/projects/sinhasa3/pax_data/BF/gray_' + filename
        filename = '/mnt/projects/sinhasa3/pax_data/BF/' + filename
        convert_rgb_to_grayscale(filename, gs)

for filename in os.listdir('./pax_data/Pax7'):
    if filename.endswith('.tif') and 'gray' not in filename:
        gs = '/mnt/projects/sinhasa3/pax_data/Pax7/gray_' + filename
        filename = '/mnt/projects/sinhasa3/pax_data/Pax7/' + filename
        convert_rgb_to_grayscale(filename, gs)

for filename in os.listdir('./pax_data/DAPI'):
    if filename.endswith('.tif') and 'gray' not in filename:
        gs = '/mnt/projects/sinhasa3/pax_data/DAPI/gray_' + filename
        filename = '/mnt/projects/sinhasa3/pax_data/DAPI/' + filename
        convert_rgb_to_grayscale(filename, gs)
        c += 1

print(c)

# Example usage:
# convert_rgb_to_grayscale("path_to_rgb_image.tif", "path_to_save_grayscale_image.tif")