# a program to practice creating a webserver on my Raspberry Pi that provides output to GPIO pins based on buttons pushed
# output will light up one of 3 LEDs and a buzzer
# basically just a toy to help me create a project utilizing the skills that I have enjoyed learning to this point (November, 2017)

from flask import Flask, render_template, url_for
import RPi.GPIO as GPIO
import time

app = Flask(__name__)


GPIO.setmode(GPIO.BCM)

# pin locations on breadboard according to BCM numbering
red = 17
yellow = 18
green = 27
buzz = 22

pins = [red, yellow, green, buzz]

# buzzer runs when GPIO is low, so set to high as defualt, set red to high as defualt for testing, change when funcitoning
for pin in pins:
    if pin == 2 or pin == 3:
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, GPIO.LOW)
    else:
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, GPIO.HIGH)

# define functions to execute when button is pressed, and clearing when done

@app.route("/redLed/", methods=['POST'])
def redLed():
    GPIO.output(red, GPIO.HIGH)
    time.sleep(5)
    GPIO.output(red, GPIO.LOW)
    GPIO.cleanup()
    return render_template("index.html")

@app.route("/yellowLed/", methods=['POST'])
def yellowLed():
    GPIO.output(yellow, GPIO.HIGH)
    time.sleep(5)
    GPIO.output(yellow, GPIO.LOW)
    GPIO.cleanup()
    return render_template("index.html")

@app.route("/greenLed/", methods=['POST'])
def greenLed():
    GPIO.output(green, GPIO.HIGH)
    time.sleep(5)
    GPIO.output(green, GPIO.LOW)
    GPIO.cleanup()
    return render_template("index.html")

@app.route("/buz/", methods=['POST'])
def buz():
    GPIO.output(buzz, GPIO.LOW)
    time.sleep(1)
    GPIO.output(buzz, GPIO.HIGH)
    GPIO.cleanup()
    return render_template("index.html")


# this is what will show up on the index page
@app.route("/")
def index():
    return render_template("index.html")


# setup pi as webserver
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)
