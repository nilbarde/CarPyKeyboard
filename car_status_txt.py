
import sys
import serial

import time

ser = serial.Serial('/dev/ttyACM1',115200,timeout=1)

v = 0
s = 0
a = 0
b = 0

while(True):
	read = ser.readline()
	string_status = read #.split(',')#ser.read(4)
	# print(string_status)
	try:
		if(string_status[0] == "v"):
			v = 100*int(string_status[1])+10*int(string_status[2])+int(string_status[3]) - 100
		elif(string_status[0] == "s"):
			if(string_status[3] == "1"):
				s = (10*int(string_status[1])+int(string_status[2]))
			elif(string_status[3] == "0"):
				s = (10*int(string_status[1])+int(string_status[2]))*(-1)
		elif(string_status[0] == "a"):
			a = 100*int(string_status[1])+10*int(string_status[2])+int(string_status[3]) - 100
		elif(string_status[0] == "b"):
			b = 100*int(string_status[1])+10*int(string_status[2])+int(string_status[3]) - 100	
	except:
		print("000000")

	file = open("can_output.txt",'w') 
	file.write(str(v)+"\n")
	file.write(str(s)+"\n")
	file.write(str(a)+"\n")
	file.write(str(b)+"\n")
	print v
	print s
	print a
	print b
	file.close()
