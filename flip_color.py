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

def flip_color_palette(input_path, output_path):
    gray = cv2.imread(input_path, cv2.IMREAD_COLOR)
    # gray = gray[:, :, 0]
    print(gray.shape)
    print(gray.dtype)

    # # Use this one for more shade different trial
    # inPalette = np.array([
    # [43, 77, 2],         # green
    # [255,255,255],       # white
    # [50, 66, 32],        # dark green
    # [49, 70, 21],        # brighter green
    # [0,0,0]],            # black
    # )

    # For flipping opposite whitescan
    # inPalette = np.array([
    # [12, 34, 10],        # dark green
    # [255,255,255],       # white
    # [0, 0, 255],         # blue
    # [255, 0, 0],         # red
    # [0,0,0]],            # black
    # )

    # Palette for consecutive normalization with all
    inPalette = np.array([
    [73, 107, 80],        # dark green
    [255,255,255],       # white
    [0, 0, 255],         # blue
    [255, 0, 0],         # red
    [0,0,0]],            # black
    )

    # For fliping consecutive whitescan
    # inPalette = np.array([
    # [0, 130, 0],         # darker green
    # [255,255,255],       # white
    # [0, 0, 255],         # blue
    # [255, 0, 0],         # red
    # [23, 160, 22]],      # lighter green
    # )

    r = QuantizeToGivenPalette(gray,inPalette)

    # Now make LUT (Look Up Table) with the 5 new colours
    # Previously replaced black with cyan and white with black
    LUT = np.zeros((5,3),dtype=np.uint8)

    # Analysis 1
    LUT[0]=[0,0,0]        # black
    LUT[1]=[255,255,255]  # white
    LUT[2]=[255,0,255]    # magenta
    LUT[3]=[255,0,0]      # blue
    LUT[4]=[43, 77, 2]    # green

    # Testing with 35-1
    # LUT[0]=[0,0,0]        # black
    # LUT[1]=[255,255,255]  # white
    # LUT[2]=[255,0,255]    # magenta
    # LUT[3]=[0,0,0]        # black
    # LUT[4]=[43, 77, 2]    # green

    # Analysis 2
    # LUT[0]=[43, 77, 2]    # green
    # LUT[1]=[255,255,255]  # white
    # LUT[2]=[0,0,0]        # black
    # LUT[3]=[255,0,0]      # blue
    # LUT[4]=[43, 77, 2]    # green

    # Analysis 3
    # LUT[0]=[43, 77, 2]    # green
    # LUT[1]=[255,255,255]  # white
    # LUT[2]=[0,0,0]        # black
    # LUT[3]=[255,0,0]      # blue
    # LUT[4]=[0,0,0]        # black

    # Analysis 4
    # LUT[0]=[43, 77, 2]    # green
    # LUT[1]=[255,255,255]  # white
    # LUT[2]=[0,0,0]        # black
    # LUT[3]=[0,0,0]        # black
    # LUT[4]=[0,0,0]        # black

    # Look up each pixel in the LUT
    result = LUT[r]

    cv2.imwrite(output_path, result)
            

c = 0

# for filename in os.listdir("/mnt/projects/sinhasa3/color_tifs_Pax7"):
#     if filename.endswith('.jpg') and 'prediction' in filename:
#         flip_color_palette("/mnt/projects/sinhasa3/color_tifs_Pax7/" + filename, "/mnt/projects/sinhasa3/denoised_Pax/" + filename)
#         c += 1

print(c)

flip_color_palette("/mnt/projects/sinhasa3/whitescan_trial1_conall.jpg", "/mnt/projects/sinhasa3/whitescan_fliptrial1_conall.jpg")
