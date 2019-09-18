# -*- coding: utf-8 -*-

import cv2
import numpy as np
import matplotlib.pyplot as plt

origin_img = cv2.imread("1.jpg",1)
cv2.imshow("before",origin_img)
HSV = cv2.cvtColor(origin_img, cv2.COLOR_BGR2HSV)
mask = cv2.inRange(HSV, 60, 120)
cv2.imshow("after",mask)
cv2.waitKey()