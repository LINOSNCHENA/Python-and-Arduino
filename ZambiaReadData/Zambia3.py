import serial
import csv
from time import time
import json
import os
from supabase import create_client, Client
from dotenv import load_dotenv
load_dotenv()
import time as t 

ser = serial.Serial('COM3', 9600)
if not ser.isOpen():
    ser.open()
url: str = os.environ.get("VITE_SUPABASE_URL")
key: str = os.environ.get("VITE_SUPABASE_ANON_KEY")
supabase: Client = create_client(url, key)

supabase: Client = create_client(url, key)


while True:
    s = ser.readline().decode()
    print("=============================1====")
    print(s)
    # convert into JSON:
    y = json.dumps(s)
# the result is a JSON string:
    print(y)
    
    data = supabase.table("audz").select("*").execute()
    print((data))
# Assert we pulled real data.
    assert len(data.data) > 0
    print("==============================2===")
    if s != "":
        # rows = [float(x[0]) for x in s.split(',')]
        x = s[0:4]
        y = s[5:10]
        z = s[11:14]
        print('First 4 character : ', x)
        print('First 4 character : ', y)
        print('First 4 character : ', z)
    data = supabase.table("audz").insert(
        {"namex": x, "namey": y, "namez": z}).execute()
    assert len(data.data) > 0
    print(data)
    t.sleep(5)  
    print("=============================3====")
