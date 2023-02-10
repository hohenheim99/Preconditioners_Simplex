from tensorflow import keras
import numpy as np
from get_data import *
from keras.callbacks import EarlyStopping
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import tensorflow as tf

#Make data and tensors for the input/output
folder='test_results'

input=make_tensors(folder)
output=make_tensor_P(folder)
#input=input[:100000]
#output=output[:100000]

epochs=20
seed = 7
batchs=50
np.random.seed(seed)
X_train, X_test,  = train_test_split(input, test_size=0.2, random_state=seed)
Y_train, Y_test = train_test_split(output, test_size=0.2, random_state=seed)



model = keras.Sequential([
        keras.layers.Dense(100,input_shape=(731,),activation="relu"),
        keras.layers.Dense(64,activation="tanh"),
        # keras.layers.Flatten(),
        keras.layers.Dense(1036, activation="sigmoid")
])

model.compile(loss='mean_absolute_error', optimizer='adam',metrics=['accuracy'])
model.summary()
model.fit(X_train,Y_train, batch_size=batchs, epochs=epochs)

score,acc = model.evaluate(X_test, Y_test,batch_size=batchs)
print("Test loss:", score)
print("Test accuracy:", acc)


prediction = model.predict(X_test)
print(prediction[0])
