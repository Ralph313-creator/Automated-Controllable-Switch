import random
import time
from thing import PiThing

from flask import *

# Create flask app and pi Thing
app = Flask(__name__)
pi_thing = PiThing()

@app.route('/homejiajsoij980906634gffddad21112')
def home():

 
   return render_template('homejiajsoij980906634gffddad21112.html')



@app.route('/', methods=['GET', 'POST'])
def index():
	error = None
	if request.method == 'POST':
		if request.form['password'] != 'admin':
			error ='Invalid crendentials. Please try again'
		else:
			return redirect(url_for('home')) 
	return render_template('index.html', error=error)
 

@app.route('/relay/<int:relay_state>',methods=['POST'])
def relay(relay_state):
	if relay_state == 0:
		pi_thing.set_relay1(True)
	elif relay_state == 1:
		pi_thing.set_relay1(False)
	elif relay_state == 2:
		pi_thing.set_relay2(True)
	elif relay_state == 3:
		pi_thing.set_relay2(False)
	elif relay_state == 4:
		pi_thing.set_relay3(True)
	elif relay_state == 5:
		pi_thing.set_relay3(False)
	elif relay_state == 6:
		pi_thing.set_relay4(True)
	elif relay_state == 7:
		pi_thing.set_relay4(False)	
	else:
		return('Unknown Relay state!', 400)
	return('',204)

@app.route('/switch1')
def switch1():
	def get_switch1_values():
		while True:
			switch1 = pi_thing.read_switch1()
			yield('data: {0}\n\n'.format(switch1))
			time.sleep(.5)
	return Response(get_switch1_values(), mimetype='text/event-stream')

@app.route('/switch2')
def switch2():
	def get_switch2_values():
		while True:
			switch2 = pi_thing.read_switch2()
			yield('data: {0}\n\n'.format(switch2))
			time.sleep(.5)
	return Response(get_switch2_values(), mimetype='text/event-stream')

@app.route('/switch3')
def switch3():
	def get_switch3_values():
		while True:
			switch3 = pi_thing.read_switch3()
			yield('data: {0}\n\n'.format(switch3))
			time.sleep(.5)
	return Response(get_switch3_values(), mimetype='text/event-stream')

@app.route('/switch4')
def switch4():
	def get_switch4_values():
		while True:
			switch4 = pi_thing.read_switch4()
			yield('data: {0}\n\n'.format(switch4))
			time.sleep(.5)
	return Response(get_switch4_values(), mimetype='text/event-stream')

if __name__ == "__main__":
	app.run(host='0.0.0.0', debug=True, threaded=True)
