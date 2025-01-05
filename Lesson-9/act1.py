import cv2
import numpy as np
import matplotlib.pyplot as plt

def display(title, image):
    plt.figure(figsize=(8, 8))
    if len(image.shape) == 2:
        plt.imshow(image, cmap='gray')
    else:
        plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.title(title)
    plt.axis('off')
    plt.show()

def interactive_edge_detection(image_path):
    image = cv2.imread(image_path)
    if image == None:
        print('Error: Image not found')
        return
    gray_image = plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2GRAY))
    display("Original Grayscale Image", gray_image)

    print('Select an option')
    print('1. Sobel Edge Detection')
    print('2. Canny Edge Detection')
    print('3. Laplacian Edge Detection')
    print('4. Gaussion Smoothing')
    print('5. Median Filtering')
    print('6. Exit')
    
    while True:
        choice = input('Enter your choice (1-6):')
        if choice == '1':
            sobelx = cv2.Sobel(gray_image, cv2.CV_64F, 1, 0, ksize=3)
            sobely = cv2.Sobel(gray_image, cv2.CV_64F, 0, 1, ksize=3)
            result = cv2.bitwise_or(sobelx.astype(np.uint8), sobely.astype(np.uint8))
            display('Sobel Edge Detection', result)
        elif choice == '2':
            print('Adjust thresholds for Canny (Default: 100, 200)')
            lower_thresh = int(input('Enter lower threshold: '))
            upper_thresh = int(input('Enter upper threshold: '))
            result = cv2.Canny(gray_image, lower_thresh, upper_thresh)
            display('Canny Edge Detection', result)
        elif choice == '3':
            result = cv2.Laplacian(gray_image, cv2.CV_64F)
            display('Laplacion Edge detection', np.abs(result).astype(np.uint8))
        elif choice == '4':
            print('Adjust kernel size for Gaussian Blur (must be odd, Default: 5)')
            kernel_size = int(input('Enter kernel size: '))
            result = cv2.gaussianBlur(image, kernel_size)
            display('Gaussian Smoothed Image', result)
        elif choice == '5':
            print('Adjust kernel size for Median Filtering (must be odd, Default: 5)')
            kernel_size = int(input('Enter kernel size: '))
            result = cv2.medianBlur(image, kernel_size)
            display('Median Filtered Image', result)
        elif choice == '6':
            print('Exiting...')
            break
        else:
            print('Invalid choice. Please enter a number between 1 and 6.')

interactive_edge_detection('Lesson-7//tomato.jpg')