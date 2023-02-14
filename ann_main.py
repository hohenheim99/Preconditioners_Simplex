from tensorflow import keras
import numpy as np
from get_data import read_data
from keras.callbacks import EarlyStopping
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import tensorflow as tf

#Make data and tensors for the input/output
input_path='tensors/tensor_input.txt'
output_path='tensors/tensor_output.txt'


input=read_data(input_path)

output=read_data(output_path)


epochs=10
seed = 7
batchs=50
np.random.seed(seed)
X_train, X_test,  = train_test_split(input, test_size=0.2)
Y_train, Y_test = train_test_split(output, test_size=0.2)



model = keras.Sequential([
        keras.layers.Dense(100,input_shape=(3095,),activation="relu"),
        keras.layers.Flatten(),
        keras.layers.Dense(50,activation="relu"),
        keras.layers.Dense(2871, activation="relu")
])

model.compile(loss='mean_absolute_error', optimizer='rmsprop',metrics=['accuracy'])
model.summary()
model.fit(X_train,Y_train, batch_size=batchs, epochs=epochs)


score,acc = model.evaluate(X_test, Y_test,batch_size=batchs)
print("Test loss:", score)
print("Test accuracy:", acc)


prediction = model.predict(X_test)

