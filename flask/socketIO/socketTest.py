from flask import Flask, render_template, jsonify, send_from_directory
from flask.ext.socketio import SocketIO, emit
from threading import Thread
from time import sleep
import serial

app = Flask(__name__)
app.debug = True
app.config['SECRET_KEY'] = 'imaginario'
socketio = SocketIO(app)

port = serial.Serial("/dev/ttyAMA0", baudrate=4800, timeout=1.0)

def checkSerial():
	while True:
		try:
			data = port.readline()
			if data:
				socketio.emit('my response', {'data':data}, namespace='/imin')
				sleep(0.3)
       			sleep(0.1)
		except UnicodeDecodeError:
			print "uni error"
		except Exception e:
			print "exception"

@app.route('/')
def index():
    	return render_template('index.html')

@app.route('/scripts/<path:filename>')
def serve_js(filename):
	return send_from_directory('./scripts', filename)

@socketio.on('connect', namespace='/imin')
def test_connect():
	print "whooo"
	emit('my response', {'data': 'Connected'})

if __name__ == "__main__":
	t1 = Thread(target=checkSerial)
	t1.start()
	socketio.run(app,"0.0.0.0",5555)
