from time import sleep
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
button=4
relay=18
GPIO.setup(button,GPIO.IN)
GPIO.setup(relay,GPIO.OUT)
button_state=False
while True:
	if GPIO.input(button)==0:
		print "Button was Pressed"
		if button_state==False:
			GPIO.output(LED1, True)
			button_state=True
			sleep(.5)
		else:
			GPIO.output(relay,False)		
			button_state=False
			sleep(.5)
