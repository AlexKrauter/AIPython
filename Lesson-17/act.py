import cv2, time
import mediapipe as mp
import numpy as np

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(min_detection_confidence=0.7,min_tracking_confidence=0.7)
mp_draw = mp.solutions.drawing_utils

filters = [
    None,
    'GRAYSCALE',
    'SEPIA',
    'NEGATIVE',
    'BLUR'
]
filter_selector = 0
cap = cv2.VideoCapture(1)
if not cap.isOpened():
    print("Error: Could not access webcam.")
    exit()

last_action_time = 0
debounce_time = 1

def apply_filter(frame, filter_type):
    if filter_type == 'GRAYSCALE':
        return cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    elif filter_type == 'SEPIA':
        sepia_filter = np.array([[0.272, 0.534, 0.131], [0.349, 0.686, 0.168], [0.393, 0.769, 0.189]])
        sepia_frame = cv2.transform(frame, sepia_filter)
        sepia_frame = np.clip(sepia_frame, 0, 255)
        return sepia_frame.astype(np.uint8)
    elif filter_type == 'NEGATIVE':
        return cv2.bitwise_not(frame)
    elif filter_type == 'BLUR':
        return cv2.GaussianBlur(frame, (15, 15), 0)
    return frame

while True:
    success, img = cap.read() 
    if not success: 
        print('Error: Failed to read frame.')
        break 
    img = cv2.flip(img, 1)
    imgrgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(img_rgb)