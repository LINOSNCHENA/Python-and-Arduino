# COSINE AND SINE
from calendar import EPOCH
import tensorflow as tf
import matplotlib.pyplot as plt
from tensorflow.keras import layers
import numpy as np
import math
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '1'
plt.rcParams["figure.figsize"] = (12, 8)

print('Numpy ' + np.__version__)
print('TensorFlow ' + tf.__version__)
print('Keras ' + tf.keras.__version__)

# Settings
nsamples = 1102     # Number of samples to use as a dataset
val_ratio = 0.12     # Percentage of samples that should be held for validation set
test_ratio = 0.12    # Percentage of samples that should be held for test set
tflite_model_name = 'zed_sine_model'  # Will be given .tflite suffix
c_model_name = 'sine_model'       # Will be given .h suffix
epochX = 201

print("================================|Make_Dataset_Line_33|=======================1=========")
# Generate some random samples
np.random.seed(1234)
x_values = np.random.uniform(low=0, high=(2 * math.pi), size=nsamples)
plt.plot(x_values)
print(x_values)
print(x_values.shape)

# Create a noisy sinewave with these values
y_values = np.sin(x_values) + (0.1 * np.random.randn(x_values.shape[0]))
plt.plot(x_values, y_values, '.')

# Plit the dataset into training, validation, and test sets
val_split = int(val_ratio * nsamples)
test_split = int(val_split + (test_ratio * nsamples))
x_val, x_test, x_train = np.split(x_values, [val_split, test_split])
y_val, y_test, y_train = np.split(y_values, [val_split, test_split])

# Check that our splits add up correctly
assert(x_train.size + x_val.size + x_test.size) == nsamples

print("================================|Plot_Training_Data_Line_33|========================2=========")
# Plot the data in each partition in different colors'
plt.plot(x_train, y_train, 'b.', label="Train")
plt.plot(x_test, y_test, 'r.', label="Test")
plt.plot(x_val, y_val, 'y.', label="Validate")
plt.title('1-Training,Testing,and validation data')
plt.legend()
plt.savefig('../uxviews/Projects/ProjectB01.png')
plt.show()

# Create a model
model = tf.keras.Sequential()
model.add(layers.Dense(16, activation='relu', input_shape=(1,)))
model.add(layers.Dense(16, activation='relu'))
model.add(layers.Dense(1))
# View model
model.summary()

# Add optimizer, loss function, and metrics to model and compile it
# model.compile(optimizer='rmsprop', loss='mae', metrics=['mae','acc','accuracy'])
# Train model
model.compile(optimizer='adam', loss='binary_crossentropy',
              metrics=['mae', 'acc', tf.keras.metrics.Accuracy()])
# Fit the model
history = model.fit(x_train,
                    y_train,
                    epochs=epochX,
                    batch_size=EPOCH, verbose=False,
                    validation_data=(x_val, y_val))


print("================================|History_Plotting_Line_33|=======================3===========")
# Plot the training history
loss = history.history['loss']
val_loss = history.history['val_loss']
epochs = range(1, len(loss) + 1)
plt.plot(epochs, loss, 'bo', label='Training loss')
plt.plot(epochs, val_loss, 'g', label='Validation loss')
plt.title('2 - Training and validation loss')
plt.legend()
plt.savefig('../uxviews/Projects/ProjectB02.png')
plt.show()


# Plot predictions against actual values
predictions = model.predict(x_test)
print("================================|Prediction_Plotting_Line_33|=======================4============")
plt.clf()
plt.title("3 - Comparison of predictions to actual values")
plt.plot(x_test, y_test, 'b.', label='Actual')
plt.plot(x_test, predictions, 'r.', label='Prediction')
plt.legend()
plt.savefig('../uxviews/Projects/ProjectB03.png')
plt.show()

# Convert Keras model to a tflite model
converter = tf.lite.TFLiteConverter.from_keras_model(model)
converter.optimizations = [tf.lite.Optimize.DEFAULT]  # OPTIMIZE_FOR_SIZE]
print("================================|Model_Create_Line_33|=================66=============5B===========")
tflite_model = converter.convert()
print("================================|Model_Create_Line_33|===============Error-Above=======5B===========")

