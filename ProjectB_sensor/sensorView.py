from datetime import datetime
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
import serial
plt.rcParams["figure.figsize"] = (12, 8)
plt.rcParams["figure.autolayout"] = True

print("====================|Successfully_Readig_Arduino_Data|==================0=======")

title1 = "Realtime-Accelemeter And Gryscope-Data-KME-1"
title2 = "Accelometer (deg A)"
title3 = "Activity-Time-Window"
title4 = "Realtime-Gyroscope-Data-SPEED-2"
title5 = "Gyroscometer (deg G)"
x_data, y_data = [], []
x_data1, y1, y2, y3, y4, y5, y6 = [], [], [], [], [], [], []
sizingFont1 = 18
sizingFont2 = 22
n = 30
portName = "COM3"
sensoredData = serial.Serial(portName, 9600, timeout=2)

print("====================|Successfully_Readig_Arduino_Data|==================1=======")
#figure = plt.figure()
figure, ax = plt.subplots()
line1, = plt.plot_date(x_data1, y1, 'b-')
line2, = plt.plot_date(x_data1, y2, 'g-')
frame = 22
# ax.set_xlim(left=0, right=frame)
line3, = plt.plot_date(x_data1, y3, 'r-')
line4, = plt.plot_date(x_data1, y4, 'm-')
line5, = plt.plot_date(x_data1, y5, 'y-')
line6, = plt.plot_date(x_data1, y6, 'k-')


def update2(frame):
    s = sensoredData.readline().decode()
    rows = [float(x) for x in s.split(',')]
    print("=================|sensor1|=========102=========")
    print(s)
    print("=================|sensor2|=========102=========")
    print(rows[0])
    print(rows)
    y1.append(rows[0])
    y2.append(rows[1])
    y3.append(rows[2])
    y4.append(rows[3])
    y5.append(rows[4])
    y6.append(rows[5])
    x_data1.append(datetime.now())
    x = len(x_data1)
    C = x_data1[x-n:x]
    D = y1[x-n:x]
    E = y2[x-n:x]
    F = y3[x-n:x]
    G = y4[x-n:x]
    H = y5[x-n:x]
    I = y6[x-n:x]
    print('Size-All-data-x-', x)
    print('Size-Non-Active', x-n)
    print('Size-Very-Active', n)
    print("=================|SizesX|=========114=========\n")
    print('Size-C-time-', len(C))
    print('Size-D-Data-', len(D))
    print('Size-TIMEin-', x)
    print('Size-E-Data-', len(E))
    print('Size-F-Data-', len(F))
    print("=================|ArraysX|==========118========\n")
    # print('c->',C)
    print('d-b1>', D)
    print('E-g2>', E)
    print('F-r3>', F)
    print('G-r4>', G)
    print('H-r5>', H)
    print('I-r6>', I)
    line1.set_data(C, D)
    line2.set_data(C, E)
    line3.set_data(C, F)
    line4.set_data(C, G)
    line5.set_data(C, H)
    line6.set_data(C, I)
    figure.gca().relim()
    figure.gca().autoscale_view()
    return line6,
animation = FuncAnimation(figure, update2, frames=20, interval=2120, repeat_delay=2120)


plt.xticks(rotation=45, ha='right', fontsize=sizingFont1)
plt.subplots_adjust(bottom=0.30)
plt.suptitle(title1, fontsize=sizingFont2, color='blue',)
plt.ylabel(title2, fontsize=sizingFont1, color='green',)
plt.xlabel(title3, fontsize=sizingFont1, color='purple',)
plt.legend(['Ax', 'Ay', 'Az', 'Ga', 'Gy', 'Gz'], loc='upper left', shadow=True,)
plt.grid(True)
plt.ylim([-2.2, 2.2])
plt.tight_layout()
plt.savefig('SmartHousePage1.png')
plt.show()


from matplotlib.animation import PillowWriter
animation.save("SmartHouseData.gif", dpi=300, writer=PillowWriter(fps=1))