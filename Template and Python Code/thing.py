import RPi.GPIO as GPIO

relay1=18
relay2=23
relay3=24
relay4=25


class PiThing(object):
	"""My RPI Internet of 'Thing'."""

	def __init__(self):

	 	GPIO.setmode(GPIO.BCM)
	 	GPIO.setwarnings(False)
	 	GPIO.setup(relay1, GPIO.OUT)
	 	GPIO.setup(relay2, GPIO.OUT)
	 	GPIO.setup(relay3, GPIO.OUT)
	 	GPIO.setup(relay4, GPIO.OUT)

	

	def read_switch1(self):
		""" Read the state of the switch and return it (as a bolean)"""
		return GPIO.input(relay1)
	def read_switch2(self):
		""" Read the state of the switch and return it (as a bolean)"""
		return GPIO.input(relay2)
	def read_switch3(self):
		""" Read the state of the switch and return it (as a bolean)"""
		return GPIO.input(relay3)
	def read_switch4(self):
		""" Read the state of the switch and return it (as a bolean)"""
		return GPIO.input(relay4)



	def set_relay1(self, value):
		"""Change  the LED to the passed in value, either True for on or False for off""" 
		GPIO.output(relay1, value)

	def set_relay2(self, value):
		"""Change  the LED to the passed in value, either True for on or False for off""" 
		GPIO.output(relay2, value)

	def set_relay3(self, value):
		"""Change  the LED to the passed in value, either True for on or False for off""" 
		GPIO.output(relay3, value)	

	def set_relay4(self, value):
		"""Change  the LED to the passed in value, either True for on or False for off""" 
		GPIO.output(relay4, value)	