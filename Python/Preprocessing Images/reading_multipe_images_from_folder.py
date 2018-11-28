# Import library
import cv2
import numpy as np
from matplotlib import pyplot as plt
import os
import sys

path = "D:/SkinSegmentation/facedata/"
dirs = os.listdir(path)

# Process each image
i = 4001
for filename in dirs:   
    image_bgr = cv2.imread(path + filename, cv2.IMREAD_COLOR)
    print(filename)
    # Convert to RGB
    image_rgb = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2RGB)
    # Check image's size.
    print(image_rgb.shape)
    w,h,c = image_rgb.shape
    
    for i in range(w):
        for j in range(h):

            if (image_rgb[i,j,0] == 0 and image_rgb[i,j,1] == 0 and image_rgb[i,j,2] == 255):

                image_rgb[i,j,0] = 0
                image_rgb[i,j,1] = 0
                image_rgb[i,j,2] = 0    
           
            else:
                image_rgb[i,j,0] = 255
                image_rgb[i,j,1] = 255
                image_rgb[i,j,2] = 255

    cv2.imwrite(filename,image_rgb)
