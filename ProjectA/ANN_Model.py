# TensorFLOW MODEL
from turtle import color
from keras.utils.vis_utils import plot_model
import matplotlib.pyplot as plt
from itertools import count
import tensorflow as tf
import pandas as pd
import numpy as np
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '1'
filename = "datainput/eventFALL.csv"
epochs = 200
skipEpocks = 50
df = pd.read_csv(filename)
index = range(1, len(df['x_acc']) + 1)

print("=====================================|GRAPD-DATA|===============50v50============================y01===============")
print(df.shape)
plt.rcParams["figure.figsize"] = (18, 10)
plt.plot(index, df['x_acc'], color='blue',
         label='x', linestyle='solid', marker=',')
plt.plot(index, df['y_acc'], color='r',
         label='y', linestyle='solid', marker=',')
plt.plot(index, df['z_acc'], color='y',
         label='z', linestyle='solid', marker=',')
plt.title("01-Acceleration")
plt.xlabel("Sample #")
plt.ylabel("Acceleration (G)")
plt.legend()
plt.savefig('../uxviews/PROJECTA/ProjectA01.png')
# plt.show()
plt.clf()
print(df.shape)
plt.plot(index, df['x_gyr'], color='g',
         label='x', linestyle='solid', marker=',')
plt.plot(index, df['y_grc'], color='orange',
         label='y', linestyle='solid', marker=',')
plt.plot(index, df['z_grc'], color='purple',
         label='z', linestyle='solid', marker=',')
plt.title("02-y_grcroscope")
plt.xlabel("Sample #")
plt.ylabel("y_grcroscope (deg/sec)")
plt.legend()
plt.savefig('../uxviews/PROJECTA/ProjectA02.png')
# plt.show()
plt.clf()

print("=====================================|TRAINING-ANN|==============================================y02==============="+'\n')

SEED = 1337
np.random.seed(SEED)
tf.random.set_seed(SEED)
# the list of gestures that data is available for

GESTURES = ["eventFALL", "eventADLX", ]
SAMPLES_PER_GESTURE = 4  # 25  # 119
NUM_GESTURES = len(GESTURES)
# create a one-hot encoded matrix that is used in the output
ONE_HOT_ENCODED_GESTURES = np.eye(NUM_GESTURES)

inputs = []
outputs = []
# read each csv file and push an input and output
for gesture_index in range(NUM_GESTURES):
    eventOccured = GESTURES[gesture_index]
    print(
        f"Processing index {gesture_index} for eventOccured '{eventOccured}'.")

    output = ONE_HOT_ENCODED_GESTURES[gesture_index]
    df = pd.read_csv('datainput/'+eventOccured + ".csv")

    # calculate the number of eventOccured recordings in the file
    num_recordings = int(df.shape[0] / SAMPLES_PER_GESTURE)
    df.to_csv(r'./dataOutput/b1Activity_'+str(gesture_index)+str(eventOccured)+str("_") +
              str(num_recordings)+'.csv', sep=',', encoding='utf-8', header='true', index=False)
    df.to_csv(r'./dataOutput/b2ActivityCombined.csv', sep=',',
              encoding='utf-8', header='true', index=False)

    print(
        f"\tThere are {num_recordings} recordings of the {eventOccured} eventOccured.")

    for i in range(num_recordings):
        sensorX = []
        for j in range(SAMPLES_PER_GESTURE):
            index = i * SAMPLES_PER_GESTURE + j
            # normalize the input data, between 0 to 1:
            # - acceleration is between: -4 to +4
            # - y_grcroscope is between: -2000 to +2000
            sensorX += [
                (df['x_acc'][index] + 4) / 8,
                (df['y_acc'][index] + 4) / 8,
                (df['z_acc'][index] + 4) / 8,
                (df['x_gyr'][index] + 2000) / 4000,
                (df['y_grc'][index] + 2000) / 4000,
                (df['z_grc'][index] + 2000) / 4000, ]

        inputs.append(sensorX)
        outputs.append(output)

# convert the list to numpy arry_acc
inputs = np.array(inputs)
outputs = np.array(outputs)
print("Data set parsing and preparation complete."+'\n')

