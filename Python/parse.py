import argparse
import numpy as np
import cv2

# construct the argument parse and parse the arguments to load an image with command-line.
parser = argparse.ArgumentParser(description='Handwritten number recognition program using CNN.')
parser.add_argument("-i", "--image", required=True, help="path to input image")
args = vars(parser.parse_args())

# load the image.
image = cv2.imread(args["image"])
orig = image.copy()
cv2.imshow("Output", image)
cv2.waitKey(0)

