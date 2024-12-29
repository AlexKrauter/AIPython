import cv2
import numpy as np
import matplotlib.pyplot as plt

class image:
    def set(path):
        image = cv2.imread(path)
        global gray_image
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        return gray_image
    
    def filter(result, f_type):
        if f_type == 'original':
            result = cv2.cvtColor(image.COLOR_BGR2RGB)
        elif f_type == 'sobel':
            sobelx = cv2.Sobel(gray_image, cv2.CV_64F, 1, 0, ksize=3)
            sobely = cv2.Sobel(gray_image, cv2.CV_64F, 0, 1, ksize=3)
            result = cv2.bitwise_or(sobelx.astype(np.uint8), sobely.astype(np.uint8))
        elif f_type == 'canny':
            result = cv2.Canny(gray_image, 100, 200)
        return result

tom = image
tom.set('test.jpg')

plt.imshow(tom.filter(tom, 'canny'))