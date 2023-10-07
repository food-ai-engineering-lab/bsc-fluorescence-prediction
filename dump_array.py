import json
import numpy as np
import cv2


img = cv2.imread('/mnt/projects/sinhasa3/color_tifs_Pax7/2_prediction_c0.jpg')

with open('output.txt', 'w') as filehandle:
    json.dump(np.asarray(img).tolist(), filehandle)