# -*- coding: utf-8 -*-
from __future__ import unicode_literals
"""
demo08_equalhist.py 直方图均衡化提高亮度
"""
import cv2 as cv

original = cv.imread('./pics/dlreba.jpg')
cv.imshow('Original', original)
gray = cv.cvtColor(original, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)
equalized_gray = cv.equalizeHist(gray)
cv.imshow('Equalized Gray', equalized_gray)
# YUV：亮度，色度，饱和度
yuv = cv.cvtColor(original, cv.COLOR_BGR2YUV)
yuv[..., 0] = cv.equalizeHist(yuv[..., 0])
equalized_color = cv.cvtColor(yuv, cv.COLOR_YUV2BGR)
cv.imshow('Equalized Color', equalized_color)
cv.waitKey()
