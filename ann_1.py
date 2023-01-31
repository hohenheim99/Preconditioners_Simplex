import os
from tensorflow import keras
import numpy as np
import random
from get_data import *
from keras.callbacks import EarlyStopping
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt




'''
def builtDataset(datasetSize,matrixSize,maxValue):
    inputs = []
    outputs = []
    for i in range(datasetSize):
        inputM = randomMatrix(matrixSize,maxValue)
        outputM = generatesOutputFromInput(inputM)
        inputs.append(inputM)
        outputs.append(outputM)
    return np.array(inputs),np.array(outputs)
'''
matrixSize = 5
maxValue = 200
epochs = 20
datasetSize = 300000

inputs,outputs = builtDataset(datasetSize,matrixSize,maxValue)
print("inputs ",len(inputs))
print("outputs ",len(outputs))

print(inputs[0])
print(outputs[0])

seed = 7
np.random.seed(seed)
X_train, X_test, Y_train, Y_test = train_test_split(inputs, outputs, test_size=0.1, random_state=seed)

es = EarlyStopping(monitor='loss', mode='min', verbose=1,min_delta=0.01, patience=20)
lr_schedule = keras.optimizers.schedules.ExponentialDecay(initial_learning_rate=0.001, decay_steps=1600, decay_rate=0.95)
rmsprop = keras.optimizers.RMSprop(learning_rate=lr_schedule, momentum=0.3)

model = keras.models.Sequential([
        keras.layers.Dense(100, input_shape=(matrixSize,matrixSize), activation="relu"),   
        keras.layers.Flatten(),
        keras.layers.Dense(30, activation="relu"),
        keras.layers.Dense(100, activation="relu"), 
        keras.layers.Dense(matrixSize*matrixSize, activation="sigmoid"),
        keras.layers.Reshape((matrixSize, matrixSize))
])

model.compile(optimizer=rmsprop,loss="mse", metrics=["accuracy"])

model.summary()

history = model.fit(X_train, Y_train, batch_size=100, callbacks=[es], shuffle=True, epochs=epochs, validation_split=0.1)

score = model.evaluate(X_test, Y_test, verbose=0)
print("Test loss:", score[0])
print("Test accuracy:", score[1])

print(X_test[0])
print(Y_test[0])
prediction = model.predict(X_test)
print(prediction[0])

plt.plot(history.history['accuracy'])
plt.plot(history.history['val_accuracy'])
plt.title('model accuracy')
plt.ylabel('accuracy')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper left')
plt.show()

plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.title('model loss')
plt.ylabel('loss')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper left')
plt.show()