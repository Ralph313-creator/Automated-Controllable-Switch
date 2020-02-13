from thing import PiThing
import time

#Create an instance of my pi thing
pi_thing = PiThing()

#Get the current state of switch state and print it out
switch = pi_thing.read_switch()
print('Switch: {0}'.format(switch))

#Switch Relay Forever.
"""print("Switching Relay (Ctrl-C to stop)")
while True:
	pi_thing.set_led(True)
	time.sleep(0.5)
	pi_thing.set_led(False)
	time.sleep(0.5)"""