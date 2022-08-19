import serial
import time
# # Serial port parameters
serial_speed = 9600
serial_port = 'COM3'  # bluetooth on Nana BLE

if __name__ == '__main__':  

    print("conecting to serial port ...")
    ser = serial.Serial(serial_port, serial_speed, timeout=1)

    print('\n --------------------------|FIRST|--------------------------')
    print("1-sending message to turn on PIN 13 ...")
    ser.write(b'1')
    print("1-recieving message from arduino ...")
    data = ser.readline()
    if (data != ""):
        print("1-Arduino says: %s" % data)
    else:
        print("1-Arduino doesnt respond")
    print('\n --------------------------|SECOND|--------------------------')
    time.sleep(4)
    print("2-sending message to turn on PIN 13 ...")
    ser.write(0)
    print("2-recieving message from arduino ...")
    data = ser.readline()
    if (data != ""):
        print("2-Arduino says: %s" % data)
    else:
        print("2-Arduino doesnt respond")
    print('\n --------------------------|THIRD|--------------------------')
    time.sleep(4)
    print("3-sending message to turn on PIN 13 ...")
    ser.write(b'0')
    print("3-recieving message from arduino ...")
    data = ser.readline()
    if (data != ""):
        print("3-Arduino says: %s" % data)
    else:
        print("3-Arduino doesnt respond")
    time.sleep(4)
    print("\n 0-finish program and close connection!")
