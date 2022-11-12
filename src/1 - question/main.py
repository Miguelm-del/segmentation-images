import cv2 as cv
import numpy as np

imgCoffee = cv.imread("../assets/cafe.png", cv.IMREAD_GRAYSCALE)
imgEagle = cv.imread("../assets/Falcao.jpg", cv.IMREAD_GRAYSCALE)

ret, thresh1 = cv.threshold(imgCoffee, 100, 255, cv.THRESH_BINARY)
ret, thresh2 = cv.threshold(imgCoffee, 100, 255, cv.THRESH_BINARY_INV)

cv.imshow("Interrese na cor preta - café ", thresh1)
cv.imshow("Interrese na cor branca - café", thresh2)


ret, thresh1 = cv.threshold(imgEagle, 100, 255, cv.THRESH_BINARY)
ret, thresh2 = cv.threshold(imgEagle, 100, 255, cv.THRESH_BINARY_INV)

cv.imshow("Interrese na cor preta - aguia", thresh1)
cv.imshow("Interrese na cor branca - aguia", thresh2)



cv.waitKey(0)
cv.destroyAllWindows()
