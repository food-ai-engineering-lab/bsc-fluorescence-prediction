import os
import re

from PIL import Image
import cv2
import numpy as np

def QuantizeToGivenPalette(im, palette):
    """Quantize image to a given palette.
    
    The input image is expected to be a Numpy array.
    The palette is expected to be a list of R,G,B values."""

    # Calculate the distance to each palette entry from each pixel
    distance = np.linalg.norm(im[:,:,None] - palette[None,None,:], axis=3)

    # Now choose whichever one of the palette colours is nearest for each pixel
    palettised = np.argmin(distance, axis=2).astype(np.uint8)

    return palettised

def convert_grayscale_to_rgb_cv(input_path, output_path):
    gray = cv2.imread(input_path, cv2.IMREAD_COLOR)
    # gray = gray[:, :, 0]
    print(gray.shape)
    print(gray.dtype)

    inPalette = np.array([
    [0,0,0],             # black
    [0,0,255],           # red
    [0,255,0],           # green
    [255,0,0],           # blue
    [255,255,255]],      # white
    )
    r = QuantizeToGivenPalette(gray,inPalette)

    # Now make LUT (Look Up Table) with the 5 new colours
    # Previously replaced black with cyan and white with black
    LUT = np.zeros((5,3),dtype=np.uint8)
    LUT[0]=[43, 77, 2]    # green
    LUT[1]=[255,255,255]  # white
    LUT[2]=[255,0,255]    # magenta
    LUT[3]=[255,0,0]      # blue
    LUT[4]=[0,0,0]        # black

    # Look up each pixel in the LUT
    result = LUT[r]

    # backtorgb = cv2.cvtColor(gray,cv2.COLOR_GRAY2BGR)
    # backtorgb = cv2.cvtColor(backtorgb,cv2.COLOR_BGR2HSV)

    # # Create random color image
    # image = (np.random.standard_normal([200,200,3]) * 255).astype(np.uint8)

    # # Convert to grayscale (1 channel)
    # gray = cv2.cvtColor(gray, cv2.COLOR_BGR2GRAY)

    # Merge channels to create color image (3 channels)
    # gray_three = cv2.merge([gray,gray,gray])

    # Fill a contour on both the single channel and three channel image
    # contour = np.array([[10,10], [190, 10], [190, 80], [10, 80]])
    # cv2.fillPoly(gray, [contour], [36,255,12])
    # cv2.fillPoly(gray_three, [contour], [36,255,12])

    # cv2.imshow('image', image)
    # cv2.imshow('gray', gray)
    # cv2.imshow('gray_three', gray_three)
    # cv2.waitKey()

    cv2.imwrite(output_path, result)
            

c = 0

def convert_grayscale_to_rgb(input_path, output_path):
    with Image.open(input_path) as img:
        rgbimg = Image.new("RGB", img.size)
        rgbimg.paste(img)
        rgbimg.save(output_path)
        # rgb = img.convert("RGB")  # Convert to RGB
        # rgb.save(output_path)

for filename in os.listdir("/mnt/projects/sinhasa3/tifs_Pax7"):
    if filename.endswith('.jpeg'):
        convert_grayscale_to_rgb_cv("/mnt/projects/sinhasa3/tifs_Pax7/" + filename, "/mnt/projects/sinhasa3/color_tifs_Pax7/" + filename.split('.')[0]+ '.jpg')
        c += 1

print(c)

# convert_grayscale_to_rgb_cv('/mnt/projects/sinhasa3/tifs/8_prediction_c0.jpeg', '/mnt/projects/sinhasa3/color_tifs/8_prediction_c0.jpg')