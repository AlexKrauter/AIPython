import cv2
import numpy as np

def apply_filter(image, filter_type):
    filtered_image = image.copy()
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    if filter_type == "red_tint":
        filtered_image[:,:,1] = 0
        filtered_image[:,:,0] = 0
    elif filter_type == 'green_tint':
        filtered_image[:,:,2] = 0
        filtered_image[:,:,0] = 0
    elif filter_type == 'blue_tint':
        filtered_image[:,:,1] = 0
        filtered_image[:,:,2] = 0
    elif filter_type == 'sobel':
        sobelx = cv2.Sobel(gray_image, cv2.CV_64F, 1, 0, ksize=3)
        sobely = cv2.Sobel(gray_image, cv2.CV_64F, 0, 1, ksize=3)
        combined_sobel = cv2.bitwise_or(sobelx.astype('uint8'), sobely.astype('unit8'))
        filtered_image = cv2.cvtColor(combined_sobel, cv2.COLOR_BGR2GRAY)
    elif filter_type == 'canny':
        edges = cv2.Canny(gray_image, 100, 200)
        filtered_image =cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)
    elif filter_type == 'reset':
        filtered_image = imager
    
    return filtered_image

imager = cv2.imread('Lesson-7//tomato.jpg')

if imager is None:
    print('Error: Image not found')
else:
    filter_type = "original"
    print('r - Red Tint')
    print('g - Green Tint')
    print('b - Blue Tint')
    print('s - Sobel Edge Detection')
    print('c - Canny Edge Detection')
    print('o - Reset to Original')
    print('q - Quit')
    key=cv2.waitKey(0) & 0xFF
    keys = 'rgbscoq'.split('')
    filters = 'red greentint blue sobel canny reset'.split(' ')
    for i in range(6):
        if key == ord(keys[i]):
            filter_type = filters[i]
    if key == ord(keys[7]):
        print('Exiting...')

cv2.destroyAllWindows()