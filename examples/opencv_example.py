import numpy as np
import cv2

# Part 1
# a = np.array([
#     [1, 1, 2],
#     [3, 5, 8]
# ])

# b = np.array([
#     [2, 3, 5],
#     [3, 11, 13]
# ])

# print(a + b)

# print(a - b)

# Part 2

img = cv2.imread('../images/cute_cat.jpg')
if img is None:
    print("Image not loaded!")
else:
    print("Image is loaded!")
    print(img.shape)

cv2.imshow('test', img)
cv2.waitKey(0)
cv2.destroyAllWindows()