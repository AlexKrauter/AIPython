import cv2
image = cv2.imread('Lesson-7//tomato.jpg')
gray_image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
cv2.namedWindow('Loaded Image', cv2.WINDOW_NORMAL)
cv2.resizeWindow('Loaded Image', 800, 500)

cv2.imshow('Loaded Image', gray_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
