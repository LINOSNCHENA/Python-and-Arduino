# Script to Remove unrelated columns!
from matplotlib import pyplot as plt
import pandas as pd

print('=============|Parameters_And_Headers|=================[1]===========')

sizingFont = 15
decimalsX = 5
plt.rcParams["figure.figsize"] = [18.50, 5.50]
plt.rcParams["figure.autolayout"] = True

lablel1 = "Data1-64 ADLs - BEFORE PROCESSING"
lablel2 = "Data2-16 FALLS - BEFORE PROCESSING"

lablel3 = "Data1-ALL-EVENTS - BEFORE PROCESSING"
lablel4 = "Data2-ALL-EVENTS - BEFORE PROCESSING"

lablel5 = "Data3-Ysis1All1.csv - AFTER-DATA-MINING"
lablel6 = "Data4-Ysis1All2.csv - AFTER-DATA-MINING"

kalas = ['palegreen', 'orange', 'yellow', 'gray', 'skyblue', 'green', 'palegreen', 'orange', 'yellow', 'gray', 'skyblue', 'green',
         'palegreen', 'orange', 'yellow', 'gray', 'skyblue', 'green', 'palegreen', 'orange', 'yellow', 'gray', 'skyblue', 'green']
# read_csv function which is used to read the required CSV file
data1 = pd.read_csv('dataInput/sisfall_64ADLs.csv')
data2 = pd.read_csv('dataInput/sisfall_16FALLS.csv')

data3 = pd.read_csv('dataInput/Ysis1All1.csv', index_col=1)
data4 = pd.read_csv('dataInput/Ysis1All2.csv', index_col=1)

print('data1.shape = ', data1.shape)
print('data2.shape = ', data2.shape)
print('data3.shape = ', data3.shape)
print('data4.shape = ', data4.shape)

print('================|Plot_One_ADLs|=======================[2]===========')

df4 = data1.iloc[0:21:, -15:]  # 22-Records, last-15X headers
l = len(df4)
c = len(df4.columns)
l2 = len(data1)
c2 = len(data1.columns)
df4 = df4.round(decimalsX)

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
plt.suptitle(lablel1)
plt.title('DATASET_1_SISFALL_ADLs_Arduino1 | # Headers= '+str(c) + ' / '+str(c2) +
          ': # Records='+str(l)+'/'+str(l2)+'|', fontsize=sizingFont, color='green', fontweight="bold")
plt.tight_layout()
plt.savefig('../UXviews/TABLES/TA1.png')
plt.show()
print(data1.head(3))

print('==============|Plot_Two_FALLs|========================[3]===========')

df4 = data2.iloc[0:22:, -15:]  # 22-Records, last-15X headers
l = len(df4)
c = len(df4.columns)
l2 = len(data2)
c2 = len(data2.columns)
df4 = df4.round(decimalsX)

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
plt.suptitle(lablel2)
plt.title('DATASET_2_SISFALL_FALLS_Arduino2 | # Headers= '+str(c) + ' / '+str(c2) +
          ': # Records='+str(l)+'/'+str(l2)+'|', fontsize=sizingFont, color='green', fontweight="bold")
plt.tight_layout()
plt.savefig('../UXviews/TABLES/TA2.png')
plt.show()
print(data2.head(3))

print('=============|Plot_Three_Ysis1All1.csv|================[4]===========')

df4 = data3.iloc[0:23:, -15:]  # 22-Records, last-15X headers
l = len(df4)
c = len(df4.columns)
l2 = len(data3)
c2 = len(data3.columns)
df4 = df4.round(decimalsX)

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
plt.suptitle(lablel3)
plt.title('DATASET_3_SISFALL_Ysis1All1.csv| # Headers= '+str(c) + ' / '+str(c2) +
          ': # Records='+str(l)+'/'+str(l2)+'|', fontsize=sizingFont, color='green', fontweight="bold")
plt.tight_layout()
plt.savefig('../UXviews/TABLES/TA3.png')
plt.show()
print(data3.head(3))

print('==============|Plot_Four_Ysis1All2.csv|===============[5]===========')
df4 = data4.iloc[0:24:, -15:]  # 22-Records, last-15X headers
l = len(df4)
c = len(df4.columns)
l2 = len(data4)
c2 = len(data4.columns)
df4 = df4.round(decimalsX)

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
plt.suptitle(lablel4)
plt.title('DATASET_4_SISFALL_Ysis1All2.csv | # Headers= '+str(c) + ' / '+str(c2) +
          ': # Records='+str(l)+'/'+str(l2)+'|', fontsize=sizingFont, color='green', fontweight="bold")
plt.tight_layout()
plt.savefig('../UXviews/TABLES/TA4.png')
plt.show()
print(data4.head(3))

print("==========|PART_ONE_SUCCESSFULLY_CONCLUDED|=============[6]===========")
# pop function which is used in removing or deleting columns
data1.pop('Sisfall_Label_X4')
data1.pop('Azimuth')
data1.pop('Pitch')
data1.pop('Roll')
data2.pop('Sisfall_Label_X4')
data2.pop('Azimuth')
data2.pop('Pitch')
data2.pop('Roll')

