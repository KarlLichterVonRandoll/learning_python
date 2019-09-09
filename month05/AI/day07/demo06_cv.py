"""
opencv
"""
import numpy as np
import cv2 as cv

img = cv.imread('./pics/dlreba.jpg')
print(img.shape, img[0, 0])
cv.imshow('img', img)
# 显示某个颜色通道的数据
blue = np.zeros_like(img)
blue[:, :, 0] = img[:, :, 0]
cv.imshow('blue', blue)
# red
red = np.zeros_like(img)
red[:, :, 2] = img[:, :, 2]
cv.imshow('red', red)
# green
green = np.zeros_like(img)
green[:, :, 1] = img[:, :, 1]
cv.imshow('green', green)

# 图像裁剪
h, w = img.shape[:2]  # 高度与宽度
l, t = int(w / 4), int(h / 4)  # 左、上
r, b = int(w * 3 / 4), int(h * 3 / 4)  # 右、下
img2 = img[t:b, l:r]
cv.imshow('croped', img2)

# 图像缩放     缩放到某个大小范围
img3 = cv.resize(img, (int(w / 4), int(h / 4)))
cv.imshow('img3', img3)
# 使x与y都放到原来的4倍
img4 = cv.resize(img3, None, fx=4, fy=4)
cv.imshow('img4', img4)

cv.waitKey()
# 保存图片
cv.imwrite('./pics/blue.jpg', blue)
cv.destroyAllWindows()