import numpy as np
import cv2

def dummy(val):
    pass

color_original = cv2.imread('./images/cute_cat.jpg')
color_original = cv2.resize(color_original, (0, 0), fx=0.5, fy=0.5)
color_modified = color_original.copy()


cv2.namedWindow('app')
cv2.createTrackbar('contrast', 'app', 1, 100, dummy)
cv2.createTrackbar('brightness', 'app', 50, 100, dummy)
cv2.createTrackbar('filter', 'app', 0, 1, dummy)
cv2.createTrackbar('grayscale', 'app', 0, 1, dummy)

while True:
    cv2.imshow('app', color_modified)
    k = cv2.waitKey(1) & 0xFF
    if k == ord('q'):
        break

    contrast = cv2.getTrackbarPos('contrast', 'app')
    brightness = cv2.getTrackbarPos('brightness', 'app')

    color_modified = cv2.addWeighted(color_original, contrast, np.zeros(color_original.shape, dtype=color_original.dtype), 0, brightness-50)

cv2.destroyAllWindows()