print("=====================================|RANDOMISE-AND-THEN-SPLIT|==================================y03==============")

# Randomize the order of the inputs, so they can be evenly distributed for training, testing, and validation
# https://stackoverflow.com/a/37710486/2020087
num_inputs = len(inputs)
randomize = np.arange(num_inputs)
np.random.shuffle(randomize)

# Swap the consecutive indexes (0, 1, 2, etc) with the randomized indexes
inputs = inputs[randomize]
outputs = outputs[randomize]

# Split the recordings (group of samples) into three sets: training(3), testing(1) and validation(1)
TRAIN_SPLIT = int(0.6 * num_inputs)
TEST_SPLIT = int(0.2 * num_inputs + TRAIN_SPLIT)

inputs_train, inputs_test, inputs_validate = np.split(
    inputs, [TRAIN_SPLIT, TEST_SPLIT])
outputs_train, outputs_test, outputs_validate = np.split(
    outputs, [TRAIN_SPLIT, TEST_SPLIT])

print('1-numberOfInput=', num_inputs)
print('2-inputs=', inputs.shape)
print('3-output=', outputs.shape)

print('4-Train_Split=', TRAIN_SPLIT)
print('5-Test_Splitt=', TEST_SPLIT)
print(type(TRAIN_SPLIT))
print("\n")

pd.DataFrame(inputs).to_csv('dataoutput/b3inputs' +
                            str(len(inputs))+'.csv', header='true', index=False)
pd.DataFrame(inputs_train).to_csv('dataoutput/b4inputs_train' +
                                  str(len(inputs_train))+'.csv', header='true', index=False)
pd.DataFrame(inputs_test).to_csv('dataoutput/b5inputs_test' +
                                 str(len(inputs_test))+'.csv', header='true', index=False)
pd.DataFrame(inputs_validate).to_csv('dataoutput/b6inputs_validate' +
                                     str(len(inputs_validate))+'.csv', header='true', index=False)

pd.DataFrame(outputs).to_csv('dataoutput/b7outputs' +
                             str(len(outputs))+'.csv', header='true', index=False)
pd.DataFrame(outputs_train).to_csv('dataoutput/b8outputs_train' +
                                   str(len(outputs_train))+'.csv', header='true', index=False)
pd.DataFrame(outputs_test).to_csv('dataoutput/b9outputs_test' +
                                  str(len(outputs_test))+'.csv', header='true', index=False)
pd.DataFrame(outputs_validate).to_csv('dataoutput/b10outputs_validate' +
                                      str(len(outputs_validate))+'.csv', header='true', index=False)

print('inputs.shape=', pd.DataFrame(inputs).shape)
print('inputsTrain.shape=', pd.DataFrame(inputs_train).shape)
print('inputsTest.shape=', pd.DataFrame(inputs_test).shape)
print('inputsValidate.shape=', pd.DataFrame(inputs_validate).shape)

print('\noutputs.shape=', pd.DataFrame(outputs).shape)
print('outputs_train.shape=', pd.DataFrame(outputs_train).shape)
print('outputs_test.shape=', pd.DataFrame(outputs_test).shape)
print('outputs_validate.shape=', pd.DataFrame(outputs_validate).shape)
# inputs_tests=pd.DataFrame(inputs_test)

print("\n Data set randomization and splitting complete.")
print("=====================================|BUILD-&-XTRAIN-MODEL|======================================y04===============")
model = tf.keras.Sequential()
model.add(tf.keras.layers.Dense(50, activation='relu'))
model.add(tf.keras.layers.Dense(15, activation='relu'))
model.add(tf.keras.layers.Dense(NUM_GESTURES, activation='softmax'))
model.compile(optimizer='rmsprop', loss='mse',
              metrics=['mae', 'acc'], run_eagerly=True)
history = model.fit(inputs_train, outputs_train, epochs=epochs, batch_size=1, verbose=1,
                    validation_data=(inputs_validate, outputs_validate))

