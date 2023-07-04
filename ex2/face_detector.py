import cv2
import os

CASCADE_PATH = os.path.join(cv2.data.haarcascades, "haarcascade_frontalface_default.xml")
# CASCADE_PATH = "cascade/haarcascade_frontalface_alt.xml"

cap = cv2.VideoCapture(0)

cascade = cv2.CascadeClassifier(CASCADE_PATH)

while True:
    ret, img = cap.read()
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = cascade.detectMultiScale(img_gray, minSize=(100, 100))

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 255, 0), thickness=3)

    cv2.imshow("Camera", img)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        # cv2.imwrite("test.png", img)
        break

cap.release()
cv2.destroyAllWindows()
