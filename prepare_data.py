"""
Organize data to following format and do necessary processing on images:
  custom_dataset
  |
  |--images
  |  |--image_1.png
  |  |--image_2.png
  |  |--...
  |
  |--labels
  |  |--label_1.png
  |  |--label_2.png
  |  |--...
"""
import os
from PIL import Image
import numpy as np

SOURCE_DIR = "raw_data/kaggle_3m/"
DEST_DIR_IMG = "PaddleSeg/data/brain_mri_seg/images/"
DEST_DIR_LAB = "PaddleSeg/data/brain_mri_seg/labels/"
img_file_extension = ".png"
lab_file_extension = ".png"
VERBOSE = True  # debug flag
counter = 1


def check_img_is_nonblack(path: str) -> bool:
    im = Image.open(path)
    return im.getbbox()  # Image.getbbox() returns the None (false) if there are no
    # non-black pixels in the image, otherwise it returns a tuple of
    # points, which is true.


if __name__ == "__main__":
    for root, dirs, files in os.walk(SOURCE_DIR):
        if root != SOURCE_DIR:
            if VERBOSE:
                print(root)

            for f in files:
                file_path = root + "/" + f
                if f[-8:-4] == "mask" and check_img_is_nonblack(file_path):
                    # i.e. file_path is the path to a mask with non-black pixels
                    if VERBOSE:
                        print("Processing " + file_path)

                    # set new names/file extension for images and labels
                    img_name = "image_" + str(counter) + img_file_extension
                    lab_name = "label_" + str(counter) + lab_file_extension

                    # process label
                    orig_color = 255
                    replacement_color = 1
                    old_lab = Image.open(file_path).convert('L')  # convert mask to grey scale
                    data = np.array(old_lab)
                    # replace all mask pixels that are 255 to 1
                    data[(data == orig_color)] = replacement_color
                    new_lab = Image.fromarray(data, mode='L')
                    new_lab.save(DEST_DIR_LAB + lab_name)

                    # process image
                    img_path = file_path.replace("_mask", "")
                    new_img = Image.open(img_path).convert('RGB')  # convert image to RGB
                    new_img.save(DEST_DIR_IMG + img_name)

                    counter += 1

            if VERBOSE:
                print("================")
