# a program to practice creating a webserver on my Raspberry Pi that provides output to GPIO pins based on buttons pushed
# output will light up one of 3 LEDs and a buzzer
# basically just a toy to help me create a project utilizing the skills that I have enjoyed learning to this point (November, 2017)

from flask import Flask, render_template, url_for, redirect
import RPi.GPIO as GPIO
import time

app = Flask(__name__)


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# pin locations on breadboard according to BCM numbering
red = 17
yellow = 18
green = 27
buzz = 22

GPIO.setup(17, GPIO.OUT)
GPIO.output(17, GPIO.LOW)

GPIO.setup(18, GPIO.OUT)
GPIO.output(18, GPIO.LOW)

GPIO.setup(27, GPIO.OUT)
GPIO.output(27, GPIO.LOW)

GPIO.setup(22, GPIO.OUT)
GPIO.output(22, GPIO.HIGH)

# todo below..... clean up code

#pins = [red, yellow, green, buzz]

# buzzer runs when GPIO is low, so set to high as defualt, set red to high as defualt for testing, change when funcitoning
#for pin in pins:
    #if pin == 2 or pin == 3:
        #GPIO.setup(pins[pin - 1], GPIO.OUT)
        #GPIO.output(pins[pin - 1], GPIO.LOW)
    #else:
        #GPIO.setup(pins[pin - 1], GPIO.OUT)
        #GPIO.output(pins[pin - 1], GPIO.HIGH)

# define functions to execute when button is pressed, and clearing when done

def main():

    @app.route("/redLed/", methods=['POST'])
    def redLed():
        GPIO.output(red, GPIO.HIGH)
        time.sleep(5)
        GPIO.output(red, GPIO.LOW)
        return render_template("index.html")

    @app.route("/yellowLed/", methods=['POST'])
    def yellowLed():
        GPIO.output(yellow, GPIO.HIGH)
        time.sleep(5)
        GPIO.output(yellow, GPIO.LOW)
        return redirect(url_for("index"))

    @app.route("/greenLed/", methods=['POST'])
    def greenLed():
        GPIO.output(green, GPIO.HIGH)
        time.sleep(5)
        GPIO.output(green, GPIO.LOW)
        return render_template("index.html")

    @app.route("/buz/", methods=['POST'])
    def buz():
        GPIO.output(buzz, GPIO.LOW)
        time.sleep(1)
        GPIO.output(buzz, GPIO.HIGH)
        return render_template("index.html")

    # this is what will show up on the index page
    @app.route("/", methods=['GET', 'POST'])
    def index():
        return render_template("index.html")


# setup pi as webserver
if __name__ == "__main__":
    main()
    app.run(host='0.0.0.0', port=80, debug=True)

