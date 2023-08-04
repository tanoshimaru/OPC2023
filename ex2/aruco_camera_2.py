import cv2
from cv2 import aruco

### --- aruco設定 --- ###
dict_aruco = aruco.getPredefinedDictionary(aruco.DICT_4X4_50)
parameters = aruco.DetectorParameters()

cap = cv2.VideoCapture(0)

name = "aruco.mov"
fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
fps = 30
w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

video = cv2.VideoWriter(name, fourcc, fps, (w, h))

try:
    while True:
        ret, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)

        corners, ids, rejectedImgPoints = aruco.detectMarkers(gray, dict_aruco, parameters=parameters)

        frame_markers = aruco.drawDetectedMarkers(frame.copy(), corners, ids)
        cv2.imshow('frame', frame_markers)
        video.write(frame_markers)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            cv2.destroyWindow('frame')
            video.release()
            cap.release()
            break
except KeyboardInterrupt:
    cv2.destroyWindow('frame')
    video.release()
    cap.release()
