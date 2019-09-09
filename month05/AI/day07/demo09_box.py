# -*- coding: utf-8 -*-
from __future__ import unicode_literals
"""
demo09_box.py   角点检测
"""
import cv2 as cv

original = cv.imread('./pics/dlreba.jpg')
cv.imshow('Original', original)
gray = cv.cvtColor(original, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)
corners = cv.cornerHarris(gray, 7, 5, 0.04)
print(gray.shape, corners.shape)
# corners[corners > 0] = 1
# cv.imshow('corners', corners)
mixture = original.copy()
mixture[corners > corners.max() * 0.01] = [0, 0, 255]
cv.imshow('Corner', mixture)
cv.waitKey()
cv.destroyAllWindows()