open(tflite_model_name + '.tflite', 'wb').write(tflite_model)


# Function' Convert some hex value into an array for C programming
def hex_to_c_array(hex_data, var_name):
    c_str = ''
    # Create header guard
    c_str += '#ifndef ' + var_name.upper() + '_H\n'
    c_str += '#define ' + var_name.upper() + '_H\n\n'
    # Add array length at top of file
    c_str += '\nunsigned int ' + var_name + \
        '_len = ' + str(len(hex_data)) + ';\n'
    # Declare C variable
    c_str += 'unsigned char ' + var_name + '[] = {'
    hex_array = []
    for i, val in enumerate(hex_data):
        # Construct string from hex
        hex_str = format(val, '#04x')
        # Add formatting so each line stays within 80 characters
        if (i + 1) < len(hex_data):
            hex_str += ','
        if (i + 1) % 12 == 0:
            hex_str += '\n '
        hex_array.append(hex_str)
    # Add closing brace
    c_str += '\n ' + format(' '.join(hex_array)) + '\n};\n\n'
    # Close out header guard
    c_str += '#endif //' + var_name.upper() + '_H'
    return c_str


print("================================|Model_Plot_Line_33|=====================6=============")
# Write TFLite model to a C source (or header) file
with open(c_model_name + '.h', 'w') as file:
    file.write(hex_to_c_array(tflite_model, c_model_name))


print("===================================|EVALUATION-REQUIRED|=========================================11===============")
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
print(history.history)
print("\n ===================================|First_Plot|=======================12===============")
print(history.history.keys())
print(accArray1)
print(accArray12)

print(accArray2)
print(accArray22)

print(accArray3)
print(accArray32)

# Setting the figure fontSized and Frame
plt.figure(figsize=(18, 10))
ax = plt.axes()
ax.set_facecolor("beige")
plt.plot(history.history['accuracy'], color="blue")
plt.plot(history.history['val_accuracy'], color="red")
plt.title('08 '+str(plotName)+' | Model-Accuracy', fontsize=fontSized)
plt.ylabel('Accuracy ', fontsize=fontSized)
plt.xlabel('epoch', fontsize=fontSized)
plt.legend(['training  : %'+str(accArray2),
           'validation : %'+str(accArray22)], loc='best', fontsize=fontSized,)
plt.savefig('../uxviews/Projects/ProjectB04.png')
plt.show()

print("\n ===================================|Second_Plot|======================13===============")
plt.figure(figsize=(12, 10))
ax = plt.axes()
ax.set_facecolor("beige")
plt.plot(history.history['loss'], color="fuchsia")
plt.plot(history.history['val_loss'], color="blue")
plt.title('09 '+str(plotName)+' | Model-Loss', fontsize=fontSized)
plt.ylabel('Loss values', fontsize=fontSized)
plt.xlabel('epoch', fontsize=fontSized)
plt.grid(True)
plt.legend(['training  : %'+str(accArray2),
           'validation : %'+str(accArray22)], loc='best', fontsize=fontSized,)
plt.savefig('../uxviews/Projects/ProjectB05.png')
plt.show()

print("\n ===================================|Third_Plot|=======================14===============")

plt.figure(figsize=(18, 10))
ax = plt.axes()
ax.set_facecolor("beige")
plt.plot(history.history['mae'], color="blue")
plt.plot(history.history['val_mae'], color="fuchsia")
plt.title('10 '+str(plotName)+' | Model-Error', fontsize=fontSized)
plt.ylabel('Error values', fontsize=fontSized)
plt.xlabel('epoch', fontsize=fontSized)
plt.legend(['training  : %'+str(accArray3),
           'validation : %'+str(accArray32)], loc='best', fontsize=fontSized,)
plt.savefig('../uxviews/Projects/ProjectB06.png')
plt.show()

print("================================|xPart1_Successfuly_Completed|===================7=============")
