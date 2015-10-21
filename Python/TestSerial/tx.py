# -*- coding: utf-8 -*-

import serial
import time

# configure the serial connections (the parameters differs on the device you are connecting to)
ser = serial.Serial("/dev/ttyAMA0", baudrate=115200, timeout=1.0)

if (ser.isOpen() == False):
	ser.open()
	print('port open')

outStr ='Imaginario Inverso 0.1 es un laboratorio de creación de tecnologías de redes alternativas.'

ser.flushInput()

while(True):
	for i,c in enumerate(outStr):
		print("send: " + outStr[0:i])
		ser.write((outStr[0:i]+"\n"))
		time.sleep(0.1)
	time.sleep(0.5)

ser.close()
