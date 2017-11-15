# a program to practice creating a webserver on my Raspberry Pi that provides output to GPIO pins based on buttons pushed
# output will light up one of 3 LEDs and a buzzer
# basically just a toy to help me create a project utilizing the skills that I have enjoyed learning to this point (November, 2017)

from flask import Flask, render_template

app = Flask(__name__)

# this is what will show up on the index page
@app.route("/")
def index():
    return render_template("index.html")
