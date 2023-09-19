from PIL import Image
import os
import re

c = 0

for filename in os.listdir('./processed_pax7'):
    if filename.endswith('.jpg'):
        input_path = '/mnt/projects/sinhasa3/processed_pax7/' + filename
        output_path = '/mnt/projects/sinhasa3/processed_pax7/' + filename.split('.')[0] + '.tif'
        with Image.open(input_path) as img:
            img.save(output_path)
            c += 1


print(c)