# arduino_LED_user.py

from platform import python_branch
import serial
import time
# Define the serial port and baud rate.
ser = serial.Serial('COM3', 9600)
def led_on_off():
    user_input = input("\n Type on / off / quit : ")
    if user_input =="on":
        print("LED is on...")
        time.sleep(0.1) 
        ser.write(b'H') 
        led_on_off()
    elif user_input =="off":
        print("LED is off...")
        time.sleep(0.1)
        ser.write(b'L')
        s = ser.read(100)
        print(s)
        led_on_off()
    elif user_input =="quit" or user_input == "q":
        print("Program Exiting")
        time.sleep(0.1)
        ser.write(b'L')
        s = ser.readline()
        print(s)
        ser.close()
    else:
        print("Invalid input. Type on / off / quit.")
        led_on_off()
time.sleep(2) # wait for the serial connection to initialize
led_on_off()

# ACTIONS
# 1-print on python_branch
# 2-send to Arduino