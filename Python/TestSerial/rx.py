import serial
import time

port = serial.Serial("/dev/ttyAMA0", baudrate=9600, timeout=1.0)

while True:
	data = port.readline()
	if data:
		print ("\nreceived:\n"+data[:-1])
	time.sleep(0.1)