print("=====================================|LOSS_GRAPH_A|===============================================y05==============")
# graph the loss, the model above is configure to use "mean squared error" as the loss function
loss = history.history['loss']
val_loss = history.history['val_loss']
epochs = range(1, len(loss) + 1)

plt.plot(epochs, loss, 'g.', label='Training loss')
plt.plot(epochs, val_loss, 'b', label='Validation loss')
plt.title('03 -Training and validation | Model loss')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.legend()
plt.savefig('../uxviews/PROJECTA/ProjectA03.png')
# plt.show()
plt.clf()

print(history.history['loss'])

print("=====================================|The-LOSS_GRAPH_B|==========================================y06===============")
# graph the loss again skipping a bit of the start
SKIP = skipEpocks
plt.plot(epochs[SKIP:], loss[SKIP:], 'g.', label='Training loss')
plt.plot(epochs[SKIP:], val_loss[SKIP:], 'b.', label='Validation loss')
plt.title('04-Training and validation | Model loss-After-100 seconds')
plt.xlabel('Epochs44')
plt.ylabel('Loss44')
plt.legend()
plt.savefig('../uxviews/PROJECTA/ProjectA04.png')
# plt.show()
plt.clf()

print("=====================================|GRAPH-THE-MEAN-ABSOLUTE-ERROR|=============================y07===============")
# graph of mean absolute error
mae = history.history['mae']
val_mae = history.history['val_mae']
plt.plot(epochs[SKIP:], mae[SKIP:], 'g.', label='Training MAE')
plt.plot(epochs[SKIP:], val_mae[SKIP:], 'b.', label='Validation MAE')
plt.title('05-Training and validation | Model Mean Absolute Error')
plt.xlabel('Epochs')
plt.ylabel('MAE')
plt.legend()
plt.savefig('../uxviews/PROJECTA/ProjectA05.png')
# plt.show()
plt.clf()
print(history.history)


print("=====================================|GRAPH-THE-MEAN-ACCURACY|===================================y08===============")
# graph of mean absolute error
mae = history.history['acc']
val_mae = history.history['val_acc']
plt.plot(epochs[SKIP:], mae[SKIP:], 'g.', label='Training ACC')
plt.plot(epochs[SKIP:], val_mae[SKIP:], 'b.', label='Validation ACC')
plt.title('06-Training and validation | Model accuracy')
plt.xlabel('Epochs')
plt.ylabel('Accuracy')
plt.legend()
plt.savefig('../uxviews/PROJECTA/ProjectA06.png')
plt.show()
plt.clf()
print(history.history)

print("=====================================|TEST-DATA|=================================================y09===============")
# use the model to predict the test inputs
print(inputs_test)
predictions = model.predict(inputs_test)
# print("predictions =\n", np.round(predictions, decimals=3))
# print("actual =\n", outputs_test)

# Plot the predictions along with to the test data
plt.title('07-Training data predicted vs actual values')
plt.plot(predictions, outputs_test, 'b', label='Actual')
# plt.plot(outputs_validate, outputs_test, 'o', label='Actual-1')
# plt.plot(inputs_validate, inputs_test, 'y')
# plt.plot(outputs_validate, outputs_test, 'g', label='Actual-3')
# plt.plot(inputs_validate, inputs_test, 'm', )
# plt.tight_ly_accout()
plt.legend()
plt.savefig('../uxviews/PROJECTA/ProjectA07.png')
plt.show()
pd.DataFrame(predictions).to_csv('dataoutput/b11Prediction' +
                                 str(len(predictions))+'.csv', header='true', index=False)

print("==============================|Converting-Trained-Model-T0-sensorXflow-rite|======================y10==============")
# Convert the model to the sensorXFlow Lite format without quantization
converter = tf.lite.TFLiteConverter.from_keras_model(model)
tflite_model = converter.convert()

# Save the model to disk
open("modelTFLite", "wb").write(tflite_model)
basic_model_size = os.path.getsize("modelTFLite")
print("Model is %d bytes" % basic_model_size)
model_h_size = os.path.getsize("backend/model.h")
print(f"Header file, model.h, is {model_h_size:,} bytes.")
print("\nOpen the side panel (refresh if needed). Double click model.h to download the file.")

