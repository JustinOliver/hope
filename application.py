''' A simple program to practice some skills I have learned including Python, html, flask, css and Raspberry Pi GPIO.
Create a webpage with buttons, wire up some GPIO pins for the Pi to a breadboard, connect the pins to 3 LEDs and a buzzer,
write some Python to interact with the pins, and host the page on a webserver on the Pi.
Pushing the buttons on the page activates the lights or buzzer for 5 seconds. Can easily be modified to output signals to
anything you want.
Basically just a toy to help me create a project utilizing the skills that I have enjoyed learning to this point (November, 2017)
'''
from flask import Flask, render_template, redirect, url_for
import RPi.GPIO as GPIO
import time

app = Flask(__name__)

# Set GPIO to use BCM numbering.
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Pin locations on breadboard according to BCM numbering
red = 17
yellow = 18
green = 27
buzz = 22

'''GPIO.setup(17, GPIO.OUT)
GPIO.output(17, GPIO.LOW)

GPIO.setup(18, GPIO.OUT)
GPIO.output(18, GPIO.LOW)

GPIO.setup(27, GPIO.OUT)
GPIO.output(27, GPIO.LOW)

GPIO.setup(22, GPIO.OUT)
GPIO.output(22, GPIO.HIGH)
'''
pins = [red, yellow, green, buzz]

# Buzzer runs when GPIO is low, so set to high (off) as defualt. Set all
for i in range(len(pins)):
    if pins[i] == buzz:
        GPIO.setup(pins[i], GPIO.OUT)
        GPIO.output(pins[i], GPIO.LOW)
    else:
        GPIO.setup(pins[i], GPIO.OUT)
        GPIO.output(pins[i], GPIO.HIGH)

def ledLight(color):
    GPIO.output(color, GPIO.HIGH)
    time.sleep(5)
    GPIO.output(color, GPIO.LOW)
    return redirect(url_for("index"))

# Define functions to execute when button is pressed.
def main():

    @app.route("/redLed/", methods=['POST'])
    def redLed():
        ledLight(red)

    @app.route("/yellowLed/", methods=['POST'])
    def yellowLed():
        ledLight(yellow)

    @app.route("/greenLed/", methods=['POST'])
    def greenLed():
        ledLight(green)

    @app.route("/buz/", methods=['POST'])
    def buz():
        GPIO.output(buzz, GPIO.LOW)
        time.sleep(1)
        GPIO.output(buzz, GPIO.HIGH)
        return redirect(url_for("index"))

    # this is what will show up on the index page
    @app.route("/")
    def index():
        return render_template("index.html")


# Setup Pi as webserver
if __name__ == "__main__":
    main()
    app.run(host='0.0.0.0', port=80, debug=True)

