import RPi.GPIO as GPIO
from time import sleep


class Motor():
    def __init__(self):
        self.p1 = 17
        self.p2 = 27
        self.p3 = 22
        self.p4 = 23
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.p1, GPIO.OUT)
        GPIO.setup(self.p2, GPIO.OUT)
        GPIO.setup(self.p3, GPIO.OUT)
        GPIO.setup(self.p4, GPIO.OUT)

    def straight(self):
        GPIO.output(self.p1, 1)
        GPIO.output(self.p2, 0)
        GPIO.output(self.p3, 1)
        GPIO.output(self.p4, 0)
        print("Straight")

    def back(self):
        GPIO.output(self.p1, 0)
        GPIO.output(self.p2, 1)
        GPIO.output(self.p3, 0)
        GPIO.output(self.p4, 1)
        print("Back")

    def stop(self):
        GPIO.output(self.p1, 0)
        GPIO.output(self.p2, 0)
        GPIO.output(self.p3, 0)
        GPIO.output(self.p4, 0)
        print("Stop")

    def __del__(self):
        GPIO.cleanup()


if __name__ == "__main__":
    duty = 80
    motor = Motor()
    while True:
        motor.straight()
        sleep(5)
        motor.stop()
        sleep(1)
        motor.back()
        sleep(5)
        motor.stop()
        sleep(1)

