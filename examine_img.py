"""
Used for debugging. Check the pixel values of an image.
"""
import cv2
from PIL import Image
import numpy as np

image_path = "PaddleSeg/data/brain_mri_seg/labels/label_1.png"
DEST_DIR_LAB = "PaddleSeg/data/brain_mri_seg/test_img.png"

# print all pixel values in image
img = cv2.imread(image_path, 0)  # 0 since the image is grayscale and we need only one channel
for i in range(img.shape[0]):  # traverses through height of the image
    for j in range(img.shape[1]):  # traverses through width of the image
        print(img[i][j])

# check brightest pixel value in image
new_lab = Image.open(image_path).convert('L')  # convert mask to grey scale
data = np.array(new_lab)
print(np.max(data))
print(data.shape)  # check size of image
