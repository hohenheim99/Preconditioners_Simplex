import os
from tensorflow import keras
import numpy as np
import random
from get_data import *
from keras.callbacks import EarlyStopping
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt





folder=input("select folder: ")


pathP=folder+'/DS_P.txt'

input=make_tensors(folder)

output=get_data_P(pathP)


seed = 7
np.random.seed(seed)
X_train, X_test,  = train_test_split(input, test_size=0.2, random_state=seed)
Y_train, Y_test = train_test_split(output, test_size=0.2, random_state=seed)


es = EarlyStopping(monitor='loss', mode='min', verbose=1,min_delta=0.01, patience=20)
lr_schedule = keras.optimizers.schedules.ExponentialDecay(initial_learning_rate=0.001, decay_steps=1600, decay_rate=0.95)
rmsprop = keras.optimizers.RMSprop(learning_rate=lr_schedule, momentum=0.3)

model = keras.Sequential()