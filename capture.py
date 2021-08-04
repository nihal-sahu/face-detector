import cv2, time

video = cv2.VideoCapture(0)

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

a = 1
while True:
    a += 1
    check, frame = video.read()

    print(check)
    print(frame)

    faces = face_cascade.detectMultiScale(frame, 
    scaleFactor = 1.1,
    minNeighbors = 5)

    for x, y, w, h in faces:
        frame = cv2.rectangle(frame, (x,y), (x + w, y + h), (0, 255, 0))

    cv2.imshow("Capturing", frame)

    key = cv2.waitKey(1)

    if key == ord('q'):
        break

print(a)
video.release()
cv2.destroyAllWindows()