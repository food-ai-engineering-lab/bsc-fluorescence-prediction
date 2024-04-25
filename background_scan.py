import numpy as np
import os
import pandas as pd
from PIL import Image
import cv2

def whitescan(input_path, output_path):

    # Loading in the whitescans
    whitescan1 = Image.open('/mnt/projects/sinhasa3/RE_Background/PAX7/1.png')
    whitescan1 = np.array(whitescan1)

    whitescan2 = Image.open('/mnt/projects/sinhasa3/RE_Background/PAX7/2.png')
    whitescan2 = np.array(whitescan2)

    whitescan3 = Image.open('/mnt/projects/sinhasa3/RE_Background/PAX7/3.png')
    whitescan3 = np.array(whitescan3)

    # Average whitescan image
    whitescan = (whitescan3 + whitescan2 + whitescan1)/3

    # print(whitescan.shape)

    img = Image.open(input_path)
    img = np.array(img)

    # Average whitescan normalization
    # diff = whitescan - img
    # diff[diff<0] = 0
    # print(diff.shape)
    # diff = diff.astype(np.uint8)

    # Average whitescan normalization 2 (usual)
    diff = img - whitescan
    diff[diff<0] = 0
    print(diff.shape)
    diff = diff.astype(np.uint8)

    # Consecutive subtraction
    # img = img.astype(np.int8)
    # whitescan1 = whitescan1.astype(np.int8)
    # whitescan2 = whitescan2.astype(np.int8)
    # whitescan3 = whitescan3.astype(np.int8)
    # diff = img - whitescan1 - whitescan2 - whitescan3
    # diff[diff<0] = 0
    # print(diff.shape)
    # diff = diff.astype(np.uint8)

    # OpenCV version
    # cv2.imwrite('whitescan_trial1.jpg', diff)

    # Pillow version
    diff_img = Image.fromarray(diff)
    diff_img.save(output_path)

    # Testing changing uint8 to int8 with manual dump
    # diff2 = img - whitescan1
    # diff2[diff2<0] = 0
    # print(diff2)
    # diff2 = diff2.astype(np.uint8)
    # diff_img2 = Image.fromarray(diff2)
    # diff_img2.save('whitescan_trial3_con.jpg')


for filename in os.listdir('./pax_data/Pax7'):
    if filename.endswith('.jpg'):
        input = '/mnt/projects/sinhasa3/pax_data/Pax7/' + filename
        output = '/mnt/projects/sinhasa3/whitescan_opp_Pax7/' + filename
        whitescan(input, output)
        