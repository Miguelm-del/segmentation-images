import cv2 as cv
import numpy as np

imgFlowers = cv.imread("../assets/flores.png", cv.IMREAD_GRAYSCALE)

imgEagle = cv.imread("../assets/Falcao.jpg", cv.IMREAD_GRAYSCALE)


grad_x = cv.Sobel(imgFlowers, -1, 1, 0, ksize=3, scale=1,
                  delta=0, borderType=cv.BORDER_DEFAULT)

grad_y = cv.Sobel(imgFlowers, -1, 0, 1, ksize=3, scale=1,
                  delta=0, borderType=cv.BORDER_DEFAULT)

cv.imshow("Grad X", grad_x)
cv.imshow("Grad Y", grad_y)

cv.imwrite("flowers-x.jpg",grad_x)
cv.imwrite("flowers-y.jpg",grad_y)


grad_x = cv.Sobel(imgEagle, -1, 1, 0, ksize=3, scale=1,
                  delta=0, borderType=cv.BORDER_DEFAULT)

grad_y = cv.Sobel(imgEagle, -1, 0, 1, ksize=3, scale=1,
                  delta=0, borderType=cv.BORDER_DEFAULT)

cv.imshow("Grad X", grad_x)
cv.imshow("Grad Y", grad_y)

cv.imwrite("eagles-x.jpg",grad_x)
cv.imwrite("eagles-y.jpg",grad_y)


cv.waitKey(0)
cv.destroyAllWindows()
