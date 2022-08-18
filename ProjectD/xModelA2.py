import os
import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '1'

filename = "punch.csv"
df = pd.read_csv("content/" + filename)
index = range(1, len(df['aX']) + 1)
print(df.head(4))

# increase the size of the graphs. The default size is (6,4).
plt.rcParams["figure.figsize"] = (10, 8)

plt.plot(index, df['aX'], 'g.', label='x', linestyle='solid', marker=',')
plt.plot(index, df['aY'], 'b.', label='y', linestyle='solid', marker=',')
plt.plot(index, df['aZ'], 'r.', label='z', linestyle='solid', marker=',')
plt.title("Acceleration")
plt.xlabel("Sample #")
plt.ylabel("Acceleration (G)")
plt.legend()
plt.savefig('../uxviews/Projects/ProjectD01.png')
plt.clf()


plt.plot(index, df['gX'], 'g.', label='x', linestyle='solid', marker=',')
plt.plot(index, df['gY'], 'b.', label='y', linestyle='solid', marker=',')
plt.plot(index, df['gZ'], 'r.', label='z', linestyle='solid', marker=',')
plt.title("Gyroscope")
plt.xlabel("Sample #")
plt.ylabel("Gyroscope (deg/sec)")
plt.legend()
plt.savefig('../uxviews/Projects/ProjectD02.png')
plt.clf()

print(f"TensorFlow version = {tf.__version__}\n")
# Set a fixed random seed value, for reproducibility, this will allow us to get
# the same random numbers each time the notebook is run
SEED = 1337
np.random.seed(SEED)
tf.random.set_seed(SEED)
# the list of gestures

GESTURES = [
    "punch",
    "flex"
]

SAMPLES_PER_GESTURE = 119
NUM_GESTURES = len(GESTURES)

# create a one-hot encoded matrix that is used in the output
ONE_HOT_ENCODED_GESTURES = np.eye(NUM_GESTURES)

inputs = []
outputs = []

# read each csv file and push an input and output
for gesture_index in range(NUM_GESTURES):
    gesture = GESTURES[gesture_index]
    print(f"Processing index {gesture_index} for gesture '{gesture}'.")
    output = ONE_HOT_ENCODED_GESTURES[gesture_index]
    df = pd.read_csv("content/" + gesture + ".csv")
    # get rid of pesky empty value lines of csv which cause NaN inputs to TensorFlow
    df = df.dropna()
    df = df.reset_index(drop=True)
    # calculate the number of gesture recordings in the file
    num_recordings = int(df.shape[0] / SAMPLES_PER_GESTURE)

    print(f"\tThere are {num_recordings} recordings of the {gesture} gesture.")
    for i in range(num_recordings):
        tensor = []
        for j in range(SAMPLES_PER_GESTURE):
            index = i * SAMPLES_PER_GESTURE + j
            # normalize the input data, between 0 to 1:
            # - acceleration is between: -4 to +4
            # - gyroscope is between: -2000 to +2000
            tensor += [
                (df['aX'][index] + 4) / 8,
                (df['aY'][index] + 4) / 8,
                (df['aZ'][index] + 4) / 8,
                (df['gX'][index] + 2000) / 4000,
                (df['gY'][index] + 2000) / 4000,
                (df['gZ'][index] + 2000) / 4000
            ]
        inputs.append(tensor)
        outputs.append(output)

# convert the list to numpy array
inputs = np.array(inputs)
outputs = np.array(outputs)
print("Data set parsing and preparation complete.")


# Randomize the order of the inputs, so they can be evenly distributed for training, testing, and validation
# https://stackoverflow.com/a/37710486/2020087
num_inputs = len(inputs)
randomize = np.arange(num_inputs)
np.random.shuffle(randomize)

# Swap the consecutive indexes (0, 1, 2, etc) with the randomized indexes
inputs = inputs[randomize]
outputs = outputs[randomize]

