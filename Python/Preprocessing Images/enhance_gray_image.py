# Enhance Contrast of Grayscale Image

# Load image
import cv2
import numpy as np
from matplotlib import pyplot as plt

# Load image
image_gray = cv2.imread('C:/Users/DELL/Desktop/Preprocessing Images/images/plane_256x256.png', cv2.IMREAD_GRAYSCALE)


# Gray enhancement

image_enhanced = cv2.equalizeHist(image_gray)
# Show image
plt.imshow(image_enhanced, cmap='gray'), plt.axis("off")

plt.show()

