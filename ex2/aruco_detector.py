### マーカーの座標を抽出する
import cv2
from cv2 import aruco
import numpy as np
import time


class MarkSearch() :
    ### --- aruco設定 --- ###
    dict_aruco = aruco.Dictionary_get(aruco.DICT_4X4_50)
    parameters = aruco.DetectorParameters_create()

    def __init__(self, cameraID):
        self.cap = cv2.VideoCapture(cameraID)
        self.cap_width = self.cap.get(cv2.CAP_PROP_FRAME_WIDTH)
        self.cap_height = self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT)

    def get_mark_coordinate(self, num_id):
        ### 静止画を取得し、所望のマークの座標を取得する ###
        ret, frame = self.cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)

        corners, ids, rejectedImgPoints = aruco.detectMarkers(gray, self.dict_aruco, parameters=self.parameters)

        ### num_id のマーカーが検出された場合 ###
        if num_id in np.ravel(ids) :
            index = np.where(ids == num_id)[0][0] #num_id が格納されているindexを抽出
            cornerUL = corners[index][0][0]
            cornerUR = corners[index][0][1]
            cornerBR = corners[index][0][2]
            cornerBL = corners[index][0][3]
            center = [(cornerUL[0]+cornerBR[0])/2 , (cornerUL[1]+cornerBR[1])/2]
            # print('左上 : {}'.format(cornerUL))
            # print('右上 : {}'.format(cornerUR))
            # print('右下 : {}'.format(cornerBR))
            # print('左下 : {}'.format(cornerBL))
            # print('中心 : {}'.format(center))
            return center

        return None


if __name__ == "__main__" :
    # ### --- aruco設定 --- ###
    # dict_aruco = aruco.Dictionary_get(aruco.DICT_4X4_50)
    # parameters = aruco.DetectorParameters_create()

    ### --- parameter --- ###
    cameraID = 0
    cam0_mark_search = MarkSearch(cameraID)
    markID = 0

    try:
        while True:
            center = cam0_mark_search.get_mark_coordinate(markID)
            if center is not None:
                print(center)
            # print(' ----- get_mark_coordinate ----- ')
            # print(cam0_mark_search.get_mark_coordinate(markID))
            # time.sleep(0.5)
    except KeyboardInterrupt:
        cam0_mark_search.cap.release()
