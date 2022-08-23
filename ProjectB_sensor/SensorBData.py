import matplotlib.pyplot as plt
from time import time
import pandas as pd
import seaborn
import serial
import csv
plt.rcParams["figure.figsize"] = [18.50, 5.50]
plt.rcParams["figure.autolayout"] = True

fileName1 = "_IMU_One_Spaced.csv"
fileName2 = "_IMU_ZeroSpaced.csv"
sizingFont = 15
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
datax=data
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
df4 = data.iloc[0:22:, -15:]  # 22-Records, last-15X headers
l = len(df4)
c = len(data.columns)
l2 = len(data)
c2 = len(data.columns)
df4 = df4.round(9)

lablel5 = "Dataset-for-experiments | 800 Records/Eight-Columns"
kalas = ['palegreen', 'orange', 'yellow', 'gray', 'skyblue', 'green', 'palegreen', 'orange', 'yellow', 'gray', 'skyblue', 'green',
         'palegreen', 'orange', 'yellow', 'gray', 'skyblue', 'green']

fig, ax = plt.subplots()
fig.patch.set_visible(False)
ax.axis('off')
ax.axis('tight')
ax1 = ax.table(cellText=df4.values, colLabels=df4.columns,
               loc='center', colColours=kalas, fontsize=sizingFont)
ax1 = ax.table(cellText=df4.values, colLabels=df4.columns,
               loc='center', fontsize=sizingFont)
ax1.auto_set_font_size(False)
ax1.set_fontsize(sizingFont)
plt.suptitle(lablel5)
plt.suptitle('Arduino1_Collected_Python1 | # Headers= '+str(c) + ' / '+str(c2) +
          ': # Records='+str(l)+'/'+str(l2)+'|', fontsize=sizingFont, color='green', fontweight="bold")
# plt.tight_layout()
# plt.axis('tight')
plt.savefig('../uxviews/ProjectA/ProjectAX1.png')
plt.show()
print(data.head(92))
print("====================|Successfully_Ploting_Collected_Data|===============4=====")
df4 = datax.iloc[0:24:, -15:]  # 22-Records, last-15X headers
l = len(df4)
c = len(data.columns)
l2 = len(data)
c2 = len(data.columns)

fig, ax = plt.subplots()
fig.patch.set_visible(False)
ax.axis('off')
ax.axis('tight')
ax1 = ax.table(cellText=df4.values, colLabels=df4.columns,
               loc='center', colColours=kalas, fontsize=sizingFont)
ax1 = ax.table(cellText=df4.values, colLabels=df4.columns,
               loc='center', fontsize=sizingFont)
ax1.auto_set_font_size(False)
ax1.set_fontsize(sizingFont)
plt.suptitle(lablel5)
plt.suptitle('Arduino_Collected_Python2 | # Headers= '+str(c) + ' / '+str(c2) +
          ': # Records='+str(l)+'/'+str(l2)+'|', fontsize=sizingFont, color='green', fontweight="bold")
plt.savefig('../uxviews/ProjectA/ProjectAX2.png')
plt.show()
print(datax.head(92))

print("====================|Successfully_Ploting_Collected_Data|===============4=====")
df4 = datax.iloc[0:211111111114:, -15:]  # 22-Records, last-15X headers
l = len(df4)
c = len(data.columns)
l2 = len(data)
c2 = len(data.columns)

fig, ax = plt.subplots()
fig.patch.set_visible(False)
ax.axis('off')
ax.axis('tight')
ax1 = ax.table(cellText=df4.values, colLabels=df4.columns,
               loc='center', colColours=kalas, fontsize=sizingFont)
ax1 = ax.table(cellText=df4.values, colLabels=df4.columns,
               loc='center', fontsize=sizingFont)
ax1.auto_set_font_size(False)
ax1.set_fontsize(sizingFont)
plt.suptitle(lablel5)
plt.suptitle('Arduino_Collected_Python3 | # Headers= '+str(c) + ' / '+str(c2) +
          ': # Records='+str(l)+'/'+str(l2)+'|', fontsize=sizingFont, color='green', fontweight="bold")
plt.savefig('../uxviews/ProjectA/ProjectAX3.png')
plt.show()
print(datax.head(92))

print("====================|Successfully_Ploting_Collected_Data|===============5=====")

