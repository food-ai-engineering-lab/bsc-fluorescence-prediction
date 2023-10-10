import numpy as np
import os
import pandas as pd
from PIL import Image
import cv2

whitescan1 = Image.open('/mnt/projects/sinhasa3/RE_Background/PAX7/1.png')
whitescan1 = np.array(whitescan1)

whitescan2 = Image.open('/mnt/projects/sinhasa3/RE_Background/PAX7/2.png')
whitescan2 = np.array(whitescan2)

whitescan3 = Image.open('/mnt/projects/sinhasa3/RE_Background/PAX7/3.png')
whitescan3 = np.array(whitescan3)

whitescan = (whitescan3 + whitescan2 + whitescan1)/3

# print(whitescan.shape)

img = Image.open('/mnt/projects/sinhasa3/pax_data/Pax7/Pax7-5-1.jpg')
img = np.array(img)

# Average whitescan normalization
# diff = whitescan - img
# diff[diff<0] = 0
# print(diff.shape)
# diff = diff.astype(np.uint8)

# Average whitescan normalization 2 (usual)
# diff = img - whitescan
# diff[diff<0] = 0
# print(diff.shape)
# diff = diff.astype(np.uint8)

# Consecutive subtraction
diff = img - whitescan1 - whitescan2 - whitescan3
diff[diff<0] = 0
print(diff.shape)
diff = diff.astype(np.uint8)

# cv2.imwrite('whitescan_trial1.jpg', diff)
diff_img = Image.fromarray(diff)
diff_img.save('whitescan_trial1_con.jpg')
