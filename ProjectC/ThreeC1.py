from pathlib import Path
from pickle import FALSE
from tabnanny import verbose
from scipy.spatial.transform import Rotation
import matplotlib.pyplot as plt
from tensorflow.keras.models import Sequential
from tensorflow.keras import layers
import tensorflow as tf
from sklearn.model_selection import train_test_split
import pandas as pd
import random
import numpy as np
import math
import warnings
warnings.filterwarnings("ignore", category=np.VisibleDeprecationWarning) 

print("=======================================|Create_DataFrame|====================================1==============")

epochX = 200
windowSize = 75
scaleFactor = 0.1
SmartFallTest = pd.read_csv("SmartFall Testing.csv")
SmartFallTest = SmartFallTest.to_numpy()
SmartFallTrain = pd.read_csv("SmartFall Training.csv")
SmartFallTrain = SmartFallTrain.to_numpy()

prevOutcome = 0
prevFuture63Outcome = 0
SmartFallData = [[]]
SmartADLData = [[]]
adlIndex = 0
fallIndex = -1

leftSide = random.randint(-12, windowSize-13)
rightSide = windowSize - leftSide - 25
print('leftSideX=>',+leftSide)
print('rightSide=>',+rightSide)

print('1-smartFallTestX=>',SmartFallTest.shape)
print('2-smartFallTrain=>',SmartFallTrain.shape)

print('3-smartFallTestX=>',pd.DataFrame(SmartFallTest).head(5))
print('4-smartFallTrain=>',pd.DataFrame(SmartFallTrain).head(5))

if(rightSide < 0):
    rightSide = 0

if(leftSide < 0):
    leftSide = 0

print("=======================================|ADLMOdel_Train|=======================================2===========")
ADLMode = True
tempFallCounter = 0
for i in range(len(SmartFallTrain)):
    currentOutcome = SmartFallTrain[i][3]
    if(i+63 < len(SmartFallTrain)):
        future63Outcome = SmartFallTrain[i+63][3]
    else:
        future63Outcome = 0
    if(future63Outcome == 1 and ADLMode):
        ADLMode = False
        SmartFallData.append([])
        fallIndex += 1

    if(ADLMode and currentOutcome == 0):
        SmartADLData[adlIndex].append(
            [SmartFallTrain[i][0], SmartFallTrain[i][1], SmartFallTrain[i][2]])
    elif(ADLMode):
        ADLMode = True
        SmartADLData.append([])
        adlIndex += 1
        tempFallCounter = 0
    else:
        SmartFallData[fallIndex].append(
            [SmartFallTrain[i][0], SmartFallTrain[i][1], SmartFallTrain[i][2]])
        tempFallCounter += 1
        if(tempFallCounter == 151):
            ADLMode = True
            SmartADLData.append([])
            adlIndex += 1
            tempFallCounter = 0
    prevOutcome = currentOutcome
    prevFuture63Outcome = future63Outcome

print(prevOutcome)
print(prevFuture63Outcome)
print("=======================================|ADLMode_Test|======================================3============")
ADLMode = True

tempFallCounter = 0
for i in range(len(SmartFallTest)):
    currentOutcome = SmartFallTest[i][3]
    if(i+63 < len(SmartFallTest)):
        future63Outcome = SmartFallTest[i+63][3]
    else:
        future63Outcome = 0
    if(future63Outcome == 1 and ADLMode):
        ADLMode = False
        SmartFallData.append([])
        fallIndex += 1
    if(ADLMode and currentOutcome == 0):
        SmartADLData[adlIndex].append(
            [SmartFallTest[i][0], SmartFallTest[i][1], SmartFallTest[i][2]])
    elif(ADLMode):
        ADLMode = True
        SmartADLData.append([])
        adlIndex += 1
        tempFallCounter = 0
    else:
        SmartFallData[fallIndex].append(
            [SmartFallTest[i][0], SmartFallTest[i][1], SmartFallTest[i][2]])
        tempFallCounter += 1
        if(tempFallCounter == 151):
            ADLMode = True
            SmartADLData.append([])
            adlIndex += 1
            tempFallCounter = 0
    prevOutcome = currentOutcome
    prevFuture63Outcome = future63Outcome

print(prevOutcome)
print(prevFuture63Outcome)

print(SmartADLData.count)
print(SmartFallData.count)
print("=======================================|Watch_Labelled_One|===================================4===============")

SmartWatch182 = pd.read_csv("WatchData/raw182_Training_Relabeled_Auto_25.csv")
SmartWatch182 = SmartWatch182.values
SmartWatch91 = pd.read_csv("WatchData/raw91_Testing_Relabeled_Auto_25.csv")
SmartWatch91 = SmartWatch91.values
print(SmartWatch182)


