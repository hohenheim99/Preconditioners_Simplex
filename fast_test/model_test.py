from keras.utils.np_utils import normalize
import numpy as np
from get_data import *
from criteria import *
from keras.models import load_model
#from tensorflow import keras


def model_predict(model_path,sample): #for predicting a single sample

    model = load_model(model_path)

    input=padd_to_n(sample,295) 

    input=normalize(input) 

    answer = model.predict(input) 
    for i in answer:
        if i > 0.5:
            return 1
        else:
            return 0
        
def model_testing(model_path,results_path,samples): #for predicting a dataset
    input=read_data_AXB_n(results_path,samples)

    model=load_model(model_path)

    input=padd_to_n(input,295)

    input=normalize(input)

    answer = model.predict(input)

    return answer