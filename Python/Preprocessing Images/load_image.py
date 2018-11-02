# Load Images

# Import library
import cv2
import numpy as np
from matplotlib import pyplot as plt


# Load image as grayscale
image_gray = cv2.imread('images/plane_256x256.png', cv2.IMREAD_GRAYSCALE)

# Show image
plt.imshow(image_gray, cmap='gray'), plt.axis("off")
plt.show()

# Load image as RGB
image_bgr = cv2.imread('images/plane_256x256.png', cv2.IMREAD_COLOR)

# Convert to RGB
image_rgb = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2RGB)

# Show image
plt.imshow(image_rgb)
plt.show()
