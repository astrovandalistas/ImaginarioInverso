# -*- coding: utf-8 -*-

import serial
import time

# configure the serial connections (the parameters differs on the device you are connecting to)
ser = serial.Serial("/dev/ttyAMA0", baudrate=9600, timeout=1.0)

if (ser.isOpen() == False):
	ser.open()
	print('port open')

outStr ='Imaginario Inverso 0.1 es un laboratorio de creación de tecnologías de redes alternativas.'

ser.flushInput()

for i,c in enumerate(outStr):
	print("send: " + outStr[0:i])
	ser.write((outStr[0:i]+"\n"))
	time.sleep(0.1)
	#inStr = ser.read(ser.inWaiting())

	#print ("inStr =  " + inStr.decode('UTF-8'))
	#print ("outStr = " + outStr)
	#if(inStr.decode('UTF-8') == outStr):
	#	print ("WORKED")
	#else:
	#	print ("failed")
ser.close()
