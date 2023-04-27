from keras.utils.np_utils import normalize
import numpy as np
from get_data import *
from criteria import *
from keras.models import load_model
from tensorflow import keras


def predict_with_model(model_path,path_results,samples):

    model = load_model(model_path) # load model

    samples=1 #samples in the dataset

    input=read_data_AXB_n(path_results,samples)

    input=padd_to_n(input,295) #ANN its trained with an input of 295-dimension, put this format everything with the zeroes pad function



    input=normalize(input) #Normalize input, with L2 norm (Note to me: try to replicated manually)


    ynew = model.predict(input) # prediction using the ANN

    for i in ynew:
        if i > 0.5:
            return 1
        else:
            return 0