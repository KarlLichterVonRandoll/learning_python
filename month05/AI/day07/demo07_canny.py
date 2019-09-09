"""
边缘检测
物体的边缘检测是物体识别常用的手段。
边缘检测常用亮度梯度方法。通过识别亮度梯度变化最大的像素点从而检测出物体的边缘。
"""
import cv2 as cv

original = cv.imread('./pics/dlreba.jpg',
                     cv.IMREAD_GRAYSCALE)
print(original.shape)
cv.imshow('Original', original)
hsobel = cv.Sobel(original, cv.CV_64F, 1, 0, ksize=5)
cv.imshow('H-Sobel', hsobel)
vsobel = cv.Sobel(original, cv.CV_64F, 0, 1, ksize=5)
cv.imshow('V-Sobel', vsobel)
sobel = cv.Sobel(original, cv.CV_64F, 1, 1, ksize=5)
cv.imshow('Sobel', sobel)
laplacian = cv.Laplacian(original, cv.CV_64F)
cv.imshow('Laplacian', laplacian)
canny = cv.Canny(original, 50, 240)
cv.imshow('Canny', canny)
cv.waitKey()
cv.destroyAllWindows()