print("===================================|EVALUATION-REQUIRED|=========================================y11===============")
# scores = model.evaluate(X, Y, verbose=0)
# # print("%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))
# print(model.metrics_names)
# print("%s: %.2f%%" % (model.metrics_names[2], scores[2]*100))
# print("%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))
# print("%s: %.2f%%" % (model.metrics_names[0], scores[0]*100))
# scores = model.evaluate(X, Y, verbose=0)
print(history.history.keys())
plotName = '- Android And Python -'
fontSized = 15
allSizes = (history.history['acc'])
arrLengthX = len(allSizes)

accArray1 = (history.history['acc'])
accArray1 = round(100*accArray1[arrLengthX-1], 4)
accArray12 = (history.history['val_acc'])
accArray12 = round(100*accArray12[arrLengthX-1], 4)

accArray2 = (history.history['mae'])
accArray2 = round(100*accArray2[arrLengthX-1], 4)
accArray22 = (history.history['val_mae'])
accArray22 = round(100*accArray22[arrLengthX-1], 4)

accArray3 = (history.history['loss'])
accArray3 = round(100*accArray3[arrLengthX-1], 4)
accArray32 = (history.history['val_loss'])
accArray32 = round(100*accArray32[arrLengthX-1], 4)

print("\n ===================================|First_Plot-acc|=======================y12===============")
print(history.history.keys())
print(accArray1)
print(accArray12)

# Setting the figure fontSized and Frame
plt.figure(figsize=(18, 10))
ax = plt.axes()
ax.set_facecolor("beige")
plt.plot(history.history['acc'], color="blue")
plt.plot(history.history['val_acc'], color="red")
plt.title('08 '+str(plotName)+' | Model-Accuracy', fontsize=fontSized)
plt.ylabel('Accuracy ', fontsize=fontSized)
plt.xlabel('epoch', fontsize=fontSized)
plt.legend(['training  : %'+str(accArray1), 'validation : %' +
           str(accArray12)], loc='best', fontsize=fontSized,)
plt.savefig('../uxviews/PROJECTA/ProjectA08.png')
plt.show()

print("\n ===================================|Second_Plot-loss|======================y13===============")
# Setting the figure fontSized and Frame
print(accArray2)
print(accArray22)

plt.figure(figsize=(18, 10))
ax = plt.axes()
ax.set_facecolor("beige")
plt.plot(history.history['loss'], color="fuchsia")
plt.plot(history.history['val_loss'], color="blue")
plt.title('09 '+str(plotName)+' | Model-Loss', fontsize=fontSized)
plt.ylabel('Loss values', fontsize=fontSized)
plt.xlabel('epoch', fontsize=fontSized)
plt.grid(True)
plt.legend(['training  : %'+str(accArray2), 'validation : %' +
           str(accArray22)], loc='best', fontsize=fontSized,)
plt.savefig('../uxviews/PROJECTA/ProjectA09.png')
plt.show()

print("\n ===================================|Third_Plot-mae|=======================y14===============")
# Setting the figure fontSized and Frame
print(accArray3)
print(accArray32)

plt.figure(figsize=(18, 10))
ax = plt.axes()
ax.set_facecolor("beige")
plt.plot(history.history['mae'], color="blue")
plt.plot(history.history['val_mae'], color="fuchsia")
plt.title('10 '+str(plotName)+' | Model-Error', fontsize=fontSized)
plt.ylabel('Error values', fontsize=fontSized)
plt.xlabel('epoch', fontsize=fontSized)
plt.legend(['training  : %'+str(accArray3), 'validation : %' +
           str(accArray32)], loc='best', fontsize=fontSized,)
plt.savefig('../uxviews/PROJECTA/ProjectA10.png')
plt.show()

# # from keras.utils.vis_utils import plot_model
plot_model(model, to_file='../UXViews/PROJECTA/ProjectA11.png',
           show_shapes=True, show_layer_names=True)

print("==================================|COMPLETED_smallFall_SUCCESSFULLY|===================|BBB|==========y15================")
