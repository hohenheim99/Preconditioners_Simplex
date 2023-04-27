from keras.utils.np_utils import normalize
import numpy as np
from get_data import *
from criteria import *
from keras.models import load_model
from tensorflow import keras


model = load_model('my_model.h5') # load model

path='test_results'  #path to the file
n=10000 #samples in the dataset

input=read_data_AXB_n(path,n)

aux = [0] * 295 #ANN its trained with an input of 295-dimension, put this format everything with the zeroes pad function

input.append(aux)
input=pad_list_with_zeros(input)#padd with zeroes. All inputs has the same lenght

input=normalize(input) #Normalize input, with L2 norm (maybe replicated manually)


ynew = model.predict(input) # prediction using the ANN

for i in ynew:
    if i > 0.5:
        print('Applied simplex')
    else:
        print('No applied simplex')