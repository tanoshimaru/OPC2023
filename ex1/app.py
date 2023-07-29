from flask import Flask, render_template, request, send_from_directory
import json
import RPi.GPIO as GPIO
import time
import servo
import pwm


app = Flask(__name__)
Servo = servo.Servo()
Motor = pwm.PWM()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/control", methods=["POST"])
def control():
    jsonData = request.get_json()
    direction = jsonData.get("directionValue")
    speed = int(jsonData.get("speedValue"))
    angle = int(jsonData.get("angleValue"))
    print(direction, speed, angle)

    if direction == "Straight":
        # ここにモータ・方向の命令を追加
        Motor.straight(speed)
        Servo.servo_ctrl(angle)

    elif direction == "Back":
        # ここにモータ・方向の命令を追加
        Motor.back(speed)
        Servo.servo_ctrl(angle)

    elif direction == "Stop":
        # ここにモータの命令を追加
        Motor.stop()
        Servo.servo_ctrl(angle)

    elif direction == "Turn_Left":
        Motor.turn_left(speed)
        Servo.servo_ctrl(-9)

    elif direction == "Turn_Right":
        Motor.turn_right(speed)
        Servo.servo_ctrl(9)

    return "OK"


if __name__ == "__main__":
    try:
        # app.run(debug=True, host = "0.0.0.0", port=8000)
        app.run(debug=False, host="0.0.0.0", port=8000)
    except Exception as e:
        print(e)
        del Servo
        del Motor
