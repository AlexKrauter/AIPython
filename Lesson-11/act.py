import cv2

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0)

errors = ['Could not open camera','Failed to capture image']
if not cap.isOpened():
    print('Error: ' + errors[0])
    exit()

while True:

    ret, frame = cap.read()

    if not ret:
        print('Error: ' + errors[1])
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y+ h), ((255, 0, 0), 2))
    
    cv2.imshow('Face Detection - Press q to quit', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()