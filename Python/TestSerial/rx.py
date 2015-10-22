import serial
import time

port = serial.Serial("/dev/ttyAMA0", baudrate=115200, timeout=1.0)

while True:
	data = port.readline()
	if data:
		print ("\nreceived:\n"+data[:-1])
	time.sleep(0.1)

