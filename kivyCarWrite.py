import sys
import serial

import time

ser = serial.Serial('/dev/ttyACM0', 115200, timeout=1)

while(True):
    file = open("kivyCar.txt", 'r')
    final_can_ = file.readline()
    print(final_can_)
    ser.write(final_can_)