ADLMode = True
tempFallCounter = 0
for i in range(len(SmartWatch182)):
    currentOutcome = SmartWatch182[i][3]
    if(i+63 < len(SmartWatch182)):
        future63Outcome = SmartWatch182[i+63][3]
    else:
        future63Outcome = 0
    if(future63Outcome == 1 and ADLMode):
        ADLMode = False
        SmartFallData.append([])
        fallIndex += 1

    if(ADLMode and currentOutcome == 0):
        SmartADLData[adlIndex].append(
            [SmartWatch182[i][0], SmartWatch182[i][1], SmartWatch182[i][2]])
    elif(ADLMode):
        ADLMode = True
        SmartADLData.append([])
        adlIndex += 1
        tempFallCounter = 0
    else:
        SmartFallData[fallIndex].append(
            [SmartWatch182[i][0], SmartWatch182[i][1], SmartWatch182[i][2]])
        tempFallCounter += 1
        if(tempFallCounter == 151):
            ADLMode = True
            SmartADLData.append([])
            adlIndex += 1
            tempFallCounter = 0

    prevOutcome = currentOutcome
    prevFuture63Outcome = future63Outcome


print("=======================================|Watch_Labelled_Two|====================================5==============")
ADLMode = True
tempFallCounter = 0
for i in range(len(SmartWatch91)):
    currentOutcome = SmartWatch91[i][3]
    if(i+63 < len(SmartWatch91)):
        future63Outcome = SmartWatch91[i+63][3]
    else:
        future63Outcome = 0
    if(future63Outcome == 1 and ADLMode):
        ADLMode = False
        SmartFallData.append([])
        fallIndex += 1

    if(ADLMode and currentOutcome == 0):
        SmartADLData[adlIndex].append(
            [SmartWatch91[i][0], SmartWatch91[i][1], SmartWatch91[i][2]])
    elif(ADLMode):
        ADLMode = True
        SmartADLData.append([])
        adlIndex += 1
        tempFallCounter = 0
    else:
        SmartFallData[fallIndex].append(
            [SmartWatch91[i][0], SmartWatch91[i][1], SmartWatch91[i][2]])
        tempFallCounter += 1
        if(tempFallCounter == 151):
            ADLMode = True
            SmartADLData.append([])
            adlIndex += 1
            tempFallCounter = 0

    prevOutcome = currentOutcome
    prevFuture63Outcome = future63Outcome


SmartADLRemoveIndexs = []
SmartFallRemoveIndexs = []
for i in range(len(SmartADLData)):
    if(len(SmartADLData[i]) < windowSize):
        SmartADLRemoveIndexs.append(i)

SmartADLData = np.delete(SmartADLData, SmartADLRemoveIndexs)
for i in range(len(SmartFallData)):
    if(len(SmartFallData[i]) < windowSize):
        SmartFallRemoveIndexs.append(i)
SmartFallData = np.delete(SmartFallData, SmartFallRemoveIndexs)

AllADL = []

for i in range(len(SmartADLData)):
    if(len(SmartADLData[i]) < 2 * windowSize and len(SmartADLData[i]) > windowSize):
        AllADL.append(SmartADLData[i][0:windowSize])
    elif(len(SmartADLData[i]) > 3 * windowSize + windowSize/4):
        z = 0
        while(z < (len(SmartADLData) - windowSize - 1) and len(SmartADLData) > z+windowSize+windowSize/4):
            AllADL.append(SmartADLData[i][z:z+windowSize])
            z += 1

AllADLRemoveIndexs = []
for i in range(len(AllADL)):
    if(len(AllADL[i]) != windowSize):
        AllADLRemoveIndexs.append(i)
AllADL = np.delete(np.array(AllADL), AllADLRemoveIndexs)

AllFall = []
for i in range(0, 10):
    for i in range(len(SmartFallData)):
        z = random.randint(0, windowSize-13)
        AllFall.append(SmartFallData[i][z:z+windowSize])


print("=======================================|Watch_Labelled_One|==================================6================")
custom1 = pd.read_csv("1.csv")
custom1 = custom1.to_numpy()[:, 1]
custom1 = custom1[:(math.floor(custom1.shape[0]/225) * 225)]
custom1 = np.reshape(custom1, (int(custom1.shape[0]/225), 75, 3))

custom2 = pd.read_csv("2.csv")
custom2 = custom2.to_numpy()[:, 1]
custom2 = custom2[:(math.floor(custom2.shape[0]/225) * 225)]
custom2 = np.reshape(custom2, (int(custom2.shape[0]/225), 75, 3))

custom3 = pd.read_csv("3.csv")
custom3 = custom3.to_numpy()[:, 1]
custom3 = custom3[:(math.floor(custom3.shape[0]/225) * 225)]
custom3 = np.reshape(custom3, (int(custom3.shape[0]/225), 75, 3))

