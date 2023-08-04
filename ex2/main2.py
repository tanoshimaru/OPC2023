import RPi.GPIO as GPIO
from aruco_detector import MarkSearch
from cv2 import aruco
from pwm import PWM
from servo import Servo
import cv2
import time


def main():
    ### --- camera --- ###
    cameraID = 0
    ms = MarkSearch(cameraID)
    markID = 0

    ### --- mortor --- ###
    duty = 80
    pwm = PWM()
    servo = Servo()

    _center = [0, 0]
    x = 0

    while True:
        frame_markers, center = ms.get_mark_coordinate(markID)
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
            t = time.time()
            while time.time() - t < 0.1:
                pass
            _center = center
            x = 0

        else:
            pwm.stop()
            servo.servo_ctrl(0)
            x += 1
            print("Search AR mark...")
            if x > 70:
                if _center[0] > ms.cap_width / 2 + 100:
                    flag = False
                    while True:
                        servo.servo_ctrl(9)
                        pwm.turn_right(100)
                        t = time.time()
                        while time.time() - t < 0.3:
                            pass
                        pwm.stop()
                        t = time.time()
                        while time.time() - t < 0.5:
                            if ms.get_mark_coordinate(markID):
                                flag = True
                                break
                        if flag:
                            break

                else:
                    flag = False
                    while True:
                        servo.servo_ctrl(-9)
                        pwm.turn_left(100)
                        t = time.time()
                        while time.time() - t < 0.3:
                            pass
                        pwm.stop()
                        t = time.time()
                        while time.time() - t < 0.5:
                            if ms.get_mark_coordinate(markID):
                                flag = True
                                break
                        if flag:
                            break

        cv2.imshow('frame', frame_markers)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            del pwm
            del servo
            GPIO.cleanup()
            break


if __name__ == "__main__":
    main()