# display
print("\nCSV Data after deleting the column 'Roll''\n")
print(data1.shape)
print(data1.head(2))
print("\nCSV Data after deleting the column 'Pitch''\n")
print(data2.shape)
print(data2.head(2))
data1.to_csv('dataInput/eventADLX.csv', index=False)
data2.to_csv('dataInput/eventFALL.csv', index=False)

print("========|REPLACEMENT_of_HEADERS_ON_TABLES|============[7]===========")
data3 = pd.DataFrame(data3)
data4 = pd.DataFrame(data4)
print('data3.shape=', data3.shape)
print('data4.shape=', data4.shape)
data3.columns = ['xlabel1', 'x_1acc', 'y_2acc', 'z_3acc',
                 'x_4gyr', 'y_5grc', 'z_6grc', 'Azimuth', 'xx']
data4.columns = ['xlabel2', 'x_21acc', 'y_22acc', 'z_23acc',
                 'x_24gyr', 'y_25grc', 'z_26grc', 'Azimuth', 'xx']
data4.columns = ['xlabel1', 'x_1acc', 'y_2acc', 'z_3acc',
                 'x_4gyr', 'y_5grc', 'z_6grc', 'Azimuth', 'xx']
print('data3.shape=', data3.shape)
print('data4.shape=', data4.shape)

print("========|RESULTS_REPLACEMENT_of_HEADERS|==============[8]===========")

data3['score'] = data3['xlabel1']
data4['score'] = data4['xlabel1']

data3.pop('xx')
data3.pop('Azimuth')
data3.pop('xlabel1')
data4.pop('xlabel1')
data4.pop('xx')
data4.pop('Azimuth')

print('data3.shape=', data3.shape)
print('data4.shape=', data4.shape)

print("=============|DATA_TWO_SAVE_and_PRINTING|=============[9]==========")

data3.to_csv('dataWatch/SmartFall Testing.csv', index=False)
data4.to_csv('dataWatch/SmartFall Training.csv', index=False)
data3.to_csv('dataWatch/raw91_Testing_Relabeled_Auto_25.csv', index=False)
data4.to_csv('dataWatch/raw182_Training_relabeled_auto_25.csv', index=False)

print(data3.head(3))
print(data4.head(3))
onex = data3.loc[data3['score'] == 1]
oney = data4.loc[data4['score'] == 1]
zerox = data3.loc[data3['score'] == 0]
zeroy = data4.loc[data4['score'] == 0]
print("===============|DATA_3_&_4_STATISTICS|==================X10=========")

print(onex.head(3))
print(oney.head(3))
print(zerox.tail(3))
print(zeroy.tail(3))
y = 6
y1 = pd.DataFrame(onex.head(y))
y2 = pd.DataFrame(oney.head(y))
y3 = pd.DataFrame(zerox.tail(y))
y4 = pd.DataFrame(zeroy.tail(y))
df5 = pd.concat([y1, y3, y2, y4])

print("==========Total===Records====added===========")
print(len(onex)+len(zerox))
print(len(oney)+len(zeroy))

print('data3.shape = ', data3.shape)
print('data4.shape = ', data4.shape)

print('=============|Plot_Five_Processed|====================[13]==========')
df4 = data3.iloc[0:25:, -15:]  # 22-Records, last-15X headers
l = len(df4)
c = len(data3.columns)
l2 = len(data3)
c2 = len(data3.columns)
df4 = df4.round(decimalsX)

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
plt.title('DATASET_5_SISFALL_Python1 | # Headers= '+str(c) + ' / '+str(c2) +
          ': # Records='+str(l)+'/'+str(l2)+'|', fontsize=sizingFont, color='green', fontweight="bold")
plt.tight_layout()
plt.savefig('../UXviews/TABLES/TA5.png')
plt.show()
print(data3.head(2))

print('=============|Plot_Five_Processed|====================[14]==========')
df4 = data4.iloc[1:24:, -15:]  # 22-Records, last-15X headers
l = len(df4)
c = len(df4.columns)
l2 = len(data4)
c2 = len(data4.columns)
df4 = df4.round(decimalsX)

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
plt.suptitle(lablel6)
plt.title('DATASET_6_SISFALL_Python2 | # Headers= '+str(c) + ' / '+str(c2) +
          ': # Records='+str(l)+'/'+str(l2)+'|', fontsize=sizingFont, color='green', fontweight="bold")
plt.tight_layout()
plt.savefig('../UXviews/TABLES/TA6.png')
plt.show()
print(data4.head(2))

print('=============|Plot_Five_Processed|====================[14]==========')
df4 = df5.iloc[1:29:, -15:]  # 22-Records, last-15X headers
l = len(df4)
c = len(df4.columns)
l2 = len(data4)
c2 = len(data4.columns)
df4 = df4.round(decimalsX)

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
plt.suptitle(lablel6)
plt.title('DATASET_7_SISFALL_Zeros&Ones | # Headers= '+str(c) + ' / '+str(c2) +
          ': # Records='+str(l)+'/'+str(l2)+'|', fontsize=sizingFont, color='green', fontweight="bold")
plt.tight_layout()
plt.savefig('../UXviews/TABLES/TA7.png')
plt.show()
print(df5.head(21))
print('=============|Plot_Five_Processed|====================[15]==========')
print(l)
print(c)
print(c2)
print(l2)

print('=============|Plot_Successfully_Completed|============[16]==========')
