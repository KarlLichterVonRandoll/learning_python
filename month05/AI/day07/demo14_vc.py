# -*- coding: utf-8 -*-
from __future__ import unicode_literals
"""
demo14_vc.py  视频捕捉
"""
import cv2 as cv

video_capture = cv.VideoCapture(0)
while True:
    frame = video_capture.read()[1]
    cv.imshow('frame', frame)
    if cv.waitKey(33) == 27:
        break
video_capture.release()
cv.destroyAllWindows()
