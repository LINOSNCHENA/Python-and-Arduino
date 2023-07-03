import csv
from time import time
import json

import serial

# Your serial port might be different!
#ser = serial.Serial('/dev/cu.usbmodem141301', timeout=1)

ser = serial.Serial('COM3', 9600)
if not ser.isOpen():
    ser.open()

f = open("df.csv", "a+")
writer = csv.writer(f, delimiter=',')

while True:
    s = ser.readline().decode()
    print("=============================1====")
    print(s)
    print("=============================2====")
    # convert into JSON:
    y = json.dumps(s)

# the result is a JSON string:
    print(y)
    print("==============================3===")
    # if s != "":
    #     rows = [float(x) for x in s.split(',')]
    #     # Insert local time to list's first position
    #     rows.insert(0, int(time()))
    #     print(rows)
    #     writer.writerow(rows)
    #     f.flush()