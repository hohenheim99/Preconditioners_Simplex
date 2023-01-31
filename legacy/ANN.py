import os
from tensorflow import keras
import numpy as np
import random
from keras.callbacks import EarlyStopping
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import matplotlib
from tkinter import *


def randomMatrix(matrixSize,maxValue):
    matrix = []
    for i in range(matrixSize):
        line = []
        for j in range(matrixSize):
            value = (random.random()*maxValue)
            line.append(value)
        matrix.append(line)
    return np.array(matrix)
    
def generatesOutputFromInput(matrix):
    output = []
    rows, cols = matrix.shape
    for i in range(rows):
        line = []
        minVal = matrix[i,0]
        for j in range(cols):
            value = matrix[i,j]
            if value < minVal:
                minVal = value
        for j in range(cols):
            value = matrix[i,j]
            if value == minVal:
                line.append(1)
            else:
                line.append(0)
        output.append(line)
    return np.array(output)

def builtDataset(datasetSize,matrixSize,maxValue):
    inputs = []
    outputs = []
    for i in range(datasetSize):
        inputM = randomMatrix(matrixSize,maxValue)
        outputM = generatesOutputFromInput(inputM)
        inputs.append(inputM)
        outputs.append(outputM)
    return np.array(inputs),np.array(outputs)
    
matrixSize = 5
maxValue = 200
epochs = 20
datasetSize = 200000

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
        keras.layers.Dense((matrixSize*matrixSize)/2, input_shape=(matrixSize,matrixSize), activation="relu"),   
        keras.layers.Dropout(0.2),
        keras.layers.Flatten(),
        keras.layers.Dense((matrixSize*matrixSize)/4, activation="relu"),
        keras.layers.Dropout(0.2),
        keras.layers.Dense((matrixSize*matrixSize)/2, activation="relu"), 
        keras.layers.Dropout(0.2),
        keras.layers.Dense(matrixSize*matrixSize, activation="sigmoid"),
        keras.layers.Reshape((matrixSize, matrixSize))
])

model.compile(optimizer=rmsprop,loss="mean_squared_error", metrics=["accuracy"])
model.summary()

history = model.fit(X_train, Y_train, batch_size=100, callbacks=[es], shuffle=True, epochs=epochs, validation_split=0.1)

score = model.evaluate(X_test, Y_test, verbose=0)
print("Test loss:", score[0])
print("Test accuracy:", score[1])

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