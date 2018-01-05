import cv2
import os
import numpy as np


def GaussianBlurImg(img_file):
    folder = 'uploads'
    img = cv2.imread(os.path.join(folder, img_file))
    GaussianImg = cv2.GaussianBlur(img, (5, 5), 0)
    cv2.imwrite(os.path.join(folder, img_file), GaussianImg)
