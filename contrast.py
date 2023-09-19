import cv2
import numpy as np
import os
import re

# # Trial 1
# image = cv2.imread('./pax_data/Pax7/Pax7-5-1.jpg')
# image=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
# se=cv2.getStructuringElement(cv2.MORPH_RECT , (8,8))
# bg=cv2.morphologyEx(image, cv2.MORPH_DILATE, se)
# out_gray=cv2.divide(image, bg, scale=255)
# out_binary=cv2.threshold(out_gray, 0, 255, cv2.THRESH_OTSU )[1] 

# # cv2.imshow('binary', out_binary)  
# cv2.imwrite('binary.png',out_binary)

# # cv2.imshow('gray', out_gray)  
# cv2.imwrite('gray.png',out_gray)

# Trial 2

def preprocess(input_file, output_file):
    # load image
    img = cv2.imread(input_file)

    # convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # blur
    blur = cv2.GaussianBlur(gray, (0,0), sigmaX=33, sigmaY=33)

    # divide
    divide = cv2.divide(gray, blur, scale=255)

    # otsu threshold
    thresh = cv2.threshold(divide, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)[1]

    # apply morphology
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3,3))
    # morph = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)

    # # write result to disk
    # cv2.imwrite("hebrew_text_division.jpg", divide)
    cv2.imwrite(output_file, thresh)
    # cv2.imwrite("hebrew_text_division_morph.jpg", morph)

for filename in os.listdir('./tifs_Pax7_raw'):
    if filename.endswith('.jpeg') and 'gray' not in filename:
        new_file = '/mnt/projects/sinhasa3/tifs_Pax7/' + filename
        filename = '/mnt/projects/sinhasa3/tifs_Pax7_raw/' + filename
        preprocess(filename, new_file)