# Split the recordings (group of samples) into three sets: training, testing and validation
TRAIN_SPLIT = int(0.6 * num_inputs)
TEST_SPLIT = int(0.2 * num_inputs + TRAIN_SPLIT)
inputs_train, inputs_test, inputs_validate = np.split(
    inputs, [TRAIN_SPLIT, TEST_SPLIT])
outputs_train, outputs_test, outputs_validate = np.split(
    outputs, [TRAIN_SPLIT, TEST_SPLIT])

print("Data set randomization and splitting complete.")
# build the model and train it
model = tf.keras.Sequential()
# relu is used for performance
model.add(tf.keras.layers.Dense(50, activation='relu'))
model.add(tf.keras.layers.Dense(15, activation='relu'))
# the final layer is softmax because we only expect one gesture to occur per input
model.add(tf.keras.layers.Dense(NUM_GESTURES, activation='softmax'))
model.compile(optimizer='rmsprop', loss='mse', metrics=['mae'],
 run_eagerly=True)
history = model.fit(inputs_train, outputs_train, epochs=120,
                    batch_size=1, validation_data=(inputs_validate, outputs_validate))




# graph the loss, the model above is configure to use "mean squared error" as the loss function
loss = history.history['loss']
val_loss = history.history['val_loss']
epochs = range(1, len(loss) + 1)
plt.plot(epochs, loss, 'g.', label='Training loss')
plt.plot(epochs, val_loss, 'b', label='Validation loss')
plt.title('Training and validation loss')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.legend()
plt.savefig('../uxviews/Projects/ProjectD03.png')
plt.show()
plt.clf()


# graph the loss again skipping a bit of the start
SKIP = 100
plt.plot(epochs[SKIP:], loss[SKIP:], 'g.', label='Training loss')
plt.plot(epochs[SKIP:], val_loss[SKIP:], 'b.', label='Validation loss')
plt.title('Training and validation loss')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.legend()
plt.savefig('../uxviews/Projects/ProjectD04.png')
plt.show()


# graph of mean absolute error
mae = history.history['mae']
val_mae = history.history['val_mae']
plt.plot(epochs[SKIP:], mae[SKIP:], 'g.', label='Training MAE')
plt.plot(epochs[SKIP:], val_mae[SKIP:], 'b.', label='Validation MAE')
plt.title('Training and validation mean absolute error')
plt.xlabel('Epochs')
plt.ylabel('MAE')
plt.legend()
plt.savefig('../uxviews/Projects/ProjectD05.png')
plt.show()
plt.clf()

print("=============|TEST-DATA|================|164|====\n")
# use the model to predict the test inputs
print(inputs_train.shape)
print(inputs_test.shape)
print(inputs_validate.shape)

predictions = model.predict(inputs_validate)
# # print the predictions and the expected ouputs
print("predictions =\n", np.round(predictions, decimals=3))
print("actual-1 =\n", outputs_test)
print("actual-2 =\n", outputs_validate)

print("=============|TEST-DATA|================|176|===\n")
# Convert the model to the TensorFlow Lite format without quantization
converter = tf.lite.TFLiteConverter.from_keras_model(model)
converter.optimizations = {tf.lite.Optimize.DEFAULT}
converter.target_spec.supported_ops = [tf.lite.OpsSet.TFLITE_BUILTINS,
                                       tf.lite.OpsSet.SELECT_TF_OPS]

converter.change_concat_input_ranges = True
converter.experimental_new_converter = True
print("=============|TEST-DATA|================|193|===\n")
tflite_model = converter.convert()
print("=============|TEST-DATA|================|195|===\n")

# Save the model to disk
open("ModelTFlite", "wb").write(tflite_model)

basic_model_size = os.path.getsize("ModelTFlite")
print("Model is %d bytes" % basic_model_size)


model_h_size = os.path.getsize("model.h")
print("")
print(f"Header file, model.h, is {model_h_size:,} bytes.")
print("\n Open the side panel (refresh if needed). Double click model.h to download the file.\n")

print("=========|Xmodel2_Successfully_Completed|===========|202|=====\n")
