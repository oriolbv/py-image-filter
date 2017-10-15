import numpy as np
import cv2

def dummy(val):
    pass

img = cv2.imread('./images/cute_cat.jpg')
img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)

cv2.namedWindow('app')
cv2.createTrackbar('contrast', 'app', 1, 100, dummy)
cv2.createTrackbar('brightness', 'app', 50, 100, dummy)
cv2.createTrackbar('filter', 'app', 0, 1, dummy)
cv2.createTrackbar('grayscale', 'app', 0, 1, dummy)

while True:
    cv2.imshow('app', img)
    k = cv2.waitKey(1) & 0xFF
    if k == ord('q'):
        break

cv2.destroyAllWindows()