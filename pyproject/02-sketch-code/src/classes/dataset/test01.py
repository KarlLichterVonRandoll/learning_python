import cv2
import numpy as np
import os

img_rgb = cv2.imread("img01.png")

img_grey = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
img_adapted = cv2.adaptiveThreshold(img_grey, 255, cv2.ADAPTIVE_THRESH_MEAN_C,
                                    cv2.THRESH_BINARY, 101, 9)
print(img_grey.shape)
print(img_adapted.shape)

img_stacked = np.repeat(img_adapted[..., None], 3, axis=2)
print(img_stacked.shape)

resized = cv2.resize(img_stacked, (200, 200), interpolation=cv2.INTER_AREA)
# cv2.imshow("img01", img_grey)
#
bg_img = 255 * np.ones(shape=(256, 256, 3))
bg_img[27:227, 27:227, :] = resized
bg_img /= 255
print(bg_img.shape)
# cv2.imshow("img01", img_grey)
# cv2.waitKey(0)
