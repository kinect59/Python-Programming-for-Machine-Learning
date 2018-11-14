# Loading images from a folder.
import numpy as np
import os
from keras.preprocessing.image import array_to_img, img_to_array, load_img
import cv2
import glob
from matplotlib import pyplot as plt


for img in glob.glob(r'C:\Users\Huy-Hieu.Pham\Desktop\SkinDetector\Skin_Images_Masks\*.png'):
    
    # Loading images.
    img = load_img(img, grayscale=True)
    
    # Show image.
    plt.imshow(img , cmap='gray')
    plt.axis("off")
    plt.show()

    
    

