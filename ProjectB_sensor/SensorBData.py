import matplotlib.pyplot as plt
from time import time
import pandas as pd
import seaborn
import serial
import csv

fileName1 = "_IMU_One_Spaced.csv"
fileName2 = "_IMU_ZeroSpaced.csv"

portName = "COM3"
f = open(fileName1, "a+")
writer = csv.writer(f, delimiter=',')
sensoredData = serial.Serial(portName, 9600, timeout=2)

i = 1
while i <= 10:
    s = sensoredData.readline().decode()
    if s != "":
        print(i, 's=>', s)
        rows = [float(x) for x in s.split(',')]
        rows.insert(0, 'IMU')
        rows.insert(0, int(time()))
        rows.insert(0, i)
        print(rows)
        writer.writerow(rows)
        f.flush()
    i += 1

"""
Print summary of Collected data
"""
print("====================|Successfully_Readig_Arduino_Data|==================1=======")
print(rows)

data = pd.read_csv(fileName1, delimiter=',')
titles = ['Index1', 'Times', 'IMU_Task3',
          'ax1', 'ay2', 'az3', 'gx4', 'gy5', 'gz6']
data.columns = titles
data.to_csv(str(int(time()))+fileName1, index=True)
data.to_csv(str(int(time()))+fileName2, index=True)
print(data)
print(data.shape)
print("======================|Successfully_Added_Data_Heading|=================2=======")

data.to_csv(fileName2, index=False)
print(data.describe())
# loading dataset using seaborn

print("======================|Successfully_Added_Data_Seaborn|=================3======")
df = seaborn.load_dataset('tips')
print(df.head(3))
print(data.head(3))

# pairplot with hue sex
seaborn.pairplot(df, hue='size')
# plt.show()

print("====================|Successfully_Ploting_Collected_Data|===============4=====")
