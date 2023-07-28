from aruco_detector import MarkSearch
from cv2 import aruco
from pwm import PWM
from servo import Servo
import cv2
import time


def main():
    ### --- aruco設定 --- ###
    dict_aruco = aruco.Dictionary_get(aruco.DICT_4X4_50)
    parameters = aruco.DetectorParameters_create()

    ### --- camera --- ###
    cameraID = 0
    ms = MarkSearch(cameraID)
    markID = 0

    ### --- mortor --- ###
    duty = 80
    pwm = PWM()
    servo = Servo()

    # while True:
    #     if ms.get_mark_coordinate(markID):
    #         break
    _center = [0, 0]

    while True:
        center = ms.get_mark_coordinate(markID)
        if center is not None:
            print(center)
            if center[0] > ms.cap_width / 2 + 100:
                servo.servo_ctrl(3)
                print("Move right")
            elif center[0] < ms.cap_width / 2 - 100:
                servo.servo_ctrl(-3)
                print("Move left")
            else:
                servo.servo_ctrl(0)
                print("Move center")
            pwm.straight(duty)
            time.sleep(0.5)
            _center = center

        else:
            # pwm.stop()
            # servo.servo_ctrl(0)
            if _center[0] < ms.cap_width:
                servo.servo_ctrl(9)
                pwm.turn_right(80)
                time.sleep(0.3)
                pwm.stop()
                time.sleep(1)
            else:
                servo.servo_ctrl(-9)
                pwm.turn_left(80)
                time.sleep(0.3)
                pwm.stop()
                time.sleep(1)
            print("Search AR mark...")

        if cv2.waitKey(1) & 0xFF == ord('q'):
            del pwm
            del servo
            GPIO.cleanup()
            break


if __name__ == "__main__":
    main()
