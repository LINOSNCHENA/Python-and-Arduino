import csv
from time import time
import json
import os
from supabase import create_client, Client
from dotenv import load_dotenv
load_dotenv()

import serial

# Your serial port might be different!
#ser = serial.Serial('/dev/cu.usbmodem141301', timeout=1)

ser = serial.Serial('COM3', 9600)
if not ser.isOpen():
    ser.open()

f = open("df.csv", "a+")
writer = csv.writer(f, delimiter=',')




url: str = os.environ.get("VITE_SUPABASE_URL")
key: str = os.environ.get("VITE_SUPABASE_ANON_KEY")
supabase: Client = create_client(url, key)

supabase: Client = create_client(url, key)


while True:
    s = ser.readline().decode()
    print("=============================1====")
    print(s)
    print("=============================2====")
    # convert into JSON:
    y = json.dumps(s)

# the result is a JSON string:
    print(y)
    data = supabase.table("audz").select("*").execute()
# Assert we pulled real data.
    assert len(data.data) > 0
    print("=============================3====")
    print(data)


    print("==============================4===")
    if s != "":
        # rows = [float(x[0]) for x in s.split(',')]
        x = s[0:4]
        y = s[5:10]
        z = s[11:14]
        print('First 4 character : ', x)
        print('First 4 character : ', y)
        print('First 4 character : ', z)
    data = supabase.table("audz").insert({"namex":x,"namey":y,"namez":z}).execute()
    assert len(data.data) > 0
    print(data)
    #     # Insert local time to list's first position
    #     rows.insert(0, int(time()))
    #     print(rows)
    #     writer.writerow(rows)
    #     f.flush()