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
    print(input)

    answer = model.predict(input) 
    print(answer)
    for i in answer:
        if i > 0.5:
            return 1
        else:
            return 0
        
def model_testing(model_path,results_path,samples): #for predicting a dataset
    input=read_data_AXB_n(results_path,samples)
    print('input',input[0])

    model=load_model(model_path)

    input=padd_to_n(input,295)

    input=normalize(input)

    answer = model.predict(input)
    print('output',answer[0])
    

    return answer


results="/home/nico/codes/test_results"
answer=model_testing("/home/nico/codes/modelos/mc-4_linear_2m.h5",results,10000)
for i in answer:
    print(i)
