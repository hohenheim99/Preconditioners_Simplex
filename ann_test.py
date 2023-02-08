from tensorflow import keras
import numpy as np
from get_data import *
from keras.callbacks import EarlyStopping
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import tensorflow as tf

#Make data and tensors for the input/output
folder='test_results'
n=300
input=make_tensors(folder,n)
output=make_tensor_P(folder,n)

# input=input[:10]
# output=output[:10]

epochs=10
seed = 7
np.random.seed(seed)
X_train, X_test,  = train_test_split(input, test_size=0.2, random_state=seed)
Y_train, Y_test = train_test_split(output, test_size=0.2, random_state=seed)



model = keras.Sequential([
        keras.layers.Dense(300,input_shape=(300,), activation="relu"),
        keras.layers.Flatten(),
        keras.layers.Dense(300, activation="sigmoid")
])

model.compile(loss='mean_absolute_error', optimizer='adam')
model.summary()
model.fit(X_test,Y_test, batch_size=100, epochs=epochs)




prediction = model.predict(X_test)
print(prediction[0])
