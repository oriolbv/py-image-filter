import numpy as np
import cv2

def dummy(val):
    pass

identity_kernel = np.array([[0,0,0],[0,1,0],[0,0,0]])
sharpen_kernel = np.array([[0,-1,0],[-1,5,-1],[0,-1,0]])
# gaussian_kernel = np.array([[1,2,1],[2,4,2],[1,2,1]], np.float32) / 16
gaussian_kernel_1 = cv2.getGaussianKernel(3, 0)
gaussian_kernel_2 = cv2.getGaussianKernel(5, 0)
box_kernel = np.array([[1,1,1],[1,1,1],[1,1,1]], np.float32) / 9

kernels = [identity_kernel, sharpen_kernel, gaussian_kernel_1, gaussian_kernel_2, box_kernel]

color_original = cv2.imread('./images/cute_cat.jpg')
color_original = cv2.resize(color_original, (0, 0), fx=0.5, fy=0.5)
color_modified = color_original.copy()

gray_original = cv2.cvtColor(color_original, cv2.COLOR_BGR2GRAY)
gray_modified = gray_original.copy()


cv2.namedWindow('app')
cv2.createTrackbar('contrast', 'app', 1, 100, dummy)
cv2.createTrackbar('brightness', 'app', 50, 100, dummy)
cv2.createTrackbar('filter', 'app', 0, len(kernels)-1, dummy)
cv2.createTrackbar('grayscale', 'app', 0, 1, dummy)

while True:
    grayscale = cv2.getTrackbarPos('grayscale', 'app')
    if grayscale == 0:
        cv2.imshow('app', color_modified)
    else:
        cv2.imshow('app', gray_modified)

    cv2.imshow('app', color_modified)
    k = cv2.waitKey(1) & 0xFF
    if k == ord('q'):
        break

    contrast = cv2.getTrackbarPos('contrast', 'app')
    brightness = cv2.getTrackbarPos('brightness', 'app')
    kernel = cv2.getTrackbarPos('filter', 'app')


    color_modified = cv2.filter2D(color_original, -1, kernels[kernel])
    gray_modified = cv2.filter2D(gray_original, -1, kernels[kernel])

    color_modified = cv2.addWeighted(color_modified, contrast, np.zeros(color_original.shape, dtype=color_original.dtype), 0, brightness-50)
    gray_modified = cv2.addWeighted(gray_modified, contrast, np.zeros(gray_original.shape, dtype=gray_original.dtype), 0, brightness-50)

cv2.destroyAllWindows()