custom4 = pd.read_csv("4.csv")
custom4 = custom4.to_numpy()[:, 1]
custom4 = custom4[:(math.floor(custom4.shape[0]/225) * 225)]
custom4 = np.reshape(custom4, (int(custom4.shape[0]/225), 75, 3))
AllYData = []

print(len(AllADL))
print(len(AllFall))
print("=======================================|Watch_Labelled_One|==================================7================")
p = 0.75
AllXData = []
for i in range(len(AllADL)):
    if(random.random() > p):
        AllXData.append(AllADL[i])
    else:
        randR = Rotation.random().as_euler('zxy', degrees=True)
        r = Rotation.from_euler('zxy', randR, degrees=True)
        AllXData.append(r.apply(vectors=AllADL[i], inverse=False))
    AllYData.append([1, 0])


for i in range(len(AllFall)):
    if(random.random() > p):
        AllXData.append(AllFall[i])
    else:
        randR = Rotation.random().as_euler('zxy', degrees=True)
        r = Rotation.from_euler('zxy', randR, degrees=True)
        AllXData.append(r.apply(vectors=AllFall[i], inverse=False))

    AllYData.append([0, 1])

    # AllYData.append([1,0])
for i in range(0, 20):
    for i in range(len(custom2)):
        if(random.random() > p):
            AllXData.append(custom2[i])
        else:
            randR = Rotation.random().as_euler('zxy', degrees=True)
            r = Rotation.from_euler('zxy', randR, degrees=True)
            AllXData.append(r.apply(vectors=custom2[i], inverse=False))
        AllYData.append([1, 0])


for i in range(0, 10):
    for i in range(len(custom3)):
        if(random.random() > p):
            AllXData.append(custom3[i])
        else:
            randR = Rotation.random().as_euler('zxy', degrees=True)
            r = Rotation.from_euler('zxy', randR, degrees=True)
            AllXData.append(r.apply(vectors=custom3[i], inverse=False))
        AllYData.append([1, 0])


for i in range(0, 10):
    for i in range(len(custom4)):
        if(random.random() > p):
            AllXData.append(custom4[i])
        else:
            randR = Rotation.random().as_euler('zxy', degrees=True)
            r = Rotation.from_euler('zxy', randR, degrees=True)
            AllXData.append(r.apply(vectors=custom4[i], inverse=False))
        AllYData.append([1, 0])

print("=======================================|Watch_Labelled_One|=================================8====A=============")
df1=pd.DataFrame(AllYData)
df2=pd.DataFrame(np.array(AllXData)[3])
# print(np.array(AllXData))
# print(np.array(AllXData)[1])
print(type(df1))
print(type(AllXData))
print(type(AllYData))
# print(np.array(AllXData)[1])
# print(np.array(AllXData)[2])
# print(np.array(AllXData)[1].shape)

print(df1.shape)
print(df2.head(5))
print("=======================================|Watch_Labelled_One|=================================8======B===========")
df1.to_csv('xdata/DF_One.csv')
df1.to_csv(r'./xdata/DF_One.csv', sep='\t', encoding='utf-8', header='true', index=False)
df2.to_csv(r'./xdata/DF_Two.csv', sep='\t', encoding='utf-8', header='true', index=False)


X_train, X_test, y_train, y_test = train_test_split(
    np.array(AllXData), np.array(AllYData), test_size=0.25, shuffle=True)

X_train = X_train.reshape(X_train.shape[0], windowSize, 1, 3) * scaleFactor
X_test = X_test.reshape(X_test.shape[0], windowSize, 1, 3) * scaleFactor
print(X_train.shape)


# pd.DataFrame(np.array(X_train)[1]).to_csv(r'./xdata/DF_1One.csv', sep='\t', encoding='utf-8', header='true', index=False)
# pd.DataFrame(X_test).to_csv(r'./xdata/DF_1Two.csv', sep='\t', encoding='utf-8', header='true', index=False)
# pd.DataFrame(y_train).to_csv(r'./xdata/DF_1One.csv', sep='\t', encoding='utf-8', header='true', index=False)

# pd.DataFrame(y_test).to_csv(r'./xdata/DF_2Two.csv', sep='\t', encoding='utf-8', header='true', index=False)
# pd.DataFrame(X_train).to_csv(r'./xdata/DF_2One.csv', sep='\t', encoding='utf-8', header='true', index=False)
# pd.DataFrame(X_test).to_csv(r'./xdata/DF_2Two.csv', sep='\t', encoding='utf-8', header='true', index=False)
gpus = tf.config.list_physical_devices('GPU')
if gpus:
    # Restrict TensorFlow to only use the first GPU
    try:
        tf.config.experimental.set_visible_devices(gpus[0], 'GPU')
        logical_gpus = tf.config.experimental.list_logical_devices('GPU')
        print(len(gpus), "Physical GPUs,", len(logical_gpus), "Logical GPU")
    except RuntimeError as e:
        # Visible devices must be set before GPUs have been initialized
        print(e)

