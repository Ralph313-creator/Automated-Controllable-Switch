# Automated-Switch
Controllable Automated Switch Using RPI
Instruction will be added soon or email: rap.ocba@gmail.com

Prerequisites

Everything in this tutorial is the end product of what we've learned so far about the Raspberry Pi and some things we learned with JavaScript and jQuery. If you get stuck anywhere, take a look at these tutorials:

    Headless Raspberry Pi
    https://www.easyprogramming.net/raspberrypi/headless_raspbery_pi.php
    
    Using the RPi.GPIO library to turn on an LED
    https://github.com/Ralph313-creator/Automated-Switch/blob/master/test.py
    
    Running a Flask App on your Pi
    https://www.easyprogramming.net/raspberrypi/pi_flask_app_server.php
    
Installation

Since we are running RPi.GPIO from a virtual environment, we need to take one extra step after activating venv and install the package:

pip3 install RPi.GPIO

We need to do this because our virtual environment can't access the globally installed RPi.GPIO package
Configurations


Only a status of on or off are accepted. Anything else will return a simple error message. Open up the JavaScript console for more info.
Authors

    Ralph Ocba 

