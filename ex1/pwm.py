import RPi.GPIO as GPIO
from time import sleep


class PWM():
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
        self.p1 = GPIO.PWM(self.p1, 50)  # 50Hz
        self.p2 = GPIO.PWM(self.p2, 50)  # 50Hz
        self.p3 = GPIO.PWM(self.p3, 50)  # 50Hz
        self.p4 = GPIO.PWM(self.p4, 50)  # 50Hz
        self.p1.start(0)
        self.p2.start(0)
        self.p3.start(0)
        self.p4.start(0)

    def straight(self, duty):
        self.p1.ChangeDutyCycle(duty)
        self.p2.ChangeDutyCycle(0)
        self.p3.ChangeDutyCycle(duty)
        self.p4.ChangeDutyCycle(0)
        print(f"Straight, {duty}")

    def back(self, duty):
        self.p1.ChangeDutyCycle(0)
        self.p2.ChangeDutyCycle(duty)
        self.p3.ChangeDutyCycle(0)
        self.p4.ChangeDutyCycle(duty)
        print(f"Back, {duty}")

    def stop(self):
        self.p1.ChangeDutyCycle(0)
        self.p2.ChangeDutyCycle(0)
        self.p3.ChangeDutyCycle(0)
        self.p4.ChangeDutyCycle(0)
        print("Stop")

    def turn_left(self, duty):
        self.p1.ChangeDutyCycle(duty)
        self.p2.ChangeDutyCycle(0)
        self.p3.ChangeDutyCycle(0)
        self.p4.ChangeDutyCycle(duty)
        print("Turn Left")

    def turn_right(self, duty):
        self.p1.ChangeDutyCycle(0)
        self.p2.ChangeDutyCycle(duty)
        self.p3.ChangeDutyCycle(duty)
        self.p4.ChangeDutyCycle(0)
        print("Turn Right")

    def __del__(self):
        GPIO.cleanup()


if __name__ == "__main__":
    duty = 80
    pwm = PWM()
    while True:
        pwm.straight(duty)
        sleep(5)
        pwm.stop()
        sleep(1)
        pwm.back(duty)
        sleep(5)
        pwm.searchAR(duty)
        sleep(5)
        pwm.stop()
        sleep(1)
