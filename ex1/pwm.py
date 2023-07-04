import RPi.GPIO as GPIO
from time import sleep


class PWM():
    def __init__(self):
        self.p1 = 17
        self.p2 = 27
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.p1, GPIO.OUT)
        GPIO.setup(self.p2, GPIO.OUT)
        self.p1 = GPIO.PWM(self.p1, 50) #50Hz
        self.p2 = GPIO.PWM(self.p2, 50) #50Hz
        self.p1.start(0)
        self.p2.start(0)

    def straight(self, duty):
        self.p1.ChangeDutyCycle(duty)
        self.p2.ChangeDutyCycle(0)
        print(f"Straight, {duty}")

    def back(self, duty):
        self.p1.ChangeDutyCycle(0)
        self.p2.ChangeDutyCycle(duty)
        print(f"Back, {duty}")

    def stop(self):
        self.p1.ChangeDutyCycle(0)
        self.p2.ChangeDutyCycle(0)
        print(f"Stop")

    def __del__(self):
        GPIO.cleanup()


if __name__ == "__main__":
    duty = 80
    while True:
        pwm = PWM()
        pwm.straight(duty)
        print("straight")
        sleep(5)
        pwm.back(duty)
        print("back")
        sleep(5)
        pwm.stop()
        print("stop")
        sleep(5)

