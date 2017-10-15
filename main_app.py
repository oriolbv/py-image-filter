import numpy as np
import cv2

cv2.namedWindow('app')

while True:
    k = cv2.waitKey(1) & 0xFF
    if k == ord('q'):
        break

cv2.destroyAllWindows()