print("=======================================|Model_Creation_One|====================================9=================")
model = Sequential()
model.add(layers.Conv2D(64, (4, 1), input_shape=(
    windowSize, 1, 3), activation='relu'))
model.add(layers.Dropout(0.2))
model.add(layers.MaxPool2D(3, padding='same'))
model.add(layers.Flatten())
model.add(layers.Dense(16, activation='relu'))
model.add(layers.Dropout(0.2))
model.add(layers.Dense(2, activation='softmax'))
model.summary()
model.compile(optimizer='adam',loss='binary_crossentropy', metrics=['mae', tf.keras.metrics.FalseNegatives(), tf.keras.metrics.FalsePositives(), 'accuracy'])
history = model.fit(x=X_train, y=y_train, batch_size=100,verbose=FALSE,
                    epochs=epochX, validation_data=(X_test, y_test))


# testing accuracy on validation data
y_pred = model.predict(X_test)
cf_matrix = tf.math.confusion_matrix(labels=y_test.argmax(
    axis=1), predictions=y_pred.argmax(axis=1)).numpy()
print(cf_matrix)

# converter = tf.lite.TFLiteConverter.from_keras_model(q_aware_model)
converter = tf.lite.TFLiteConverter.from_keras_model(model)
model_tflite = converter.convert()
print(Path('modelTFLite').write_bytes(model_tflite))

print("===================================|EVALUATION-REQUIRED|=========================================10===============")
print(history.history.keys())
plotName = '- Android And Python -'
fontSized = 15
allSizes = (history.history['accuracy'])
arrLengthX = len(allSizes)

accArray1 = (history.history['accuracy'])
accArray1 = round(100*accArray1[arrLengthX-1], 4)
accArray12 = (history.history['val_accuracy'])
accArray12 = round(100*accArray12[arrLengthX-1], 4)

accArray2 = (history.history['mae'])
accArray2 = round(100*accArray2[arrLengthX-1], 4)
accArray22 = (history.history['val_mae'])
accArray22 = round(100*accArray22[arrLengthX-1], 4)

accArray3 = (history.history['loss'])
accArray3 = round(100*accArray3[arrLengthX-1], 4)
accArray32 = (history.history['val_loss'])
accArray32 = round(100*accArray32[arrLengthX-1], 4)

print("\n ===================================|First_Plot|==============================================11===============")
print(history.history.keys())
print(accArray1)
print(accArray12)

# print(accArray2)
# print(accArray22)

# print(accArray3)
# print(accArray32)

# Setting the figure fontSized and Frame
plt.figure(figsize=(18, 10))
ax = plt.axes()
ax.set_facecolor("beige")
plt.plot(history.history['accuracy'], color="blue")
plt.plot(history.history['val_accuracy'], color="red")
plt.title('08 '+str(plotName)+' | Model-Accuracy', fontsize=fontSized)
plt.ylabel('Accuracy ', fontsize=fontSized)
plt.xlabel('epoch', fontsize=fontSized)
plt.legend(['training  : %'+str(accArray1),'validation : %'+str(accArray12)], loc='best', fontsize=fontSized,)
plt.savefig('../uxviews/Projects/ProjectC01.png')
# plt.show()

print("\n ===================================|Second_Plot|======================12===============")
plt.figure(figsize=(18, 10))
ax = plt.axes()
ax.set_facecolor("beige")
plt.plot(history.history['loss'], color="fuchsia")
plt.plot(history.history['val_loss'], color="blue")
plt.title('09 '+str(plotName)+' | Model-Loss', fontsize=fontSized)
plt.ylabel('Loss values', fontsize=fontSized)
plt.xlabel('epoch', fontsize=fontSized)
plt.grid(True)
plt.legend(['training  : %'+str(accArray2),'validation : %'+str(accArray22)], loc='best', fontsize=fontSized,)
plt.savefig('../uxviews/Projects/ProjectC02.png')
# plt.show()

print("\n ===================================|Third_Plot|=======================13===============")

plt.figure(figsize=(18, 10))
ax = plt.axes()
ax.set_facecolor("beige")
plt.plot(history.history['mae'], color="blue")
plt.plot(history.history['val_mae'], color="fuchsia")
plt.title('10 '+str(plotName)+' | Model-Error', fontsize=fontSized)
plt.ylabel('Error values', fontsize=fontSized)
plt.xlabel('epoch', fontsize=fontSized)
plt.legend(['training  : %'+str(accArray3),'validation : %'+str(accArray32)], loc='best', fontsize=fontSized,)
plt.savefig('../uxviews/Projects/ProjectC03.png')
# plt.show()

print("======================|Successfully Completed-Third_Model_490|==============================14=============")
