# Automated-Switch
Controllable Automated Switch Using RPI
Instruction will be added soon or email: rap.ocba@gmail.com

Prerequisites

Everything in this tutorial is the end product of what we've learned so far about the Raspberry Pi and some things we learned with JavaScript and jQuery. If you get stuck anywhere, take a look at these tutorials:

    Headless Raspberry Pi
    Using the RPi.GPIO library to turn on an LED
    Run Apache on your Pi
    Running a Flask App on your Pi
    Run Flask behind Apache
    Simple AJAX with jQuery/JavaScript

Installation

Follow the tutorial here to learn how to run a Flask app behind Apache: https://www.easyprogramming.net/raspberrypi/pi_flask_apache.php

Since we are running RPi.GPIO from a virtual environment, we need to take one extra step after activating venv and install the package:

pip3 install RPi.GPIO

We need to do this because our virtual environment can't access the globally installed RPi.GPIO package
Configurations

The script.js has jQuery that calls the Flask app using simple AJAX calls. They assume that the path for the flask app is /led - if you use another path, change this in the JavaScript to avoid getting 404s on your AJAX calls.

Place the utils/apache-led.conf configuration file in the appropriate Apache/sites-available directory and enable it with with:

sudo a2ensite apache-led.conf

The led.wsgi file should be placed in the same directory as led.py which contains your Flask controllers. If you rename the flask controller, you have edit the wsgi file to reflect the changes.

If everything is set up correctly, the AJAX call will happen with the following url: http://{{ip_addr}}/led?status=on

Only a status of on or off are accepted. Anything else will return a simple error message. Open up the JavaScript console for more info.
Authors

    Nazmus Nasir - Nazm.us - Owner of EasyProgramming.net

