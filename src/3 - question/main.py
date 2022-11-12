#3 - Selecione duas imagens em anexo e aplique a função Canny, com diferentes parâmetros (pelo menos 2 mudanças), salve as imagens resultantes.

import cv2 as cv
import numpy as np


imgEagle = cv.imread("../assets/Falcao.jpg",cv.IMREAD_GRAYSCALE)

imgCoffee = cv.imread("../assets/cafe.png",cv.IMREAD_GRAYSCALE)

eagleCanny = cv.Canny(imgEagle,1,1,1,3)
coffeeCanny = cv.Canny(imgCoffee,1,1,1,3)

cv.imshow("Eagle Canny",eagleCanny)
cv.imshow("Canny",coffeeCanny)

cv.waitKey(0)
cv.destroyAllWindows()
