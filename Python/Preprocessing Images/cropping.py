# Cropping image

# Load image
import cv2
import numpy as np
from matplotlib import pyplot as plt

# Load image as grayscale
image = cv2.imread('images/plane_256x256.png', cv2.IMREAD_GRAYSCALE)


# Select first half of the columns and all rows
image_cropped = image[:,:126]

# View image
plt.imshow(image_cropped, cmap='gray'), plt.axis("off")
plt.show()

