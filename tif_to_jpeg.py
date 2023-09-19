import os
from PIL import Image

# Did not work when I tried again and reverted back to same error
for filename in os.listdir('/mnt/projects/sinhasa3/tifs/'):
    if filename.endswith('.tif'):
        # filename = '/mnt/projects/sinhasa3/tifs/' + filename
        im = Image.open('/mnt/projects/sinhasa3/tifs/' + filename)
        im.convert('L')
        filename = '/mnt/projects/sinhasa3/color_tifs/'+ filename.split('.')[0] + '.jpg'
        im.save(filename)