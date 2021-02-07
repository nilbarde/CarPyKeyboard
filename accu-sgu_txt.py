
import sys
import serial

import time

ser = serial.Serial('/dev/ttyACM1',115200,timeout=1)

while(True):
	file = open("can_input.txt",'r') 
	final_can_ = file.readline()
	print final_can_
	ser.write(final_can_)
