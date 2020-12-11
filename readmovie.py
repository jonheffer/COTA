#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 14:24:17 2020

@author: jon.heffer
"""

import cv2
print(cv2.__version__)  # my version is 3.1.0
vidcap = cv2.VideoCapture('test_video.mp4')
count = 0

image = vidcap.read()
cv2.imshow('image',imgage)
cv2.waitKey(0)
cv2.destroyAllWindows()