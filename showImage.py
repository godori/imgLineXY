import numpy as np
import cv2

def showImage():
    imgfile = 'img/roar.png'
    img = cv2.imread(imgfile, cv2.IMREAD_COLOR)

    cv2.imshow('roar',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

showImage()
