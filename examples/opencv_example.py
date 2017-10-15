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

# img = cv2.imread('../images/cute_cat.jpg')
# if img is None:
#     print("Image not loaded!")
# else:
#     print("Image is loaded!")
#     print(img.shape)
#
# cv2.imshow('test', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# Colorspace conversion
# img = cv2.imread('../images/cute_cat.jpg')
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#
# cv2.imshow('color', img)
# cv2.imshow('gray', gray)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# Brightness and contrast
# img = cv2.imread('../images/cute_cat.jpg')
#
# # image, contrast(alpha), image same dim, beta, gamma
# cb_img = cv2.addWeighted(img, 4, np.zeros(img.shape, dtype=img.dtype), 0, 100)
#
# cv2.imshow('img', cb_img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# Convolution
img = cv2.imread('../images/cute_cat.jpg')

K = np.array([
    [0,-1,0],
    [-1,5,-1],
    [0,-1,0]
])

convolved = cv2.filter2D(img, -1, K)

cv2.imshow('original', img)
cv2.imshow('convolved', convolved)

cv2.waitKey(0)
cv2.destroyAllWindows()