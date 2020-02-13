import RPi.GPIO as GPIO 
from time import sleep 
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
 
while True:
     GPIO.output(18, GPIO.HIGH) 
     sleep(1) 
     GPIO.output(18, GPIO.LOW) 
     sleep(1)
